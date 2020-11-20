import boto3

# Create an SNS client
sns = boto3.client('sns')

# Create email subscription
response = sns.subscribe(TopicArn="arn:aws:sns:us-east-1:1234567890:MyTopic", Protocol="email", Endpoint="ugetaws@gmail.com")
subscription_arn = response["SubscriptionArn"]

print(subscription_arn)