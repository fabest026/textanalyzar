import streamlit as st
import string

# Custom CSS
custom_css = """
body {
  background-color: #f5f5f5;
  font-family: Arial, Helvetica, sans-serif;
}

.container {
  max-width: 800px;
  padding: 20px;
}

.title {
  font-size: 48px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 40px;
}

.input-group {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.input-group label {
  font-size: 18px;
  font-weight: bold;
  margin-right: 10px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.results {
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 40px;
}

.results-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}

.results-value {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
}

.results-text {
  font-size: 18px;
  font-weight: normal;
  text-align: center;
  margin-bottom: 20px;
}
"""

# Add custom CSS to the app
st.write(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Page title
st.title("Text Analyzer")

# Input text area
text = st.text_area("Enter your text here:", height=250)

# Update counters when the text changes
word_count = len(text.split())
character_count = len(text)
paragraph_count = text.count("\n\n") + 1

# Results
st.subheader("Results:")



features = {
    "Words": word_count,
    "Characters": character_count,
    "Paragraphs": paragraph_count,
}

st.markdown(
    """
<style>
.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    padding: 16px;
    text-align: center;
    background-color: #f5f5f5;
    border-radius: 20px;
    margin-bottom: 20px;
}

.card h3{
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 0px;
}

.card p{
    font-size: 18px;
    margin-bottom: 0px;
}

</style>
""",
    unsafe_allow_html=True)

st.write("""
<div class="row">
""", unsafe_allow_html=True)

for feature, value in features.items():
    st.write(f"<div class='col-sm-4'><div class='card'><h3>{feature}</h3><p>{value}</p></div></div>", unsafe_allow_html=True)


st.write("""
</div>
""", unsafe_allow_html=True)
