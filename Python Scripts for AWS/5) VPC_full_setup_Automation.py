# This is program is for automate VPC full setup end to end

import boto3

client = boto3.client('ec2', region_name = "us-west-2", aws_access_key_id = "AKIAQGXMSAXLNTOYR6UN", aws_secret_access_key = "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")

# VPC Creation 
print ("Enter the value for VPC Cidr: ")
vpc_cidr = input()
Var_Create_VPC = client.create_vpc(
    CidrBlock=vpc_cidr,
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Hi-Tech_VPC-01'
                },
            ]
        },
    ]
)

print ("VPC has been successfully created, The VPC ID is: ",Var_Create_VPC['Vpc']['VpcId'])
vpc_id = Var_Create_VPC['Vpc']['VpcId']

# Subnet-01 Creation 
print ("Enter the value for Subnet-01 Cidr: ")
Subnet_01_cidr = input()
Var_Create_subnet = client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Hi-Tech_Subnet-01'
                },
            ]
        },
    ],
    VpcId=vpc_id,
    CidrBlock=Subnet_01_cidr
)

print ("Subnet-01 has been successfully created, The Subnet-01 ID is: ", Var_Create_subnet['Subnet']['SubnetId'])


# Subnet-02 Creation 
print ("Enter the value for Subnet-02 Cidr: ")
Subnet_02_cidr = input()
Var_Create_subnet_02 = client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Hi-Tech_Subnet-02'
                },
            ]
        },
    ],
    VpcId=vpc_id,
    CidrBlock=Subnet_02_cidr
)

subnet02id = Var_Create_subnet_02['Subnet']['SubnetId']
print ("Subnet-02 has been successfully created, The Subnet-02 ID is: ", subnet02id)



#Task
# RT + IGW + Routing entries