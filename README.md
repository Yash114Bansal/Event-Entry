# Backend for Event Attendance App

This repository contains the backend system utilized for managing attendance during the ITeR8 event organized by Software Incubator (SDC-SI). It effectively handled approximately 150 attendees, ensuring smooth and efficient attendance tracking.

## Key Features

### 🔷 User Authentication
- Enhanced security is ensured through the implementation of JSON Web Tokens (JWT) for user authentication, safeguarding the system from unauthorized access.

### 🔷 Day-wise Attendance Tracking
- The system seamlessly tracks attendance on a day-to-day basis, providing a comprehensive overview of candidate participation throughout the event duration.

### 🔷 Attendee and Absentee List Retrieval
- Easily retrieve lists of attendees and absentees, facilitating efficient management of event participation.

## Frontend
The frontend for this application is developed by Rachit Katiyar ([rockyhappy](https://github.com/rockyhappy)). You can find the frontend repository at [Choco-Chip-Reader](https://github.com/rockyhappy/Choco-Chip-Reader).

## Usage with Docker

1. **Clone the Repository**
   - `git clone https://github.com/Yash114Bansal/Event-Entry.git`
   
2. **Set Environment Variables**
   - Set the following environment variables:
     - `SECRET_KEY`: Django secret key for security.
     - `ALLOWED_HOST`: Hostname or IP addresses allowed to serve the application.
   
3. **Build and Start the Docker Containers**
   - `cd evententry`
   - `docker-compose up --build`

## Screenshots
![Screenshot](evententry/docs/ScreenShot.png)

## Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.
