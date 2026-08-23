# Database Schema

## specialists
- id (INTEGER, primary key)
- name (TEXT) — e.g. "Cardiologist"
- description (TEXT) — what they treat

## symptom_rules
- id (INTEGER, primary key)
- symptom_tag (TEXT) — e.g. "chest pain"
- specialist_id (INTEGER, foreign key -> specialists.id)
- notes (TEXT, optional)