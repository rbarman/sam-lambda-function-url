import pytest
from http import HTTPStatus
from src import app
from dataclasses import dataclass

@dataclass
class LambdaContext:
    function_name: str = "test"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
    aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"


REQUEST_CONTEXT = {
    "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"}, 
    "http": {
        "method": "GET",
    },
    "stage": "$default",
}

@pytest.fixture
def lambda_context() -> LambdaContext:
    return LambdaContext()

def test_search_no_id(lambda_context: LambdaContext):
    minimal_event = {
        "rawPath": "/search",
        "requestContext": REQUEST_CONTEXT,
    }
    ret = app.lambda_handler(minimal_event, lambda_context)
    assert ret["statusCode"] == HTTPStatus.BAD_REQUEST
    assert ret["body"] == "Id parameter is required"

def test_search_with_id(lambda_context: LambdaContext):
    minimal_event = {
        "rawPath": "/search",
        "requestContext": REQUEST_CONTEXT,
        "queryStringParameters": {
            "my_id": "123"
        }
    }
    ret = app.lambda_handler(minimal_event, lambda_context)
    assert ret["statusCode"] == HTTPStatus.OK