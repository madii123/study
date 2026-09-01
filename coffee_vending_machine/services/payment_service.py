class PaymentService:

    def process_payment(
        self,
        price: int,
        amount_paid: int,
    ) -> int:

        if amount_paid < price:
            raise ValueError(
                f"Insufficient payment. "
                f"Price: {price}, Paid: {amount_paid}"
            )

        return amount_paid - price