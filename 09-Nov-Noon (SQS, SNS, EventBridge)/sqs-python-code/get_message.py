import time
import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/1234567890/MyQueue'

# Create a SQS Client
sqs = boto3.client('sqs')

# Receive message from SQS queue
response = sqs.receive_message(QueueUrl=queue_url)
message = response['Messages'][0]

# Delete received message from queue
receipt_handle = message['ReceiptHandle']

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print('Received and deleted message: %s' % message["Body"])