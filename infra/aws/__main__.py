import pulumi
import pulumi_aws as aws
import random
import string

# Generate a unique bucket name
suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
bucket_name = f"ai-devx-mandeep-{suffix}"

# Create a plain S3 bucket (no versioning, no extras)
bucket = aws.s3.Bucket("task-backups", bucket=bucket_name)

# Export the bucket name for the API to use
pulumi.export('bucket_name', bucket.id)
