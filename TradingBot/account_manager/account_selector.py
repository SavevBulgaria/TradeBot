class AccountSelector:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def select_account_with_highest_balance(self, num_accounts):
        """
        Select the top `num_accounts` accounts with the highest balance.
        """
        accounts = self.account_manager.get_all_accounts()
        sorted_accounts = sorted(accounts, key=lambda x: x["balance"], reverse=True)
        return sorted_accounts[:num_accounts]