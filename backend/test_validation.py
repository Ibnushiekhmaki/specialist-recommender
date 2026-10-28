import pytest
from validation import validate_patient


def good_patient():
    return {
        "symptoms": ["Chest Pain", " dizziness "],
        "age": 55,
        "gender": "male",
        "duration": "today",
        "previous": False,
        "history": ["hypertension"],
    }


def test_good_patient_is_cleaned():
    result = validate_patient(good_patient())
    assert result["symptoms"] == ["chest pain", "dizziness"]
    assert result["age"] == 55


def test_history_is_optional():
    data = good_patient()
    del data["history"]
    assert validate_patient(data)["history"] == []


def test_no_symptoms_is_rejected():
    data = good_patient()
    data["symptoms"] = []
    with pytest.raises(ValueError):
        validate_patient(data)


def test_bad_age_is_rejected():
    data = good_patient()
    data["age"] = -5
    with pytest.raises(ValueError):
        validate_patient(data)


def test_bad_gender_is_rejected():
    data = good_patient()
    data["gender"] = "purple"
    with pytest.raises(ValueError):
        validate_patient(data)


def test_bad_duration_is_rejected():
    data = good_patient()
    data["duration"] = "forever"
    with pytest.raises(ValueError):
        validate_patient(data)