import streamlit as st
import time

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="AI Mentor - THCS Thuận Hưng", layout="centered", page_icon="🤖")

st.markdown("""
    <style>
    .chat-container { border-radius: 10px; padding: 15px; background-color: #f8fafc; border: 1px solid #e2e8f0; margin-bottom: 10px; }
    .user-msg { color: #1e3a8a; font-weight: bold; }
    .ai-msg { color: #047857; }
    .stButton>button { background-color: #1e40af !important; color: white !important; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Trợ lý Học tập 24/7 - Thầy Hậu")
st.subheader("Hệ thống phát triển Năng lực số cá nhân hóa (Thông tư 02/2025)")

# Danh sách thử thách năng lực số (Dựa theo Phụ lục 3)
challenges = {
    "Bài 7: Tính toán Excel": {
        "mã": "5.2.TC1a",
        "tình_huống": "Mẹ em vừa mở một cửa hàng bán trái cây. Hãy giúp mẹ tạo một bảng tính để tự động tính tổng tiền khách mua.",
        "gợi_ý": "Em hãy nhớ lại: Khi muốn tính TỔNG nhiều con số trong Excel, mình dùng hàm gì nhỉ?"
    },
    "Bài 5: Ứng xử trên mạng": {
        "mã": "4.3.TC1b",
        "tình_huống": "Một người bạn rủ em tham gia bình luận chê bai một bạn khác trên Facebook. Em sẽ xử lý thế nào?",
        "gợi_ý": "Trước khi bình luận, em hãy đặt câu hỏi: Hành động này có an toàn và có làm tổn thương người khác không?"
    }
}

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🏆 Bảng điều khiển")
    selected_task = st.selectbox("Chọn Thử thách số:", list(challenges.keys()))
    st.info(f"**Mã NLS:** {challenges[selected_task]['mã']}")
    st.write("---")
    st.write("**Tiến trình của em:**")
    st.progress(65, text="Đạt 65% Năng lực số")
    
with col2:
    st.markdown("### 💬 Khu vực Thảo luận với AI Mentor")
    
    # Khu vực chat giả lập
    with st.container():
        st.markdown(f'<div class="chat-container"><b>Tình huống hiện tại:</b> {challenges[selected_task]["tình_huống"]}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="chat-container"><span class="user-msg">Học sinh:</span> Thầy AI ơi, em không biết phải bắt đầu lập công thức từ đâu ạ.</div>', unsafe_allow_html=True)
        
        if st.button("Hỏi AI Mentor gợi ý"):
            with st.spinner("AI Mentor đang suy nghĩ..."):
                time.sleep(1.5)
                reply = challenges[selected_task]["gợi_ý"]
                st.markdown(f'<div class="chat-container"><span class="ai-msg">AI Mentor:</span> Chào em! Em đừng lo. {reply}</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phát triển bởi Thầy Trần Trung Hậu - Trường THCS Thuận Hưng - Phường Thuận Hưng  tháng 9/2025</p>", unsafe_allow_html=True)
