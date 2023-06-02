# API Documentation

Below is the documentation for the API that can be used in this project. The API consists of the following endpoints:

| Endpoint   | Method | Content Type     | Description                                   |
| ---------- | ------ | ---------------- | --------------------------------------------- |
| `/`        | GET    | None             | Provides information about TaniTama Indonesia |
| `/predict` | POST   | application/json | Makes predictions using the deployed model    |

## Endpoint `/`

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

## Endpoint `/predict`

- **Method**: POST
- **Content Type**: application/json

**Description**: This endpoint is used to make predictions using the deployed model.

Example Request:

```
POST http://localhost:8881/predict
Content-Type: application/json

{
    "input": "data to be predicted"
}
```

Example Response:

```
Status: 200 OK
Content-Type: application/json

{
    "prediction": "prediction result"
}
```

Note: Make sure to send data in the expected format in the request body. Replace "data to be predicted" with the actual data you want to predict.

You can use HTTP libraries or tools like cURL or Postman to send requests to these endpoints.

Make sure to replace the base URL and port with the appropriate address for your API implementation.

## Conclusion

With this documentation, you can use the `/` endpoint to get information about TaniTama Indonesia and use the `/predict` endpoint to make predictions using the deployed model.

Please note that this is an example documentation and you should adjust it to match your own API implementation and specifications.
