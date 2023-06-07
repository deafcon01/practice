terraform {
    backend "s3" {
        bucket = "myTfStateBucket"
        key= "us-west-1/apollo/apollo.tfstate"
        region = "us-west-1"
        encrypt = true
        dynamodb_table = "terraform_locks"
    }
}