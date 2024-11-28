import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "f3fd70aa795a0e14ddc0a248e1f8e44a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400
    
    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()

        if response.status_code == 200:
            return jsonify({
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            })
        else:
            return jsonify({"error": data.get("message", "Unknown error")}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

