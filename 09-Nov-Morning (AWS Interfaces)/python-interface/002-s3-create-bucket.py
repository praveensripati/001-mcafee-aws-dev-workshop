import boto3

s3 = boto3.client('s3')

# CHANGE
s3.create_bucket(Bucket='my-bucket-praveen')