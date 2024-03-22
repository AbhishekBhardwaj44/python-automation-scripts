import boto3
client =  boto3.client('s3')

bucket_name= input("enter the bucket name to create : ")
bucket_loc= input("enter the location of bucket : ")

print(f"{bucket_name} Bucket creation start")

client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint':bucket_loc }
    )

print(f" S3 bucket created successfully at location {bucket_loc}")
