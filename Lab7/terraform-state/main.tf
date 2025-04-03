terraform {
  backend "s3" {
    bucket         = "terraform-state-example5"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
resource "aws_instance" "example" {
  ami           = "ami-00a929b66ed6e0de6"
  instance_type = "t2.micro"
  tags = {
    Name = "Terraform-Test-Instance"
  }
}
