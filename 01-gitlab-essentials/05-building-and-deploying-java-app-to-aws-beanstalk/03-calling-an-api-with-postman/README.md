# Calling an API with Postman

## Table of Contents

- [Introduction](#introduction)
- [Getting Started with Postman](#getting-started-with-postman)
- [Importing Collections and Environments](#importing-collections-and-environments)
- [Activating the Localhost Environment](#activating-the-localhost-environment)
- [Working with the Cars API](#working-with-the-cars-api)
   - [CRUD Operations](#crud-operations)
   - [Additional Endpoints](#additional-endpoints)
- [Understanding Responses](#understanding-responses)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to this beginner-friendly guide on using Postman to call APIs! Postman is a powerful tool for API testing, allowing users to send requests to web servers and receive responses. This guide focuses on a practical example: the Cars API. By the end of this document, you'll understand how to import collections and environments into Postman, make various types of requests, and interpret the responses. Whether you're a developer, tester, or just curious about APIs, this guide is for you!

## Getting Started with Postman

Postman is an interactive tool for testing APIs. To begin, download and install Postman from their [official website](https://www.postman.com/downloads/). Once installed, open Postman to import the necessary files for our API.

## Importing Collections and Environments

### Steps:

1. Open Postman.
2. Click on 'Import'.
3. Select the 'Cars API' collection and 'Localhost' environment files.

After importing, you should see the 'Cars API' under collections and 'Localhost' under environments in Postman.

### Example of Localhost Environment:

```json
{
	"id": "6778ac6a-0aa8-464c-87ae-4f72578a9313",
	"name": "Localhost",
	"values": [
		{
			"key": "baseUrl",
			"value": "http://localhost:5000",
			"enabled": true
		}
	],
	"_postman_variable_scope": "environment",
	"_postman_exported_at": "2020-02-12T15:59:45.951Z",
	"_postman_exported_using": "Postman/7.16.0"
}
```

## Activating the Localhost Environment

After importing the Localhost environment, it's important to activate it for your API calls.

### Steps:

1. Go to the top-right corner of Postman.
2. In the environment dropdown, select 'Localhost'.
3. This action will enable the environment variables, such as 'baseUrl', for use in your API requests.

## Working with the Cars API

### CRUD Operations

CRUD stands for Create, Retrieve, Update, and Delete - essential operations for most APIs.

#### Example Requests:

1. **Get All Cars**: Retrieves a list of cars from the database.

- Method: POST
- Endpoint: `{{baseUrl}}/cars/`
- Response Example:

```json
[
    {
        "id": 1,
        "manufacturer": "Ford",
        "model": "Model T",
        "build": 1927
    },
    {
        "id": 2,
        "manufacturer": "Tesla",
        "model": "Model 3",
        "build": 2017
    },
    {
        "id": 3,
        "manufacturer": "Tesla",
        "model": "Cybertruck",
        "build": 2019
    }
]
```

2. **Add Car**: Adds a new car to the database.

- Method: POST
- Endpoint: `{{baseUrl}}/cars`
- Request Body:

```json
{
    "manufacturer": "Dacia",
    "model": "Logan",
    "build": 2000
}
```

- Response Example:

```json
{
    "id": 4,
    "manufacturer": "Dacia",
    "model": "Logan",
    "build": 2000
}
```

3. **Get Single Car**: Retrieves details of a specific car.

- Method: GET
- Endpoint: `{{baseUrl}}/cars/3`
- Response Example:

```json
{
    "id": 3,
    "manufacturer": "Tesla",
    "model": "Cybertruck",
    "build": 2019
}
```

4. **Delete Car**: Removes a car from the database.

- Method: DELETE
- Endpoint: `{{baseUrl}}/cars/3`
- Response Example:

```bash
Status: 200 OK
```

### Additional Endpoints

1. **Statistics**: Provides data such as the average age of the vehicles.

- Method: GET
- Endpoint: `{{baseUrl}}/statistics/age`
- Response Example:

```json
{
    "vehicles": 3,
    "age": 32.333333333333336
}
```

2. **Health Check**: Indicates if the server is up and running.

- Method: GET
- Endpoint: `{{baseUrl}}/actuator/health`
- Response Example:

```json
{
    "status": "UP"
}
```

## Understanding Responses

Postman displays responses in a clear, readable format. For instance, a GET request to the Cars endpoint will show a JSON response with a list of cars.

## Conclusion

This guide has walked you through the basics of using Postman to interact with an API. With the Cars API as an example, you've learned how to import collections and environments, make different types of requests, and understand the responses. Experiment with these concepts to deepen your understanding.

## References

- [Postman Learning Center](https://learning.postman.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API)