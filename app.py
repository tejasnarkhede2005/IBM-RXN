import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="IBM RXN Protocol Extractor", page_icon="🧪", layout="wide")

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* Navbar container */
    .navbar {
        display: flex;
        justify-content: left;
        background-color: #1E1E2F;
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        gap: 10px;
        flex-wrap: wrap;
    }
    /* Navbar links as buttons */
    .navbar a {
        display: inline-block;
        color: #f2f2f2;
        text-align: center;
        padding: 10px 18px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        border-radius: 12px;
        transition: 0.3s;
        border: 1.5px solid transparent;
    }
    .navbar a:hover {
        background-color: #5757D1;
        color: white;
        border: 1.5px solid #3A3AA9;
    }
    /* Active page */
    .navbar a.active {
        background-color: #5757D1;
        color: white;
        border: 1.5px solid #3A3AA9;
    }
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
    </style>
""", unsafe_allow_html=True)

# --- QUERY PARAMS & SESSION STATE ---
query_params = st.experimental_get_query_params()
if "page" not in st.session_state:
    st.session_state.page = query_params.get("page", ["Home"])[0]

# --- TOP NAVBAR WITH ACTIVE PAGE ---
nav_items = {
    "🏠 Home": "Home",
    "⚗️ Extractor": "Extractor",
    "📘 Documentation": "Documentation",
    "ℹ️ About": "About",
    "📞 Contact": "Contact",
    "⚙️ Settings": "Settings"
}

nav_html = '<div class="navbar">'
for label, page in nav_items.items():
    active_class = "active" if st.session_state.page == page else ""
    nav_html += f'<a class="{active_class}" href="?page={page}">{label}</a>'
nav_html += '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
with st.sidebar:
    choice = option_menu(
        "Navigation Menu",
        ["Home", "Extractor", "Documentation", "About", "Contact", "Settings"],
        icons=["house", "beaker", "book", "info-circle", "telephone", "gear"],
        menu_icon="list",
        default_index=list(nav_items.values()).index(st.session_state.page),
    )

# Sync sidebar choice with session state
st.session_state.page = choice

# --- IBM RXN APP LOGIC ---
API_KEY = "apk-4c35f5a6f7d59ca8ec45d45b9bbd45a7b4656075632d948af776aa73ce020837"
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

# --- PAGE FUNCTIONS ---
def home_page():
    st.markdown('<div class="title">🏠 Welcome to IBM RXN Chemistry App</div>', unsafe_allow_html=True)
    st.write("This app helps you extract **chemical reaction protocol steps** using the IBM RXN API.")
    st.info("➡️ Use the **Extractor** page to start!")

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
    1. Paste your reaction text in the **Extractor**.
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
    st.write("- 📧 Email: support@rxnchemistry.com")
    st.write("- 🌐 Website: [IBM RXN](https://rxn.res.ibm.com)")

def settings_page():
    st.markdown('<div class="title">⚙️ Settings</div>', unsafe_allow_html=True)
    st.write("Customize app preferences below:")
    theme_choice = st.radio("Choose Theme:", ["Light", "Dark"], index=0 if st.get_option("theme.base") == "light" else 1)
    if theme_choice == "Light":
        st.write("🌞 Light theme activated (refresh required)")
        st.set_option("theme.base", "light")
    else:
        st.write("🌙 Dark theme activated (refresh required)")
        st.set_option("theme.base", "dark")
    st.info("⚡ Some theme changes may require page refresh.")

# --- PAGE ROUTING ---
page_routes = {
    "Home": home_page,
    "Extractor": extractor_page,
    "Documentation": documentation_page,
    "About": about_page,
    "Contact": contact_page,
    "Settings": settings_page
}

page_routes[st.session_state.page]()
