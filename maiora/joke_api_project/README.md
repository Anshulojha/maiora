# Joke API Project

This project is a FastAPI application that fetches jokes from the JokeAPI, processes them, and stores them in an SQLite database.

---

## Table of Contents

1. [Overview](#overview)
2. [Setup and Installation](#setup-and-installation)
3. [How to Run the Program](#how-to-run-the-program)
4. [SQL Validation Queries](#sql-validation-queries)
5. [Assumptions and Decisions](#assumptions-and-decisions)
6. [License](#license)

---

## Overview

This project consists of a FastAPI application that fetches jokes from the JokeAPI and stores them in an SQLite database. The process includes:

- **Extract**: Fetches data from JokeAPI.
- **Transform**: Processes the jokes and extracts:
    - `category`
    - `type`
    - `joke` (if type is "single") or `setup` and `delivery` (if type is "twopart")
    - Flags for `nsfw`, `political`, `sexist`, `safe`
    - `lang`
- **Load**: Stores the transformed data in an SQLite database (`jokes.db`).
- **Validate**: SQL queries are provided to validate the data in the database.

---

## Setup and Installation

Before running the script, ensure the following dependencies are installed:

1. **Python 3.8+**
2. **FastAPI**
    - Install via pip:
      ```bash
      pip install fastapi
      ```
3. **Uvicorn** (ASGI server for FastAPI)
    - Install via pip:
      ```bash
      pip install uvicorn
      ```
4. **SQLAlchemy** (for database interactions)
    - Install via pip:
      ```bash
      pip install sqlalchemy
      ```
5. **Pydantic** (data validation)
    - Install via pip:
      ```bash
      pip install pydantic
      ```
6. **httpx** (for making HTTP requests to JokeAPI)
    - Install via pip:
      ```bash
      pip install httpx
      ```

Additionally, ensure that the following files are included in the repository:

- `app/main.py` (FastAPI application file)
- `jokes.db` (SQLite database where jokes will be stored)

---

## How to Run the Program

1. **Clone the repository** or download the script to your local machine:
   ```bash
   git clone <repo_link>
   ```
2. **Navigate to the project directory:**
   ```bash
   cd joke-api-project
   ```
3. **Set Up a Virtual Environment (optional but recommended):**
   
   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. **Access the API Documentation (Optional):**
   FastAPI automatically generates API documentation using Swagger UI. You can access it by visiting:
   ```bash
   http://127.0.0.1:8000/docs
   ```

7. **Fetch Jokes and Store in Database:**
   - Call the following endpoint to fetch jokes from JokeAPI and store them in the SQLite database:
     ```bash
     GET /fetch-jokes
     ```
   - You can make this request either by:
     - Visiting the URL in your browser: [http://127.0.0.1:8000/fetch-jokes](http://127.0.0.1:8000/fetch-jokes)
     - Using an API client like Postman or cURL:
       ```bash
       curl -X GET http://127.0.0.1:8000/fetch-jokes
       ```

---

## SQL Validation Queries

Once the data is loaded into the SQLite database, you can use the following SQL queries to validate the data:

- **Count the Total Number of Records:**
  ```sql
  SELECT COUNT(*) FROM jokes;
  ```
- **Find the Total Jokes by Category:**
  ```sql
  SELECT category, COUNT(*) AS total_jokes_by_category
  FROM jokes
  GROUP BY category;
  ```
- **Find the Average Joke Length:**
  ```sql
  SELECT AVG(LENGTH(joke)) AS avg_joke_length FROM jokes;
  ```
- **Ensure There Are No Duplicate Jokes:**
  ```sql
  SELECT joke, COUNT(*)
  FROM jokes
  GROUP BY joke
  HAVING COUNT(*) > 1;
  ```
- **Retrieve All Safe Jokes:**
  ```sql
  SELECT * FROM jokes WHERE safe = 1;
  ```

---

## Assumptions and Decisions

- **Data Integrity:** All jokes fetched from JokeAPI are stored in the database. We ensure there are no duplicate jokes by checking for the `joke` field.
- **Database Choice:** SQLite is used as it is lightweight and requires no additional setup, making it ideal for small-scale projects like this.
- **API Limitation:** We fetch a minimum of 100 jokes from the JokeAPI.
- **Error Handling:** If the JokeAPI fetch fails, the process stops, and an error message is returned.

---

## License

This project is not under any License.

