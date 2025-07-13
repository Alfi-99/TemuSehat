import streamlit as st
import random
import re

st.set_page_config(
    page_title="TemuSehat - Asisten Herbal Cerdas",
    page_icon="🌿",
    layout="wide"
)

# Enhanced Styling with modern UI and animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #2e7d32, #388e3c);
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-radius: 0 0 20px 20px;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeInDown 1s ease-out;
    }
    
    .sub-title {
        font-size: 1.1rem;
        font-weight: 400;
        opacity: 0.9;
        margin-bottom: 1rem;
        animation: fadeInUp 1s ease-out 0.2s both;
    }
    
    .feature-badges {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    
    .feature-badge {
        background: rgba(255,255,255,0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        backdrop-filter: blur(10px);
        animation: fadeInUp 1s ease-out 0.4s both;
    }
    
    .intro {
        text-align: center;
        font-size: 16px;
        max-width: 600px;
        margin: 2rem auto;
        color: #2f2f2f;
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #4caf50;
    }
    
    .chat-bubble-user {
        background: linear-gradient(135deg, #81c784, #66bb6a);
        color: white;
        font-size: 14px;
        padding: 12px 16px;
        border-radius: 18px 18px 4px 18px;
        max-width: 70%;
        margin-left: auto;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        animation: slideInRight 0.3s ease-out;
    }
    
    .chat-bubble-bot {
        background: white;
        color: #2e2e2e;
        font-size: 14px;
        padding: 12px 16px;
        border-radius: 18px 18px 18px 4px;
        max-width: 75%;
        margin-right: auto;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 3px solid #4caf50;
        animation: slideInLeft 0.3s ease-out;
    }
    
    .red-flag-alert {
        background: linear-gradient(135deg, #ffebee, #ffcdd2);
        color: #c62828;
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid #f44336;
        margin: 10px 0;
        box-shadow: 0 2px 8px rgba(244, 67, 54, 0.2);
    }
    
            
    .chat-container {
        max-width: 800px;
        margin: auto;
        padding: 0 0 10px 0;
        min-height: 0;
    }
    
    .typing-indicator {
        display: flex;
        align-items: center;
        gap: 5px;
        color: #666;
        font-style: italic;
        margin: 10px 0;
    }
    
    .dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #4caf50;
        animation: typing 1.4s infinite;
    }
    
    .dot:nth-child(2) { animation-delay: 0.2s; }
    .dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes typing {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-10px); }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .stChatInput > div {
        background: white;
        border-radius: 25px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .quick-buttons {
        margin: 20px 0;
        padding: 15px;
        background: rgba(255,255,255,0.7);
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .stButton > button {
        border-radius: 20px;
        border: 2px solid #4caf50;
        background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
        color: #2e7d32;
        font-weight: 500;
        transition: all 0.3s ease;
        margin: 5px 0;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #4caf50, #66bb6a);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    
    .clear-button button {
        background: linear-gradient(135deg, #ffcdd2, #ffebee);
        border: 2px solid #f44336;
        color: #c62828;
    }
    
    .clear-button button:hover {
        background: linear-gradient(135deg, #f44336, #e53935);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Header dengan desain menarik
st.markdown("""
<div class='main-header'>
    <div class='main-title'>🌿 TemuSehat</div>
    <div class='sub-title'>Asisten Herbal Cerdas - Solusi Alami untuk Hidup Sehat</div>
    <div class='feature-badges'>
        <span class='feature-badge'>🔍 Red Flag Detection</span>
        <span class='feature-badge'>💬 Chat Informal</span>
        <span class='feature-badge'>🌱 Herbal Lokal</span>
        <span class='feature-badge'>📚 E-book Premium</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='intro'>
    <strong>Halo! Gimana kabarnya hari ini? 😊</strong><br><br>
    Ceritain aja keluhan yang lagi kamu rasain, seperti pusing, batuk, mual, atau yang lainnya. 
    Aku bakal kasih saran herbal alami yang cocok buat kamu! Tapi inget ya, kalau gejalanya parah 
    atau nggak membaik, langsung ke dokter aja. Kesehatan kamu prioritas utama! 💚
</div><br>
""", unsafe_allow_html=True)

# Inisialisasi sesi
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Database pengetahuan herbal (dummy)
herbal_recommendations = {
    "pusing": [
        "Minum teh daun mint atau peppermint hangat. Aromanya bisa bantu redakan tension di kepala!",
        "Coba kompres dingin di dahi sambil minum air jahe hangat. Biasanya manjur buat pusing karena kelelahan.",
        "Daun sirsak direbus jadi teh, diminum 2x sehari. Tapi jangan kebanyakan ya, nanti malah ngantuk 😴"
    ],
    "batuk": [
        "Campuran madu + jeruk nipis + jahe merah. Diminum hangat-hangat, dijamin batuknya reda!",
        "Air rebusan daun thyme atau oregano segar. Tapi kalau susah cari, bisa pake teh herbal yang ada thyme-nya.",
        "Daun sirih direbus, airnya buat kumur dan diminum sedikit. Antiseptik alami yang ampuh!"
    ],
    "mual": [
        "Jahe segar diparut, diseduh air hangat + madu. Atau kalau males, permen jahe juga oke!",
        "Daun mint segar dikunyah atau diseduh. Efeknya segar dan langsung mengurangi rasa mual.",
        "Air kelapa muda + perasan jeruk nipis. Selain anti mual, juga nambah elektrolit tubuh!"
    ],
    "demam": [
        "Rebusan daun sambiloto + sedikit madu. Pahit sih, tapi manjur buat turunin demam ringan.",
        "Kompres air hangat + minyak kayu putih di dahi. Sambil minum banyak air putih ya!",
        "Teh jahe merah + kunyit + madu. Triple combo yang ampuh buat boost imunitas!"
    ],
    "sakit_perut": [
        "Air hangat + perasan jeruk nipis + garam sedikit. Bisa bantu netralkan asam lambung.",
        "Daun jambu biji muda direbus, airnya diminum. Bagus buat masalah pencernaan ringan.",
        "Teh chamomile atau teh peppermint hangat. Efek relaxing-nya bikin perut jadi tenang."
    ],
    "insomnia": [
        "Teh lavender atau chamomile 1 jam sebelum tidur. Dijamin tidur nyenyak!",
        "Minum susu hangat + kunyit + madu. Resep nenek yang nggak pernah gagal 😊",
        "Aromaterapi minyak esensial lavender di kamar. Atau bisa taro kantung kering lavender di bawah bantal."
    ]
}

# Red flag symptoms yang perlu penanganan medis
red_flag_keywords = [
    "sesak napas", "nyeri dada", "darah", "muntah darah", "demam tinggi", 
    "pingsan", "kejang", "tidak sadarkan diri", "denyut jantung", 
    "stroke", "serangan jantung", "overdosis", "keracunan"
]

def detect_red_flag(text):
    """Deteksi gejala berbahaya yang memerlukan penanganan medis"""
    text_lower = text.lower()
    for keyword in red_flag_keywords:
        if keyword in text_lower:
            return True
    return False

def get_herbal_recommendation(user_input):
    """Generate respons berdasarkan keluhan user"""
    user_input_lower = user_input.lower()
    
    # Cek red flag dulu
    if detect_red_flag(user_input):
        return """
        <div class='red-flag-alert'>
        🚨 <strong>PERINGATAN!</strong><br>
        Gejala yang kamu sebutin ini perlu penanganan medis segera! 
        Jangan tunda lagi, langsung ke IGD atau dokter terdekat ya! 
        Kesehatan kamu jauh lebih penting dari apapun! 🏥
        </div>
        """
    
    # Mapping kata kunci ke kategori gejala
    symptom_mapping = {
        "pusing": ["pusing", "sakit kepala", "kepala pusing", "migrain", "vertigo"],
        "batuk": ["batuk", "batuk kering", "batuk berdahak", "tenggorokan", "serak"],
        "mual": ["mual", "muntah", "eneg", "perut mual", "morning sickness"],
        "demam": ["demam", "panas", "meriang", "flu", "pilek", "hidung tersumbat"],
        "sakit_perut": ["sakit perut", "perut sakit", "kembung", "diare", "sembelit", "mag"],
        "insomnia": ["susah tidur", "insomnia", "tidak bisa tidur", "begadang", "gangguan tidur"]
    }
    
    # Cari kategori yang cocok
    matched_category = None
    for category, keywords in symptom_mapping.items():
        for keyword in keywords:
            if keyword in user_input_lower:
                matched_category = category
                break
        if matched_category:
            break
    
    if matched_category:
        recommendation = random.choice(herbal_recommendations[matched_category])
        return f"""🌱 <strong>Oke, aku paham keluhannya!</strong><br><br>
        {recommendation}<br><br>
        💡 <em>Tips tambahan:</em> Pastikan istirahat cukup dan minum air putih yang banyak ya!<br><br>
        ⚠️ Kalau dalam 2-3 hari nggak ada perbaikan atau malah memburuk, 
        langsung konsultasi ke dokter aja ya! Jangan diabaikan 😊
        """
    else:
        # Respons umum untuk keluhan yang tidak spesifik
        general_responses = [
            """🤔 <strong>Hmm, bisa ceritain lebih detail nggak?</strong><br><br>
            Misalnya: lokasi sakitnya dimana, udah berapa lama, atau ada gejala lain yang menyertai? 
            Biar aku bisa kasih saran yang lebih tepat! 😊""",
            
            """💭 <strong>Aku belum terlalu paham keluhannya nih...</strong><br><br>
            Coba sebutin gejala spesifiknya ya, seperti: pusing, batuk, mual, demam, sakit perut, 
            atau susah tidur. Biar rekomendasinya lebih akurat! 🎯""",
            
            """🌿 <strong>Secara umum, untuk menjaga kesehatan:</strong><br><br>
            • Minum air putih minimal 8 gelas/hari<br>
            • Konsumsi buah dan sayur segar<br>
            • Istirahat cukup 7-8 jam<br>
            • Olahraga ringan rutin<br><br>
            Ada keluhan spesifik yang bisa aku bantu? 😊"""
        ]
        
        return random.choice(general_responses)

# Sidebar dengan informasi produk
with st.sidebar:
    st.markdown("### 🌿 TemuSehat Premium")
    st.markdown("---")
    
    # Fitur unggulan
    st.markdown("#### ✨ Fitur Unggulan")
    st.markdown("""
    - 🔍 **Red Flag Detection**: Deteksi dini gejala darurat
    - 💬 **Chat Informal**: Ngobrol santai seperti teman
    - 🌱 **Database Herbal**: 100+ tanaman obat lokal
    - 📚 **E-book Premium**: Panduan lengkap herbal
    """)
    
    st.markdown("---")
    
    # Quick tips
    st.markdown("#### 💡 Tips Sehat Hari Ini")
    daily_tips = [
        "Minum air jahe hangat di pagi hari untuk boost imunitas! 🫖",
        "Daun mint bisa jadi aromaterapi alami untuk relaksasi 🌿",
        "Madu + jeruk nipis = combo anti batuk yang manjur! 🍯",
        "Teh chamomile sebelum tidur bikin tidur lebih nyenyak 😴",
        "Kompres jahe hangat bisa redakan pegal-pegal 💆‍♀️"
    ]
    st.info(random.choice(daily_tips))
    
    st.markdown("---")
    
    # Afiliasi toko herbal
    st.markdown("#### 🏪 Mitra Toko Herbal")
    st.markdown("""
    **Beli bahan herbal berkualitas:**
    - 🌿 Toko Herbal Nusantara
    - 🌱 Kebun Rempah Indonesia  
    - 🍃 Apotek Tradisional Sehat
    
    *Dapatkan diskon 10% dengan kode: TEMUSEHAT*
    """)
    
    st.markdown("---")
    
    # Upgrade premium
    if st.button("📚 Upgrade Premium"):
        st.balloons()
        st.success("Terima kasih! Fitur premium segera hadir! 🎉")

# Tampilkan riwayat chat
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"<div class='chat-bubble-user'>🧑 {user_msg}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-bubble-bot'>🌿 {bot_msg}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Fungsi untuk menambahkan quick reply buttons
def show_quick_buttons():
    st.markdown('<h3 style="color:black;">💡 Pilihan Cepat:</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤕 Lagi pusing nih", key="pusing_btn", use_container_width=True):
            response = get_herbal_recommendation("pusing")
            st.session_state.chat_history.append(("Lagi pusing nih", response))
            st.rerun()
    
    with col2:
        if st.button("😷 Batuk terus", key="batuk_btn", use_container_width=True):
            response = get_herbal_recommendation("batuk")
            st.session_state.chat_history.append(("Batuk terus", response))
            st.rerun()
    
    with col3:
        if st.button("🤢 Perut mual", key="mual_btn", use_container_width=True):
            response = get_herbal_recommendation("mual")
            st.session_state.chat_history.append(("Perut mual", response))
            st.rerun()
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("🔥 Demam ringan", key="demam_btn", use_container_width=True):
            response = get_herbal_recommendation("demam")
            st.session_state.chat_history.append(("Demam ringan", response))
            st.rerun()
    
    with col5:
        if st.button("😴 Susah tidur", key="tidur_btn", use_container_width=True):
            response = get_herbal_recommendation("susah tidur")
            st.session_state.chat_history.append(("Susah tidur", response))
            st.rerun()
    
    with col6:
        if st.button("🤰 Sakit perut", key="perut_btn", use_container_width=True):
            response = get_herbal_recommendation("sakit perut")
            st.session_state.chat_history.append(("Sakit perut", response))
            st.rerun()

# Input user
user_input = st.chat_input("Ceritain keluhan kamu disini... (contoh: lagi pusing nih)")

if user_input:
    # Generate response menggunakan fungsi yang sudah dibuat
    response = get_herbal_recommendation(user_input)
    st.session_state.chat_history.append((user_input, response))
    st.rerun()

# Tampilkan menu pilihan
if len(st.session_state.chat_history) == 0:
    st.markdown('<h3 style="color:black;">💬 Mulai Percakapan:</h3>', unsafe_allow_html=True)
    show_quick_buttons()
else:
    # Tambahkan separator dan menu di bawah chat
    st.markdown("---")
    show_quick_buttons()
    
    # Tambahkan tombol clear chat
    col_clear1, col_clear2, col_clear3 = st.columns([1, 1, 1])
    with col_clear2:
        if st.button("🗑️ Hapus Riwayat Chat", key="clear_chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
