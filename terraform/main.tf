terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "genai-gateway-488421" 
  region  = "us-east4"
}

resource "google_compute_network" "custom_vpc" {
  name                    = "genai-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "custom_subnet" {
  name          = "genai-subnet"
  ip_cidr_range = "10.0.0.0/16"
  region        = "us-east4"
  network       = google_compute_network.custom_vpc.id
}

resource "google_container_cluster" "primary_cluster" {
  name     = "genai-cluster"
  location = "us-east4-a"
  network    = google_compute_network.custom_vpc.name
  subnetwork = google_compute_subnetwork.custom_subnet.name
  remove_default_node_pool = true
  initial_node_count       = 1
  deletion_protection      = false

  # Enables the modern Gateway API
  gateway_api_config {
    channel = "CHANNEL_STANDARD"
  }

  # Enables Workload Identity for secure Vertex AI access
  workload_identity_config {
    workload_pool = "genai-gateway-488421.svc.id.goog"
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "genai-node-pool"
  location   = "us-east4-a"
  cluster    = google_container_cluster.primary_cluster.name
  node_count = 2
    
  node_config {
    machine_type = "e2-medium"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}