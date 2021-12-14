import logging
import os

# setup logging
logging.basicConfig()
bullish_log = logging.getLogger("bullish.bullish")
bullish_log.setLevel(logging.DEBUG)

# load environment variables

if 'BULLISH_HOSTNAME' in os.environ:
    hostname = os.environ['BULLISH_HOSTNAME']
else:
    raise ValueError('"BULLISH_HOSTNAME" environment variable not set')

if 'BULLISH_KEY' in os.environ:
    api_key_priv = os.environ['BULLISH_KEY']
else:
    raise ValueError('"BULLISH_KEY" environment variable not set')

if 'BULLISH_METADATA' in os.environ:
    metadata = os.environ['BULLISH_METADATA']
else:
    raise ValueError('"BULLISH_METADATA" environment variable not set')