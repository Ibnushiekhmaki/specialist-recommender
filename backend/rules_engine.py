from database import get_connection


def general_practitioner_fallback():
    """Safe answer used when no rule matches: advise the nearest general practitioner."""
    conn = get_connection()
    cursor = conn.cursor()

    # Read the General Practitioner description from the database
    cursor.execute(
        "SELECT description FROM specialists WHERE name = ?",
        ("General Practitioner",),
    )
    row = cursor.fetchone()
    conn.close()

    # If the database has no description, use a simple default
    description = row[0] if row else "A family doctor who sees all kinds of problems"

    return {
        "specialist": "General Practitioner",
        "description": description,
        "matched_symptoms": [],
        "confidence": 0.0,
        "other_candidates": [],
        "fallback": True,  # tells the website this is a safety suggestion
    }


def get_specialist_for_symptoms(symptom_tags):
    """Take a list of symptoms and return the best specialist with a confidence score."""
    conn = get_connection()
    cursor = conn.cursor()

    # matches groups the symptoms by specialist: {specialist_id: {...}}
    matches = {}

    for tag in symptom_tags:
        # Find the specialist linked to this symptom (parameterized query)
        cursor.execute("""
            SELECT specialists.id, specialists.name, specialists.description
            FROM symptom_rules
            JOIN specialists ON symptom_rules.specialist_id = specialists.id
            WHERE symptom_rules.symptom_tag = ?
        """, (tag,))
        result = cursor.fetchone()

        if result:
            specialist_id, name, description = result

            # Create the entry the first time we see this specialist
            if specialist_id not in matches:
                matches[specialist_id] = {
                    "name": name,
                    "description": description,
                    "matched_symptoms": [],
                }

            # Remember which symptom matched
            matches[specialist_id]["matched_symptoms"].append(tag)

    conn.close()

    # No rule matched at all: give the safe fallback instead of nothing
    if not matches:
        return general_practitioner_fallback()

    # Rank specialists by how many symptoms they matched (most first)
    ranked = sorted(
        matches.values(),
        key=lambda m: len(m["matched_symptoms"]),
        reverse=True,
    )

    top = ranked[0]

    # Confidence = matched symptoms divided by all symptoms given
    confidence = len(top["matched_symptoms"]) / len(symptom_tags)

    # Everyone except the winner is kept as another possible option
    other_candidates = [
        {
            "specialist": m["name"],
            "matched_symptoms": m["matched_symptoms"],
        }
        for m in ranked[1:]
    ]

    return {
        "specialist": top["name"],
        "description": top["description"],
        "matched_symptoms": top["matched_symptoms"],
        "confidence": round(confidence, 2),
        "other_candidates": other_candidates,
        "fallback": False,  # a real match, not a safety suggestion
    }


# This block only runs when you start this file directly
if __name__ == "__main__":
    result = get_specialist_for_symptoms(["chest pain", "dizziness"])
    print(result)