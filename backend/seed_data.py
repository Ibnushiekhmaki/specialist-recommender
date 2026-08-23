from database import get_connection

specialists = [
    ("Cardiologist", "Treats heart and blood vessel conditions"),
    ("General Practitioner", "First point of contact for general symptoms"),
    ("Pulmonologist", "Treats lung and breathing conditions"),
    ("Dermatologist", "Treats skin, hair, and nail conditions"),
]

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM specialists")
    cursor.execute("DELETE FROM symptom_rules")

    cursor.executemany(
        "INSERT INTO specialists (name, description) VALUES (?, ?)",
        specialists
    )

    cursor.execute("SELECT id, name FROM specialists")
    specialist_ids = {name: id for id, name in cursor.fetchall()}

    rules = [
        ("chest pain", specialist_ids["Cardiologist"], "Common cardiac symptom"),
        ("dizziness", specialist_ids["General Practitioner"], "Needs general evaluation first"),
        ("shortness of breath", specialist_ids["Pulmonologist"], "Common respiratory symptom"),
        ("skin rash", specialist_ids["Dermatologist"], "Common dermatological symptom"),
    ]

    cursor.executemany(
        "INSERT INTO symptom_rules (symptom_tag, specialist_id, notes) VALUES (?, ?, ?)",
        rules
    )

    conn.commit()
    conn.close()
    print(f"Seeded {len(specialists)} specialists and {len(rules)} rules.")

if __name__ == "__main__":
    seed()