import json
import os

import boto3
import requests
from botocore.config import Config
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv(override=False)

RUSTFS_ENDPOINT = os.environ["RUSTFS_ENDPOINT"]  # must be the S3 API endpoint (not the UI)
ACCESS_KEY = os.environ["ACCESS_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]
BUCKET = os.environ.get("BUCKET", "test")

s3 = boto3.client(
    "s3",
    endpoint_url=RUSTFS_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1",
    verify=False,  # replace with a CA bundle path when ready
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "path"},  # more compatible with S3-compatible servers behind proxies
    ),
)

def ensure_bucket(name: str) -> None:
    """
    Avoid list_buckets() (often blocked/404 behind reverse proxies).
    Use head_bucket + create_bucket if missing.
    """
    try:
        s3.head_bucket(Bucket=name)
        return
    except ClientError as e:
        err = e.response.get("Error", {})
        code = str(err.get("Code", ""))  # can be '404', 'NoSuchBucket', 'AccessDenied', etc.

        # Missing bucket
        if code in ("404", "NoSuchBucket", "NotFound"):
            s3.create_bucket(Bucket=name)
            return

        # Some S3-compatible servers return 400 on head_bucket for missing buckets
        if code in ("400", "BadRequest"):
            s3.create_bucket(Bucket=name)
            return

        raise  # propagate AccessDenied/InvalidAccessKeyId/etc.

ensure_bucket(BUCKET)

resp = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=30)
resp.raise_for_status()
posts = resp.json()[:50]

for p in posts:
    key = f"api/posts/id={p['id']}.json"
    body = (json.dumps(p) + "\n").encode("utf-8")
    s3.put_object(Bucket=BUCKET, Key=key, Body=body, ContentType="application/json")

print(f"uploaded {len(posts)} objects to s3://{BUCKET}/api/posts/")
