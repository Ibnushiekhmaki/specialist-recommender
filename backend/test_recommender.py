from recommender import recommend


def good_patient():
    return {
        "symptoms": ["chest pain"],
        "age": 55,
        "gender": "male",
        "duration": "today",
        "previous": False,
        "history": ["hypertension"],
    }


def test_good_answers_give_a_result():
    response = recommend(good_patient())
    assert response["ok"] is True
    assert response["result"]["specialist"] == "Cardiologist"


def test_bad_answers_give_an_error_message():
    data = good_patient()
    data["age"] = -5
    response = recommend(data)
    assert response["ok"] is False
    assert "Age" in response["error"]


def test_no_match_gives_general_practitioner():
    data = good_patient()
    data["symptoms"] = ["unknown symptom"]
    response = recommend(data)
    assert response["ok"] is True
    assert response["result"]["fallback"] is True