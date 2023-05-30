# Tanitama-Endpoint-Model

| Endpoint   | Method | Content-Type            | Description                                      |
|------------|--------|-------------------------|--------------------------------------------------|
| /          | GET    | text/html; charset=utf-8| Dokumentasi Model API                            |
| /rice-leaf | POST   | multipart/form-data     | This endpoint allows you to make predictions using the trained machine learning model on image inputs. |

#### Request:

Form Parameters:

| Parameter | Type | Description              |
|-----------|------|--------------------------|
| image     | file | The image file for prediction. |

Example Request:

```
POST /rice-leaf
Content-Type: multipart/form-data

[image file]
```

#### Response:

- Content-Type: application/json

Body Parameters:

| Parameter  | Type   | Description                                 |
|------------|--------|---------------------------------------------|
| prediction | String | The predicted class label for the input image. |

Example Response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "prediction": "0"
}
```

#### Error Responses:

| HTTP Status Code | Description                                     |
|------------------|-------------------------------------------------|
| 400 Bad Request  | Invalid request body or unsupported image format. |
| 500 Internal Server Error | An error occurred while processing the prediction. |

Example Error Response (400 Bad Request):

```
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "Invalid request body or unsupported image format."
}
```

Example Error Response (500 Internal Server Error):

```
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
  "error": "An error occurred while processing the prediction."
}
```