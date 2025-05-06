import json
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler.api_gateway import Response
from http import HTTPStatus

app = LambdaFunctionUrlResolver()

@app.get("/search")
def search():
    current_event = app.current_event
    print(f"received event: {current_event}")

    my_id = app.current_event.query_string_parameters.get("my_id")
    print(f"received my_id: {my_id}")
    if not my_id:
        return Response(status_code=HTTPStatus.BAD_REQUEST, body="Id parameter is required")

    return Response(
        status_code=HTTPStatus.OK,
        content_type="application/json",
        body={
            "id": my_id,
        },
    )


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)