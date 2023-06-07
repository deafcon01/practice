variable "aws_access_key" {
  type = string
}

variable "aws_secret_key" {
  type = string
}

variable "aws_key_pair_pub" { type = string }
variable "local_key_pair_priv" { type = string }

variable "lab_tag" {
    default = "Auto-Scaling-Lab"
}

variable "instance_ami" {
    default = "ami-02354e95b39ca8dec"
}
variable "instance_type" {
    default = "t2.micro"
}

variable "web_user_data" {
  default = <<EOF
    #!/bin/bash
    yum update -y
    yum install httpd -y
    service httpd start
    chkconfig httpd on
    cd /var/www/html
    echo "<html><h1>This is WebServer" `curl http://169.254.169.254/latest/meta-data/local-ipv4` "</h1></html>" > index.html
    EOF
}

// provider.tf 

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region = var.region
}

// vpc.tf 

resource "aws_vpc" "vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "vpc"
  }
}

variable "public_subnet_numbers" {
  type = map(number)

  default = {
    "us-east-2a" = 0
    "us-east-2b" = 1
    "us-east-2c" = 2
  }
}


resource "aws_subnet" "public" {
  for_each = var.public_subnet_numbers
  vpc_id = aws_vpc.vpc.id
  availability_zone = each.key
  cidr_block = cidrsubnet(aws_vpc.vpc.cidr_block, 4, each.value)
   tags = {
    Subnet = "${each.key}-${each.value}",
    K8S-CNI = "public"
   }
}

resource "aws_internet_gateway" "ig" {
  vpc_id = aws_vpc.vpc.id
}

resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ig.id
  }
}