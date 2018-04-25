# Website statistics

This program aims to collect websites events which represent the user and the pages they visit,
and return KPIs on their activity on the website.

## Usage
A Makefile has been created to facilitate the usage of `docker` and `docker-compose` commands.

### Prerequisites

- Docker
- docker-compose

### Build and run

To build the stack (this step is optional as the run command will build the stack anyway):
```bash
make build
```

To run the stack:
```bash
make run
```

### Stop and clean

To stop the stack:
```bash
make stop
```

To clean the created containers:
```bash
make clean
```

To clean all created untagged images:
```bash
make clean-dangling-images
```

### Test suite

To start syntax checks tests:
```bash
make syntax-check
```

To start typing checks tests:
```bash
make typing-check
```

To launch unit and integration tests:
```bash
make tests
```

## Endpoints

Index endpoint:
```bash
GET /
```
Response:
```bash
It works!
```

Ping endpoint:
```bash
GET /ping
```
Response:
```bash
pong
```

New event endpoint:
```bash
POST /v1/page
{
  "user_id": "019mr8mf4r",
  "name": "Pricing Page",
  "timestamp": "2018-04-23T00:31:12.984Z"
}
```
Response:
```bash
{
    "message": "Success"
}
```

User statistics endpoint:
```bash
GET /v1/users/:user_id
```
Response:
```bash
{
    "most_viewed_page_last_7_days": "Pricing Page",
    "number_of_days_active_last_7_days": 1,
    "number_pages_viewed_the_last_7_days": 2,
    "time_spent_on_site_last_7_days": 8h,
    "user_id": "019mr8mf4r"
}
```

Delete user events endpoint:
```bash
DELETE /v1/users/:user_id
```
Response:
```bash
{
    "deleted_records": 2
}
```
