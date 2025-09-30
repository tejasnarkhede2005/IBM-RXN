import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# Load API key from Streamlit secrets
API_KEY = st.secrets["ibm_rxn_api_key"]

# Initialize IBM RXN wrapper with API key
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Navbar */
        .navbar {
            background-color: #1f2937;
            padding: 1rem;
            color: white;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        /* Input box styling */
        textarea {
            border: 2px solid #3b82f6 !important;
            border-radius: 8px !important;
            font-size: 15px !important;
            padding: 10px !important;
        }
        /* Button */
        div.stButton > button {
            background-color: #3b82f6;
            color: white;
            border-radius: 6px;
            font-weight: 600;
            padding: 8px 16px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #2563eb;
            transform: scale(1.02);
        }
        /* Protocol steps */
        .protocol-step {
            background: #f3f4f6;
            padding: 10px 14px;
            border-radius: 6px;
            margin-bottom: 10px;
            font-size: 16px;
            border-left: 4px solid #3b82f6;
        }
    </style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown('<div class="navbar">⚗️ IBM RXN Chemistry Protocol Extractor</div>', unsafe_allow_html=True)

st.write("Paste your **chemical reaction procedure text** below to extract structured protocol steps:")

# Input text area
input_text = st.text_area("Reaction Procedure Text", height=300)

# Extract button
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
                        st.markdown(f"<div class='protocol-step'><b>{i}.</b> {action}</div>", unsafe_allow_html=True)
                else:
                    st.info("No protocol steps extracted. Please verify the input format.")
            except Exception as e:
                st.error(f"Error calling IBM RXN API: {e}")
