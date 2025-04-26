#!/bin/bash

# chmod +x get_lambda_url.sh
# Usage: ./get_lambda_url.sh my-stack-name

STACK_NAME="$1"

if [ -z "$STACK_NAME" ]; then
  echo "Usage: $0 <stack-name>"
  exit 1
fi

# Get the physical resource ID of the Lambda function
FUNCTION_NAME=$(aws cloudformation describe-stack-resources \
  --stack-name "$STACK_NAME" \
  --query "StackResources[?ResourceType=='AWS::Lambda::Function'].PhysicalResourceId" \
  --output text)

if [ -z "$FUNCTION_NAME" ]; then
  echo "No Lambda function found in stack $STACK_NAME"
  exit 1
fi

# Get the Lambda Function URL
aws lambda get-function-url-config --function-name "$FUNCTION_NAME" \
  --query "FunctionUrl" \
  --output text
