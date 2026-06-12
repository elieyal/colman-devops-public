output "external_ip" {
  value       = google_compute_instance.web_server.network_interface[0].access_config[0].nat_ip
  description = "The external IP of the web server"
}

output "instance_name" {
  value       = google_compute_instance.web_server.name
  description = "The name of the compute instance"
}
