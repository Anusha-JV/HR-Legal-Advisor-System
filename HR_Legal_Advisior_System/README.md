# ⚖️ AI-Powered HR Legal Advisor System

## 📌 Overview
The AI-Powered HR Legal Advisor System is a smart application designed to help HR professionals and employees identify applicable labour laws based on real workplace scenarios.

This system uses Natural Language Processing (NLP) techniques to match user input with predefined legal cases and provides:
- Applicable Labour Laws
- Detailed Explanation
- HR Recommendations

---

## 🎯 Objective
- To simplify understanding of Indian labour laws
- To provide quick legal guidance for workplace issues
- To demonstrate the use of AI in HR compliance systems

---

## 🚀 Features
- 🔍 AI-based scenario matching (TF-IDF + Cosine Similarity)
- ⚖️ Multi-law identification for each case
- 📖 Detailed legal explanations
- ✅ Preventive HR recommendations
- 🎯 Confidence score for prediction
- 🖥️ Interactive UI using Streamlit

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn (NLP)
- Pandas

---

## 📦 Dependencies Explained

- **streamlit** → Used to build the interactive web interface  
- **scikit-learn** → Used for AI/NLP (TF-IDF vectorization and similarity matching)  
- **pandas** → Used for handling and managing data (optional but useful)

---

## 🧠 How It Works
1. User enters a workplace issue or selects a scenario
2. The system processes input using TF-IDF vectorization
3. Cosine similarity is used to find the closest matching scenario
4. The system outputs:
   - Applicable Laws
   - Explanation
   - HR Recommendations

---

## ▶️ How to Run the Project

### 1. Clone / Download the project
Download the folder or clone the repository

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
streamlit run app.py

---

## 📂 Project Structure
HR_Legal_Advisor_System/
│── app.py
│── data.py
│── requirements.txt
│── README.md

---

## 💡 Use Cases
- HR compliance checks
- Employee awareness of labour laws
- Academic and learning purposes
- HR automation tools

---

## 🔮 Future Improvements
- Integration with real-time legal databases
- Advanced NLP using machine learning models
- Chatbot-based interaction
- Multi-language support

---

## 👩‍💻 Author
ANUSHA J V

---

## ⭐ Conclusion
This project demonstrates how AI can be used to simplify complex legal frameworks and assist HR professionals in making informed, compliant decisions.
