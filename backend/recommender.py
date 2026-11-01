from validation import validate_patient
from rules_engine import get_specialist_for_symptoms


def recommend(raw_data):
    """The one function the website will call.

    It always returns a reply with the same shape:
    {"ok": True, "result": {...}}   when everything is fine
    {"ok": False, "error": "..."}   when an answer is wrong
    """

    # The website must send a set of answers, not something else
    if not isinstance(raw_data, dict):
        return {"ok": False, "error": "The answers must be sent as a set of fields."}

    # Step 1: check and clean the answers.
    # If an answer is wrong, validate_patient raises a ValueError.
    # We catch it here and turn it into a normal reply with the message.
    try:
        patient = validate_patient(raw_data)
    except ValueError as problem:
        return {"ok": False, "error": str(problem)}

    # Step 2: ask the engine. For now it uses only the symptoms.
    # Age, gender, duration and the rest will be used when we add the rules for them.
    result = get_specialist_for_symptoms(patient["symptoms"])

    return {"ok": True, "result": result}