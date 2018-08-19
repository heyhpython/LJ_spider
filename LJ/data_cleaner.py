from pymongo import MongoClient
from decorator import contextmanager
import logging

logger = logging.getLogger(__name__)


@contextmanager
def make_client(ip=None, port=None):
    try:
        client = MongoClient()
        yield client
    except Exception as e:
        logger.error(str(e))
    finally:
        logger.info('client closing .....')
        client.close()


with make_client() as client:
    collcetion = client['LJ']['LJ']