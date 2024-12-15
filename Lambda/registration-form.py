#edited the original tutorial by the assistance of ChatGPT
import boto3
import json

# Initialize DynamoDB and SNS clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Replace with your DynamoDB table name and SNS topic ARN
TABLE_NAME = 'registration-table'
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-2:982081045604:emailR:64ff3f22-7d87-44f0-8975-9aef6d424e52'

def lambda_handler(event, context):
    table = dynamodb.Table(registration-table)

    try:
        # Create new item in DynamoDB table
        response = table.put_item(
            Item={
                'email': event['email'],
                'name': event['name'],
                'phone': event['phone'],
                'password': event['password']
            }
        )

        # Publish a notification to SNS
        sns.publish(
            TopicArn=arn:aws:sns:us-west-2:982081045604:emailR:64ff3f22-7d87-44f0-8975-9aef6d424e52,
            Subject='New User Registration',
            Message=(
                f"A new user has registered:\n\n"
                f"Name: {event['name']}\n"
                f"Email: {event['email']}\n"
                f"Phone: {event['phone']}"
            )
        )

        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Registration successful'})
        }

    except Exception as e:
        # Handle errors and return a failure response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
