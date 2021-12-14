import bullish_config
from bullish import Bullish
from bullish.objects.exception import InvalidReqestException
import pytest
import requests
import json

def test_login(connection):
    ''''''
    connection.login()

def test_login_fail_key():
    with pytest.raises(InvalidReqestException):
        conn = Bullish(bullish_config.hostname, '', bullish_config.metadata)
        conn.login()

def test_login_fail_metadata():
    with pytest.raises(json.decoder.JSONDecodeError):
        conn = Bullish(bullish_config.hostname, bullish_config.api_key_priv, '')
        conn.login()

def test_login_fail_invalid_metadata():
    with pytest.raises(UnicodeDecodeError):
        conn = Bullish(bullish_config.hostname, bullish_config.api_key_priv, '12341234')
        conn.login()