# Calendar

## Project details
### Development environment
- Visual Studio Code 1.61.2
- Docker Desktop 4.1.1
### Dependencies
- Docker Engine 19.03
- Python 3.10
- django 3.2.8
- postgres 14.0
- psycopg2 2.9.1
### Minimum viable product
- Have a live calendar to track staff assignments and availability in real time
### Stretch features
- Approvals system for calendar changes
- Generate calendars in PDF format suitable for printing for clients
- Comment threads/discussion on calendar events
- Wiki style knowledge base
- File storage/sharing
- Timesheet entry/tracking
- Invoice generation

## Fictional company
- Named Generic Company Ltd., GC for short
- Stock photos with free to use licences taken from https://www.pexels.com/
- Logo designed using https://boxy-svg.com/app
- .svg converted to .ico using https://redketchup.io/icon-converter

## Commands
- Build without cache: `docker-compose build --no-cache`
- Build and run: `docker-compose up --build`
- Create superuser in django: `docker-compose run django python manage.py createsuperuser`

## Model for MVP
### Object overview
- **Profile:** extends the default django user model
- **Client:** represents companies that work is done for
- **Project:** represents work given by clients
- **Booking:** assigns engineers to projects
