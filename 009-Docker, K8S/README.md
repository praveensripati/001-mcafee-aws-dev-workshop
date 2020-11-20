# Topics

    - Introduction to Docker and K8S
    - How are AWS and K8S related to each other
    - Different ways of setting up an ECS and EKS Cluster in AWS
    - Creating a Docker Container with a static page
    - Registering the Container with AWS ECR

# Theory

1. Evolution towards containers\
![](images/evolution-towards-containers.png)

1. Container orchestration on AWS\
![](images/container-orchestration-on-aws.png)
![](images/ecs-vs-eks.png)
    - Amazon ECS vs Amazon EKS: making sense of AWS container services
        - https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/

1. Pod (basic unit) Orchestration with K8S\
![](images/k8s-pod-basic-unit-Orchestration-k8s.png)

1. K8S Workloads (https://kubernetes.io/docs/concepts/workloads/controllers/)
    - Deployments
    - ReplicaSet
    - StatefulSets
    - DaemonSet
    - Jobs
    - CronJob

1. K8S Architecture
    - https://kubernetes.io/docs/concepts/overview/components/
    - https://www.redhat.com/en/topics/containers/kubernetes-architecture\
![](images/k8s-architecture.png)

1. Ecosystem
    - https://www.cncf.io/projects/

1. Beneath the container runtime\
![](images/beneath-container-runtime.png)\
`Runc` is a low-level, lightweight, portable container runtime. Runc is a tool for spawning and running containers according to the Open Container Initiative (OCI) specification. `Containerd` builds on top of it, and adds higher-level features, such as image transfer and storage, container execution, and supervision, as well as network and storage attachments. There exist alternative implementations of the OCI specification. Some of them are rkt by CoreOS, CRI-O by RedHat, and LXD by Linux Containers. However, containerd at this time is by far the most popular container runtime and is the default runtime of Kubernetes 1.8 or later and the Docker platform.

# Further Reading

1. Docker Base Image OS Size Comparison
    - https://www.brianchristner.io/docker-image-base-os-size-comparison/

1. Amazon Linux container image
    - https://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html

1. Cloud Native Computing Foundation
    - https://www.cncf.io/

1. K8S Documentation
    - https://kubernetes.io/docs/home/

1. K8S Blog
    - https://kubernetes.io/blog/

1. K8S Certifications
    - https://www.cncf.io/certification/cka/
    - https://www.cncf.io/certification/ckad/

1. CNCF Projects
    - https://www.cncf.io/projects/