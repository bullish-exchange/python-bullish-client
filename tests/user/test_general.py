import pytest
import datetime as dt

def test_nonce(connection):
    ''' '''
    nonce = connection.get_nonce()
    # confirm nonce is valid
    ct = dt.datetime.utcnow()
    min_nonce = dt.datetime.combine(ct, dt.time.min, tzinfo=dt.timezone.utc)
    max_nonce = dt.datetime.combine(ct, dt.time.max, tzinfo=dt.timezone.utc)
    # convert to microseconds
    assert int(int(min_nonce.timestamp()* 1000) * 1000) == nonce.lowerBound
    # convert to microseconds
    assert int(int(max_nonce.timestamp()* 1000) * 1000) == nonce.upperBound

def test_time(connection):
    ''' '''
    time = connection.get_exchange_time()
    ct = dt.datetime.now(dt.timezone.utc)
    # confirm exchange time and current time is < 100 millisecond 
    # possibly a bogus test
    assert (time.timestamp - int(ct.timestamp()* 1000)) < 100