# Learning Log

## Day 1 - August 22, 2026
### Concepts learned
- Functions with parameters, string methods (.strip, .lower, .split), list comprehensions
- Dictionaries (key-value lookups)
- JSON (json.dumps and json.loads: converting Python data to text and back)
- try and except (handling bad input without crashing)
- Environment variables (load_dotenv), the requests library, HTTP status codes (200 = success, 404 = not found)
- Flask basics: the app object, the @app.route decorator, jsonify(), running a local development server

### What I built
- parse_symptoms(): cleans a comma-separated symptom string into a list
- specialist_rules dictionary that maps symptoms to specialists, and a lookup test
- Converted specialist_rules to JSON text and back, and confirmed the lookup still works
- get_specialist(): a function with a fallback for symptoms that are not in the table
- A real HTTP GET request to GitHub's public API, with a 200 success response
- First Flask app with two routes: a plain text home route and a JSON /api/hello route, both tested in the browser

### Problems I ran into and how I solved them
- The Code Runner button used a different Python than my virtual environment, so packages were missing (ModuleNotFoundError). I now run everything from the VS Code terminal with (venv) active.
- Tested a real broken URL to see a 404 status code.

## Day 2 - August 23, 2026
### Concepts learned
- SQLite table design with the sqlite3 module, PRIMARY KEY and FOREIGN KEY
- Filling tables with executemany(), and building a lookup dictionary from a query result
- SQL JOIN, the WHERE clause, and parameterized queries (? placeholders that protect against SQL injection)

### What I built
- database.py: creates the specialists and symptom_rules tables, checked with SQLite Viewer
- seed_data.py: fills both tables (4 rows in each), checked with SQLite Viewer
- test_queries.py: a JOIN query with a parameter, tested with "chest pain" and "headache"

### Problems I ran into and how I solved them
- The virtual environment was not active in the terminal. I learned to check that (venv) shows at the start of the line before running anything.

## Day 3 - August 2026
### Concepts learned
- Grouping results by specialist with a dictionary
- Sorting a list with a key function
- Confidence as matched symptoms divided by all symptoms given

### What I built
- rules_engine.py, first version: finds the specialist for each symptom, groups the matches, ranks the specialists, and returns the best one with a confidence score and the other candidates

### Problems I ran into and how I solved them
- The file ran with no output because nothing printed the result. I added a print block at the bottom.
- My first version used max(), which kept only one specialist and lost the others. I replaced it with a sorted ranking.

Date: 26 October 2026
Where I stopped: First tests written and measured
Goal for the day: Restart the project and start the test dataset
What I did: Checked that the rule engine runs. Made the data folder with 3 test cases, each with a real source. Wrote 3 tests with pytest. Measured test coverage.
What I learned (concepts): What a CSV file is, why every test case needs a source, what pytest does, what coverage means
Problems and how I solved them: The data folder was created in the wrong place and I moved it with git mv. One test failed because of a lowercase letter
Evidence: Commits d0ffe20, 536ecd0, d27856e, 57cb30b; 88 percent coverage on the rule engine
Plan for next session: Add the safe answer for when nothing matches

Date: 27 October 2026
Where I stopped: General Practitioner fallback finished and pushed
Goal for the day: Make the system advise the nearest general practitioner when nothing matches
What I did: Wrote two tests first and watched them fail, then added a fallback function to the rule engine and a "fallback" flag on every result. Moved the project from the Desktop to C:\dev\specialist-recommender and rebuilt the virtual environment. Stopped Git from tracking the coverage file
What I learned (concepts): Test first (red, then green), a function that returns nothing causes an error when you read from it, round brackets call a function and square brackets look something up, exact text is case sensitive, a missing comma turns text into a function call, a virtual environment remembers its location so it must be rebuilt when moved
Problems and how I solved them: Three typos in my own code (function name, table name, missing comma). The pytest error messages and a line-by-line check found each one. The old virtual environment could not be deleted from inside VS Code, so I closed VS Code and deleted it from Command Prompt
Evidence: Commits 2320817, 82b6081, 29296e4; 5 tests passing; 94 percent coverage on the rule engine
Plan for next session: Add the new questions with checks

Date: 28 October 2026
Where I stopped: Validation finished and pushed; not yet joined to the engine
Goal for the day: Add the new questions (age, gender, how long, happened before, known conditions) with checks
What I did: Wrote 6 tests first and watched them fail, then wrote a new file with a function that checks every answer and cleans it
What I learned (concepts): Validation (checking input before using it), raising an error with a clear message, testing that bad input is refused with pytest.raises, cleaning text (remove extra spaces, make it lowercase), copying a good example and breaking one thing per test
Problems and how I solved them: None today. The first run failed as expected because the file did not exist yet
Evidence: Commit f3f266c; 6 new tests passing
Plan for next session: Join the validation to the engine in one function, then make the first web route