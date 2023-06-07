// Deploy EKS Cluster with Terraform

IAM
--
name: sudoaccess
Administrator access
AmazonEKSCLusterPolicy

provider.tf
--
provider "aws" {
  region = "us-east-2"
}

vpc.tf
--
//a VPC, subnets and availability zones using the AWS VPC Module.
variable "region" {
    default = "us-east-2"
    description = "aws region"
}

provider "aws" {
    version = ">=2.28.1"
    region =  var.region
}

data "aws_availability_zones" "available" {}

resource "random_string" "suffix" {
  length  = 8
  special = false
}

locals {
    cluster_name = "training-eks-${random_string.suffix.result}"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "2.6.0"

  name = "training-vpc"
  cidr = "10.0.0.0/16"
  azs = data.aws_availability_zones.available.names
  private_subnets      = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets       = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true
  tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
  }

  public_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/elb"                      = "1"
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb"             = "1"
  }
}


securitygroup.tf
--
// provisions the security groups

resource "aws_security_group" "worker_group_mgmt_one" {
  name_prefix = "worker_group_mgmt_one"
  vpc_id = module.vpc.vpc_id

  ingress = {
    from_port = 22
    to_port = 22
    protocol = "tcp"

    cidr_blocks = [
        "10.0.0.0/8",
    ]
  }
}

resource "aws_security_group" "worker_group_mgmt_two" {
  name_prefix = "worker_group_mgmt_two"
  vpc_id = module.vpc.vpc_id

  ingress = {
    from_port = 22
    to_port = 22
    protocol = "tcp"

    cidr_blocks = [
        "192.168.0.0/16",
    ]
  }
}

resource "aws_security_group" "all_worker_mgmt" {
  name_prefix = "all_worker_mgmt"
  vpc_id = module.vpc.vpc_id

  ingress = {
    from_port = 22
    to_port = 22
    protocol = "tcp"

    cidr_blocks = [
        "10.0.0.0/8",
      "172.16.0.0/12",
      "192.168.0.0/16",
    ]
  }
}

eks-cluster.tf
--
//  provisions all the resources (AutoScaling Groups, etc...) required to set up an EKS cluster in the private subnets and bastion servers

module "eks" {
    source =  "terraform-aws_modules/eks/aws"
    cluster_name = local.cluster_name
    subnets = module.vpc.private_subnets

    vpc_id = module.vpc.vpc_id
    worker_groups = [{
        name = "worker-group-1"
        instance_type = "t2.small"
        additional_user_data = "echo foo bar"
        asg_desired_capacity = 2
        additional_security_group_ids = [aws_security_group.worker_group_mgmt_one.id]
    },
    {
        name = "worker-group-2"
        instance_type = "t2.medium"
        additional_user_data = "echo foo bar"
        asg_desired_capacity = 1
        additional_security_group_ids = [aws_security_group.worker_group_mgmt_two.id]
    },
  ]
}

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}

outputs.tf
--
// defines the output configuration

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "cluster_security_group_id" {
  value = module.eks.cluster_security_group_id
}

output "kubectl_config" {
  value = module.eks.kubeconfig
}

output "region" {
  description = "AWS region"
  value       = var.region
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = local.cluster_name
}

versions.tf
--
// set terraform atleast 0.12

terraform {
  required_version = ">= 0.12"
}

provider "random" {
  version = "~> 2.1"
}

provider "local" {
  version = "~> 1.2"
}

provider "null" {
  version = "~> 2.1"
}

provider "template" {
  version = "~> 2.1"
}