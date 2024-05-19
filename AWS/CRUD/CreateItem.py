import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.put_item(
    Item = {
        'Name': 'Mark Cole',
        'Email': 'markcole@engineer.cloud',
        'Department': 'IT'
    }
)
print(response)