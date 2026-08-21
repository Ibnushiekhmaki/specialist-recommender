def parse_symptoms(text):
    """Split a comma-separated symptom string into a clean list."""
    symptoms = [s.strip().lower() for s in text.split(",")]
    return symptoms

result = parse_symptoms("Chest pain, Dizziness,  Shortness of breath")
print(result)

specialist_rules = {
    "chest pain": "Cardiologist",
    "dizziness": "General Practitioner",
    "shortness of breath": "Pulmonologist",
    "skin rash": "Dermatologist",
}

symptom = "chest pain"
print(specialist_rules[symptom])

import json

json_text = json.dumps(specialist_rules, indent=2)
print(json_text)

loaded_back = json.loads(json_text)
print(loaded_back["chest pain"])

def get_specialist(symptom):
    try:
        return specialist_rules[symptom]
    except KeyError:
        return "No matching specialist found  please consult a general practitioner."

print(get_specialist("chest pain"))
print(get_specialist("headache"))
import os
from dotenv import load_dotenv
import requests

load_dotenv()

response = requests.get("https://api.github.com/thisdoesnotexist")
print(response.status_code)
print(response.json())


