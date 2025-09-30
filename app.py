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

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
  <a href="#">🏠 Home</a>
  <a href="#">📘 Documentation</a>
  <a href="#">📞 Contact</a>
  <a href="#" class="right">⚙️ Settings</a>
</div>
""", unsafe_allow_html=True)

# --- IBM RXN APP LOGIC ---
API_KEY = "apk-4c35f5a6f7d59ca8ec45d45b9bbd45a7b4656075632d948af776aa73ce020837"

rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

st.markdown('<div class="title">IBM RXN Chemistry Protocol Extractor</div>', unsafe_allow_html=True)
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
