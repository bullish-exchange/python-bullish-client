from bullish import Bullish

import config

if __name__ == '__main__':
    # create connection
    conn = Bullish(config.hostname, config.api_key_priv, 
                   config.metadata, verify=False)
                   
    # login
    conn.login()

    # get nonce
    nonce_obj = conn.get_nonce()
    print(f'Lower Bound: {nonce_obj.lowerBound}')
    print(f'Upper Bound: {nonce_obj.upperBound}')

    # get time
    time_obj = conn.get_exchange_time()
    print(f'{time_obj.datetime}')

    