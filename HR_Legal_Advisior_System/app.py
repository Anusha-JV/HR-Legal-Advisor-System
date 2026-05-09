import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import cases

# Page setup
st.set_page_config(page_title="HR Legal Advisor", layout="centered")

st.title("⚖️ AI-Powered HR Legal Advisor System")
st.write("Get labour law guidance based on workplace scenarios.")

# Prepare data
scenarios = [case["scenario"] for case in cases]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(scenarios)

# Function to find best match
def find_match(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    score = similarity[0][index]
    return cases[index], score

# Dropdown option
selected_scenario = st.selectbox(
    "Select a scenario (optional):",
    [""] + scenarios
)

# Text input
user_input = st.text_input("describe your workplace issue:")

# Decide query
query = user_input if user_input else selected_scenario

# Show results
if query:
    result, score = find_match(query)

    # Confidence score
    st.markdown(f"### 🔍 Match Confidence: {round(score * 100, 2)}%")

    # Low confidence warning
    if score < 0.3:
        st.warning("⚠️ Low confidence match. Try rephrasing your input.")

    # Applicable Laws
    st.markdown("### 📜 Applicable Laws:")
    for law in result["act"]:
        st.write(f"- {law}")

    # Explanation
    st.markdown("### 📖 Explanation:")
    st.write(result["explanation"])

    # Recommendation
    st.markdown("### ✅ HR Recommendation:")
    st.write(result["recommendation"])

# Footer
st.markdown("---")
#st.caption("Built using Python, Streamlit & NLP (TF-IDF + Cosine Similarity)")