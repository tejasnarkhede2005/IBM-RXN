import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# --- PAGE CONFIG ---
st.set_page_config(page_title="IBM RXN Protocol Extractor", page_icon="🧪", layout="wide")

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* Navbar styling */
    .navbar {
        background-color: #1E1E2F;
        overflow: hidden;
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
    }
    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 10px 18px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        transition: 0.3s;
        border-radius: 8px;
    }
    .navbar a:hover {
        background-color: #5757D1;
        color: white;
    }
    .navbar .right {
        float: right;
    }
    /* Title styling */
    .title {
        font-size: 32px;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 15px;
    }
    /* Main container */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1.5px solid #5757D1 !important;
        font-size: 15px !important;
    }
    .stButton>button {
        background-color: #5757D1 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3A3AA9 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVBAR (linked with session state) ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

nav_items = {
    "🏠 Home": "Home",
    "⚗️ Extractor": "Extractor",
    "📘 Documentation": "Docs",
    "ℹ️ About": "About",
    "📞 Contact": "Contact",
    "⚙️ Settings": "Settings"
}

# Render Navbar
nav_html = '<div class="navbar">'
for label, page in nav_items.items():
    nav_html += f'<a href="?page={page}">{label}</a>'
nav_html += '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

# Detect page from query params
query_params = st.experimental_get_query_params()
if "page" in query_params:
    st.session_state.page = query_params["page"][0]

# --- PAGES ---
API_KEY = "apk-4c35f5a6f7d59ca8ec45d45b9bbd45a7b4656075632d948af776aa73ce020837"
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

if st.session_state.page == "Home":
    st.markdown('<div class="title">🏠 Welcome to IBM RXN Chemistry App</div>', unsafe_allow_html=True)
    st.write("This app helps you extract **chemical reaction protocol steps** using the IBM RXN API.")
    st.info("Navigate to the **Extractor** page to start!")

elif st.session_state.page == "Extractor":
    st.markdown('<div class="title">⚗️ Protocol Extractor</div>', unsafe_allow_html=True)
    st.write("Paste your **chemical reaction procedure text** below to extract protocol steps:")
    input_text = st.text_area("Reaction Procedure Text", height=300)
    if st.button("Extract Protocol Steps"):
        if not input_text.strip():
            st.warning("⚠️ Please enter some reaction procedure text first.")
        else:
            with st.spinner("🔄 Extracting synthesis protocol steps..."):
                try:
                    result = rxn_wrapper.paragraph_to_actions(paragraph=input_text)
                    actions = result.get("actions", [])
                    if actions:
                        st.subheader("✅ Extracted Protocol Steps:")
                        for i, action in enumerate(actions, 1):
                            st.success(f"{i}. {action}")
                    else:
                        st.info("ℹ️ No protocol steps extracted. Please verify the input format.")
                except Exception as e:
                    st.error(f"❌ Error calling IBM RXN API: {e}")

elif st.session_state.page == "Docs":
    st.markdown('<div class="title">📘 Documentation</div>', unsafe_allow_html=True)
    st.write("""
    **How it works:**
    - Paste your chemical reaction text in the Extractor.
    - The IBM RXN API parses and extracts **step-by-step synthesis instructions**.
    - Results are shown as a numbered list of protocol actions.
    
    **Tech stack:**
    - Streamlit (Frontend)
    - IBM RXN API (Backend AI Engine)
    """)

elif st.session_state.page == "About":
    st.markdown('<div class="title">ℹ️ About This App</div>', unsafe_allow_html=True)
    st.write("""
    This project demonstrates how to use the **IBM RXN for Chemistry API**
    inside a modern **Streamlit app** with a stylish UI.

    Created for chemists, researchers, and students 🧪✨
    """)

elif st.session_state.page == "Contact":
    st.markdown('<div class="title">📞 Contact</div>', unsafe_allow_html=True)
    st.write("For any queries, reach out via:")
    st.write("- 📧 Email: support@rxnchemistry.com")
    st.write("- 🌐 Website: [IBM RXN](https://rxn.res.ibm.com)")

elif st.session_state.page == "Settings":
    st.markdown('<div class="title">⚙️ Settings</div>', unsafe_allow_html=True)
    st.write("Here you can configure app preferences (future feature).")
    st.info("⚡ Currently, settings are not customizable.")
