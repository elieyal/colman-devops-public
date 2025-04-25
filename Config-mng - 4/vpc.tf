data "aws_availability_zones" "available" {
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.19.0"  
  
  # VPC Basic Details
  name            = local.vpc_name
  cidr            = local.vpc_cidr_block
  azs             = data.aws_availability_zones.available.names
  public_subnets  = local.public_subnets
 
  # VPC DNS Parameters
  enable_dns_hostnames = true
  enable_dns_support   = true

  
  tags = local.common_tags
  vpc_tags = local.common_tags

  # Additional Tags to Subnets
  public_subnet_tags = {
    Type = "Public Subnets"       
  }

  map_public_ip_on_launch = true
}