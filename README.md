# 📝 AI Grammar & Style Corrector — Simple Version

A simple, offline-friendly grammar and style correction web app built with **Python**, **LanguageTool**, and **Streamlit**.

---

## 🚀 Features
- Grammar and spelling correction using LanguageTool
- Simple style improvements (remove weak phrases, collapse repeated words)
- Side-by-side comparison (original vs corrected)
- Grammar explanations
- Inline diff view and download option

---

## ⚙️ Setup Instructions

### 1. Clone the repository or unzip this project
```bash
cd grammar-corrector
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
# Activate it:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

Then open the local URL shown in your terminal.

---

## 🧠 Example Input
```
He go to school every day. He is very very good at study. In order to improve, he read a lot of books.
```

### Output
```
He goes to school every day. He is excellent at study. To improve, he read many books.
```

---

## 🛠 Notes
- Requires **Java (JRE)** installed for LanguageTool to work offline.
- To disable style corrections, uncheck the box in the app interface.
- You can deploy this easily on Streamlit Cloud or Hugging Face Spaces.

---

## 📈 Future Enhancements
- Integrate a transformer model for more fluent rewrites (e.g., T5, BERT)
- Add user login and history of corrections
- Provide style tone options (Formal, Academic, Casual)
