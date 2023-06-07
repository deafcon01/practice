// Creating a single EC2 instance, EBS volume, and attaching that volume to the instance

provider "aws" {
    region =var.region
}

data "aws_ami" "app-ami" { 
  most_recent = true 
  filter {
    name = "name"
    values = ["myami-*"]
  }
} 


resource "aws_instance" "ec2_node" {
    ami = data.aws_ami.app-ami.id
    instance_type = var.instance_type
    availability_zone = var.availability_zone
    
    tags = {
        Name = "EC2 Node"
    }
}

resource "aws_ebs_volume" "ebs" {
  availability_zone = var.availability_zone
  size = 1

  tags = {
    Name = "EBS volume"
  }
}

resource "aws_volume_attachment" "vol_attach" {
    device_name= "/dev/sdh"
    volume_id = aws_ebs_volume.ebs.id 
    instance_id = aws_instance.ec2_node.id 
}
