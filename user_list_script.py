#Automated script to listing the all users in IAM 

import boto3
#Automated way to access the AWS management console using boto3 library
aws_management_console = boto3.session.Session(profile_name="default")

#Moving to the IAM console
iam_console_resource = aws_management_console.resource('iam') 

#for-each loop to print all users in IAM console 
for each_user in iam_console_resource.users.all():
    print(each_user.name)
