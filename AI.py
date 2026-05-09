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

# --- KHO DỮ LIỆU 5 BÀI HỌC (TỪ LỚP 7 ĐẾN LỚP 9) ---
lessons = {
    "Bài 5 (Lớp 7): Ứng xử trên mạng": {
        "mã": "4.3.TC1b",
        "tình_huống": "Một người bạn rủ em tham gia bình luận chê bai một bạn khác trên mạng xã hội. Em sẽ xử lý thế nào?",
        "keywords": {
            "từ chối": "Tuyệt vời! Em đã biết cách bảo vệ bản thân và bạn bè. Em có thể áp dụng quy tắc T.H.I.N.K (Sự thật, Hữu ích, Tử tế) để khuyên người bạn kia dừng hành động đó lại nhé.",
            "không tham gia": "Quyết định rất chính xác! Không tham gia bắt nạt trên mạng (Cyberbullying) là hành động của một công dân số có đạo đức.",
            "báo cáo": "Cách xử lý rất trưởng thành! Em có thể dùng tính năng Report (Báo cáo vi phạm) của mạng xã hội hoặc nhờ giáo viên, phụ huynh can thiệp kịp thời.",
            "chê bai": "Khoan đã em ơi! Việc bình luận chê bai người khác trên mạng có thể gây tổn thương tâm lý rất lớn cho họ. Em hãy thử đặt mình vào vị trí của bạn bị chê bai xem sao nhé?"
        }
    },
    "Bài 6 (Lớp 7): Làm quen với phần mềm bảng tính": {
        "mã": "3.1.TC1a",
        "tình_huống": "Thầy giáo yêu cầu em nhập danh sách lớp, nhưng tên các bạn bị che khuất một phần do cột quá hẹp. Làm sao để cột tên rộng ra?",
        "keywords": {
            "rộng": "Em hãy di chuyển chuột lên ranh giới giữa 2 chữ cái tên cột (VD: cột A và B). Khi trỏ chuột thành mũi tên 2 chiều, em nhấp đúp (double-click) chuột trái để máy tự căn chỉnh nhé!",
            "kéo": "Đúng rồi! Em có thể nhấn giữ chuột trái tại vạch ngăn cách giữa tên 2 cột trên cùng và kéo sang phải để mở rộng cột theo ý muốn.",
            "không biết": "Em hãy nhìn lên thanh chứa các chữ cái A, B, C... ở trên cùng. Em thử đưa con trỏ chuột vào đường kẻ giữa cột chứa tên và cột bên cạnh xem con trỏ có đổi hình dạng không?"
        }
    },
    "Bài 7 (Lớp 7): Tính toán tự động trên bảng tính": {
        "mã": "5.2.TC1a",
        "tình_huống": "Mẹ em bán trái cây, cần tính tổng tiền cho khách hàng nhanh chóng và chính xác.",
        "keywords": {
            "hàm": "Để tính tổng, em cần dùng hàm SUM. Cú pháp là `=SUM(vùng_chứa_giá_tiền)`. Em đã quét đúng vùng dữ liệu chưa?",
            "công thức": "Mọi công thức trong Excel đều phải bắt đầu bằng dấu bằng (=). Em đã gõ dấu bằng trước khi nhập tên hàm chưa?",
            "sai": "Nếu kết quả ra chữ #VALUE!, có thể ô dữ liệu của em đang chứa chữ thay vì số. Em kiểm tra lại nhé!"
        }
    },
    "Bài 14 (Lớp 7): Thuật toán tìm kiếm": {
        "mã": "3.4.TC1a",
        "tình_huống": "Em có một xấp bài kiểm tra đã sắp xếp theo thứ tự A, B, C... Làm sao tìm ra bài của bạn 'Trần Trung Hậu' nhanh nhất?",
        "keywords": {
            "chia đôi": "Chính xác! Vì danh sách đã SẮP XẾP, em rút ngay bài ở giữa. Nếu vần H nằm trước, em bỏ luôn nửa xấp bài phía sau. Em nhớ thuật toán này gọi là gì không?",
            "giữa": "Tư duy rất tuyệt! Kiểm tra phần tử ở giữa là bước đầu tiên của Thuật toán Tìm kiếm nhị phân. Nó giúp em thu hẹp phạm vi tìm kiếm đi một nửa sau mỗi lần đoán.",
            "từng tờ": "Nếu tìm từng tờ từ trên xuống (Tìm kiếm tuần tự) sẽ rất lâu nếu xấp bài có 100 tờ. Vì bài đã được SẮP XẾP A-C, em thử nghĩ xem có cách nào nhảy thẳng vào giữa xấp bài không?"
        }
    },
    "Bài (Lớp 9): Quản lý tài chính gia đình": {
        "mã": "5.3.TC1b",
        "tình_huống": "Thiết kế bảng chi tiêu gia đình tháng 5 và tìm khoản chi tốn kém nhất để có kế hoạch tiết kiệm.",
        "keywords": {
            "chi tiêu": "Em hãy tạo các cột: Ngày, Nội dung, Số tiền, Ghi chú. Việc này giúp gia đình kiểm soát dòng tiền tốt hơn.",
            "cao nhất": "Có 2 cách: 1. Dùng lệnh Sort (Sắp xếp) giảm dần. 2. Dùng hàm MAX để máy tự tìm con số lớn nhất cho em.",
            "biểu đồ": "Để thuyết phục ba mẹ, em nên vẽ biểu đồ tròn (Pie Chart). Nó sẽ cho thấy khoản nào chiếm 'miếng bánh' to nhất.",
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
        
        # Đặt lại hội thoại khi đổi bài
        if "current_lesson" not in st.session_state or st.session_state.current_lesson != selected_lesson:
            st.session_state.current_lesson = selected_lesson
            st.session_state.messages = [{"role": "ai", "content": "Chào em! Thầy Hậu đã huấn luyện thầy để giúp em chinh phục bài học này. Em đã đọc kỹ tình huống chưa, em định sẽ làm bước nào trước?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        user_input = st.chat_input("Nhập câu trả lời hoặc thắc mắc của em...")
        
        if user_input:
            if not student_name:
                st.warning("Em vui lòng nhập tên trước khi trò chuyện nhé!")
            else:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.chat_message("user").write(user_input)
                
                # Lưu log vào CSV
                save_log(student_name, selected_lesson, user_input)
                
                # Socratic AI Logic
                with st.spinner("AI Mentor đang phân tích..."):
                    time.sleep(1)
                    reply = ""
                    lower_input = user_input.lower()
                    
                    context_keys = lessons[selected_lesson]["keywords"]
                    found = False
                    for key, val in context_keys.items():
                        if key in lower_input:
                            reply = val
                            found = True
                            break
                    
                    if not found:
                        reply = f"Câu nói '{user_input}' của em rất thú vị! Hãy bám sát vào tình huống thực tế của bài học này nhé. Em có thể nhắc lại cho thầy biết, mục tiêu cuối cùng của chúng ta ở nhiệm vụ này là gì không?"
                    
                    st.session_state.messages.append({"role": "ai", "content": reply})
                    st.chat_message("ai").write(reply)

# --- TAB 2: THỐNG KÊ DÀNH CHO GIÁO VIÊN ---
with tabs[1]:
    st.title("📊 Bảng Quản trị & Thống kê Tương tác")
    
    if os.path.isfile(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="stats-card"><h3>Tổng lượt tương tác</h3><h2>{}</h2></div>'.format(len(df)), unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="stats-card"><h3>Số học sinh sử dụng</h3><h2>{}</h2></div>'.format(df['Học sinh'].nunique()), unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="stats-card"><h3>Bài học quan tâm nhất</h3><p>{}</p></div>'.format(df['Bài học'].mode()[0]), unsafe_allow_html=True)
            
        st.markdown("### 📋 Nhật ký truy cập chi tiết")
        st.dataframe(df, use_container_width=True)
        
        st.download_button(
            label="📥 Tải file CSV minh chứng ",
            data=df.to_csv(index=False).encode('utf-8-sig'),
            file_name=f"Minh_Chung_AI_Mentor_{datetime.date.today()}.csv",
            mime='text/csv',
        )
    else:
        st.info("Chưa có dữ liệu. Hãy tạo tương tác bằng cách đóng vai học sinh ở Tab bên cạnh nhé!")
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phát triển bởi Thầy Trần Trung Hậu - Trường THCS Thuận Hưng, phường Thuận Hưng tháng 9/2025</p>", unsafe_allow_html=True)
