ALLOWED_GENDERS = ["male", "female"]
ALLOWED_DURATIONS = ["today", "few days", "weeks", "over 8 weeks"]


def validate_patient(data):
    """Check the answers from the website and return a clean copy.
    If something is wrong, raise a ValueError with a clear message."""

    # Symptoms: a list with 1 to 10 real words
    symptoms = data.get("symptoms")
    if not isinstance(symptoms, list) or len(symptoms) == 0:
        raise ValueError("Please choose at least one symptom.")
    if len(symptoms) > 10:
        raise ValueError("Please choose at most 10 symptoms.")

    clean_symptoms = []
    for symptom in symptoms:
        if not isinstance(symptom, str) or symptom.strip() == "":
            raise ValueError("Each symptom must be a word or a short phrase.")
        # Remove extra spaces and make everything lowercase
        clean_symptoms.append(symptom.strip().lower())

    # Age: a whole number from 0 to 120
    # (Python counts True and False as numbers, so we block them too)
    age = data.get("age")
    if isinstance(age, bool) or not isinstance(age, int) or age < 0 or age > 120:
        raise ValueError("Age must be a whole number from 0 to 120.")

    # Gender: must be one of the allowed words
    gender = data.get("gender")
    if isinstance(gender, str):
        gender = gender.strip().lower()
    if gender not in ALLOWED_GENDERS:
        raise ValueError("Gender must be male or female.")

    # Duration: must be one of the allowed choices
    duration = data.get("duration")
    if isinstance(duration, str):
        duration = duration.strip().lower()
    if duration not in ALLOWED_DURATIONS:
        raise ValueError("Duration must be one of: " + ", ".join(ALLOWED_DURATIONS) + ".")

    # Previous: only True or False
    previous = data.get("previous")
    if not isinstance(previous, bool):
        raise ValueError("Previous must be true or false.")

    # History: optional list of words, empty if not given
    history = data.get("history", [])
    if not isinstance(history, list):
        raise ValueError("History must be a list.")
    clean_history = []
    for item in history:
        if isinstance(item, str) and item.strip() != "":
            clean_history.append(item.strip().lower())

    return {
        "symptoms": clean_symptoms,
        "age": age,
        "gender": gender,
        "duration": duration,
        "previous": previous,
        "history": clean_history,
    }