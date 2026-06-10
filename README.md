# 🌤️Global Weather Application

A dynamic, real-time web application built with Python and Flask that allows users to fetch instant weather updates for any city globally by integrating the **OpenWeatherMap REST API**.

## 🚀 Key Features
* **Global Search Scope:** Fetches data for any city across the world using standardized query handling.
* **REST API Integration:** Implements live HTTP requests to retrieve real-time weather matrices (Temperature, Humidity, Wind Speed, Weather Status).
* **Robust Error Handling:** Native catch blocks to handle invalid API keys, down networks, and non-existent city exceptions seamlessly without crashing the server.
<img width="583" height="592" alt="Screenshot 2026-06-10 125450" src="https://github.com/user-attachments/assets/977d6da0-fd7a-442f-a6b7-f13fc1eb0437" />


---

## 🧠 Concepts Covered & Learning Journey

This project was built to master external API communications and dynamic data parsing in backend systems. To resolve deployment environment mismatches on Cloud platforms (like Render dependencies) and structure python environment parameters, I systematically integrated information from **Google developer documentations** and utilized **AI assistance (Gemini/ChatGPT)** for logic debugging.

Key technical concepts implemented include:
* **HTTP Client Request Engine:** Utilizing Python's `requests` library to handle network-level connection protocols.
* **JSON Payload Parsing:** Decoding complex multi-nested JSON structures sent by OpenWeather servers into optimized local Python dictionaries.
* **Exception & Edge-Case Management:** Writing defensive blocks using `try-except` structures and HTTP status code tracking (`200 OK`, `401 Unauthorized`, `404 Not Found`).

---

## 🛠️ Tech Stack Used

* **Backend Framework:** Python 3.x, Flask
* **API Integration Tool:** Python `requests` library
* **Production Server:** Gunicorn (WSGI HTTP Server)
* **Frontend UI:** Modern Semantic HTML5, Embed CSS3 UI

---

## 💻 Setup and Installation

1. **Clone the project:**
   ```bash
   git clone [https://github.com/qudsiyashaikh/Weather-App-API.git](https://github.com/qudsiyashaikh/Weather-App-API)
   
