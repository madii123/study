import operation
from atm import ATM
from exceptions import ATMServiceException


class ATMDemo:
    @staticmethod
    def main():
        atm = ATM.get_instance()

        account = atm.create_account("6754567890", 500)
        atm.create_card("1234-5678-9012-3456", "1234", account)

        # Perform Check Balance operation
        atm.insert_card("1234-5678-9012-3456")
        atm.enter_pin("1234")
        atm.select_operation(operation.CheckBalance())  # $1000
        atm.eject_card()

        # Perform Withdraw Cash operation
        atm.insert_card("1234-5678-9012-3456")
        atm.enter_pin("1234")
        atm.select_operation(operation.WithdrawCash(570))
        atm.eject_card()

        # Perform Deposit Cash operation
        atm.insert_card("1234-5678-9012-3456")
        atm.enter_pin("1234")
        atm.select_operation(operation.DepositCash(200))
        atm.eject_card()

        # Perform Check Balance operation
        atm.insert_card("1234-5678-9012-3456")
        atm.enter_pin("1234")
        atm.select_operation(operation.CheckBalance())  # $630
        atm.eject_card()

        # Perform Withdraw Cash more than balance
        atm.insert_card("1234-5678-9012-3456")
        atm.enter_pin("1234")
        atm.select_operation(operation.WithdrawCash(700))  # Insufficient balance
        atm.eject_card()

        # Insert Incorrect PIN
        atm.insert_card("1234-5678-9012-3456")
        try:
            atm.enter_pin("3425")
            atm.eject_card()
        except ATMServiceException as e:
            print(e)


if __name__ == "__main__":
    ATMDemo.main()
