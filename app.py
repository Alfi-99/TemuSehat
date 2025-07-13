import streamlit as st

st.set_page_config(
    page_title="TemuSehat",
    page_icon="🌿",
    layout="centered"
)

# Styling tampilan kecil + warna font jelas
st.markdown("""
    <style>
    .stApp {
        background-color: #e8f5e9;
        font-family: 'Segoe UI', sans-serif;
        color: #1b1b1b;
    }
    h1 {
        color: #1b5e20;
        text-align: center;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 0.2em;
    }
    h3 {
        color: #2e7d32;
        text-align: center;
        font-size: 17px;
        font-weight: 500;
        margin-top: 0;
    }
    .intro {
        text-align: center;
        font-size: 14px;
        max-width: 520px;
        margin: auto;
        color: #2f2f2f;
    }
    .chat-bubble-user {
        background-color: #dcedc8;
        color: #000;
        font-size: 13px;
        padding: 8px 12px;
        border-radius: 12px 12px 0px 12px;
        max-width: 65%;
        margin-left: auto;
        margin-bottom: 8px;
    }
    .chat-bubble-bot {
        background-color: #c8e6c9;
        color: #000;
        font-size: 13px;
        padding: 8px 12px;
        border-radius: 12px 12px 12px 0px;
        max-width: 65%;
        margin-right: auto;
        margin-bottom: 8px;
    }
    .chat-container {
        max-width: 600px;
        margin: auto;
        padding: 10px 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul & deskripsi
st.markdown("<h1>🌿 TemuSehat</h1>", unsafe_allow_html=True)
st.markdown("<h3>Asisten Virtual Herbal Mandiri</h3>", unsafe_allow_html=True)
st.markdown("""
<div class='intro'>
Tanyakan gejala ringan Anda seperti pusing, batuk, mual, dll.  
TemuSehat akan bantu beri saran berbasis tanaman obat.
</div><br>
""", unsafe_allow_html=True)

# Inisialisasi sesi
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tampilkan riwayat chat
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"<div class='chat-bubble-user'>🧑 {user_msg}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-bubble-bot'>🌿 {bot_msg}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Input user
user_input = st.chat_input("Tulis keluhan Anda...")

if user_input:
    response = """🌱 <strong>Saran Herbal:</strong><br>
Minum rebusan <em>jahe merah + madu</em> 2x sehari.<br><br>
📝 Jika tidak membaik dalam 3 hari, segera periksa ke dokter."""
    st.session_state.chat_history.append((user_input, response))
    st.rerun()
