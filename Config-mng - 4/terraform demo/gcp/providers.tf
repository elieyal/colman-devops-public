provider "google" {
  project = local.project_id
  region  = local.region
  credentials = file("service-account-key.json")
}
