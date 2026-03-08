import pulumi
import pulumi_aws as aws
import random
import string

# Generate a unique suffix
suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
bucket_name = f"ai-devx-mandeep-{suffix}"

# Create the bucket (Versioning is now a property, not a separate resource)
bucket = aws.s3.Bucket("task-backups",
    bucket=bucket_name,
    versioning=aws.s3.BucketVersioningArgs(
        enabled=True,
    )
)

# Export the name
pulumi.export('bucket_name', bucket.id)
