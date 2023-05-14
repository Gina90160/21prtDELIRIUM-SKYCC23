import boto3
import zipfile
from io import BytesIO
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App, Ack, BoltContext
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime
SLACK_APP_TOKEN = "xapp-1-A0576NE15PZ-5262261130308-35d61ab88765a1841afd8e79ef7194d5933edb4ec5342ab6a239c64d547d4357"
SLACK_BOT_TOKEN = "xoxb-5204338656257-5272338587137-TUjQSJOLqtHSI4fDFGvzfYkw"
AWS_REGION = "ap-northeast-2"
AWS_ACCESS_KEY = "AKIA5KRU2MITQNVYJ3GH"
AWS_SECRET_KEY = "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"
AWS_BUCKET_NAME = "21prt-delirium"
AWS_FOLDER_NAME = datetime.now().strftime("%Y%m%d%H%M%S")
s3 = boto3.client('s3',
                  region_name=AWS_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY)
slack_client = WebClient(token=SLACK_BOT_TOKEN)
app = App(token=SLACK_BOT_TOKEN)
@app.event("app_mention")
def handle_mention(ack: Ack, context: BoltContext, event: dict):
    text = event['text']
    user = event['user']
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name_upload = f"{timestamp}.py"
    folder_name_download = f"{timestamp}"
    folder_name_download_zip = f"{timestamp}.zip"
    # Create file on local
    with open(file_name_upload, 'w') as f:
        f.write(text)
    # Zip file
    zip_bytes = BytesIO()
    with zipfile.ZipFile(zip_bytes, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(file_name_upload)
    zip_bytes.seek(0)
    # Upload zip file to AWS S3
    s3.upload_fileobj(zip_bytes, AWS_BUCKET_NAME, f"{AWS_FOLDER_NAME}/{folder_name_download_zip}")
    # Send S3 link to Slack thread
    channel_id = event['channel']
    thread_ts = event['ts']
    s3_link = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{AWS_FOLDER_NAME}/{folder_name_download_zip}"
    try:
        slack_client.chat_postMessage(
            channel=channel_id,
            text=f"Uploaded `{file_name_upload}` to S3 folder: {s3_link}",
            thread_ts=thread_ts)
    except SlackApiError as e:
        print("Error posting message: {}".format(e))
if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    handler.start()