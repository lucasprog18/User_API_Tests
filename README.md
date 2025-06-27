🧪 User API Tests — Python + Pytest + Requests  
Structured and realistic API testing project designed to showcase professional-quality testing with a focus on clarity, modularity, and value delivery.  
This project validates a public API (https://reqres.in) using dynamic test data, full CRUD coverage, and reliable reporting — all in a clean and scalable structure.

> ⚠️ As I'm transitioning my portfolio into English, some files and comments may contain both English and Portuguese. This is intentional and reflects my gradual language shift to make my work more globally accessible.

---

🎯 Main Goals

✅ Build a lightweight API testing suite with real-world structure  
✅ Cover the full CRUD cycle (GET, POST, PUT, DELETE)  
✅ Use dynamic test data with `faker`  
✅ Apply Pydantic for response schema validation  
✅ Keep tests efficient to respect daily API usage limits  
✅ Produce readable reports and modular code suitable for interviews or contribution

---

🚀 Tech Stack

- Python 3.11+
- Pytest
- Requests
- Faker
- Pydantic
- Dotenv
- Pytest-HTML
- Pytest-Cov (for coverage reports)

---

🧪 Test Scenarios

### ✅ Positive Tests

- `GET /users` — validate user listing with status and structure
- `POST /users` — user creation with dynamic payload generation
- `PUT /users/{id}` — update user data and validate updatedAt field
- `DELETE /users/{id}` — simulate user deletion (204 No Content)
- **User Lifecycle** — end-to-end: create → update → delete (simulated real user journey)

### ❌ Negative Tests

- `POST /users` with empty payload — confirms that the fake API still returns 201  
- `PUT /users/9999` — demonstrates that updates succeed even for nonexistent users  
- `DELETE /users/nonexistent_id` — shows that deletion returns 204 with any ID  
- These tests help document the **non-standard behavior** of the mock API and reflect realistic test modeling

---

📂 Project Structure

```
user_api_tests/
├── conftest.py                # Test fixtures (e.g. Faker instance)
├── data/
│   └── user_payloads.py       # Valid and invalid payload generators
├── reports/                   # HTML reports generated per run
├── schemas/
│   └── user_schemas.py        # Pydantic models for response validation
├── src/
│   └── services/
│       └── user_service.py    # All HTTP methods to interact with API
├── tests/
│   ├── test_create_user.py     # Tests for POST
│   ├── test_delete_user.py     # Tests for DELETE
│   ├── test_get_users.py       # Tests for GET
│   ├── test_update_user.py     # Tests for PUT
│   ├── test_user_lifecycle.py  # One test covering create → update → delete
│   └── test_negative_scenarios.py  # Negative tests to document edge behavior
├── .env                        # API Key file (ignored)
├── .gitignore
├── pytest.ini
├── requirements.txt
└── run_tests.py                # Custom test runner with timestamped reports
```

---

▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests and generate HTML report:

```bash
python run_tests.py
```

Run a single test file:

```bash
pytest tests/test_update_user.py
```

📈 Run with code coverage (optional):

```bash
pytest --cov=src --cov-report=html
# → Output in htmlcov/index.html
```

---

📊 HTML Reports

A new report is created on each run inside `/reports/` and includes:

- Test status, names and durations
- Logs and traceback for each failure
- Aggregated test summary and timestamp

Just open the latest `.html` file in your browser!

---

🛠 Why We Added Optional Improvements

Although the MVP was initially scoped to basic CRUD coverage, we identified key lightweight enhancements that would improve the **professional quality** of this project without increasing complexity:

- ✅ **Schema validation with Pydantic** — assert response fields are present and correctly typed  
- ✅ **Lifecycle testing** — simulate real user journey from creation to deletion  
- ✅ **Code coverage with pytest-cov** — better visibility into what is tested  
- ✅ **Negative testing scenarios** — document edge cases and API quirks without asserting incorrect behavior  
- ✅ **Execution tips documented in run_tests.py** — helpful for future contributors

---

📮 Author

**Lucas Ferreira**  
QA Engineer | Automation | API & Web Testing  
GitHub: [lucasprog18](https://github.com/lucasprog18)  
Location: 🇧🇷 Brazil

---

🔭 What's Next (Optional Ideas)

This project is complete as-is, but could evolve with:

- Contract schema validation for GET responses  
- Parallel test execution or test grouping (markers)  
- Mock server testing or GitHub Actions CI  
- Status badge, GIF and README enhancements for visual polish  

