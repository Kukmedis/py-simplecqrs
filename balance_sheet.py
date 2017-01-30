class BalanceSheet():

    __document_store = {}

    def account_debited(self, event):
        self.__document_store[event.account_id] = event.balance

    def account_credited(self, event):
        self.__document_store[event.account_id] = event.balance
