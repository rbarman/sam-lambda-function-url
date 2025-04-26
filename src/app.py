import json
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.utilities.typing import LambdaContext

app = LambdaFunctionUrlResolver()

@app.get("/")
def root():

    current_event = app.current_event
    print(f"received event: {current_event}")

    my_id = app.current_event.query_string_parameters.get("my_id")
    print(f"received my_id: {my_id}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, World!"
        })
    }

def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)