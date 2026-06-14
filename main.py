import random
import time
import streamlit as st

# Configure the page appearance
st.set_page_config(page_title="Premium Money Roulette", page_icon="💸", layout="centered")

# Enhanced Custom CSS styling
st.markdown(
    """
    <style>
    /* Elegant modern dark gradient */
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #111126 50%, #1a103c 100%);
        color: #ffffff;
    }
    /* Clean text typography */
    h1, h2, h3, p, label {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    /* Transparent header bug fix */
    [data-testid="stHeader"] {
        background: transparent;
    }
    /* Premium Red Glow Action Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff4b4b 0%, #e11d48 100%);
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 3.5em;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 4px 20px rgba(255, 75, 75, 0.25);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff6b6b 0%, #f43f5e 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 75, 75, 0.45);
    }
    /* Input field modern styling */
    div[data-baseweb="input"] {
        background-color: #1e1b4b !important;
        border-radius: 10px !important;
        border: 1px solid #312e81 !important;
    }
    input {
        color: white !important;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #090d16;
        border-right: 1px solid #1e1b4b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize application state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "registered_users" not in st.session_state:
    # Default admin credentials can go here or be completely empty
    st.session_state.registered_users = {"admin": "password123"}

# ==========================================
# PAGE 1: AUTHENTICATION SCREEN (LOGIN & SIGNUP)
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; margin-top: 40px;'>🔐 Access the Roulette</h1>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login 🔓", "Create Account 📝"])

    with tab1:
        st.markdown("<p style='opacity:0.7; text-align:center;'>Enter your credentials to unlock the application.</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            login_username = st.text_input("Username", placeholder="Enter your username...", autocomplete="off",
                                           key="login_user")
            login_password = st.text_input("Password", type="password", placeholder="Enter your password...")
            login_button = st.button("Unlock Application 🔓", key="login_btn")

            if login_button:
                if login_username in st.session_state.registered_users and st.session_state.registered_users[
                    login_username] == login_password:
                    st.session_state.logged_in = True
                    st.session_state.admin_user = login_username
                    st.success("Access granted! Loading table...")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password.")

    with tab2:
        st.markdown("<p style='opacity:0.7; text-align:center;'>Register a new username and password below.</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            new_username = st.text_input("Create Username", placeholder="Choose a username...", autocomplete="off",
                                         key="new_user")
            new_password = st.text_input("Create Password", type="password", placeholder="Choose a password...",
                                         key="new_pass")
            signup_button = st.button("Register & Login 🚀", key="signup_btn")

            if signup_button:
                if not new_username or not new_password:
                    st.warning("Please fill in both fields to register.")
                elif new_username in st.session_state.registered_users:
                    st.error("Username already exists. Please pick another one.")
                else:
                    # Save the new user
                    st.session_state.registered_users[new_username] = new_password
                    st.session_state.logged_in = True
                    st.session_state.admin_user = new_username
                    st.success(f"Account created successfully! Welcome, @{new_username}")
                    st.rerun()

# ==========================================
# PAGE 2: THE MONEY ROULETTE SOFTWARE
# ==========================================
else:
    # Sidebar control panel
    with st.sidebar:
        st.title("⚙️ Control Panel")
        st.write(f"Session Active: **@{st.session_state.admin_user}**")
        st.write("---")
        # Easy logout option
        if st.button("Log Out 🚪"):
            st.session_state.logged_in = False
            st.rerun()

    # Main App Header
    st.markdown(
        "<h1 style='text-align: center; color: #ff4b4b; font-size: 3.2rem; font-weight: 800; margin-bottom: 0;'>💸 Money Roulette</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 1.1rem; opacity: 0.7; margin-bottom: 25px;'>Who is stuck handling the check today?</p>",
        unsafe_allow_html=True)

    # Input Area Panel
    with st.container(border=True):
        st.markdown("### 👥 Manage Player Pool")
        raw_names = st.text_input("Add names to the wheel (separate with commas):",
                                  placeholder="Michael, Dwight, Jim, Pam, Angela")

        # Standardize input into lists
        cleaned_input = raw_names.strip()
        list_of_names = [name.strip() for name in cleaned_input.split(",") if name.strip()]

    # Bottom Action Layout
    st.write("")
    spin_clicked = st.button("🎯 Spin the Roulette Wheels!")

    # Dynamic Game Core Execution
    if spin_clicked:
        if len(list_of_names) >= 2:
            # Visual hype simulator
            with st.spinner("🎲 Shuffling profiles and rolling the wheel..."):
                time.sleep(1.8)  # Intentional suspense builder delay

                # Choose winner
                selected_payer = random.choice(list_of_names)

                # Beautiful Card Reveal Display
                st.write("")
                with st.container(border=True):
                    st.markdown(
                        "<h2 style='text-align: center; color: #f43f5e; letter-spacing: 2px;'>🚨 WE HAVE A WINNER 🚨</h2>",
                        unsafe_allow_html=True)
                    html_card = f"""
                    <div style="background: linear-gradient(145deg, rgba(225, 29, 72, 0.15), rgba(159, 18, 57, 0.3)); border: 2px solid #e11d48; border-radius: 16px; padding: 30px 15px; text-align: center; margin: 15px 0; box-shadow: 0 10px 30px rgba(225, 29, 72, 0.2);">
                        <span style="font-size: 1.1rem; display: block; margin-bottom: 8px; color: #fda4af; font-weight: 500; text-transform: uppercase;">The Selected Payer Is:</span>
                        <strong style="font-size: 3rem; color: #ffffff; text-shadow: 0px 0px 15px rgba(244,63,94,0.8); font-weight: 800;">{selected_payer}</strong>
                    </div>
                    """
                    st.markdown(html_card, unsafe_allow_html=True)
                    st.balloons()
        else:
            st.warning("⚠️ Access denied. Please provide at least two individual player names to run the generator.")
