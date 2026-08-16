
Basic:

    # seats.screen_id -> screens.id
    # A foreign key creates the (db level) connection between two tables
    # database relationship
    # stores the actual ID
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))

    # seats.screen = screen, (creates python-side) relationship
    # python/ORM relationship
    # gives you python object
    # seat = db.get(Seat, 1) and screen = seat.screen
    screen: Mapped["Screen"] = relationship(back_populates="seats")

    # e.g.:
    # seat = db.get(Seat, 1)
    # print(seat.screen_id)
    # print(seat.screen.id)


in pair, double side relations:
    screen: Mapped["Screen"] = relationship(back_populates="seats")
    seats: Mapped[list["Seat"]] = relationship(back_populates="screen")
    Screen -----seats-----> [Seat, Seat, Seat]
    Seat -----screen-----> Screen
But it does not create the database foreign key, for that: 
    ForeignKey("screens.id")

### Database reference — relationships (SQLAlchemy)

This document explains common SQL/ORM relationship patterns and how they map to SQLAlchemy (2.0 style typing). It covers:

- Foreign keys vs ORM `relationship`
- One-to-many and one-to-one
- Many-to-many (simple association table and full association object)
- A safe conditional UPDATE pattern

---

## Foreign key vs ORM relationship

- `ForeignKey`: creates the database-level connection (stores the raw id in the table).
- `relationship()`: creates a Python/ORM-level view that returns model objects.
- `back_populates` (or `backref`) connects both sides at the ORM level so you can navigate in both directions.

Example (SQLAlchemy 2.0 typing):

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Seat(Base):
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(primary_key=True)
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))

    # ORM-level relationship — gives you `seat.screen` as a Screen object
    screen: Mapped["Screen"] = relationship(back_populates="seats")

class Screen(Base):
    __tablename__ = "screens"

    id: Mapped[int] = mapped_column(primary_key=True)
    # ORM-level relationship — gives you a list of Seat objects
    seats: Mapped[list["Seat"]] = relationship(back_populates="screen")
```

Notes:

- `screen_id` stores the raw integer foreign key in the database.
- `seat.screen` and `screen.seats` are convenience ORM accessors — they do not create DB columns by themselves.

---

## One-to-many

Typical pattern: `Screen` 1 → * `Seat`.

```python
class Screen(Base):
    __tablename__ = "screens"
    id: Mapped[int] = mapped_column(primary_key=True)
    seats: Mapped[list["Seat"]] = relationship(back_populates="screen")

class Seat(Base):
    __tablename__ = "seats"
    id: Mapped[int] = mapped_column(primary_key=True)
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id"))
    screen: Mapped["Screen"] = relationship(back_populates="seats")
```

Usage:

```py
seat = db.get(Seat, 1)
print(seat.screen_id)    # raw FK
print(seat.screen.id)    # loaded Screen object (may lazy-load)
```

---

## One-to-one

One-to-one is modeled like one-to-many but constrained to a single related row. Use a unique foreign key (or primary key) on the child.

```python
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)

class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="profile")
```

Use `uselist=False` on the parent side to signal a scalar relationship.

---

## Many-to-many

There are two common ways to model many-to-many relationships.

1) Simple association table (no extra columns):

```python
from sqlalchemy import Table, Column

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    courses: Mapped[list["Course"]] = relationship(secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    students: Mapped[list["Student"]] = relationship(secondary=student_course, back_populates="courses")
```

Usage: appending a `Course` to `student.courses` will insert into the association table automatically.

2) Association object (when the join table has extra data or behavior):

```python
class StudentCourse(Base):
    __tablename__ = "student_course"
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    assigned_on: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    student: Mapped["Student"] = relationship(back_populates="enrollments")
    course: Mapped["Course"] = relationship(back_populates="enrollments")

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    enrollments: Mapped[list[StudentCourse]] = relationship(back_populates="student")

class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    enrollments: Mapped[list[StudentCourse]] = relationship(back_populates="course")
```

Use an association object when you need to store metadata about the relationship itself.

---

## Safe conditional UPDATE (avoid lost-update race)

SQL pattern — update column only if it still has the expected value:

```sql
UPDATE seats
SET available = false
WHERE id = :id
  AND available = true;
```

SQLAlchemy Core pattern (update with condition):

```python
from sqlalchemy import update

stmt = (
    update(Seat)
    .where(
        Seat.id == seat_id,
        Seat.available.is_(True),
    )
    .values(available=False)
)
result = session.execute(stmt)
session.commit()

# result.rowcount tells you whether the update succeeded (1) or the condition failed (0)
```

This pattern avoids a race where two workers read `available` as `true` and both try to claim the seat.

---

## Quick tips

- Prefer `ForeignKey` + `relationship` pattern — FK defines the DB schema, `relationship` gives easy object navigation.
- Use `uselist=False` for one-to-one scalar relationships.
- Choose simple association table for plain many-to-many; use association objects for extra columns/behavior.
- When changing state that can be concurrently claimed, use conditional updates and check `rowcount`.

---

If you want, I can add small runnable examples (mini scripts) that create the tables, insert sample rows, and demonstrate both the simple many-to-many and association-object patterns.
