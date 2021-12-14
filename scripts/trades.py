from bullish import Bullish

import config

if __name__ == '__main__':
    # create connection
    conn = Bullish(config.hostname, config.api_key_priv, 
                   config.metadata, verify=False)
                   
    # login
    conn.login()

    # get trades: BTCUSD
    trades = conn.get_trades(True, symbol='BTCUSD', _pageSize=5)
    for t in trades.data:
        print(t.to_dict())

    if len(trades.data) > 0:
        tr = conn.get_trade_by_id(trades.data[0].tradeId)
        print(tr.to_dict())