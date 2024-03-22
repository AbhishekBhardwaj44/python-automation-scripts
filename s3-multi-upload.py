import boto3
import os

s3 = boto3.client("s3")

bucket_name = "networknuts-py"

files_path = input("Enter directory which contains files: ")

files_list = os.listdir(files_path)

n = 0
for filename in files_list:
    n = n + 1
    file_absolute_path = os.path.join(files_path,filename)
    if os.path.isfile(file_absolute_path):
        s3.upload_file(file_absolute_path,bucket_name,filename)
        print(f"{filename} ---> {bucket_name}")

print("Upload complete!")
print(f"Total files uploaded: {n}")
