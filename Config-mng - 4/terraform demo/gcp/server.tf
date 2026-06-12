# Data source to get the latest Debian image
data "google_compute_image" "debian" {
  family  = "debian-12"
  project = "debian-cloud"
}

# Compute Instance
resource "google_compute_instance" "web_server" {
  name         = "web-server"
  machine_type = local.machine_type
  zone         = local.zone

  tags = ["web-server"]

  boot_disk {
    initialize_params {
      image = data.google_compute_image.debian.self_link
      size  = 10
      type  = "pd-standard"
    }
  }

  network_interface {
    network    = google_compute_network.vpc.name
    subnetwork = google_compute_subnetwork.public_subnet.name

    access_config {
      // Ephemeral public IP
    }
  }

  metadata_startup_script = file("init.sh")

  labels = {
    owner = "me"
    usage = "demo"
  }
}
