# This is program is for listing Ec2 Instance

import boto3

client = boto3.client('ec2', region_name = "us-west-2", aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")

var_list_ec2_ins = client.describe_instances()
#print (var_list_ec2_ins['Reservations'])

for i in var_list_ec2_ins['Reservations']:
	#print (i['Instances'])
	for j in i['Instances']:
		print (j['ImageId'], j['InstanceId'], j['InstanceType'], j['KeyName'], j['LaunchTime'])