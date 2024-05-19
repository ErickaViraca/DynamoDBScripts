import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.update_item(
    Key={
        'Name': 'Mark Cole',
        'Email': 'markcole@engineer.cloud'
    },
    ExpressionAttributeValues={
        ':d': 'finance'
    },
    UpdateExpression="set Department = :d",
)
print(response)