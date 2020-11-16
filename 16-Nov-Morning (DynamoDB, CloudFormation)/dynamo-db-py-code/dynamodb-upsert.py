import sys
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Metrics')

response = table.update_item(
    Key={
        'Name': 'Users'
    },
    UpdateExpression='SET Connected = :newConnected',
    ExpressionAttributeValues={
        ':newConnected': sys.argv[1]
    },
    ReturnValues="UPDATED_NEW"
)
