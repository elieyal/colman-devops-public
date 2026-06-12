# VPC Network
resource "google_compute_network" "vpc" {
  name                    = local.vpc_name
  auto_create_subnetworks = true
  description             = "VPC for Terraform demo"
}

# Subnet
resource "google_compute_subnetwork" "public_subnet" {
  name          = "${local.vpc_name}-public-subnet"
  ip_cidr_range = local.subnet_cidr
  region        = local.region
  network       = google_compute_network.vpc.id
  
  description = "Public subnet for web servers"
}

# resource "google_compute_route" "gateway" {
#   name             = "gateway"
#   dest_range       = "0.0.0.0/0"
#   network          = google_compute_network.vpc.name
#   next_hop_gateway = "default-internet-gateway"
#   priority         = 1000
# }

# resource "google_compute_route" "default_internet_route" {
#   name             = "default-internet-route"
#   dest_range       = "0.0.0.0/0"
#   network          = google_compute_network.vpc.name
#   next_hop_gateway = "default-internet-gateway"
#   priority         = 1000
# }
