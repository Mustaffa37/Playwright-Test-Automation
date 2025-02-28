# 🚀 Playwright Automation Project

## 📌 Project Overview
This project automates the testing of an e-commerce website using **Playwright** and **pytest**. It includes:
- Login test: Verifies user authentication.
- Cart test: Adds items to the cart and verifies the cart page.
- Checkout test: Completes an order with user details.
- HTML Report Generation: Generates a test execution report.

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies  
Ensure you have **Python 3.11+** installed, then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Install Playwright Browsers  
Playwright requires browsers to run tests. Install them using:
```bash
playwright install
```

### 3️⃣ Run Tests  
Run all tests and generate an HTML report:
```bash
pytest --html=reports/test_report.html --self-contained-html
```

To run individual test files:
```bash
pytest tests/login_test.py     # Run login test
pytest tests/test_cart.py      # Run cart test
pytest tests/test_checkout.py  # Run checkout test
```

### 4️⃣ View Test Report  
After running the tests, open the report:

```bash
start reports/test_report.html  # Windows
open reports/test_report.html   # macOS/Linux
```

---

## 📋 Requirements File (`requirements.txt`)
```txt
pytest
pytest-html
playwright
pytest-ordering
```

---

## 🔍 Notes

- **Test Execution Order:**  
  Tests run in the following sequence:  
  ✅ **Login → Cart → Checkout**  
  This order is maintained using `pytest-ordering`.

- **Headless Mode:**  
  By default, tests run in **headless mode**. To see the execution in action, modify:
  ```python
  browser = p.chromium.launch(headless=False)
  ```

---

## 👨‍💻 Contributing
Feel free to **fork** the repository and submit a **pull request** for improvements. 🚀

---

## 📜 License
This project is open-source under the **MIT License**.

---
✅ **Happy Testing!** 🎉
```