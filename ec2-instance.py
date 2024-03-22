import boto3

ec2= boto3.resource("ec2")

ec2.create_instances(
        ImageId="ami-0a0f1259dd1c90938",
        InstanceType="t2.micro",
        KeyName= "pythonkeyabhi",
        MaxCount=1,
        MinCount=1)
print("EC2 instances created successfully")
        
