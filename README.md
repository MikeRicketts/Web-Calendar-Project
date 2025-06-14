# Flask Event Manager API

This is a simple RESTful API built with Flask and Flask-RESTful for managing events. Users can create, view, filter, and delete calendar events by date.

## Features

- Add an event with a name and date
- View all events or filter events by a date range
- View events scheduled for today
- Retrieve or delete an event by its ID

## Requirements

- Python 3.x
- Flask
- Flask-RESTful

## How to Run

1. Install dependencies:
    ```
    pip install flask flask-restful
    ```

2. Start the server (default localhost:5000):
    ```
    python app.py
    ```

3. Optionally, run with a custom host and port:
    ```
    python app.py 0.0.0.0:8000
    ```

## API Endpoints

- `POST /event` — Create a new event  
- `GET /event` — List all events or filter by start and end dates  
- `GET /event/today` — List today's events  
- `GET /event/<id>` — Get a specific event  
- `DELETE /event/<id>` — Delete a specific event

