# 1. Create a VPC
resource "aws_vpc" "prod-vpc" {
    cidr_block = "10.0.0.0/16"
    tags =  {
      Name = "vpc_production"
    }
}

# 2. Create Internet Gateway to access outside world
resource "aws_internet_gateway" "gw" {
    vpc_id = aws_vpc.prod-vpc.id
    tags = {
        Name = "internet_gateway_gw"
    }
}

# 3. Create Custom route table
resource "aws_route_table" "prod-route-table" {
    vpc_id = aws_vpc.prod-vpc.id
    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.gw.id
    }
    route {
      ipv6_cidr_block = "::/0"
      egress_only_gateway_id = aws_internet_gateway.gw.id
    }
    tags = {
        Name = "prod-route-table"
    }
}

# 4. Create a subnet
resource "aws_subnet" "subnet-1" {
    vpc_id = aws_vpc.prod-vpc.id
    cidr_block = "10.0.1.0/24" 
    availability_zone = "us-east-1a"

    tags = {
        Name = "prod-subnet-1"
    }
}

# 5. Associate subnet with route table
resource "aws_route_table_association" "rta" {
    subnet_id = aws_subnet.subnet-1.id
    route_table_id = aws_route_table.prod-route-table.id
}

# 6. Create security group to allow port 22, 80,443
resource "aws_security_group" "allow_web" {
    name = "allow_web_traffic"
    description = "Allow web inbound traffic"
    vpc_id =  aws_vpc.prod-vpc.id

    ingress = {
        description = "HTTPS"
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_block = ["0.0.0.0/0"]
    }

    ingress = {
        description = "HTTP"
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_block = ["0.0.0.0/0"]
    }

    ingress = {
        description = "SSH"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_block = ["0.0.0.0/0"]
    }

    egress = {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_block = ["0.0.0.0/0"]
    }

    tags = {
        Name = "allow_web"
    }
}

# 7. Create a network i/f with ip in subnet 
resource "aws_network_interface" "web-server-nic" {
    subnet_id = aws_subnet.subnet-1.id
    private_ips = ["10.0.1.50"]
    security_groups = [aws_security_group.allow_web.id]

    #attachment {
    #    instance = ""
    #    device_index = 1 
    #}
}

# 8. Assign elastic ip to network i/f so that anyone on the internet can access internet
resource "aws_eip" " " {
    vpc =  true
    network_interface = aws_network_interface.web-server-nic.id
    associated_private_ip = "10.0.1.50"
    depends_on = [aws_internet_gateway.gw] 
}

# 9. Create ubuntu server and install apache2 
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