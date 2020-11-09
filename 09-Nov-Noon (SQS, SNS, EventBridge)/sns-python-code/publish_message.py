import boto3

# Create an SNS client
sns = boto3.client('sns')

# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:1234567890:MyTopic',    
    Message='Hello World!',    
)

# Print out the response
print(response)
  
