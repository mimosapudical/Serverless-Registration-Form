#edited the original tutorial by the assistance of ChatGPT
import boto3
import json

# Initialize DynamoDB and SES clients
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')

# Replace with your DynamoDB table name and SES sender email
TABLE_NAME = 'registration-table'
SES_SENDER_EMAIL = 'cjzmimosapudical@gmail.com'

def lambda_handler(event, context):
    table = dynamodb.Table(registeration-table)

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

        # Send an email using Amazon SES
        email_response = ses.send_email(
            Source=SES_SENDER_EMAIL,
            Destination={
                'ToAddresses': [event['email']]  # User's email
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to Our Service!'
                },
                'Body': {
                    'Text': {
                        'Data': (
                            f"Hi {event['name']},\n\n"
                            f"Thank you for registering with us. Here are your details:\n\n"
                            f"Name: {event['name']}\n"
                            f"Email: {event['email']}\n"
                            f"Phone: {event['phone']}\n\n"
                            f"Welcome aboard!\n"
                        )
                    }
                }
            }
        )

        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Registration successful, email sent'})
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
