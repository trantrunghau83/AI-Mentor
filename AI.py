import streamlit as st
import time

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="AI Mentor - THCS Thuận Hưng", layout="wide", page_icon="🤖")

st.markdown("""
    <style>
    .stButton>button { background-color: #1e40af !important; color: white !important; border-radius: 8px; }
    .challenge-box { background-color: #f0fdf4; padding: 15px; border-left: 5px solid #16a34a; border-radius: 5px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Trợ lý Học tập 24/7 - AI Mentor")
st.subheader("Hệ thống phát triển Năng lực số cá nhân hóa (Thông tư 02/2025)")

# 1. BỔ SUNG NHIỀU BÀI HỌC VÀ THỬ THÁCH (TỪ PHỤ LỤC 3)
challenges = {
    "Bài 5: Ứng xử trên mạng": {
        "mã": "4.3.TC1b",
        "tình_huống": "Một người bạn rủ em tham gia bình luận chê bai một bạn khác trên mạng xã hội. Em sẽ xử lý thế nào?",
        "topic": "Đạo đức và an toàn trên mạng"
    },
    "Bài 6: Làm quen với phần mềm bảng tính": {
        "mã": "3.1.TC1a",
        "tình_huống": "Thầy giáo yêu cầu em nhập danh sách lớp kèm theo điểm số vào máy tính, nhưng tên các bạn bị che khuất một phần. Em sẽ làm sao để cột tên rộng ra cho dễ nhìn?",
        "topic": "Định dạng bảng tính cơ bản"
    },
    "Bài 7: Tính toán tự động trên bảng tính": {
        "mã": "5.2.TC1a",
        "tình_huống": "Mẹ em vừa mở một cửa hàng bán trái cây. Hãy giúp mẹ tạo một bảng tính để tự động tính tổng tiền khách mua mà không cần bấm máy tính cầm tay.",
        "topic": "Hàm tính toán trong Excel"
    },
    "Bài 14: Thuật toán tìm kiếm": {
        "mã": "3.4.TC1a",
        "tình_huống": "Em có một xấp bài kiểm tra đã được sắp xếp theo thứ tự A, B, C... Làm cách nào để em tìm ra bài của bạn 'Trần Trung Hậu' nhanh nhất?",
        "topic": "Tư duy thuật toán (Tìm kiếm nhị phân)"
    }
}

col1, col2 = st.columns([1, 2.5])

with col1:
    st.markdown("### 🏆 Bảng điều khiển")
    # Học sinh chọn bài học
    selected_task = st.selectbox("📚 Chọn Thử thách số:", list(challenges.keys()))
    
    st.info(f"**Mã NLS:** {challenges[selected_task]['mã']}")
    st.markdown(f"**Chủ đề:** {challenges[selected_task]['topic']}")
    st.write("---")
    st.write("**Tiến trình của em:**")
    st.progress(75, text="Đạt 75% Năng lực số")
    
with col2:
    st.markdown("### 💬 Lớp học 1-kèm-1 với AI Mentor")
    
    # Hiển thị Tình huống thực tế
    st.markdown(f'<div class="challenge-box"><b>Tình huống hiện tại:</b> {challenges[selected_task]["tình_huống"]}</div>', unsafe_allow_html=True)
    
    # 2. HỆ THỐNG CHAT TƯƠNG TÁC (HS ĐẶT CÂU HỎI TỰ DO)
    # Khởi tạo bộ nhớ tạm thời để lưu lịch sử đoạn chat
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "ai", "content": "Chào em! Thầy là AI Mentor. Em đã đọc kỹ tình huống chưa? Em có câu hỏi nào hay cần thầy hướng dẫn bước đầu tiên không?"})
        
    # Nút reset đoạn chat khi học sinh đổi bài
    if st.button("🔄 Làm mới khung chat (Bắt đầu lại bài học này)"):
        st.session_state.messages = [{"role": "ai", "content": "Chào em! Thầy là AI Mentor. Em đã đọc kỹ tình huống chưa? Em có câu hỏi nào hay cần thầy hướng dẫn bước đầu tiên không?"}]

    # In ra toàn bộ lịch sử trò chuyện
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👦"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.write(msg["content"])

    # Khung nhập liệu cho học sinh
    user_input = st.chat_input("Nhập câu hỏi của em tại đây (VD: Thầy ơi em không biết dùng hàm gì để tính tổng ạ?)...")
    
    if user_input:
        # Hiển thị câu hỏi của HS lên màn hình
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👦"):
            st.write(user_input)
            
        # Tạo hiệu ứng "AI đang suy nghĩ"
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("AI Mentor đang phân tích câu hỏi..."):
                time.sleep(1.5) # Giả lập thời gian AI xử lý
                
                # --- AI XỬ LÝ VÀ ĐƯA RA CÂU TRẢ LỜI CHI TIẾT ---
                reply = ""
                lower_input = user_input.lower()
                
                if "hàm" in lower_input or "tổng" in lower_input or "tính" in lower_input:
                    reply = "Để tính toán tự động, Excel cung cấp các hàm rất tiện lợi. Nếu em muốn tính **TỔNG**, em có thể dùng hàm **SUM**.\n\n👉 **Cú pháp:** `=SUM(vùng_dữ_liệu)` \n\nEm thử nhấp vào ô cần tính kết quả, gõ `=SUM(` rồi dùng chuột kéo quét các ô chứa giá tiền của mẹ xem sao nhé. Cứ thử đi, nếu làm sai mình có thể ấn Ctrl+Z để quay lại mà!"
                
                elif "tìm" in lower_input or "nhanh nhất" in lower_input or "cách nào" in lower_input:
                    reply = "Câu hỏi rất thông minh! Trong bài này, vì xấp bài đã được **sắp xếp theo vần A-B-C**, nên em không cần tìm từng tờ một từ trên xuống dưới (đó là tìm kiếm tuần tự).\n\n💡 **Gợi ý:** Em hãy lấy ngay tờ ở chính giữa xấp bài ra xem. Tên là 'Hậu' (vần H) sẽ nằm trước vần M, đúng không? Vậy em có thể bỏ luôn nửa xấp bài phía sau đi và tiếp tục chia đôi phần còn lại. Thuật toán này gọi là gì, em còn nhớ không?"
                
                elif "rộng" in lower_input or "cột" in lower_input or "che khuất" in lower_input:
                    reply = "Ah, lỗi chữ bị che khuất là rất phổ biến! Để làm rộng cột nhanh nhất, em không cần phải dùng chuột kéo rát tay đâu.\n\n👉 **Cách làm:** Em hãy di chuyển chuột lên dòng tiêu đề cột (chỗ các chữ cái A, B, C...). Khi con trỏ chuột lọt vào giữa ranh giới 2 cột và biến thành mũi tên 2 chiều, em hãy **nhấp đúp chuột trái** (Double-click) nhé. Excel sẽ tự động căn chỉnh độ rộng cột vừa khít với dòng chữ dài nhất!"
                
                elif "không" in lower_input or "chê" in lower_input or "mạng" in lower_input or "từ chối" in lower_input:
                    reply = "Tuyệt vời! Chúng ta tuyệt đối không nên hùa theo bình luận chê bai người khác em nhé. \n\nTrên môi trường mạng, em hãy áp dụng quy tắc **T.H.I.N.K** trước khi phát ngôn (T: True - Sự thật, H: Helpful - Có ích, K: Kind - Tử tế). Em có thể nhắn lại với bạn kia rằng: *'Việc này không hay đâu, tụi mình không nên làm tổn thương bạn ấy'* để từ chối một cách khéo léo."
                
                else:
                    reply = f"Thầy hiểu ý của em rồi. Với câu hỏi '{user_input}' của em, hãy thử vận dụng các kiến thức cốt lõi trong **{selected_task.split(':')[0]}** xem sao. Hãy bám sát vào yêu cầu chính của tình huống. Cứ mạnh dạn đưa ra ý tưởng, nếu có chỗ nào chưa hợp lý, thầy sẽ phân tích và hướng dẫn em điều chỉnh ngay!"
                    
                st.write(reply)
        
        # Lưu câu trả lời của AI vào bộ nhớ
        st.session_state.messages.append({"role": "ai", "content": reply})
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phát triển bởi Thầy Trần Trung Hậu - Trường THCS Thuận Hưng, phường Thuận Hưng tháng 9/2025</p>", unsafe_allow_html=True)
