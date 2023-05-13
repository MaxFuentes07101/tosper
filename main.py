import openai
import time
import cv2
import numpy as np
import face_recognition
import os
import speech_recognition as sr
import requests
from robot_controller import Robot
from camera import Camera
from speaker import Speaker
from microphone import Microphone
from user import User

openai.api_key = "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"

def send_message(prompt):
    # check if the prompt is a request for weather information
    if "weather" in prompt.lower():
        city = input("Please enter the name of the city: ")
        weather_api_key = "your_openweathermap_api_key"
        response_text = get_weather(city, weather_api_key)
    else:
        # otherwise use the ChatGPT API
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        response_text = response.choices[0].text.strip()

    # make the robot speak the response
    speaker.speak(response_text)

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        return f"The current weather in {city} is {weather_desc} with a temperature of {main_data['temp']} Kelvin."
    else:
        return f"Sorry, I couldn't find the weather for {city}."

def listen_for_name():
    audio_data = microphone.listen()
    text = microphone.recognize_speech(audio_data)
    return "osmo" in text.lower() if text is not None else False

robot = Robot()
camera = Camera()
speaker = Speaker()
microphone = Microphone()

# Load MobileNet-SSD model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Load known faces
known_faces_dir = "known_faces"
known_face_encodings = []
known_face_names = []

for file in os.listdir(known_faces_dir):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, file))
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        name = os.path.splitext(file)[0]
        known_face_names.append(name)

# Load users
users = {}
for file in os.listdir("users"):
    if file.endswith(".json"):
        user = User.load(os.path.join("users", file))
        users[user.name] = user

following = False

while True:
    if listen_for_name():
        speaker.speak("Yes, I am here. How can I assist you?")
        audio_data = microphone.listen()
        text = microphone.recognize_speech(audio_data)
        send_message(text)
