# URL Shortener Service

A containerized URL shortening service built with FastAPI and Redis. This service allows you to create short URLs for sharing long links more efficiently.

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
- **Persistent Storage**: Redis backend ensures URLs are preserved during container uptime
- **Containerized**: Fully Dockerized for easy deployment in any environment
- **Fast Redirects**: Optimized lookups for quick redirection to original URLs
- **Simple REST API**: Easy-to-use JSON API for programmatic access

## Prerequisites

- Docker installed on your system ([Get Docker](https://docs.docker.com/get-docker/))
- Basic familiarity with terminal/command line

## Quick Start Guide (Copy-Paste)

```bash
# Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# Start everything using Docker Compose
docker-compose up --build
```

After running these commands, your URL shortener will be available at:

```
http://localhost:8000
```

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Start the Redis Container (Handled by Docker Compose)

No separate setup needed. The `docker-compose.yml` includes Redis.

### 3. Build and Run the App

```bash
docker-compose up --build
```

This will:
- Start Redis
- Build and run the FastAPI app
- Expose the app on port `8000`

### 4. Verify Containers

```bash
docker ps
```

You should see:
- `redis`
- `url-shortener`

## How to Use the URL Shortener

### Creating a Short URL

```bash
curl -X POST "http://localhost:8000/shorten"   -H "Content-Type: application/json"   -d '{"long_url": "https://www.example.com/very/long/url/that/needs/shortening"}'
```

Sample response:

```json
{
  "short_url": "http://localhost:8000/XyZ1234", 
  "long_url": "https://www.example.com/very/long/url/that/needs/shortening"
}
```

### Creating a Custom Short URL

```bash
curl -X POST "http://localhost:8000/shorten"   -H "Content-Type: application/json"   -d '{"long_url": "https://github.com/your-username/url-shortener", "custom_id": "github"}'
```

Sample response:

```json
{
  "short_url": "http://localhost:8000/github", 
  "long_url": "https://github.com/your-username/url-shortener"
}
```

### Using Your Short URLs

Simply visit:

```
http://localhost:8000/github
```

Or test with curl:

```bash
curl -L "http://localhost:8000/github"
```

## Data Persistence

Redis stores your short URLs in memory. To persist data across container restarts:

1. Add a named volume in `docker-compose.yml`:
```yaml
volumes:
  - redis_data:/data
```

2. Add the volume definition:
```yaml
volumes:
  redis_data:
```

This ensures the data inside Redis survives restarts as long as the volume is not deleted.

## Viewing and Managing Your Data

### Access Redis CLI

```bash
docker exec -it redis redis-cli
```

### View Keys

```redis
KEYS *
```

### View a Specific Short URL

```redis
GET github
```

## Troubleshooting

### If Containers Won't Start

Check for existing containers:

```bash
docker ps -a
```

Stop and remove them:

```bash
docker stop redis url-shortener
docker rm redis url-shortener
```

### If URLs Don’t Work

Check logs:

```bash
docker logs url-shortener
docker logs redis
```

Check for active ports:

```bash
docker ps
```

## Advanced Usage

### Docker Compose (Recommended)

Bring everything up:

```bash
docker-compose up -d
```

Shut everything down:

```bash
docker-compose down
```

You can also rebuild the containers with:

```bash
docker-compose up --build
```

## Technical Details

- **FastAPI**: Modern web framework for high-performance APIs
- **Redis**: In-memory key-value store
- **ShortUUID**: Generates unique short identifiers
- **Uvicorn**: ASGI server for FastAPI
- **Docker & Docker Compose**: Containerized development and deployment

### How It Works

1. User submits a long URL via POST `/shorten`
2. A random (or custom) ID is generated
3. The pair is stored in Redis
4. The GET endpoint retrieves and returns the long URL

## License

MIT License — free to use, modify, and distribute.
