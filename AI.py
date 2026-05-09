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

# 1. KHO HỌC LIỆU VÀ THỬ THÁCH SỐ (TỪ LỚP 7 ĐẾN LỚP 9)
challenges = {
    "Bài 5 (Lớp 7): Ứng xử trên mạng": {
        "mã": "4.3.TC1b",
        "tình_huống": "Một người bạn rủ em tham gia bình luận chê bai một bạn khác trên mạng xã hội. Em sẽ xử lý thế nào?",
        "topic": "Đạo đức và an toàn trên mạng"
    },
    "Bài 6 (Lớp 7): Làm quen với phần mềm bảng tính": {
        "mã": "3.1.TC1a",
        "tình_huống": "Thầy giáo yêu cầu em nhập danh sách lớp kèm theo điểm số vào máy tính, nhưng tên các bạn bị che khuất một phần. Em sẽ làm sao để cột tên rộng ra cho dễ nhìn?",
        "topic": "Định dạng bảng tính cơ bản"
    },
    "Bài 7 (Lớp 7): Tính toán tự động trên bảng tính": {
        "mã": "5.2.TC1a",
        "tình_huống": "Mẹ em vừa mở một cửa hàng bán trái cây. Hãy giúp mẹ tạo một bảng tính để tự động tính tổng tiền khách mua mà không cần bấm máy tính cầm tay.",
        "topic": "Hàm tính toán trong Excel"
    },
    "Bài 14 (Lớp 7): Thuật toán tìm kiếm": {
        "mã": "3.4.TC1a",
        "tình_huống": "Em có một xấp bài kiểm tra đã được sắp xếp theo thứ tự A, B, C... Làm cách nào để em tìm ra bài của bạn 'Trần Trung Hậu' nhanh nhất?",
        "topic": "Tư duy thuật toán (Tìm kiếm nhị phân)"
    },
    "Bài (Lớp 9): Hoàn thiện bảng tính quản lí tài chính gia đình": {
        "mã": "5.3.TC1b",
        "tình_huống": "Gia đình em muốn tổng kết chi tiêu tháng qua để lên kế hoạch tiết kiệm. Nhiệm vụ của em là hoàn thiện bảng tính và chỉ ra xem khoản chi nào đang tốn nhiều tiền nhất. Để nhìn ra ngay khoản chi cao nhất đó, em định dùng tính năng nào của phần mềm?",
        "topic": "Ứng dụng bảng tính vào đời sống & Trực quan hóa dữ liệu"
    }
}

col1, col2 = st.columns([1, 2.5])

with col1:
    st.markdown("### 🏆 Bảng điều khiển")
    selected_task = st.selectbox("📚 Chọn Thử thách số:", list(challenges.keys()))
    
    st.info(f"**Mã NLS:** {challenges[selected_task]['mã']}")
    st.markdown(f"**Chủ đề:** {challenges[selected_task]['topic']}")
    st.write("---")
    st.write("**Tiến trình của em:**")
    st.progress(85, text="Đạt 85% Năng lực số")
    
with col2:
    st.markdown("### 💬 Lớp học 1-kèm-1 với AI Mentor")
    
    st.markdown(f'<div class="challenge-box"><b>Tình huống hiện tại:</b> {challenges[selected_task]["tình_huống"]}</div>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "ai", "content": "Chào em! Thầy là AI Mentor. Em đã đọc kỹ tình huống chưa? Em có câu hỏi nào hay cần thầy hướng dẫn bước đầu tiên không?"})
        
    if st.button("🔄 Làm mới khung chat (Bắt đầu lại bài học này)"):
        st.session_state.messages = [{"role": "ai", "content": "Chào em! Thầy là AI Mentor. Em đã đọc kỹ tình huống chưa? Em có câu hỏi nào hay cần thầy hướng dẫn bước đầu tiên không?"}]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👦"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.write(msg["content"])

    user_input = st.chat_input("Nhập câu hỏi của em tại đây...")
    
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👦"):
            st.write(user_input)
            
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("AI Mentor đang phân tích câu hỏi..."):
                time.sleep(1.5) 
                
                reply = ""
                lower_input = user_input.lower()
                
                # --- AI XỬ LÝ CHO BÀI QUẢN LÝ TÀI CHÍNH LỚP 9 ---
                if any(kw in lower_input for kw in ["chi tiêu", "cao nhất", "tỉ lệ", "biểu đồ", "sắp xếp", "lọc", "tài chính", "nhiều tiền"]):
                    reply = "Để tìm ra khoản chi tiêu cao nhất hoặc nhìn rõ tỉ lệ các khoản chi của gia đình, thầy có 2 gợi ý rất hay cho em:\n\n1️⃣ **Dùng công cụ Sắp xếp (Sort):** Em có thể bôi đen bảng dữ liệu, sau đó sắp xếp cột 'Số tiền' theo thứ tự giảm dần (Từ lớn đến bé). Khoản chi tốn kém nhất sẽ chạy lên đầu danh sách!\n2️⃣ **Vẽ Biểu đồ (Chart):** Em thử bôi đen cột 'Tên khoản chi' và 'Số tiền', sau đó chèn một **Biểu đồ tròn (Pie Chart)**. Biểu đồ sẽ cho em thấy ngay 'miếng bánh' nào to nhất một cách rất trực quan.\n\nEm muốn thầy hướng dẫn chi tiết cách làm thứ 1 hay thứ 2 trước?"
                
                # --- CÁC BÀI CÒN LẠI ---
                elif "hàm" in lower_input or "tổng" in lower_input or "tính" in lower_input:
                    reply = "Để tính toán tự động, Excel cung cấp hàm **SUM**.\n\n👉 **Cú pháp:** `=SUM(vùng_dữ_liệu)` \n\nEm hãy gõ `=SUM(` rồi dùng chuột quét các ô chứa giá tiền nhé!"
                
                elif "tìm" in lower_input or "nhanh nhất" in lower_input or "cách nào" in lower_input:
                    reply = "Vì xấp bài đã được **sắp xếp theo vần A-B-C**, em không cần tìm từng tờ một. \n\n💡 **Gợi ý:** Em hãy lấy ngay tờ ở chính giữa xấp bài ra xem. Nếu tên là vần H, nó sẽ nằm trước vần M, lúc đó em có thể loại bỏ ngay một nửa xấp bài phía sau. Em nhớ thuật toán này tên là gì không?"
                
                elif "rộng" in lower_input or "cột" in lower_input or "che khuất" in lower_input:
                    reply = "👉 **Cách làm:** Em hãy di chuyển chuột lên ranh giới giữa 2 chữ cái tên cột (VD: giữa cột A và B). Khi con trỏ chuột biến thành mũi tên 2 chiều, em hãy **nhấp đúp chuột trái** (Double-click) nhé. Excel sẽ tự động căn chỉnh vừa khít!"
                
                elif "không" in lower_input or "chê" in lower_input or "mạng" in lower_input:
                    reply = "Tuyệt vời! Chúng ta tuyệt đối không hùa theo bình luận chê bai. Em hãy áp dụng quy tắc **T.H.I.N.K** và khéo léo từ chối bạn mình nhé."
                
                else:
                    reply = f"Thầy hiểu ý của em rồi. Với câu hỏi này, em hãy đọc kỹ lại tình huống '{selected_task.split(':')[1].strip()}' nhé. Mình sẽ cần vận dụng công cụ trên máy tính để giải bài toán thực tế. Cứ mạnh dạn đưa ra ý tưởng, thầy sẽ hướng dẫn em điều chỉnh!"
                    
                st.write(reply)
        
        st.session_state.messages.append({"role": "ai", "content": reply})
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phát triển bởi Thầy Trần Trung Hậu - Trường THCS Thuận Hưng, phường Thuận Hưng tháng 9/2025</p>", unsafe_allow_html=True)
