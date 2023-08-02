""" Main IEC Python API module. """

from logging import getLogger
from logging.config import fileConfig as logConfig

import login

logConfig("./logging.conf", disable_existing_loggers=False)
logger = getLogger(__name__)

if __name__ == "__main__":  # pragma: no cover
    try:
        token = login.get_authorization_token()
        print(f"Token: {token}")
    except login.IECLoginError as err:
        logger.error("Failed Login: (Code %d): %s", err.code, err.error)
