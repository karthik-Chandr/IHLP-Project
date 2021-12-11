# This is program is for listing VPC by creating new function

import boto3

def VPC_fun():		#Defining the FUnction
	client = boto3.client('ec2', region_name = "us-west-2", aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")

	list_VPC_response = client.describe_vpcs()
	#print (list_VPC_response['Vpcs'])
	for i in list_VPC_response['Vpcs']:
		print (i['VpcId'], i['CidrBlock'])

VPC_fun()			#Calling the Function