# URL Shortener Service

A containerized URL shortening service built with FastAPI and MongoDB. This service allows you to create short URLs for sharing long links more efficiently.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start Guide (Copy-Paste)](#quick-start-guide-copy-paste)
- [Step-by-Step Installation](#step-by-step-installation)
- [How to Use the URL Shortener](#how-to-use-the-url-shortener)
- [Data Persistence](#data-persistence)
- [Viewing and Managing Your Data](#viewing-and-managing-your-data)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)
- [Technical Details](#technical-details)

## Features

- **URL Shortening**: Convert long, unwieldy URLs into compact, shareable links
- **Custom Short IDs**: Define your own memorable short URL identifiers
- **Persistent Storage**: MongoDB backend ensures URLs are preserved even after system restarts
- **Containerized**: Fully Dockerized for easy deployment in any environment
- **Fast Redirects**: Optimized lookups for quick redirection to original URLs
- **Simple REST API**: Easy-to-use JSON API for programmatic access

## Prerequisites

- Docker installed on your system ([Get Docker](https://docs.docker.com/get-docker/))
- Basic familiarity with terminal/command line

## Quick Start Guide (Copy-Paste)

For those who just want to get it running quickly, copy and paste these commands:

```bash
# Create a persistent volume for MongoDB data
docker volume create mongodb_data

# Start MongoDB container
docker run -d --name mongodb -p 27017:27017   -e MONGO_INITDB_ROOT_USERNAME=anosh   -e MONGO_INITDB_ROOT_PASSWORD=3214   -v mongodb_data:/data/db mongo:4.4

# Create a Docker network for the containers
docker network create url-shortener-network

# Connect MongoDB to the network
docker network connect url-shortener-network mongodb

# Clone the repository (if you haven't already)
git clone https://github.com/Anoshpshroff/Load-Balanced-URL-Shortener.git
cd Load-Balanced-URL-Shortener

# Build the URL shortener container
docker build -t url-shortener .

# Start the URL shortener container
docker run -d --name url-shortener -p 8000:8000   --network url-shortener-network   -e MONGO_USER=anosh -e MONGO_PASSWORD=3214   url-shortener

# Service is now available at http://localhost:8000
```

... (truncated for length, rest of README continues)
