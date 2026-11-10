# Centralized Observability Platform

A full observability stack built with Docker Compose, Prometheus, Grafana, Loki, Promtail and Flask.

## Features

- Infrastructure monitoring
- Application monitoring
- Metrics collection
- Centralized log aggregation
- Real-time dashboards
- Dockerized deployment

## Architecture

<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/4c56e4b9-5336-4535-b8ec-787c212b59ce" />


## Technology Stack

- Docker
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Node Exporter
- Flask

## Monitoring

### Infrastructure Metrics

- CPU Usage
- RAM Usage
- Disk Usage
- Network Traffic

### Application Metrics

- Total HTTP Requests
- Requests Per Second

### Log Aggregation

- Flask application logs
- Loki centralized storage
- Grafana log exploration

## Quick Start

```bash
docker compose up -d --build
```

## Services

| Service | URL |
|----------|----------|
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Flask App | http://localhost:5000 |
| Loki | http://localhost:3100 |
