# 3rd party imports
import boto3
# local imports
import config


def create_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    try:
        dynamodb.create_table(table_name)
    except:
        
