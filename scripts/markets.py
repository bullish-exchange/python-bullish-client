from bullish import Bullish

import config

if __name__ == '__main__':
    # create connection
    conn = Bullish(config.hostname, config.api_key_priv, 
                   config.metadata, verify=False)
                   
    # get challenge and generate
    conn.login()

    # get markets
    markets = conn.get_markets()
    for m in markets:
        print(m)

    # get market
    btcusd = conn.get_market('BTCUSD')
    print(f'{btcusd} - {btcusd.orderTypes}')

    # get order book
    orderbook = conn.get_market_orderbook(btcusd.symbol)
    print(orderbook.bids[0].__dict__)
