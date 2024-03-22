import boto3

def uploadfile(file_path,bucket_name,object_name=None):
    if object_name is None:
        object_name = file_path
    s3= boto3.client('s3')
    try:
        s3.upload_file(file_path,bucket_name,object_name)
    except Exception as e:
        print(e)
    else:
        print(f"{file_path}----->{bucket_name}")
        print(f"Object name is {object_name}")

uploadfile("/etc/hosts","nujis3","hosts")

