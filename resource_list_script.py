import boto3

#Opening AWS managementconsole
aws_management_console = boto3.session.Session(profile_name="default")

#Resource name as iam
iam_console_resource = aws_management_console.resource('iam') # Resource Object

#Client name as iam
iam_console_client = aws_management_console.client('iam') # Client Object

# IAM users list with resource object:
for each_user in iam_console_resource.users.all():
    print(each_user.name)

# IAM users list with client object:
    #Returning a dictionary with userName and UserId as Key value pair as a dictionary.
for each in iam_console_client.list_users()['Users']:
   print(each['UserName'])

#use python interpreted CLI to access available resources
   
# dir(aws_management_console)
# print(aws_management_console.get_available_resources())