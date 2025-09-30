import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="IBM RXN Chemistry Protocol Extractor",
    page_icon="🧪",
    layout="wide"
)

# --- STYLISH CSS ---
st.markdown("""
    <style>
    /* Navbar Container */
    .navbar {
        background-color: #0d47a1;
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }
    /* Navbar Links */
    .navbar a {
        color: white;
        padding: 12px 18px;
        text-decoration: none;
        font-size: 18px;
        font-weight: 500;
        transition: 0.3s;
        border-radius: 6px;
        margin: 0 10px;
    }
    .navbar a:hover {
        background-color: #1565c0;
        color: #ffeb3b;
    }
    /* Title Styling */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #0d47a1;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#extractor">Extractor</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# --- API KEY & WRAPPER ---
API_KEY = st.secrets["ibm_rxn_api_key"]
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

# --- CONTENT ---
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">IBM RXN Chemistry Protocol Extractor</h1>', unsafe_allow_html=True)

st.write("Paste your chemical reaction procedure text below:")

st.markdown('<div id="extractor"></div>', unsafe_allow_html=True)
input_text = st.text_area("Reaction Procedure Text", height=300)

if st.button("Extract Protocol Steps"):
    if not input_text.strip():
        st.warning("Please enter some reaction procedure text first.")
    else:
        with st.spinner("Extracting synthesis protocol steps..."):
            try:
                result = rxn_wrapper.paragraph_to_actions(paragraph=input_text)
                actions = result.get("actions", [])
                if actions:
                    st.subheader("✅ Extracted Protocol Steps:")
                    for i, action in enumerate(actions, 1):
                        st.write(f"{i}. {action}")
                else:
                    st.info("No protocol steps extracted. Please verify the input format.")
            except Exception as e:
                st.error(f"Error calling IBM RXN API: {e}")

# --- ABOUT SECTION ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.subheader("ℹ️ About")
st.write("""
This app uses **IBM RXN for Chemistry** to automatically extract synthesis protocol steps 
from raw experimental procedure text.  
It helps researchers save time in converting unstructured text into actionable synthesis steps.
""")

# --- CONTACT SECTION ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.subheader("📬 Contact")
st.write("""
- Developer: **Your Name**  
- Email: yourname@example.com  
- GitHub: [yourgithub](https://github.com)  
""")
