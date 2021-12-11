import boto3
import csv

def List_ec2_fun(writer):

	client = boto3.client('ec2', region_name = "ap-south-1", aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")
	epmty_dict = {}

	var_list_ec2_ins = client.describe_instances()
	for i in var_list_ec2_ins['Reservations']:
		for j in i['Instances']:
			# print (j['ImageId'], j['InstanceId'], j['InstanceType'], j['KeyName'], j['LaunchTime'])
			epmty_dict["AMI_ID"] = j['ImageId']
			epmty_dict["INSTANCE_ID"] = j['InstanceId']
			epmty_dict["INSTANCE_TYPE"] = j['InstanceType']
			epmty_dict["KEYNAME"] = j['KeyName']
			epmty_dict["LAUNCH_TIME"] = j['LaunchTime']
			writer.writerow(epmty_dict)
			print ("CSV Report has been generated")

def main():
	
	fieldnames = ["AMI_ID","INSTANCE_ID","INSTANCE_TYPE","KEYNAME","LAUNCH_TIME"]
	file_name = "epmty_dict.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()

		List_ec2_fun(writer)	#Function Calling + Passing Parameter

main()