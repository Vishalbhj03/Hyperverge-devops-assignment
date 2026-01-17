import boto3
import os
import time

dynamodb = boto3.resource("dynamodb")

CONFIG_TABLE = os.environ.get("CONFIG_TABLE", "api_config")
STATE_TABLE = os.environ.get("STATE_TABLE", "api_state")

config_table = dynamodb.Table(CONFIG_TABLE)
state_table = dynamodb.Table(STATE_TABLE)


def get_all_apis():
    response = config_table.scan()
    return response.get("Items", [])


def get_previous_state(api_id):
    response = state_table.get_item(Key={"api_id": api_id})
    return response.get("Item")


def update_state(api_id, state):
    state_table.put_item(
        Item={
            "api_id": api_id,
            "last_state": state,
            "last_checked": int(time.time())
        }
    )

