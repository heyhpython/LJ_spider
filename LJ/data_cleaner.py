from pymongo import MongoClient
from pymongo.collection import Collection
from contextlib import contextmanager
import logging
import json

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


def cleaner(db):
    collection = db.LJ
    count = collection.find().count()
    l = 10000
    s = 0
    with open('./data.txt', 'w') as f:
        i = 0
        for r in collection.find():
            r.pop('_id')
            if i==0:
                for k in r.keys():
                    f.write(k)
                    f.write('\t')
                f.write('\n')
                i += 1

            for k,v in r.items():

                f.write(v.replace(' ', '').replace('n','').replace(',', '') if isinstance(v, str) else str(v))
                f.write('\t')
            f.write('\n')


def run():
    with make_client() as client:
        db = client.LJ
        cleaner(db)

if __name__ == "__main__":
    run()
