# Banknote Authenticator

## Running the API

1. Build the docker image

    ```bash
    docker build -t banknote-authenticator .
    ```

2. Run the docker image

    ```bash
    docker run -d -p 5000 banknote-authenticator
    ```

## Testing the API

After Running the API container with the above command, the API can be accessed through `http://localhost:5000/authentication` REST endpoint.

### Request

The API anticipates a GET request, with a JSON body like the following.

```JSON
{
    "skewness": 0.03,
    "curtosis": 0.12,
    "entropy": 0.02
}
```

### Response

The API responds with a JSON object like the following, and with a status code `200`.

```JSON
{
    "output": 0.9973539654815496
}
```
