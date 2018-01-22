ddb = {
    'tableName': 'testTable',
    'tableSchema': {
        'TableName': 'testTable',
        'AttributeDefinitions': [
            {'AttributeName': 'test_id', 'AttributeType': 'S'},
            {'AttributeName': 'test_date', 'AttributeType': 'N'},
        ],
        'KeySchema': [
            {'AttributeName': 'test_id', 'KeyType': 'HASH'},
            {'AttributeName': 'test_date', 'KeyType': 'SORT'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    },
}
