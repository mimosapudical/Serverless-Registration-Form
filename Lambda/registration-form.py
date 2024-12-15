#edited the original tutorial by the assistance of ChatGPT
import boto3
import json
import os

# Set up SES and DynamoDB clients
ses = boto3.client('ses', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns', region_name='us-west-2')

TABLE_NAME = 'registration-table'
SES_SENDER_EMAIL = 'cjzmimosapudical@gmail.com'
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-2:982081045604:emailR:64ff3f22-7d87-44f0-8975-9aef6d424e52'

# Function to send an email via SES
def send_email(to_email, user_name):
    subject = "Welcome to Our Service!"
    body = f"Hello {user_name},\n\nThank you for registering with us. We're excited to have you on board!"
    
    # Send the email using SES
    response = ses.send_email(
        Source=SES_SENDER_EMAIL,
        Destination={'ToAddresses': [to_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )
    return response

# Function to trigger SNS notification
def send_sns_notification(user_email):
    message = f"User {user_email} has successfully registered!"
    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject='New User Registration'
    )
    return response

# Lambda handler function
def lambda_handler(event, context):
    try:
        user_email = event['email']
        user_name = event['name']
        user_phone = event['phone']
        user_password = event['password']

        # Save user data to DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(
            Item={
                'email': user_email,
                'name': user_name,
                'phone': user_phone,
                'password': user_password
            }
        )

        # Send welcome email via SES
        send_email(user_email, user_name)

        # Send SNS notification
        send_sns_notification(user_email)

        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Registration successful, email sent, and SNS notification triggered!'})
        }

    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Error occurred: ' + str(e)})
        }
