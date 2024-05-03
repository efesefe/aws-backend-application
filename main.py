import boto3
from bottle import route, run, template, get, post, request

try:
    dynamodb = boto3.client(
        'dynamodb',
    )
except:
    print("Boto failed to connect")

#response = dynamodb.scan(TableName='picus')
#item = response['Items']

@get('/picus/list')
def index():
    return dynamodb.scan(TableName='picus')

@get('/picus/get/<item>')
def index(item):
    return dynamodb.get_item(TableName='picus',
            Key={
                    'PicusID': {'S':item}
                })

@post('/picus/put/')
def index():
    print(request.json)
    item = request.json
    res = dynamodb.put_item(
                TableName='picus',
                Item=item
            )
    print(res)
    print(type(res))
    return res

run(host='0.0.0.0', port=8080)
