API with AWS Lambda Function URL

Initially created with AWS SAM cli

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

* https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html
* https://aws.amazon.com/serverless/serverlessrepo/
