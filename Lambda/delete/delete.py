import boto3
import json

dynamodb = boto3.client(
        'dynamodb',
)

def handler(event, context):
    id = event.get("path").replace("/", "")
    try:
        res = dynamodb.delete_item(
                    TableName='picus',
                    Key={
                            "PicusID":{"S": id},
                        },
                    ConditionExpression="attribute_exists (PicusID)",
                )
    except:
        return {"statusCode": 404,"body": json.dumps("item not found")}
    return {"statusCode": 200,"body": json.dumps(res)}
