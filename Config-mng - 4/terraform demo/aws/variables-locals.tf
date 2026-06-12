locals {
  common_tags = {
      owner = "Me"
      usage = "demo"
  }
  vpc_name       = "colman-devops-terraform-demo"
  vpc_cidr_block = "10.10.0.0/16"
  public_subnets = ["10.10.0.0/20"]
  keypair        = "Colman2025"
}