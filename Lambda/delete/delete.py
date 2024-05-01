import boto3

dynamodb = boto3.client(
        'dynamodb',
)

def handler(event, context):
    id = event["PicusID"]
    res = dynamodb.delete_item(
                TableName='picus',
                Key={
                        "PicusID":{"S": id},
                    },
                ConditionExpression="attribute_exists (PicusID)",
            )
    return res
