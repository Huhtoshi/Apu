import streamlit as st
import base64

# Load the logo and background images
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page background
def set_background(png_file):
    bg_image_encoded = load_image_as_base64(png_file)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_image_encoded}");
        background-size: cover;
        background-position: center;
        font-family: 'Courier New', monospace;
    }}
    .center-title {{
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        color: #FFFFFF;
        margin-top: 10px;
        gap: 10px;
    }}
    .center-title img {{
        width: 150px;
        height: 150px;
    }}
    h1, h2, h3, h4 {{
        color: #FFD700; /* Gold for headings */
        text-align: center;
    }}
    .card {{
        background-color: rgba(30, 30, 30, 0.8); /* Dark background for card style */
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }}
    .section-title {{
        font-size: 22px;
        font-weight: bold;
        color: #FFD700; /* Gold color */
        margin-bottom: 10px;
    }}
    .section-content {{
        font-size: 16px;
        color: #FFFFFF;
        line-height: 1.6;
    }}
    .nav-bar {{
        background-color: rgba(30, 30, 30, 0.9);
        padding: 10px 20px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        gap: 30px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }}
    .nav-item {{
        font-size: 16px;
        font-weight: bold;
        color: #FFD700;
        cursor: pointer;
    }}
    .nav-item-selected {{
        color: #FFFFFF;
        border-bottom: 2px solid #FFD700;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set the background image
set_background("APU_web.png")  # Replace with your background image file path

# Centered Title with Logo
st.markdown(f"""
<div class="center-title">
    <img src="data:image/png;base64,{load_image_as_base64('Apu_logo.png')}" alt="Apu Coin Logo"> <!-- Replace with your logo file path -->
    <h1>Apu Coin</h1>
</div>
""", unsafe_allow_html=True)

# Navigation buttons
selected_section = st.radio("", ["About Apu Coin", "Tokenomics", "Roadmap"], horizontal=True)

# Apply style based on the selected section
nav_items = {
    "About Apu Coin": "nav-item-selected" if selected_section == "About Apu Coin" else "nav-item",
    "Tokenomics": "nav-item-selected" if selected_section == "Tokenomics" else "nav-item",
    "Roadmap": "nav-item-selected" if selected_section == "Roadmap" else "nav-item"
}

# Custom HTML for the Navigation Bar
st.markdown(f"""
<div class="nav-bar">
    <span class="{nav_items['About Apu Coin']}">About Apu Coin</span>
    <span class="{nav_items['Tokenomics']}">Tokenomics</span>
    <span class="{nav_items['Roadmap']}">Roadmap</span>
</div>
""", unsafe_allow_html=True)

# Content Sections
if selected_section == "About Apu Coin":
    st.markdown("""
    <div class="card">
        <h2 class="section-title">About Apu Coin</h2>
        <div class="section-content">
            <p><strong>Apu Coin – A Meme Coin with a Twist!</strong></p>
            <p>Apu Coin is inspired by the Apu meme community and is here to bring meme culture to the world of cryptocurrency. Holders of Apu Coin will be part of an exclusive community that shares, laughs, and builds together in a unique, internet-driven ecosystem. Join us as we redefine the meme coin landscape with Apu's signature style!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Tokenomics":
    st.markdown("""
    <div class="card">
        <h2 class="section-title">Apu Coin Tokenomics</h2>
        <div class="section-content">
            <strong>Total Supply</strong>: 1 Billion Apu Coins<br><br>
            <strong>Community Rewards</strong>: 40% - Rewarding engagement, memes, and creative content.<br><br>
            <strong>Liquidity Pool</strong>: 30% - Locked to ensure stability and trust.<br><br>
            <strong>Marketing & Partnerships</strong>: 15% - For brand outreach and partnerships within the meme culture.<br><br>
            <strong>Development</strong>: 10% - Supporting innovative features and future updates.<br><br>
            <strong>Reserve</strong>: 5% - Held for future upgrades and strategic needs.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Roadmap":
    st.markdown("""
    <div class="card">
        <h2 class="section-title">Apu Coin Roadmap</h2>
        <div class="section-content">
            <strong>Phase 1: Launch & Awareness</strong><br>
            - Initial coin launch, social media campaigns, and community building.<br><br>
            <strong>Phase 2: Meme Expansion</strong><br>
            - Collaborations with meme creators, community events, and reward programs.<br><br>
            <strong>Phase 3: Digital Assets Integration</strong><br>
            - Launch Apu-themed NFTs and collectible assets.<br><br>
            <strong>Phase 4: Growth & Listings</strong><br>
            - Aim for listings on major exchanges, expanding community engagement and outreach.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Community Links
st.markdown("""
<div style="
    background-color: rgba(30, 30, 30, 0.85); 
    padding: 15px; 
    border-radius: 10px; 
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); 
    max-width: 300px;
    margin: 20px auto;
    text-align: center;
">
    <h3 style="color: #FFD700; margin-top: 0;">Join the Community</h3>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/twitter.png" width="24"/>
        <a href="https://x.com/ApuCoin" target="_blank" style="color: #1DA1F2; text-decoration: none; font-weight: bold;">Follow us on Twitter</a>
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/telegram-app.png" width="24"/>
        <a href="https://t.me/ApuCoinCommunity" target="_blank" style="color: #0088cc; text-decoration: none; font-weight: bold;">Join our Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)
