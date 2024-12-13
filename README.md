# Serverless Registration Form

## Step 1: Create DynamoDB Table

```sh
Table Name: registration-table
Partition key: email

```

## Step 2: Create IAM Role for Lambda Function
```sh
IAM Role Name: RegistrationFormRole

Permissions:
1. CloudWatch Full Access
2. DynamoDB Full Access

```

## Step 3: Create Lambda Function

```sh
Function Name: registration-form-function
Runtime: Python 3.9

```

## Step 4: Write Lambda Function

## Step 5: Create API Gateway and Enable CORS

## Step 6: Test the Project


### Enable CORS: 

```sh
Access-Control-Allow-Origin: '*'
Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token
Access-Control-Allow-Methods: POST

```

## Step 5: Test the Application



Thanks for tutorials here: https://www.youtube.com/@amonkincloud/videos \

