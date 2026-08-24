from database import get_connection

def get_specialist_for_symptoms(symptom_tags):
    conn = get_connection()
    cursor = conn.cursor()

    matches = {}

    for tag in symptom_tags:
        cursor.execute("""
            SELECT specialists.id, specialists.name, specialists.description
            FROM symptom_rules
            JOIN specialists ON symptom_rules.specialist_id = specialists.id
            WHERE symptom_rules.symptom_tag = ?
        """, (tag,))
        result = cursor.fetchone()

        if result:
            specialist_id, name, description = result
            if specialist_id not in matches:
                matches[specialist_id] = {
                    "name": name,
                    "description": description,
                    "matched_symptoms": []
                }
            matches[specialist_id]["matched_symptoms"].append(tag)

    conn.close()

    if not matches:
        return None

    ranked = sorted(
        matches.values(),
        key=lambda m: len(m["matched_symptoms"]),
        reverse=True
    )

    top = ranked[0]
    confidence = len(top["matched_symptoms"]) / len(symptom_tags)

    other_candidates = [
        {
            "specialist": m["name"],
            "matched_symptoms": m["matched_symptoms"]
        }
        for m in ranked[1:]
    ]

    return {
        "specialist": top["name"],
        "description": top["description"],
        "matched_symptoms": top["matched_symptoms"],
        "confidence": round(confidence, 2),
        "other_candidates": other_candidates
    }

if __name__ == "__main__":
    result = get_specialist_for_symptoms(["chest pain", "dizziness"])
    print(result)