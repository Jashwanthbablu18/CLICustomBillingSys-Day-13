# 💰 Day 13 - Custom Billing System (with *args, **kwargs)

Welcome to **Day 13** of my **#30DaysOfPythonChallenge**!  
Today’s project is a **Custom Billing System** built using flexible function arguments — `*args` and `**kwargs`.

---

## 📌 Topic
**Functions in Python** — with a focus on:
- `*args` (non-keyword variable-length arguments)
- `**kwargs` (keyword variable-length arguments)

---

## 🧠 What I Built
A dynamic and interactive **Billing System** that:
- Accepts any number of items using `*args`
- Applies optional charges like tax, discounts, and delivery via `**kwargs`
- Calculates the final total and prints a clean bill summary

---

## 🔧 How It Works
- `*args` accepts multiple items in the form of tuples:  
  Example: `("Book", 120)`, `("Pen", 20)`
- `**kwargs` handles optional keyword-based charges like:  
  `tax=10`, `discount=-5`, `delivery=30`

---

## 🛠️ Concepts Used
- Function argument unpacking
- Tuple and dictionary processing
- Conditional logic for charges
- String formatting for structured bill display

---

## 💻 How to Run
```bash
python Day-13Code.py
