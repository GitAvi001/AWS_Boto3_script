#script to list all EC2 instances in the AWS account using sessions

# Import all the modules and Libraries
import boto3
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

result = ec2_console.describe_instances()['Reservations']

for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId']) #prints only the extracted instance id