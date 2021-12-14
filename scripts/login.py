from bullish import Bullish
import config
import logging

if __name__ == '__main__':
    conn = Bullish(config.hostname,
                  config.api_key_priv, config.metadata, 
                  verify=False)
                   
    logging.basicConfig()
    bullish_log = logging.getLogger("bullish.bullish")
    bullish_log.setLevel(logging.DEBUG)

    conn.login()