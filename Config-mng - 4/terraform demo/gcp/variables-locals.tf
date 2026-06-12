locals {
  common_tags = {
    owner = "Me"
    usage = "demo"
  }
  project_id     = "test01-eyaleli"  # Update with your GCP project ID
  region         = "europe-west3"    # Frankfurt region (similar to eu-central-1)
  zone           = "europe-west3-a"
  vpc_name       = "colman-devops-terraform-demo"
  subnet_cidr    = "10.10.0.0/20"
  machine_type   = "e2-micro"             # GCP free tier equivalent to t2.micro
}
