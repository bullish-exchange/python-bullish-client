from bullish import Bullish

import config

if __name__ == '__main__':
    # create connection
    conn = Bullish(config.hostname, config.api_key_priv, 
                   config.metadata, verify=False)
                   
    # login
    conn.login()

    # get spot accounts
    spot_accts = conn.get_spot_accounts()
    for acct in spot_accts:
        print(f'spot acct: symbol: {acct.symbol} total: {acct.total}')

    spot_btc = conn.get_spot_accounts(symbol='BTC')
    print(f'BTC Spot: {spot_btc.total}')

    margin_accts = conn.get_margin_accounts()
    for acct in margin_accts:
        print(f'spot acct: symbol: {acct.symbol} total: {acct.baseTotal}')