data "aws_vpc" "pa-vpc" {
    tags = {
        VpcAppTags="AA-VPC"
    }
}