# Bullish

A python wrapper to the Bullish Exchange API. Documentation for the API can be found [here](https://bugbounty.bullish.com/docs/api/rest/)

## Installation

### Development
To install the library during development run the command:
```bash
pip install -e .
```

### Running Scripts
To install the library using a virtual enviornment run:
```bash
mkdir -p ~/envs
python3 -m venv ~/envs/test
source ~/envs/test/bin/activate
pip install git+https://github.com/bullish-exchange/py-bullish.git@develop
```
*Note* git ssh keys must be setup
## Scripts

A directory of example scripts. All of the scripts use a [config.py](#Configuration) module that requires the following lines:

## Tests

To run the tests do the following:

1. Create a [bullish_config.py](#Configuration) file in the tests directory
2. Ensure `tox` and `python3.9` are installed on the system
3. Run the tests
```bash
tox
```
```bash
# truncated output
tests/login/test_login.py ..                                                                                                     [100%]
========================================================== 2 passed in 3.22s ===========================================================
_______________________________________________________________ summary ________________________________________________________________
  py39: commands succeeded
  congratulations :)
```

## Configuration

Both the tests and scripts require that certain environment variables be set. Below is an example environment file.

```
# .env
# private api key
export BULLISH_KEY="PVT_R1_L...."
# metadata string generated at addition of API key 
export BULLISH_METADATA="eyJwdWJsaWNLZXkiOi..."
# hostname of api
export BULLISH_HOSTNAME="https://api.uat.vdevel.net"
```
Environment file must be sourced to add to the environment
```bash
source .env
```
## Logging

The `bullish` library uses the [logging](https://docs.python.org/3/library/logging.html) library for logging output. It can be turned on using the following code:

```python
logging.basicConfig()
bullish_log = logging.getLogger("bullish.bullish")
bullish_log.setLevel(logging.DEBUG)
```