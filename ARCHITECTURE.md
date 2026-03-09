# System Architecture
#test
```mermaid
graph TD
    Client[Browser/Curl] -->|HTTP| API[FastAPI - src/main.py]
    API -->|Routes| R[src/routes/tasks.py]
    R -->|Logic| S[src/services/task_service.py]
    S -->|Validation| M[src/models/task.py]
    S -->|State| DB[(In-Memory Store)]
