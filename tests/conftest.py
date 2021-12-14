import sys, os
# add config file to the path
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import pytest

from bullish import Bullish
import bullish_config

@pytest.fixture(scope='session', autouse=True)
def connection():
    conn = Bullish(bullish_config.hostname, 
                   bullish_config.api_key_priv,
                   bullish_config.metadata)

    conn.login()
    print(conn)
    return conn

    