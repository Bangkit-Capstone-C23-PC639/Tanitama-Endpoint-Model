# API Documentation

Below is the documentation for the API used in this project. The API consists of the following endpoints:

| Endpoint   | Method | Content Type     | Description                                   |
| ---------- | ------ | ---------------- | --------------------------------------------- |
| `/`        | GET    | None             | Provides information about TaniTama Indonesia |
| `/predict` | POST   | application/json | Makes predictions using the deployed model    |

## Docker

The API can be run inside a Docker container for easy management and deployment. Make sure Docker is installed in your environment before proceeding.

### Running the API with Docker:

1. Pull the Docker image that has been prepared for this application:

```
docker pull rosyihuddin/leaf-disease-endpoints-model:latest
```

2. Run a Docker container using the downloaded image:

```
docker run -p 8881:8881 rosyihuddin/leaf-disease-endpoints-model:latest
```

This command will run a Docker container and map port 8881 inside the container to port 8881 on your localhost. You can change the port as per your preference.

## Endpoints

Below are the details of each available endpoint in the API:

### Endpoint `/`

- **Method**: GET
- **Content Type**: None

**Description**: This endpoint provides information about TaniTama Indonesia.

Example Request:

```
GET http://localhost:8881/
```

Example Response:

```
Status: 200 OK
Content-Type: application/json

{
    "message": "TaniTama Indonesia"
}
```

### Endpoint `/predict`

- **Method**: POST
- **Content Type**: application/json

**Description**: This endpoint is used to make predictions using the deployed model.

Example Request:

```
POST http://localhost:8881/predict
Content-Type: application/json

{
    "input": "https://content.peat-cloud.com/w400/bacterial-blight-of-rice-rice-1581498954.jpg"
}
```

Example Response:

```
Status: 200 OK
Content-Type: application/json

{
    "prediction": 0
}
```

Note: Make sure to send data in the expected format in the request body. Replace the value of "input" with the URL of the image you want to predict. The response will contain the predicted value.

Please ensure that you have the correct base URL and port when making requests to the endpoints.

## Conclusion

By running the Docker container provided, you can access the two API endpoints to get information about TaniTama Indonesia and make predictions using the deployed model.

Please note that this is an example documentation and you should adjust it to match your own API implementation and specifications.

**Docker Image**: [rosyihuddin/leaf-disease-endpoints-model](https://hub.docker.com/r/rosyihuddin/leaf-disease-endpoints-model)
