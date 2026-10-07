"""Buổi 19: chatbot LLM chạy trên Amazon Bedrock, đối thủ của chatbot LSTM.

Cài thư viện:  pip install -r requirements.txt
Đặt key AWS:   export AWS_ACCESS_KEY_ID=...  và  export AWS_SECRET_ACCESS_KEY=...
Chạy:          python app.py   rồi mở http://127.0.0.1:7860
"""
import boto3
import gradio as gr

# ---------- 1. Cấu hình ----------
REGION = "ap-southeast-1"                # IAM policy chỉ cho phép region này
MODEL_ID = "apac.amazon.nova-lite-v1:0"  # model Amazon Nova Lite (rẻ, đủ dùng cho demo)

SYSTEM_PROMPT = """You are a supportive mental-health information assistant used in a machine-learning class demo.
- Answer general questions about mental health clearly and kindly, in 2-4 short sentences.
- Reply in the same language as the user (Vietnamese or English).
- You are not a doctor: do not diagnose or prescribe. Suggest talking to a professional when appropriate.
- If the user may be in danger or mentions self-harm, respond with empathy and urge them to contact local emergency services or a trusted person right away.
- For questions unrelated to mental health, say briefly and politely that you only cover mental-health topics."""

# ---------- 2. Kết nối tới Bedrock ----------
client = boto3.client("bedrock-runtime", region_name=REGION)


# ---------- 3. Hàm chat: Gradio gọi hàm này mỗi lần người dùng gửi tin ----------
def chat(message, history):
    if not message.strip():
        return "Bạn hãy nhập một câu hỏi."

    # LLM không tự nhớ gì: mỗi lần gọi phải gửi lại cả đoạn hội thoại.
    # Chỉ gửi 6 lượt hỏi-đáp gần nhất (12 tin) cho đỡ tốn token.
    messages = []
    for turn in history[-12:]:
        messages.append({"role": turn["role"], "content": [{"text": turn["content"]}]})
    messages.append({"role": "user", "content": [{"text": message[:500]}]})  # cắt câu hỏi tối đa 500 ký tự

    try:
        response = client.converse(
            modelId=MODEL_ID,
            system=[{"text": SYSTEM_PROMPT}],
            messages=messages,
            inferenceConfig={"maxTokens": 300, "temperature": 0.3},
        )
    except Exception as error:
        return f"Lỗi khi gọi Bedrock: {error}"

    return response["output"]["message"]["content"][0]["text"]


# ---------- 4. Giao diện web ----------
demo = gr.ChatInterface(
    chat,
    type="messages",
    title="Chatbot LLM · Amazon Bedrock",
    description="Buổi 19 · Đối thủ của chatbot LSTM. Bài tập kỹ thuật, không phải công cụ tư vấn.",
    examples=["What is mental health?", "wat causes mental problems", "Dạo này mình hay mất ngủ"],
)

if __name__ == "__main__":
    demo.launch()
