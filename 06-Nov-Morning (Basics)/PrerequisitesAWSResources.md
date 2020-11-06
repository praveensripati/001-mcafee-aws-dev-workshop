# Prerequisites AWS Resources required to be created as part of the course

1. Make sure to select the `New EC2 Experience` from the EC2 Management Console as shown below.\
![](images/2020-11-04-10-00-53.png)

1. Create a Security Group (AllowAll) with Inbound `All Protocols/Ports/Sources`. The Outbound rules can be left as default.\
![](images/2020-11-05-13-57-43.png)
![](images/2020-11-05-13-58-03.png)

1. Create a KeyPair with private key in the `ppk` format. When prompted download the Privatekey to Laptop.\
![](images/2020-11-04-19-44-47.png)

1. Create an `EC2 Launch Template` with the below details
    - Navigate to
        - https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchTemplates:
    - Click on `Create launch template`\
![](images/2020-11-05-10-17-55.png)
    - Give the Launch Template a name and description
    - `Ubuntu Server 18.04 LTS (HVM), SSD Volume Type` as the AMI
    - Instance type as `t2.medium`
    - Earlier created KeyPair
    - Earlier created SecurityGroup (AllowAll)
    - Click on `Create launch template`

1. To launch EC2 from the above template.
![](images/2020-11-05-10-19-14.png)

1. Download Putty from the below URL.\
        - https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
![](images/2020-11-05-10-36-37.png)