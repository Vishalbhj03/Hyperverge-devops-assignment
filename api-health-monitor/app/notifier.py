import boto3
import os

sns = boto3.client("sns")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")


def send_notification(message):
    if not SNS_TOPIC_ARN:
        return

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="API Health Status Changed"
    )

