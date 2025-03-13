provider "aws" {
  region = "us-east-1"  # Modify region if needed
}
resource "aws_instance" "my_ec2" {
  ami           = "ami-04aa00acb1165b32a"  # Replace with a valid AMI ID
  instance_type = "t2.micro"
  key_name      = "EC2-Template"  # Replace with an existing AWS key pair
  tags = {
    Name = "terraform-ec2-instance"  # Modify instance name
  }
}
