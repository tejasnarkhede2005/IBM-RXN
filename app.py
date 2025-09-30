import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="IBM RXN Protocol Extractor", page_icon="🧪", layout="wide")

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* Title styling */
    .title {
        font-size: 32px;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 15px;
    }
    /* Input areas */
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
    a {text-decoration: none;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR MENU ---
with st.sidebar:
    choice = option_menu(
        "Navigation Menu",
        ["Home", "Extractor", "Documentation", "About", "Contact", "Settings"],
        icons=["house", "beaker", "book", "info-circle", "telephone", "gear"],
        menu_icon="list",
        default_index=0,
    )

# --- IBM RXN APP LOGIC ---
API_KEY = "apk-4c35f5a6f7d59ca8ec45d45b9bbd45a7b4656075632d948af776aa73ce020837"
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

# --- PAGE FUNCTIONS ---
def home_page():
    st.markdown('<div class="title">🏠 Welcome to IBM RXN Chemistry App</div>', unsafe_allow_html=True)
    st.write("""
    **IBM RXN Chemistry Protocol Extractor** helps chemists, researchers, and students 
    automatically extract **step-by-step synthesis protocols** from plain text reaction descriptions.
    """)
    
    st.write("### 🔹 Features")
    st.write("- Extract protocol steps from reaction procedures easily.")
    st.write("- Clean and modern **Streamlit interface**.")
    st.write("- Sidebar navigation for quick access to pages.")
    
    st.write("### 🔹 How to Use")
    st.write("1. Go to the **Extractor** page.")
    st.write("2. Paste your chemical reaction procedure text.")
    st.write("3. Click **Extract Protocol Steps** to view results.")
    
    st.write("### 🔹 Benefits")
    st.write("- Save time manually parsing reaction protocols.")
    st.write("- Easily share extracted protocols with your team.")
    st.write("- Ideal for research and educational purposes.")

def extractor_page():
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

def documentation_page():
    st.markdown('<div class="title">📘 Documentation</div>', unsafe_allow_html=True)
    st.write("""
    ### How it Works
    1. Paste your reaction text in the **Extractor** page.
    2. IBM RXN API parses and extracts **step-by-step instructions**.
    3. Results appear as a numbered list of actions.

    ### Tech Stack
    - **Frontend:** Streamlit
    - **Backend:** IBM RXN API
    """)

def about_page():
    st.markdown('<div class="title">ℹ️ About This App</div>', unsafe_allow_html=True)
    st.write("""
    This project demonstrates the integration of **IBM RXN for Chemistry API**
    with a modern **Streamlit interface** for protocol extraction.  
    Made for **researchers, chemists, and students** 🧪✨
    """)

def contact_page():
    st.markdown('<div class="title">📞 Contact</div>', unsafe_allow_html=True)
    st.write("For any queries, reach out via:")
    st.write("- 📧 Email: tejasnarkhede03@gmail.com")
    st.write("- 🌐 Website: [IBM RXN](https://rxn.res.ibm.com)")

def settings_page():
    st.markdown('<div class="title">⚙️ Settings</div>', unsafe_allow_html=True)
    st.write("Learn more about the app and its usage below:")

    # Use columns to display cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background-color:#5757D1; padding:20px; border-radius:12px; color:white;">
            <h3>📝 App Information</h3>
            <ul>
                <li><b>App Name:</b> IBM RXN Chemistry Protocol Extractor</li>
                <li><b>Version:</b> 1.0.0</li>
                <li><b>Developer:</b> Tejas </li>
                <li><b>Purpose:</b> Extract step-by-step chemical reaction protocols</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color:#3A3AA9; padding:20px; border-radius:12px; color:white;">
            <h3>💡 Usage Guide</h3>
            <ul>
                <li>Go to the <b>Extractor</b> page</li>
                <li>Paste chemical reaction procedure text</li>
                <li>Click <b>Extract Protocol Steps</b></li>
                <li>View the extracted step-by-step instructions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div style="background-color:#5757D1; padding:20px; border-radius:12px; color:white;">
            <h3>⚠️ Notes</h3>
            <ul>
                <li>Ensure reaction text is clear and complete</li>
                <li>Results depend on IBM RXN API parsing accuracy</li>
                <li>Check formatting for best results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background-color:#3A3AA9; padding:20px; border-radius:12px; color:white;">
            <h3>📞 Support</h3>
            <ul>
                <li>Email: tejasnarkhede03@gmail.com</li>
                <li>Website: <a href='https://rxn.res.ibm.com' style='color:white;' target='_blank'>IBM RXN</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE ROUTING ---
page_routes = {
    "Home": home_page,
    "Extractor": extractor_page,
    "Documentation": documentation_page,
    "About": about_page,
    "Contact": contact_page,
    "Settings": settings_page
}

page_routes[choice]()
