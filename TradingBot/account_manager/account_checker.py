class AccountChecker:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def check_balance(self, account_id, amount):
        """
        Check if the balance of the specified account is sufficient to make a trade.
        """
        balance = self.account_manager.get_account_balance(account_id)
        if balance >= amount:
            return True
        else:
            return False