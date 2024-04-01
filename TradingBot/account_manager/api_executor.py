class ApiExecutor:
    def __init__(self, api_url):
        self.api_url = api_url

    def execute_trade(self, account_id, trade_data):
        """
        Execute a trade on the specified account.
        """
        url = f"{self.api_url}/accounts/{account_id}/trades"
        response = requests.post(url, json=trade_data)
        return response.json()