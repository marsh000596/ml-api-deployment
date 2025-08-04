# ML API Deployment with FastAPI & Docker 🚀

A production-ready pipeline to serve machine learning models using FastAPI, Docker, and GitHub Actions.

## Features

- FastAPI-based REST API
- Dockerized for portability
- CI/CD with GitHub Actions
- Ready for AWS EC2 or Render deployment

## Usage

```bash
docker build -t ml-api .
docker run -d -p 8000:8000 ml-api
