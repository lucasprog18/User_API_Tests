# 🧪 User API Tests — Python + Requests

Automated REST API testing focused on user management operations using Python, requests and pytest.  
This project simulates real-world API interactions (GET, POST, PUT, DELETE) — validating user flows, handling edge cases, and generating readable test reports. Designed as a clean, modular, and job-focused portfolio piece for junior QA/Automation positions.

---

## 🎯 Main Goals

- ✅ Practice API test automation using **Python + requests**
- ✅ Organize code with a clean, modular structure
- ✅ Deliver a project tailored for QA/Automation Jr. roles
- ✅ Generate HTML reports from test executions

---

## 🚀 Tech Stack

- `Python 3.13`
- `requests`
- `pytest`
- `pytest-html`
- `faker` (for dynamic test data)
- API under test: [https://reqres.in](https://reqres.in)
⚠️ API usage notice
> The API used in this project (reqres.in) is rate-limited to 100 requests per day on the free plan. > All development and test execution were consciously scoped to stay within this limit. > Tests are isolated and lightweight to prevent exceeding this quota unintentionally.

---

## 📂 Project Structure

```
user_api_tests/
├── .gitignore
├── README.md
├── requirements.txt
├── run_tests.py
├── pytest.ini
├── reports/
├── data/
│   └── user_payloads.py
├── src/
│   └── services/
│       └── user_service.py
├── tests/
│   ├── conftest.py
│   ├── test_get_users.py
│   ├── test_create_user.py
│   ├── test_update_user.py
│   └── test_delete_user.py
└── venv/  (not versioned)
```

---

## 🛠️ In Progress

This project is under active development. Upcoming features:

- ✅ Real test cases
- ✅ Dynamic test data
- ✅ HTML report generation
- ✅ Full README with roadmap, learnings and how to expand

---

**Created by: Lucas Gonçalves**
