import boto3
from datetime import date, datetime, timedelta,timezone
from datetime import date
import csv

def accesskey_fun(writer):
	
	empty_dict_IAM = {}

	client = boto3.client('iam', aws_access_key_id = "AKIAVCKCWWNV", aws_secret_access_key = "6uqEBkWqVi5CL/qOZhP")

	iam_users_var = client.list_users()
	for i in iam_users_var['Users']:
		all_iam_users = i['UserName']

		acc_key_response_var = client.list_access_keys(UserName=all_iam_users)
		for j in acc_key_response_var['AccessKeyMetadata']:
			
			User_Crated_Date = j['CreateDate']
			accesskey = j['AccessKeyId']
			
			access_key_lastusd = client.get_access_key_last_used(AccessKeyId=accesskey)
			access_key_lastusd_date = access_key_lastusd['AccessKeyLastUsed']['LastUsedDate']

			Todays_date = datetime.now(timezone.utc)

			age_access_key = (Todays_date - User_Crated_Date).days

			if (age_access_key >= 0):
				empty_dict_IAM['Username'] = all_iam_users
				empty_dict_IAM['CreateDate'] = User_Crated_Date
				empty_dict_IAM['age_of_key'] = age_access_key
				empty_dict_IAM['Status'] = j['Status']
				empty_dict_IAM['Key Last Used'] = access_key_lastusd_date
				writer.writerow(empty_dict_IAM)
				print (empty_dict_IAM)

def send_email_report(file_name):
	SENDER = "hitechmay2020@gmail.com"
	RECIPIENT = "hitechmay2020@gmail.com"
	SUBJECT = "Accesskey 150 Age Data"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created 150days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])

def main():
	fieldnames = ["Username","CreateDate","age_of_key"]
	file_name = "empty_dict_IAM.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		accesskey_fun(writer)
	send_email_report(file_name)

main()


