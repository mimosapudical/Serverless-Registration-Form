Serverless Registration Form
Overview
This project implements a Serverless Registration Form using AWS Lambda, API Gateway, and DynamoDB.
It provides a backend service that allows users to submit their email address via an HTTP POST request.
The Lambda function processes the incoming request and stores the provided email into a DynamoDB table.

Tech Stack
AWS Lambda (Python 3.9)

AWS DynamoDB

AWS API Gateway

IAM Role-based Access Control

CloudWatch for Logging

Project Structure
registration-form/
├── lambda_function.py    # Main Lambda handler to process registration requests
├── README.md              # Project documentation
Setup Instructions
Create DynamoDB Table

Table Name: registration-table

Partition Key: email (String)

Create IAM Role

Role Name: RegistrationFormRole

Attach the following permissions:

CloudWatchFullAccess

DynamoDBFullAccess

Create Lambda Function

Function Name: registration-form-function

Runtime: Python 3.9

Assign the IAM role created above.

Create API Gateway

Set up a POST method integrated with the Lambda function.

Enable CORS with the following settings:

Access-Control-Allow-Origin: '*'
Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token
Access-Control-Allow-Methods: POST
API Usage
Endpoint:
POST https://your-api-gateway-url.com/registration

Request Body Example:

{
  "email": "user@example.com"
}
Behavior:

The Lambda function receives the email from the POST request.

It saves the email to the registration-table in DynamoDB.

Basic error handling and CORS support are implemented.

Key Learnings
Through this project, I gained practical experience with:

Building and deploying AWS Lambda functions.

Setting up DynamoDB tables for persistent storage.

Managing permissions securely with IAM roles.

Integrating API Gateway with Lambda and configuring CORS.

Understanding the basics of serverless application architecture.

Although this project initially followed a basic tutorial, I independently completed the deployment and configuration steps, and deepened my understanding of AWS serverless services through hands-on practice.

🚀 Serverless Registration — Lightweight, Scalable, and Cloud-Native!
