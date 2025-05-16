# Microblogging platform like Twitter (Ualá Test)

Microblogging platform API similar to Twitter. It's a MVP project, it allows users to follow other users, create publications and view publications from followed users in a timeline. 

## Using Docker to run/test the application

### Requirements

- Docker (tested in version 28.1.1 but should not be a problem in older ones).

### Build Docker image

Since the image needed for this project is not available online, you must build it locally executing the next command from the root of the project:
```sh
docker build -t social-network .
```

### Running the application with Docker

Execute the application.
```sh
docker run --rm -p 8080:8080 social-network
```

The application will be available at http://localhost:8080.

Swagger UI will be available at http://localhost:8080/docs.

### Running the unit tests with Docker

Executing the next command unit tests will be applied and shown:
```
docker run --rm -t social-network unittest -v
```

## Locally running/testing the application

### Requirements

- Python >= 3.10
- fastapi == 0.115.12 (installed with requirements.txt)
- pydantic == 2.11.4 (installed with requirements.txt)
- uvicorn == 0.34.2 (installed with requirements.txt)

**NOTE**: All the commands below this section must be executed from the root of this project.

### Running the application locally

Install the dependencies.
```
pip install -r requirements.txt
```

Execute the application.
```
uvicorn main:app --host 0.0.0.0 --port 8080
```

The application will be available at http://localhost:8080.

Swagger UI will be available at http://localhost:8080/docs.

### Running the unit tests locally

Execute unit tests from the root of the project.
```
python -m unittest -v
```
