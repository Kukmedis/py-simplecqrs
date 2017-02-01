from simple_accounting.account_handler import AccountHandler
from simple_accounting.balance_sheet import BalanceSheet
from simple_accounting.event_store import EventStore


def main():
    event_store = EventStore()
    account_handler = AccountHandler(event_store)
    balance_sheet = BalanceSheet(event_store)
    account_handler.deposit_to_account("ID_1000", 100)
    account_handler.withdraw_from_account("ID_1000", 30)
    account_handler.deposit_to_account("ID_1000", 50)
    account_handler.deposit_to_account("ID_2000", 1000)
    account_handler.deposit_to_account("ID_2000", 500)
    balance_sheet.check_for_events()
    print(balance_sheet.get_balances())


if __name__ == "__main__":
    main()
