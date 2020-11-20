# Prerequisites to get started with EKS and ECS

1. Get the Access Keys and provide them to the EC2 using the `aws configure` command along with the region `us-east-1`.

1. Install `eksctl`.
    >curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp\
    >sudo mv /tmp/eksctl /usr/local/bin\
    >eksctl version

1. Install `kubectl`.
    >curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/linux/amd64/kubectl  
    >chmod +x ./kubectl\
    >sudo mv ./kubectl /usr/local/bin\
    >kubectl version --short --client\

1. Generate the ssh keys.
    >ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa