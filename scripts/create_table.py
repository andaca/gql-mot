# stdlib imports
import logging
# 3rd party imports
import boto3
# local imports
import config


logging.basicConfig()
log = logging.getLogger(__name__)


def create_table(ddb_cfg):
    dynamodb = boto3.resource('dynamodb')
    try:
        table = dynamodb.create_table(
            TableName=ddb_cfg['TableName'],
            KeySchema=ddb_cfg['KeySchema'],
            AttributeDefinitions=ddb_cfg['AttributeDefinitions'],
            ProvisionedThroughput=ddb_cfg['ProvisionedThroughput']
        )
    except Exception as e:
        log.fatal(e)
        raise SystemExit()
    
    table.meta.client.get_waiter('table_exists').wait(TableName=ddb_cfg['TableName'])
    log.info('Table created: {}'.format(ddb_cfg['TableName']))


if __name__ == '__main__':
    create_table(config.ddb)