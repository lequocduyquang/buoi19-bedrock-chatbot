"""Buổi 19 · Hands-on: tự viết chatbot LLM chạy trên Amazon Bedrock.

Làm lần lượt TODO 1 → TODO 6. Mỗi TODO chỉ cần 1–3 dòng code.
Cài thư viện:  pip install -r requirements.txt
Đặt key AWS:   export AWS_ACCESS_KEY_ID=...  và  export AWS_SECRET_ACCESS_KEY=...
Chạy thử:      python app_todo.py   rồi mở http://127.0.0.1:7860
Bí quá thì hỏi giảng viên hoặc print() từng biến ra để xem.
"""
import boto3
import gradio as gr

# ---------- 1. Cấu hình (đã có sẵn) ----------
REGION = "ap-southeast-1"                # IAM policy chỉ cho phép region này
MODEL_ID = "apac.amazon.nova-lite-v1:0"  # model Amazon Nova Lite (rẻ, đủ dùng cho demo)

SYSTEM_PROMPT = """You are a supportive mental-health information assistant used in a machine-learning class demo.
- Answer general questions about mental health clearly and kindly, in 2-4 short sentences.
- Reply in the same language as the user (Vietnamese or English).
- You are not a doctor: do not diagnose or prescribe. Suggest talking to a professional when appropriate.
- If the user may be in danger or mentions self-harm, respond with empathy and urge them to contact local emergency services or a trusted person right away.
- For questions unrelated to mental health, say briefly and politely that you only cover mental-health topics."""

# ---------- 2. Kết nối tới Bedrock ----------
# TODO 1: Tạo client để gọi Bedrock.
#   Gợi ý: boto3.client(<tên service>, region_name=<region>)
#   - Tên service để GỌI model là "bedrock-runtime" (còn "bedrock" là service quản lý, không dùng ở đây).
#   - Region lấy từ biến REGION ở trên.
client = None


# ---------- 3. Hàm chat: Gradio gọi hàm này mỗi lần người dùng gửi tin ----------
def chat(message, history):
    """message: câu người dùng vừa gõ (str).
    history: các tin nhắn trước đó, dạng list các dict, ví dụ:
        [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello!"}]
    Hàm trả về: câu trả lời của bot (str).
    """
    # TODO 2: Nếu người dùng gửi chuỗi rỗng (hoặc toàn dấu cách) thì trả về
    #   "Bạn hãy nhập một câu hỏi." và dừng luôn, không gọi Bedrock.
    #   Gợi ý: message.strip() bỏ khoảng trắng hai đầu; chuỗi rỗng "" được coi là False.

    # LLM không tự nhớ gì: mỗi lần gọi phải gửi lại cả đoạn hội thoại.
    # Bedrock muốn mỗi tin nhắn có dạng:
    #     {"role": "user", "content": [{"text": "câu hỏi"}]}
    # tức là "content" là một LIST chứa dict {"text": ...}, không phải str như của Gradio.
    messages = []

    # TODO 3: Duyệt 12 tin nhắn gần nhất trong history (history[-12:]),
    #   đổi từng tin sang dạng của Bedrock rồi append vào messages.
    #   Gợi ý: turn["role"] và turn["content"].

    # TODO 4: Thêm câu hỏi mới của người dùng vào cuối messages (role là "user").
    #   Cắt câu hỏi tối đa 500 ký tự cho đỡ tốn tiền: message[:500]

    try:
        # TODO 5: Gọi Bedrock bằng client.converse(...) với 4 tham số:
        #   modelId=MODEL_ID
        #   system=[{"text": SYSTEM_PROMPT}]
        #   messages=messages
        #   inferenceConfig={"maxTokens": 300, "temperature": 0.3}
        #   Gán kết quả vào biến response.
        response = None
    except Exception as error:
        return f"Lỗi khi gọi Bedrock: {error}"

    # TODO 6: Lấy câu trả lời (str) từ response rồi return.
    #   response là một dict lồng nhau, câu trả lời nằm ở:
    #       response["output"]["message"]["content"][0]["text"]
    #   Mẹo: print(response) để tự nhìn cấu trúc trước khi viết.
    return "TODO 6: chưa lấy câu trả lời từ response"


# ---------- 4. Giao diện web (đã có sẵn) ----------
demo = gr.ChatInterface(
    chat,
    type="messages",
    title="Chatbot LLM · Amazon Bedrock",
    description="Buổi 19 · Hands-on. Bài tập kỹ thuật, không phải công cụ tư vấn.",
    examples=["What is mental health?", "wat causes mental problems", "Dạo này mình hay mất ngủ"],
)

if __name__ == "__main__":
    demo.launch()

# ---------- Bonus (làm xong 6 TODO rồi hãy thử) ----------
# B1. Đổi temperature thành 0 rồi 1.0, hỏi cùng một câu vài lần. Câu trả lời thay đổi thế nào?
# B2. Sửa SYSTEM_PROMPT để bot chỉ trả lời bằng tiếng Việt, hoặc trả lời như một nhà thơ.
# B3. Hỏi lại đúng các câu đã thử với chatbot LSTM trong notebook. So sánh: bot nào hiểu câu
#     gõ sai chính tả ("wat causes...")? Bot nào nhớ được câu hỏi trước đó?
