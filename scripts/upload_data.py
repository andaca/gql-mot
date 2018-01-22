# stdlib imports
import csv
from datetime import datetime
import sys
# 3rd party imports
import boto3
# relative imports
import config


def get_dicts(fname):
    with open(fname, 'r') as f:
        for d in csv.DictReader(f, delimiter='|'):
            yield d


def prep_dicts(d):
    for key in ['test_date', 'first_use_date']:
        d[key] = int(datetime.strptime(d[key], '%Y-%m-%d').timestamp())
    for key in ['test_mileage', 'cylinder_capacity']:
        d[key] = int(d[key]) if d[key] else None
    return d


if __name__ == '__main__':

    data = get_dicts(sys.argv[1])
    items = (prep_dicts(d) for d in data)

    table = boto3.resource('dynamodb').Table(config.ddb['tableName'])
    with table.batch_writer() as writer:
        i = 0
        for item in items:
            writer.put_item(Item=item)
            i += 1
            print('{} items put'.format(i), end='\r')
