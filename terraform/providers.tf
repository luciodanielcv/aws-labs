terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  shared_config_files      = ["/home/ldcv/.aws/config"]
  shared_credentials_files = ["/home/ldcv/.aws/credentials"]
  profile                  = "default"
}


