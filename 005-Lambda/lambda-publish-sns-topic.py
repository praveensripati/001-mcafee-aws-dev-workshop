import boto3
from botocore.exceptions import ClientError
print('Loading function')

def lambda_handler(event, context):

    # Create an SNS client
    client = boto3.client('sns', region_name=AWS_REGION)

    try:
        # Publish a simple message to the specified SNS topic
        response = sns.publish(
            TopicArn='arn:aws:sns:region:0123456789:my-topic-arn',    
            Message='Hello World!',    
        )

    # Error handling
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
