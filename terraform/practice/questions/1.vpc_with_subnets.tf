// Build vpc with 2 public and 2 private subnets

// the module has 3 files 
// variable.tf

variable "public_subnet_numbers" {
  type = map(number)

  default = {
    "us-east-2a" = 0
    "us-east-2b" = 1
    "us-east-2c" = 2
  }
}

variable "private_subnet_numbers" {
  type = map(number)

  default = {
    "us-east-2a" = 4
    "us-east-2b" = 5
    "us-east-2c" = 6
  }
}

variable "vpc_cidr" {
    type = string
    default = "10.0.0.0/16"
}

variable "infra_env" {
    type = string
    default = "dev"
}

// main.tf 
resource "aws_vpc" "vpc" {
  cidr_block = var.cidr

  tags = {
    Name = "MyVpc"
  }
}

# create 1 public subnet for each AZ
 resource "aws_subnet" "public" {
   for_each = var.public_subnet_numbers
   vpc_id = aws_vpc.vpc.id
   availability_zone = each.key

   cidr_block = cidrsubnet(aws_vpc.vpc.cidr_block, 4, each.value)
   tags = {
    Subnet = "${each.key}-${each.value}"
   }
 }

 # create 1 private subnet for each AZ
 resource "aws_subnet" "private" {
   for_each = var.private_subnet_numbers
   vpc_id = aws_vpc.vpc.id
   availability_zone = each.key

   cidr_block = cidrsubnet(aws_vpc.vpc.cidr_block, 4, each.value)
   tags = {
    Subnet = "${each.key}-${each.value}"
   }
 }

 //outputs.tf 
 output "vpc_id" {
    value = aws_vpc.vpc.id   
 }

 output "vpc_cidr" {
  value = aws_vpc.vpc.cidr_block
}

output "vpc_public_subnets" {
    value = {
        for subnet in aws_aws_subnet.public :
        subnet.id => subnet.cidr_block
    }  
}

output "vpc_private_subnets" {
    value = {
        for subnet in aws_aws_subnet.private :
        subnet.id => subnet.cidr_block
    }  
}

// working.tf 
module "vpc" {
    source = "./modules/vpc"
    infra_env = var.infra_env
}