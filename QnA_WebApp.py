import streamlit as st
from main import get_connection

# Set page configuration
st.set_page_config(page_title="Hospital Management Q&A", page_icon="🏥", layout="centered")

# Title and subtitle
st.title("🏥 Hospital Management: Database Q&A")
st.markdown("Ask any question about the hospital management database, and get an instant response!")

# Sidebar with sample questions
st.sidebar.title("💡 Sample Questions")
st.sidebar.markdown("""
- List all hospitals in the Kingdom of Bahrain.
- Find all patients who have purchased "Aspirin"
- Retrieve the details of nurses working under doctor "Ahmed".
- Details of the patients those appointments scheduled for the date '2024-07-17'.
- List all medicines with an expiration date after '2024-01-01'.
- Find which medicine manufactured in which country.
- Find which patients examined by Doctor 'Ameera'.
""")

# Input section with styling
st.markdown("### 🔍 Enter your Question below:")
question = st.text_input("")

# Divider for better visual separation
st.markdown("---")

if question:
    # Loading spinner to indicate processing
    with st.spinner("Generating your response..."):
        chain = get_connection()
        response = chain.run(question)

    # Display response with enhanced styling
    st.header("📋 Your Answer")
    st.text_area("Response", response, height=200, disabled=True)
else:
    st.info("Please enter a question to get started.")

# Footer with additional information or links
st.markdown(
    """
    ---
    *Created by Atif Ansari | [GitHub](https://github.com/atifansari10) | [LinkedIn](https://www.linkedin.com/in/atifansari01/)*
    """
)
