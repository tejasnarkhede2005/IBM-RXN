import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# --- PAGE CONFIG ---
st.set_page_config(page_title="IBM RXN Protocol Extractor", layout="wide")

# --- CUSTOM CSS FOR NAVBAR ---
st.markdown("""
    <style>
    /* Navbar Container */
    .navbar {
        background-color: #1E1E2F;
        overflow: hidden;
        display: flex;
        justify-content: space-between;
        padding: 15px 40px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    /* Navbar Left Title */
    .navbar h1 {
        color: #ffffff;
        font-size: 22px;
        margin: 0;
        font-family: 'Poppins', sans-serif;
    }
    /* Navbar Links */
    .navbar a {
        float: left;
        color: #f2f2f2;
        text-align: center;
        padding: 8px 16px;
        text-decoration: none;
        font-size: 16px;
        font-family: 'Poppins', sans-serif;
        transition: 0.3s;
        border-radius: 8px;
    }
    .navbar a:hover {
        background-color: #5755d9;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVBAR HTML ---
st.markdown("""
    <div class="navbar">
        <h1>IBM RXN Chemistry</h1>
        <div>
            <a href="https://rxn.res.ibm.com" target="_blank">IBM RXN Home</a>
            <a href="https://github.com/rxn4chemistry" target="_blank">GitHub</a>
            <a href="https://streamlit.io" target="_blank">About</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- APP LOGIC ---
# Load API key from Streamlit secrets
API_KEY = st.secrets["ibm_rxn_api_key"]

# Initialize IBM RXN wrapper
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

st.title("🧪 Protocol Extractor")
st.write("Paste your chemical reaction procedure text below:")

input_text = st.text_area("Reaction Procedure Text", height=300)

if st.button("Extract Protocol Steps"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some reaction procedure text first.")
    else:
        with st.spinner("🔍 Extracting synthesis protocol steps..."):
            try:
                result = rxn_wrapper.paragraph_to_actions(paragraph=input_text)
                actions = result.get("actions", [])
                if actions:
                    st.subheader("✅ Extracted Protocol Steps:")
                    for i, action in enumerate(actions, 1):
                        st.write(f"**{i}.** {action}")
                else:
                    st.info("ℹ️ No protocol steps extracted. Please verify the input format.")
            except Exception as e:
                st.error(f"❌ Error calling IBM RXN API: {e}")
