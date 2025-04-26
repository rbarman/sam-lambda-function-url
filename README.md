# README

Build an API with AWS Lambda Function URLs. Automated with SAM CLI and Lambda Powertools

# Steps

## Local

* pip3 install -r src/requirements.txt
* modify utils/
* python3 -m pytest tests/unit

## Local lambda

* replace "my-stack-name" in samconfig.toml
* modify src/app lambda handler
* turn on docker
* sam build
* sam local invoke ApiFunction -e events/event.json

## Deploy

* sam build && sam deploy --guided

# Resources

* Lambda Function URL: https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html
* Lambda Powertools: https://docs.powertools.aws.dev/lambda/python/latest/
* SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html
* https://aws.amazon.com/serverless/serverlessrepo/
