import requests
import pandas as pd
from account_manager import AccountManager
from config import API_URL, ACCOUNT_ID, TRADE_AMOUNT
from account_manager.account_manager import AccountManager
def load_trades_data(file_path):
    # load trades data from file
    pass

def execute_trade(account_id, trade_data):
    # execute trade using account manager
    pass

def main():
    trades_data = load_trades_data("trades.txt")
    account_manager = AccountManager(API_URL, ACCOUNT_ID)
    for trade in trades_data:
        execute_trade(account_manager, trade)

if __name__ == "__main__":
    main()