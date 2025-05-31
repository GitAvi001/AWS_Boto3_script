import boto3

aws_management_console = boto3.session.Session(profile_name="boto3")

ec2_console = aws_management_console.client("ec2")

response = ec2_console.run_instances(
    ImageId='ami-00f34bf9aeacdf007',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1
)
