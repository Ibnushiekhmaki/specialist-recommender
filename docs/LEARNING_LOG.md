# Learning Log

## Day 1 — August 22, 2026
### Concepts learned
- Functions with parameters, string methods (.strip, .lower, .split), list comprehensions
- Dictionaries (key-value lookups)
- JSON (json.dumps / json.loads — converting Python data to text and back)
- try/except (graceful error handling instead of crashing on bad input)

### What I built
- parse_symptoms() function that cleans a comma-separated symptom string into a list
- specialist_rules dictionary mapping symptoms to specialists, tested a lookup
- Converted specialist_rules to JSON text and back, confirmed round-trip lookup still works
- get_specialist() function with fallback for symptoms not in the rule table

### Problems I ran into and how I solved them
-