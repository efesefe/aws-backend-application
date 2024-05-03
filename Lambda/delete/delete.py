import boto3
import json

dynamodb = boto3.client(
        'dynamodb',
)

def handler(event, context):
    id = json.dumps(event.get("rawPath")).replace(r"/", "")
    res = dynamodb.delete_item(
                TableName='picus',
                Key={
                        "PicusID":{"S": id},
                    },
                ConditionExpression="attribute_exists (PicusID)",
            )
    return res
