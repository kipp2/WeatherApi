from flask import Flask, request, jsonify
from weather_api import get_weather_data
from dotenv import load_dotenv
import os 

load_dotenv()
app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def weather():
    city = request.args.get()
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    \