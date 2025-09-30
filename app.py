import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# --- PAGE CONFIG ---
st.set_page_config(page_title="IBM RXN Protocol Extractor", layout="wide")

# --- INIT SESSION STATE ---
if "api_key" not in st.session_state:
    # Default to secrets if available
    st.session_state.api_key = st.secrets.get("ibm_rxn_api_key", "")

# --- CUSTOM CSS FOR NAVBAR ---
st.markdown("""
    <style>
    .navbar {
        background-color: #1E1E2F;
        overflow: hidden;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 40px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .navbar h1 {
        color: #ffffff;
        font-size: 22px;
        margin: 0;
        font-family: 'Poppins', sans-serif;
    }
    .navbar a {
        color: #f2f2f2;
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

# --- NAVIGATION ---
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

st.markdown(f"""
    <div class="navbar">
        <h1>IBM RXN Chemistry</h1>
        <div>
            <a href="?page=home">Home</a>
            <a href="?page=docs">Documentation</a>
            <a href="?page=help">Help</a>
            <a href="?page=settings">Settings</a>
            <a href="mailto:support@ibmrxn.com?subject=Support%20Request%20%E2%80%93%20RXN%20App&body=Hello%20Support%20Team,%0D%0A%0D%0AI%20need%20help%20with%20the%20IBM%20RXN%20Protocol%20Extractor.%0D%0A%0D%0ADetails%20of%20the%20issue:%0D%0A-%20Steps%20to%20reproduce:%0D%0A-%20Expected%20output:%0D%0A-%20Actual%20output:%0D%0A%0D%0AThanks,%0D%0A[Your%20Name]" target="_blank">Contact</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- PAGE CONTENTS ---
if page == "home":
    st.title("🧪 Protocol Extractor")
    st.write("Paste your **chemical reaction procedure text** below:")

    api_key = st.session_state.api_key
    if not api_key:
        st.warning("⚠️ No API key set. Please go to **Settings** to enter your IBM RXN API key.")
    else:
        rxn_wrapper = RXN4ChemistryWrapper(api_key=api_key)

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

elif page == "docs":
    st.title("📘 Documentation")
    st.markdown("""
    Welcome to the **IBM RXN Protocol Extractor Documentation**.  
    Here’s what you can do:
    - **Input chemical reaction procedures** in plain text.
    - The app will extract **step-by-step synthesis actions**.
    - Useful for chemists, researchers, and lab automation.
    
    🔗 Official Docs: [IBM RXN for Chemistry](https://rxn.res.ibm.com)
    """)

elif page == "help":
    st.title("🆘 Help & Usage Guide")
    st.markdown("""
    ### How to Use the IBM RXN Protocol Extractor:
    1. Go to the **Home** page.
    2. Paste your reaction procedure text into the textbox.
    3. Click **Extract Protocol Steps**.
    4. The system will return step-by-step synthesis instructions.
    
    ### Example Input:
    ```
    Add 5 g of NaCl to 50 mL of water and stir for 10 minutes at room temperature.
    ```
    
    ### Example Output:
    1. Weigh 5 g of NaCl  
    2. Add to 50 mL water  
    3. Stir for 10 minutes at room temperature  
    
    ---
    💡 If you still face issues, click **Contact** in the navbar to email our support team.
    """)

elif page == "settings":
    st.title("⚙️ Settings")
    st.write("Update your IBM RXN API key here:")

    new_key = st.text_input("API Key", value=st.session_state.api_key, type="password")

    if st.button("Save API Key"):
        st.session_state.api_key = new_key
        st.success("✅ API key updated successfully!")

else:
    st.error("❌ Page not found.")
