# Installing Python SDK and execute programs.

1. Execute the below commands on the EC2 instance.

    >#Get the list of softwares\
    >sudo apt-get update

    >#Install Python and pip\
    >sudo apt-get install python3 python3-pip -y

    >#Install Python AWS SDK\
    >pip3 install boto3

1. Copy the py files to the same folder. Execute the program using the below command.

    >python3 create-s3-bucket-object.py

1. Execute the different programs in this folder and also from the below `Examples` section.

# Further Reading

1. Quick start guide
    - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

1. Boto3 API
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

1. Examples
    - https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code
    - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html