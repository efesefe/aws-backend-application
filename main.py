import boto3
from bottle import route, run, template, get, post, request
dynamodb = boto3.client(
        'dynamodb',
)

#dynamodb.put_item(
#    TableName='picus',
#    Item={
#        'PicusID': {'S': 'id#1'},
#        'name': {'S': 'SomeName'},
#        'inventory': {'N': '500'},
#    }
#)
#response = dynamodb.get_item(
#    TableName='picus',
#    Key={
#        'PicusID': {'S': 'id#1'},
#    }
#)
response = dynamodb.scan(TableName='picus')
item = response['Items']
print(item)

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
#    res = res["PicusID"]["S"]
    print(res)
    print(type(res))
    return res

run(host='localhost', port=8080)
