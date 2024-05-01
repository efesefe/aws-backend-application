print("testing...")

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(TableName='picus')

item = response['Items']

if item:
    print("success")
else:
    print("failure")

