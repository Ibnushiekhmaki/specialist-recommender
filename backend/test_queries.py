from database import get_connection

def find_specialist_for_symptom(symptom_tag):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT symptom_rules.symptom_tag, specialists.name, specialists.description
        FROM symptom_rules
        JOIN specialists ON symptom_rules.specialist_id = specialists.id
        WHERE symptom_rules.symptom_tag = ?
    """, (symptom_tag,))

    result = cursor.fetchone()
    conn.close()
    return result

if __name__ == "__main__":
    test_symptom = "headache"
    result = find_specialist_for_symptom(test_symptom)

    if result:
        symptom, specialist_name, description = result
        print(f"Symptom: {symptom}")
        print(f"Recommended: {specialist_name}")
        print(f"About: {description}")
    else:
        print(f"No match found for '{test_symptom}'")