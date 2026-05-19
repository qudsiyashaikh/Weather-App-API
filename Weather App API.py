import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Replace this with your actual OpenWeatherMap API Key
API_KEY = "7e9ca7f5ee3e4bdf5e3f749d25f7beb9"

# --- HTML & CSS TEMPLATE ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather App</title>
    <style>
        body { font-family: Arial, sans-serif; background: #e0f2f1; text-align: center; margin-top: 50px; }
        .container { display: inline-block; padding: 30px; background: white; border-radius: 10px; box-shadow: 0px 0px 15px rgba(0,0,0,0.1); width: 400px; }
        input[type="text"] { width: 80%; padding: 10px; margin: 15px 0; border: 1px solid #ccc; border-radius: 5px; font-size: 16px; text-align: center; }
        button { width: 84%; background-color: #00796b; color: white; border: none; padding: 12px; font-size: 16px; font-weight: bold; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #004d40; }
        .weather-box { margin-top: 25px; padding: 15px; border-radius: 5px; background: #f5f5f5; text-align: left; }
        .error { color: #d32f2f; font-weight: bold; margin-top: 20px; }
    </style>
</head>
<body>

<div class="container">
    <h2>🌤️ Weather App</h2>
    <form method="POST">
        <input type="text" name="city" placeholder="Enter City Name (e.g., London)" required autofocus>
        <button type="submit">Search Weather</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if data %}
        <div class="weather-box">
            <h3>Weather in {{ data.city }}, {{ data.country }}</h3>
            <p><strong>Temperature:</strong> {{ data.temp }}°C</p>
            <p><strong>Status:</strong> {{ data.status }}</p>
            <p><strong>Humidity:</strong> {{ data.humidity }}%</p>
        </div>
    {% endif %}
</div>

</body>
</html>
"""

# --- GAME LOGIC ROUTE ---
@app.route('/', methods=['GET', 'POST'])
def weather_app():
    data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        # APIs Concept: Building the endpoint URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        try:
            # Requests Module Concept: Fetching live data from API
            response = requests.get(url)
            # JSON Concept: Parsing response data into a Python dictionary
            weather_json = response.json()

            if weather_json.get("cod") == 200:
                data = {
                    "city": weather_json["name"],
                    "country": weather_json["sys"]["country"],
                    "temp": weather_json["main"]["temp"],
                    "status": weather_json["weather"][0]["description"].title(),
                    "humidity": weather_json["main"]["humidity"]
                }
            else:
                error = "City not found! Please check the spelling."
        except Exception:
            error = "Unable to connect to the Weather Service. Verify your API Key."

    return render_template_string(HTML, data=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)