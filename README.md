# URL-Shortener
# URL Shortener Service

A containerized URL shortening service built with FastAPI and Redis. This service allows you to create short URLs for sharing long links more efficiently.

---

## 📚 Table of Contents

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

---

## 🚀 Features

- **URL Shortening**: Convert long URLs into compact, shareable links.
- **Custom Short IDs**: Define your own memorable short URL identifiers.
- **Persistent Storage**: Redis backend ensures fast and temporary storage of URL mappings.
- **Containerized**: Fully Dockerized for easy deployment in any environment.
- **Fast Redirects**: Optimized lookups for quick redirection.
- **Simple REST API**: Easy-to-use JSON API for programmatic access.

---

## 🛠 Prerequisites

- Docker installed on your system ([Get Docker](https://docs.docker.com/get-docker/))
- Basic familiarity with terminal/command line

---

## ⚡ Quick Start Guide (Copy-Paste)

For those who just want to get it running quickly:

```bash
# Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# Start the application using Docker Compose
docker-compose up --build
