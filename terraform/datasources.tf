

data "aws_ami" "server_ami" {
  most_recent = true

  #This owner id is not your AWS id
  #This id is the owner of the aws marketplace owner for the ubuntu ami
  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server*"]
  }
}