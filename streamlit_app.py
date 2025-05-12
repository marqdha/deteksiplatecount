import streamlit as st

st.markdown("""
    <style>
    .main {
        background-color: #99BC85;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4CAF50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🧫 KALKULATOR KOLONI BAKTERI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Capek hitung bakteri? Biar kami bantu 🤪</p>', unsafe_allow_html=True)

st.write("Masukkan datamu di bawah ini, dan lihat hasilnya 🎯.")



jumlah_koloni = st.number_input("🧫 Masukkan jumlah koloni:", min_value=0, step=1)
faktor_pengenceran = st.number_input("💧 Masukkan faktor pengenceran:", min_value=1, step=1)
volume_inokulasi = st.number_input("📏 Masukkan volume inokulasi (mL):", min_value=0.01, step=0.01)


if st.button("🚀 Hitung CFU/mL"):
    if volume_inokulasi > 0:
        hasil = jumlah_koloni / (faktor_pengenceran * volume_inokulasi)
        st.success(f"🎯 Hasil hitungan: {hasil:.2f} CFU/mL (Colony Forming Units per mL)")
        st.balloons()  # <--- ini animasi confetti / balon!
        st.info("Bakteri udah dihitung, sekarang waktunya kamu santai dulu! ☕🦠")
    else:
        st.error("❌ Volume inokulasi tidak boleh nol ya!")

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)

