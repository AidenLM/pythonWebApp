
# Disaster Aid Coordination Web App

![App Screenshot](./Screenshot%202025-05-13%20at%2000.03.17.png)

This is a disaster aid coordination platform built using **Python (Flask)** for the backend and **React.js** for the frontend. The goal of this application is to provide a real-time, location-based communication tool for those in need and those offering help during emergency or disaster scenarios.

---

## Features

- ✉ **Message Submission**: Users can submit messages indicating what aid they need or what they can offer.
- 📍 **Location Tracking**: Messages are tagged with district names and plotted on an interactive map using Leaflet and OpenStreetMap.
- 📅 **Real-Time Updates**: Recent messages are displayed instantly with timestamp and category labels ("Need" or "Offer").
- ⭐ **Filter View**: Easily toggle between messages offering aid or requesting help.
- 🔍 **Clean UI**: A simple and responsive layout for quick usage in critical situations.

---

## Tech Stack

**Frontend**
- React.js
- Leaflet.js
- Bootstrap (or Tailwind depending on branch)

**Backend**
- Python
- Flask
- SQLite (or JSON-based local storage for testing)

---

## How to Run

### 1. Backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 2. Frontend (React)
```bash
cd frontend
npm install
npm start
```

Then visit: [http://localhost:3000](http://localhost:3000)

---

## Contribution

Feel free to fork the repository, open issues, and submit pull requests to improve the app. Suggestions for better geolocation, scalability, and real-time WebSocket integration are welcome.

---

## License

MIT License.

---

## Author

- GitHub: [AidenLM](https://github.com/AidenLM)
