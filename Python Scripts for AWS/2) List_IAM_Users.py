# This is program is for listing IAM Users

import boto3

client = boto3.client('iam', aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")

var_List_users = client.list_users()
#print (var_List_users['Users'])

for new_var in var_List_users['Users']:
	print (new_var['UserName'], new_var['CreateDate'])