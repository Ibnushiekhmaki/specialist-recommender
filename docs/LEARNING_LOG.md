# Learning Log

## Day 1 — August 22, 2026
### Concepts learned
- Functions with parameters, string methods (.strip, .lower, .split), list comprehensions
- Dictionaries (key-value lookups)
- JSON (json.dumps / json.loads — converting Python data to text and back)
- try/except (graceful error handling instead of crashing on bad input)

- Environment variables (load_dotenv), requests library, HTTP status codes

- Flask basics: app object, @app.route decorator, jsonify(), running a local dev server
### What I built
- parse_symptoms() function that cleans a comma-separated symptom string into a list
- specialist_rules dictionary mapping symptoms to specialists, tested a lookup
- Converted specialist_rules to JSON text and back, confirmed round-trip lookup still works
- get_specialist() function with fallback for symptoms not in the rule table
- Made a real HTTP GET request to GitHub's public API, confirmed a 200 success response

- First working Flask app with two routes: a plain text home route and a JSON /api/hello route, tested both in the browser




### Problems I ran into and how I solved them

- Code Runner button used a different Python than my activated venv, missing packages. Fixed by running via terminal (python backend/practice.py) instead, which correctly uses the venv.


- HTTP status codes (200 = success, 404 = not found), tested with a real broken URL

- Code Runner button kept using a different Python interpreter than my venv, causing ModuleNotFoundError. Standardized on running everything through the VS Code terminal instead, which reliably uses the activated venv.
-



## Day 2 — August 23, 2026
### Concepts learned
- SQLite schema design, sqlite3 module, PRIMARY KEY / FOREIGN KEY
- Seeding data with executemany(), building an id lookup dict from a query result
- SQL JOIN, WHERE clause, parameterized queries (? placeholders for SQL injection safety)

### What I built
- database.py creating specialists and symptom_rules tables, verified with SQLite Viewer
- seed_data.py populating specialists and symptom_rules tables, verified 4 rows in each via SQLite Viewer
- SQL JOIN, WHERE clause, parameterized queries (? placeholders for SQL injection safety)
### Problems I ran into and how I solved them