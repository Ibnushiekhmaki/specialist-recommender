from rules_engine import get_specialist_for_symptoms


def test_single_symptom_gives_full_confidence():
    result = get_specialist_for_symptoms(["chest pain"])
    assert result["specialist"] == "Cardiologist"
    assert result["confidence"] == 1.0


def test_tie_keeps_other_candidate():
    result = get_specialist_for_symptoms(["chest pain", "dizziness"])
    assert result["specialist"] == "Cardiologist"
    assert result["confidence"] == 0.5
    assert result["other_candidates"][0]["specialist"] == "General Practitioner"


def test_skin_rash_goes_to_dermatologist():
    result = get_specialist_for_symptoms(["skin rash"])
    assert result["specialist"] == "Dermatologist"