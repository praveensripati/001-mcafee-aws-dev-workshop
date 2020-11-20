# Creating a VPC and EC2 in private/public subnets using the wizard

1. Create a VPC (Public) using Wizard.
	- Navigate to the VPC Management Console (https://console.aws.amazon.com/vpc/home?region=us-east-1)
	- Create an `Elastic IP`.
	- Click on `Launch VPC Wizard` in the `VPC Dashboard`.
	- Select `VPC with Public and Private Subnets`. Click on `Select`.
	- Give the VPC, Public and Private Subnet a name.
	- Select the `Elastic IP`.
	- Click on `Create VPC`.

# Steps for Peering across VPCs

1. Create one EC2 instance in the Public Subnet in the default VPC and another EC2 instance in the VPC created in the previous step.
	-  Note that  a new Security Group has to be created for the new VPC, as the Security Groups are VPC specific.
	-  Login to both the instances via Putty.
	-  Make sure to add "All ICMP - IPv4" protocol in the Security Group to allow testing through Ping.

1. Go to the VPC Management Console and go to the "Peering Connections" Tab.
	-  Click on "Create Peering Connection"
	-  Enter the name
	-  Select the requester as the Default VPC.
	-  Select the accepter as the newly created VPC.
	-  Click on "Create Peering Connection"
	-  The status of the VPC Peering will be in a "Pending Acceptance" status.
	-  Select the VPC and select "Actions -> Accept Request". Now the status should change to Active.

1. Check if the ping is working from one EC2 to other using the Private IP address. It should not work as the routing tables have not been configured between the two VPC.

	- Note down the CIDR for both the VPC
    - The following should be performed for both the EC2 instances.
        - Select the EC2 instance.
        - Identify the Subnet for the above EC2 and select it.
        - Identify the Routing Table for above Subnet and select it.
        - Click on Route and edit it.
        - Add the missing VPC CIDR destination and target as the earlier created VPC peering.
	- Now the ping should work from both the EC2 using the private IP address as the peering has been properly established.

1. If the Ping works make sure to delete all the resources created earlier including the Elastic IP.

## Steps for deleting the VPC
1. Terminate the EC2
1. Delete the Peering connections
1. Delete the NAT Gateway
1. Wait for a few Minutes
1. Delete ElasticIP
1. Finally delete the VPC

# Further Reading

1. Traffic Mirroring
	- https://aws.amazon.com/blogs/aws/new-vpc-traffic-mirroring/

1. Transit Gateway (a better alternate to VPC Peering)
	- https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html
	- https://aws.amazon.com/blogs/networking-and-content-delivery/migrate-from-transit-vpc-to-aws-transit-gateway/
	- https://aws.amazon.com/blogs/aws/new-use-an-aws-transit-gateway-to-simplify-your-network-architecture/
	- https://www.youtube.com/watch?v=yQGxPEGt_-w/