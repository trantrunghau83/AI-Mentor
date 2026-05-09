import streamlit as st
import pandas as pd
import datetime
import time
import os

# --- CẤU HÌNH GIAO DIỆN & STYLE ---
st.set_page_config(page_title="Hệ thống AI Mentor - THCS Thuận Hưng", layout="wide", page_icon="🤖")

st.markdown("""
    <style>
    .stButton>button { background-color: #1e40af !important; color: white !important; border-radius: 8px; }
    .challenge-box { background-color: #f0fdf4; padding: 15px; border-left: 5px solid #16a34a; border-radius: 8px; margin-bottom: 20px;}
    .stats-card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; text-align: center;}
    </style>
""", unsafe_allow_html=True)

# --- HỆ THỐNG LƯU TRỮ THỐNG KÊ (PERSISTENT STORAGE) ---
LOG_FILE = "app_usage_log.csv"

def save_log(student_name, lesson, question):
    """Lưu lịch sử tương tác của học sinh để làm minh chứng"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[now, student_name, lesson, question]], 
                            columns=['Thời gian', 'Học sinh', 'Bài học', 'Câu hỏi'])
    if not os.path.isfile(LOG_FILE):
        new_data.to_csv(LOG_FILE, index=False)
    else:
        new_data.to_csv(LOG_FILE, mode='a', header=False, index=False)

# --- KHO DỮ LIỆU BÀI HỌC (LỚP 7 - 9) ---
lessons = {
    "Bài 7 (Lớp 7): Tính toán tự động": {
        "mã": "5.2.TC1a",
        "tình_huống": "Mẹ em bán trái cây, cần tính tổng tiền cho khách hàng nhanh chóng.",
        "keywords": {
            "hàm": "Để tính tổng, em cần dùng hàm SUM. Cú pháp là `=SUM(vùng_chứa_giá_tiền)`. Em đã quét đúng vùng dữ liệu chưa?",
            "công thức": "Mọi công thức trong Excel đều phải bắt đầu bằng dấu bằng (=). Em đã gõ dấu bằng trước khi nhập tên hàm chưa?",
            "sai": "Nếu kết quả ra chữ #VALUE!, có thể ô dữ liệu của em đang chứa chữ thay vì số. Em kiểm tra lại nhé!"
        }
    },
    "Bài (Lớp 9): Quản lý tài chính gia đình": {
        "mã": "5.3.TC1b",
        "tình_huống": "Thiết kế bảng chi tiêu gia đình tháng 5 và tìm khoản chi tốn kém nhất.",
        "keywords": {
            "chi tiêu": "Em hãy tạo các cột: Ngày, Nội dung, Số tiền, Ghi chú. Việc này giúp gia đình kiểm soát dòng tiền tốt hơn.",
            "cao nhất": "Có 2 cách: 1. Dùng lệnh Sort (Sắp xếp) giảm dần. 2. Dùng hàm MAX để máy tự tìm con số lớn nhất cho em.",
            "biểu đồ": "Để thuyết phục ba mẹ tiết kiệm, em nên vẽ biểu đồ tròn (Pie Chart). Nó sẽ cho thấy khoản nào chiếm 'miếng bánh' to nhất.",
            "tiết kiệm": "Em thử tính tổng thu nhập trừ đi tổng chi tiêu xem còn dư bao nhiêu? Đó chính là số tiền tiết kiệm đấy!"
        }
    }
}

# --- GIAO DIỆN CHÍNH ---
tabs = st.tabs(["👦 Khu vực Học sinh", "📊 Bảng thống kê (Dành cho Giáo viên)"])

# --- TAB 1: KHÔNG GIAN HỌC TẬP ---
with tabs[0]:
    st.title("🤖 AI Mentor: Trợ lý học tập thông minh")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 1. Thông tin học sinh")
        student_name = st.text_input("Nhập tên của em:", placeholder="VD: Trần Văn An")
        selected_lesson = st.selectbox("2. Chọn bài học:", list(lessons.keys()))
        
        st.info(f"**Yêu cầu cần đạt:** {lessons[selected_lesson]['mã']}")
        st.success(f"**Nhiệm vụ:** {lessons[selected_lesson]['tình_huống']}")
        
    with col2:
        st.markdown("### 3. Thảo luận cùng AI Mentor")
        
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "ai", "content": "Chào em! Thầy Hậu đã huấn luyện cho mình AI để giúp em chinh phục bài học này. Em đang gặp khó khăn ở bước nào?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        user_input = st.chat_input("Nhập câu hỏi của em...")
        
        if user_input:
            if not student_name:
                st.warning("Em vui lòng nhập tên trước khi đặt câu hỏi nhé!")
            else:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.chat_message("user").write(user_input)
                
                # Lưu log vào file CSV làm minh chứng
                save_log(student_name, selected_lesson, user_input)
                
                # Logic AI tự động hóa (Socratic Logic)
                with st.spinner("AI Mentor đang suy nghĩ..."):
                    time.sleep(1)
                    reply = ""
                    lower_input = user_input.lower()
                    
                    # Tìm câu trả lời phù hợp dựa trên bài học và từ khóa
                    context_keys = lessons[selected_lesson]["keywords"]
                    found = False
                    for key, val in context_keys.items():
                        if key in lower_input:
                            reply = val
                            found = True
                            break
                    
                    if not found:
                        reply = f"Câu hỏi '{user_input}' của em rất thú vị! Để giải quyết vấn đề này, thầy gợi ý em nên xem lại phần thực hành trang... của sách giáo khoa hoặc thử dùng công cụ tìm kiếm trong Excel nhé. Em có muốn thầy gợi ý cụ thể hơn không?"
                    
                    st.session_state.messages.append({"role": "ai", "content": reply})
                    st.chat_message("ai").write(reply)

# --- TAB 2: THỐNG KÊ DÀNH CHO GIÁO VIÊN ---
with tabs[1]:
    st.title("📊 Hệ thống quản lý & Thống kê")
    
    if os.path.isfile(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        
        # Dashboard nhanh
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="stats-card"><h3>Tổng lượt hỏi</h3><h2>{}</h2></div>'.format(len(df)), unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="stats-card"><h3>Số học sinh tham gia</h3><h2>{}</h2></div>'.format(df['Học sinh'].nunique()), unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="stats-card"><h3>Bài học "Hot" nhất</h3><p>{}</p></div>'.format(df['Bài học'].mode()[0]), unsafe_allow_html=True)
            
        st.markdown("### 📈 Biểu đồ tần suất truy cập")
        df['Thời gian'] = pd.to_datetime(df['Thời gian'])
        daily_counts = df.resample('D', on='Thời gian').count()['Câu hỏi']
        st.line_chart(daily_counts)
        
        st.markdown("### 📋 Nhật ký tương tác chi tiết")
        st.dataframe(df, use_container_width=True)
        
        # Nút tải file minh chứng
        st.download_button(
            label="📥 Tải file CSV minh chứng",
            data=df.to_csv(index=False).encode('utf-8-sig'),
            file_name=f"Minh_chung_AI_Mentor_{datetime.date.today()}.csv",
            mime='text/csv',
        )
    else:
        st.info("Chưa có dữ liệu tương tác. Hãy bắt đầu cho học sinh sử dụng App nhé!")
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phát triển bởi Thầy Trần Trung Hậu - Trường THCS Thuận Hưng, phường Thuận Hưng tháng 9/2025</p>", unsafe_allow_html=True)
