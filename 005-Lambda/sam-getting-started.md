# Steps for getting started with SAM (Serverless Application Module)

**Don't forget to delete the CloudFormation Stack after deploying with the AWS SAM**

## Install the AWS SAM CLI

1. Launch an `Amazon Linux 2` EC2 and connect to it.

1. Install NodeJS on the EC2.


    >curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash\
    >. ~/.nvm/nvm.sh\
    >nvm install node\
    >node -e "console.log('Running Node.js ' + process.version)"

1. Install Docker
	>sudo yum update -y\
	>sudo amazon-linux-extras install docker\
	>sudo service docker start\
	>sudo usermod -a -G docker ec2-user
	
1. Logout/login to the EC2. Verify Docker installation using `docker ps` command.

1. Install Homebrew.

    #Prerequisites
    >sudo yum groupinstall 'Development Tools'\
    >sudo yum install curl file git

    #Brew itself
    >sudo passwd ec2-user\
    >/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

    #Add Homebrew to your PATH
    >test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)\
    >test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\
    >test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile\
    >echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

    #Verify Homebrew
    >brew --version\

1. Install the AWS SAM CLI

    >brew tap aws/tap\
    >brew install aws-sam-cli

    #Verify the AWS SAM CLI
    sam --version

1. Generate the AWS Access Keys and configure them using

    >aws configure

## Deploy the Lambda Translate Application to the AWS

https://aws.amazon.com/blogs/compute/translating-documents-at-enterprise-scale-with-serverless/

1. Clone the Translate application.
    >git clone https://github.com/aws-samples/s3-to-lambda-patterns.git

1. Navigate to the V1 folder.

    >sam build\
    >sam deploy --guided

1. Upload a file in english to the S3 bucket.

1. Notice that the Lambda gets called and the file is automatically translated.

## Deploying the sample application with SAM

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

1. Init with the sample application. Follow the on-screen prompts. For this tutorial, we recommend that you choose AWS Quick Start Templates, the Zip package type, the runtime of your choice, and the Hello World Example.
    >sam init

1. Build the application
    >cd sam-app\
    >sam build

1. Host your API locally
    >sam local start-api\
    >curl http://127.0.0.1:3000/hello

1. Invoke your Lambda function directly
    >sam local invoke "HelloWorldFunction" -e events/event.json

1. Deploy the Lambda and the API Gateway to AWS
    >sam deploy --guided

# Further Reading

1. AWS SAM
    - https://aws.amazon.com/serverless/sam/

1. Testing and Debugging
    - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html
