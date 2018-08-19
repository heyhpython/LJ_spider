from pymongo import MongoClient
from pymongo.collection import Collection
from contextlib import contextmanager
import logging
import json

logger = logging.getLogger(__name__)
write_order = ['city', 'name', 'community_name', 'type', 'acreage', 'orientation',
               'style', 'elevator', 'location', 'floor', 'follower', 'visitor', 'tag',
               'total_price', 'unit_price', 'distinct', 'partitioned']
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
    with open('./data.txt', 'w') as f:
        for r in collection.find():
            r.pop('_id')

            for k, v in r.items():

                f.write(v.replace(' ', '').replace('n', '').replace(',', '') if isinstance(v, str) else str(v))
                f.write(',')
            f.write('\n')


def run():
    with make_client() as client:
        db = client.LJ
        cleaner(db)


if __name__ == "__main__":
    run()
