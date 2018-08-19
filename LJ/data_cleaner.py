from pymongo import MongoClient
from contextlib import contextmanager
import datetime
import logging

logger = logging.getLogger(__name__)
write_order = ['city', 'name', 'community_name', 'type', 'acreage', 'orientation',
               'style', 'elevator', 'location', 'floor', 'follower', 'visitor', 'tag',
               'total_price', 'unit_price', 'district', 'partitioned']


@contextmanager
def make_client(ip=None, port=None):
    try:
        client = MongoClient()
        yield client
    except Exception as e:
        raise e
    finally:
        logger.info('client closing .....')
        client.close()


def cleaner(db):

    collection = db['LJ']
    with open('./data{}.txt'.format(datetime.datetime.now()), 'w', encoding='utf-8') as f:
        for r in collection.find():
            print(r)
            r.pop('_id')

            for k in write_order:
                f.write(str(r.get(k)))
                f.write('\t')
            f.write('\n')


def run():
    with make_client() as client:
        db = client.LJ
        cleaner(db)


if __name__ == "__main__":
    run()
