Here's the README in English:

---

# Django EventsPipe

**Django EventsPipe** is a Django app designed to manage, log, and stream events in a structured and scalable way. Ideal for systems requiring an event log and notifications (like user actions, data changes, or system events).

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Event Management**: Create, log, and manage structured events within the system.
- **Event Pipeline**: Configure flows to manage, forward, and process events.
- **Easy Integration**: Simple setup as a Django app with configurable settings for flexibility.
- **Notifications & Logging**: Automatic notifications and logging based on app configuration.

## Requirements

- **Python**: >= 3.7
- **Django**: >= 3.0

## Installation

1. Clone the repository into your Django project:
   ```bash
   git clone https://github.com/r3vn/django-eventspipe.git
   ```

2. Add the app to Django's `INSTALLED_APPS`:
   ```python
   # settings.py
   INSTALLED_APPS = [
       ...,
       'django_eventspipe',
   ]
   ```

3. Apply migrations to create the necessary tables:
   ```bash
   python manage.py migrate
   ```

## Configuration

**django-eventspipe** can be configured through variables in the `settings.py` file. Here is a sample configuration:

```python
# Configure log level and other optional settings
EVENTS_PIPE_CONFIG = {
    "LOG_LEVEL": "INFO",  # Levels: DEBUG, INFO, WARNING, ERROR
    "ENABLE_NOTIFICATIONS": True,
    "DEFAULT_HANDLER": "django_eventspipe.handlers.DefaultEventHandler",
}
```

### Configuration Variables

- **`LOG_LEVEL`**: Sets the logging level for events. Default: `INFO`.
- **`ENABLE_NOTIFICATIONS`**: Enables automatic notifications for events if `True`.
- **`DEFAULT_HANDLER`**: The default handler for events.

## Usage

### Creating an Event

You can create and send an event by calling the `send_event` function:

```python
from django_eventspipe import send_event

send_event(
    event_type="user_login",
    data={
        "username": "testuser",
        "login_time": "2024-10-28 10:30:00",
    },
)
```

### Custom Event Handlers

To create a custom event handler, extend the `EventHandler` class and override the `handle` method:

```python
from django_eventspipe.handlers import EventHandler

class CustomEventHandler(EventHandler):
    def handle(self, event):
        # Logic for handling a custom event
        print(f"Custom handling for event: {event}")
```

Configure the new handler in `settings.py`:
```python
EVENTS_PIPE_CONFIG = {
    "DEFAULT_HANDLER": "path.to.CustomEventHandler",
}
```

## API

### `send_event(event_type, data, handler=None)`

- **event_type**: `str` - Type of event (e.g., `"user_login"`, `"data_update"`).
- **data**: `dict` - Dictionary containing data associated with the event.
- **handler**: `EventHandler` (optional) - Handler for the specific event.

**Example:**
```python
send_event(
    event_type="user_signup",
    data={
        "username": "newuser",
        "email": "newuser@example.com",
    },
)
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the project.
2. Create a new branch for your changes.
3. Submit a pull request describing the changes.

## License

This project is licensed under the MIT License.

---

This README covers the essential information for using and configuring **django-eventspipe** and can be further enhanced with more detailed examples or additional sections if needed.
