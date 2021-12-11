# Listing S3 Buckets 

import boto3

client = boto3.client('s3', aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")

Var_S3_list = client.list_buckets()
#print (Var_S3_list['Buckets'])

for i in Var_S3_list['Buckets']:
	print(i['Name'])