import boto3

s3 = boto3.resource('s3')
bucket_name =input("Enter the bucket name : ")
bucketvar = s3.Bucket(bucket_name)
n = 0
for obj in bucketvar.objects.all():
    n=n+1
    print(f"{n}. {obj.key}")
print(f"Total number of objects are {n}")
