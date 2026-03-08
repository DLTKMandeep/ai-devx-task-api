# AI-Driven Task Management API (Python + FastAPI)

This repository is a **learning project** to build an end-to-end, AI-augmented developer experience:
- Multi-cloud ready (starting with AWS)
- Multi-stage DevX: planning → coding → testing → review → deploy
- Python-based API using FastAPI

## Goals

1. Learn how to infuse AI into each step of the dev lifecycle.
2. Build a real Task Management API.
3. Set up:
   - Devcontainers
   - GitHub Actions (CI)
   - Pulumi (AWS)
   - AI-assisted coding, testing, and reviews

## Stack

- Language: Python 3.12
- API: FastAPI
- Tests: pytest
- Infra: Pulumi (Python)
- Cloud: AWS
- Container: Docker
- Dev Environment: Devcontainer

## High-Level API

- `POST /tasks` – create a task
- `GET /tasks` – list tasks
- `GET /tasks/{id}` – get a task by ID
- `PUT /tasks/{id}` – update a task
- `DELETE /tasks/{id}` – delete a task
- `POST /tasks/{id}/assign` – assign a task to a user

We will iterate on this README as we build out the platform.# ai-devx-task-api
AI devx 
