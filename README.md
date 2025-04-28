# 📄 Serverless Registration Form

## Overview
This project implements a **Serverless Registration Form** using **AWS Lambda**, **API Gateway**, and **DynamoDB**.  
Users submit their registration information via an HTTP **POST** request. The Lambda function processes the input and stores the data into DynamoDB.

---

## Tech Stack
- AWS Lambda (Python 3.9)
- AWS DynamoDB
- AWS API Gateway
- IAM Roles (for permission management)
- CloudWatch (for logging)

---


---## Setup Instructions

1. **Create DynamoDB Table**  
   - Table Name: `registration-table`  
   - Partition Key: `email` (String)

2. **Create IAM Role**  
   - Role Name: `RegistrationFormRole`  
   - Attach Policies:  
     - `CloudWatchFullAccess`  
     - `DynamoDBFullAccess`

3. **Create Lambda Function**  
   - Function Name: `registration-form-function`  
   - Runtime: Python 3.9  
   - Assign the IAM role created above.

4. **Create API Gateway**  
   - Configure a **POST** method integrated with the Lambda function.  
   - Enable CORS with:
     ```
     Access-Control-Allow-Origin: *
     Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token
     Access-Control-Allow-Methods: POST
     ```

---

## API Usage

**Endpoint**  
`POST https://<your-api-id>.execute-api.<region>.amazonaws.com/registration`

**Request Body**
```json
{
  "email": "user@example.com"
}
