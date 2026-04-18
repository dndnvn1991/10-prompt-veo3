import streamlit as st
from google import genai

# Cấu hình giao diện trang web
st.set_page_config(page_title="Veo 3 Prompt Generator", page_icon="🎥")
st.title("🚀 Veo 3 Prompt Generator")

# Nhập API Key (Có thể dùng st.secrets để bảo mật hơn)
api_key = st.text_input("Nhập Gemini API Key:", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    topic = st.text_input("Chủ đề video của bạn:", "Thành phố tương lai dưới mưa")
    num_prompts = st.slider("Số lượng prompt:", 1, 10, 10)

    if st.button("Tạo Prompts"):
        with st.spinner("Đang tạo..."):
            system_instruction = "Bạn là chuyên gia viết prompt cho Google Veo 3. Tạo prompt chi tiết (50-100 từ) bằng tiếng Anh."
            user_prompt = f"Tạo {num_prompts} prompts video về: {topic}"
            
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    config={'system_instruction': system_instruction},
                    contents=user_prompt
                )
                st.success("Đã tạo xong!")
                st.text_area("Kết quả:", value=response.text, height=400)
            except Exception as e:
                st.error(f"Lỗi: {e}")
