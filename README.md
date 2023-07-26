# Elevator System

The Elevator System is a simplified elevator model implemented using Django and Django REST Framework. It allows users to control multiple elevators and make requests to move the elevators between floors.

## Features

- Initialize the elevator system with a specified number of elevators.
- Each elevator can move up and down, open and close its door, start and stop running, and display its current status.
- The system decides which elevator to associate with which floor and marks elevators as available or busy.
- Elevators can be marked as operational or under maintenance.
- Users can make requests to the elevators to move to specific floors.
- The system automatically determines the most optimal elevator to handle user requests based on the current state of the elevators and the requested floors.

## Requirements

- Python (3.6 or higher)
- Django (3.0 or higher)
- Django REST Framework (3.11 or higher)
- Postgres (optional, for database storage)
- Redis (optional, for caching)

## Installation

1. Run setup.sh file to setup the project:

```
chmod +x setup.sh
source setup.sh
```

2. The API will be available at `http://localhost:8000/`.

## API Endpoints

- `GET api/elevators/`: List all elevators or create a new elevator.
- `GET api/elevators/{id}/`: Retrieve details of a specific elevator.
- `POST api/elevators/{id}/move_up/`: Move an elevator up to the next destination.
- `POST api/elevators/{id}/move_down/`: Move an elevator down to the next destination.
- `POST api/elevators/{id}/open_door/`: Open the door of an elevator.
- `POST api/elevators/{id}/close_door/`: Close the door of an elevator.
- `GET api/elevators/{id}/get_next_destination/`: Get the next destination floor for an elevator.
- `POST api/elevators/{id}/associate_floor/`: Associate an elevator with a specific floor.
- `POST api/elevators/{id}/mark_maintenance/`: Mark an elevator as under maintenance.
- `GET api/floors/`: List all floors or create a new floor.
- `GET api/floors/{id}/`: Retrieve details of a specific floor.

## Usage

1. Initialize the Elevator System by creating elevators with the desired number of floors.
2. Users can make requests to move elevators to specific floors using the provided API endpoints.
3. The system will automatically determine the best elevator to handle each user request based on the current state of the elevators and the requested floors.
4. Elevators can be marked as under maintenance when needed, and the system will exclude them from user requests until they are marked operational again.

## Contributing

Contributions to this project are welcome. Please create a pull request with your proposed changes, and they will be reviewed.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Please note that this is a simplified example of a README file, and you can customize it further based on your specific project details and requirements.
