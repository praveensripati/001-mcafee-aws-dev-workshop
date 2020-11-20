# Push the Docker Image to ECR

1. Create an IAM Role with the Admin Policy and attach the Role to the EC2.

1. Install the AWS CLI

1. Run the `aws configure` command and specify only the region as `us-east-1`, rest can be left blank.

1. Create a repository in ECR.
    >aws ecr create-repository --repository-name hello-world --region us-east-1

1. Grab the ECR Repository URL and replace the same in the below commands.

1. Tag the Docker image created earlier. Make sure to specify the proper repository name, got from the previous step.
    >docker tag hello-world:latest **327762702280.dkr.ecr.us-east-1.amazonaws.com**/hello-world:latest

1. Get the ECR credentials and provide the same to Docker. This enables Docker to authenticate and pull the image from ECR. The warning during the process can be ignored.
    >aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin **327762702280.dkr.ecr.us-east-1.amazonaws.com**

1. Push the Docker image to the ECR. Make sure to specify the proper repository name, got from the previous step.
    >docker push **327762702280.dkr.ecr.us-east-1.amazonaws.com**/hello-world:latest

1. There is no need to delete the ECR repository now. FYI, below is the command for the same.
    >aws ecr delete-repository --repository-name hello-repository --region us-east-1 --force