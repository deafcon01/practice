 terraform {
   required_providers {
     aws = {
        source =  "hashicorp/aws"
        version = "~> 4.0"
     }
   }
 }

 provider "aws" {
   region = var.aws_region
 }


resource "aws_vpc" "dev-vpc" {
    cidr_block = "10.0.0.0/16"
    tags {
        Name = "dev-vpc"
    }
}

resource "aws_internet_gateway" "dev-gw" {
    vpc_id = aws_vpc.dev-vpc.id

    tags {
        Name = "dev-igw"
    }
}

resource "aws_route_table" "dev-route-table" {
    vpc_id = aws_vpc.dev-vpc.id
    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.dev-gw.id
    }
}

resource "aws_subnet" "dev-subnet-1" {
    vpc_id = aws_vpc.dev-vpc.id
    cidr_block = "10.1.0.0/24"
    availability_zone = "us-east-1a"
    tags {
        Name= "dev-subnet-1"
    }
}

resource "aws_route_table_association" "dev-rta" {
    route_table_id = aws_route_table.dev-route-table.id
    subnet_id = aws_subnet.dev-subnet-1
}

resource "aws_security_group" "dev-sg" {
    vpc_id = aws_vpc.dev-vpc
    ingress = {
        from_port = 32222
        to_port = 32225
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress = {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_block = ["0.0.0.0/0"]
    }
}

resource "aws_network_interface" "dev-nic" {
    subnet_id = aws_subnet.dev-subnet-1.id
    private_ips = ["10.1.0.4"]
    security_groups = [aws_security_group.dev-sg.id]
}

resource "aws_eip" "" {
    vpc =  true
    network_interface = aws_network_interface.web-server-nic.id
    associated_private_ip = "10.0.1.50"
    depends_on = [aws_internet_gateway.gw] 
}

resource "aws_instance" "web-server-instance" {
    ami = "ami-085925f29.."
    instance_type= "t2.micro"
    availability_zone = "us-east-1a"
    key_name = "ssh-key"

    network_interface {
        device_index = 0
        network_interface_id = aws_network_interface.web-server-nic.id
    }

    user_data = <<-EOF
                #!/bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
                sudo systemctl start apache2
                sudo bash -c ' echo Your very first web server > /var/www/html/index.html'
                EOF

    tags = {
        Name = "web-server"
    } 
}

