# Library Management System API

This is a custom Library Management System API built using Python's FastAPI framework. It allows you to manage student records within a library.

## Features

- Create a new student record.
- Retrieve a list of students with optional filters (country, age).
- Get details of a specific student by ID.
- Update student information.
- Delete a student record.

## API Endpoints

### Create Student

- **Endpoint:** `POST /students`
- **Summary:** Create a new student.
- **Request Body:**

  ```json
  {
    "name": "string",
    "age": "integer",
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```

- **Responses:**
  - `201`: Successful Response
    ```json
    {
      "name": "string",
      "age": "integer",
      "address": {
        "city": "string",
        "country": "string"
      },
      "id": "string"
    }
    ```
  - `422`: Validation Error

### Get Students

- **Endpoint:** `GET /students`
- **Summary:** Retrieve a list of students.
- **Query Parameters:**
  - `country` (optional): Filter students by country.
  - `age` (optional): Filter students by age.
- **Responses:**
  - `200`: Successful Response
    ```json
    [
      {
        "name": "string",
        "age": "integer",
        "address": {
          "city": "string",
          "country": "string"
        },
        "id": "string"
      }
    ]
    ```
  - `422`: Validation Error

### Get Student by ID

- **Endpoint:** `GET /students/{id}`
- **Summary:** Retrieve a student by ID.
- **Path Parameters:**
  - `id` (required): The ID of the student.
- **Responses:**
  - `200`: Successful Response
    ```json
    {
      "name": "string",
      "age": "integer",
      "address": {
        "city": "string",
        "country": "string"
      },
      "id": "string"
    }
    ```
  - `422`: Validation Error

### Update Student

- **Endpoint:** `PATCH /students/{id}`
- **Summary:** Update student information.
- **Path Parameters:**
  - `id` (required): The ID of the student.
- **Request Body:**
  ```json
  {
    "name": "string",
    "age": "integer",
    "address": {
      "city": "string",
      "country": "string"
    }
  }
  ```
- **Responses:**
  - `204`: Successful Response
  - `422`: Validation Error

### Delete Student

- **Endpoint:** `DELETE /students/{id}`
- **Summary:** Delete a student record.
- **Path Parameters:**
  - `id` (required): The ID of the student.
- **Responses:**
  - `200`: Successful Response
  - `422`: Validation Error

## Schemas

### Student

```json
{
  "name": "string",
  "age": "integer",
  "address": {
    "city": "string",
    "country": "string"
  }
}
```

### StudentInDB

```json
{
  "name": "string",
  "age": "integer",
  "address": {
    "city": "string",
    "country": "string"
  },
  "id": "string"
}
```

### Address

```json
{
  "city": "string",
  "country": "string"
}
```

### HTTPValidationError

```json
{
  "detail": [
    {
      "loc": ["string", "integer"],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

### ValidationError

```json
{
  "loc": ["string", "integer"],
  "msg": "string",
  "type": "string"
}
```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/eternal-titan-7/Library-Managment-System---Cosmocloud.git
   cd Library-Managment-System---Cosmocloud
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:

   ```sh
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
