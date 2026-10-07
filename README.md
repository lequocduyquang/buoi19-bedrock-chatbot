# Chatbot LLM trên Amazon Bedrock (Buổi 19)

Chatbot hỏi đáp về sức khoẻ tinh thần, dùng để so sánh với chatbot LSTM mà học viên tự train trong Buổi 19. App gọi mô hình ngôn ngữ Amazon Nova Lite thông qua Amazon Bedrock (dịch vụ AWS cho phép gọi LLM qua API), dùng hàm Converse API.

| File | Dùng để |
|---|---|
| `app_todo.py` | Bài hands-on: học viên điền 6 TODO |
| `app.py` | Đáp án hoàn chỉnh |
| `lstm/Chatbot_using_LSTM_pytorch_hands_on.ipynb` | Bài hands-on chatbot LSTM: học viên điền các TODO (chạy trên Colab) |
| `lstm/Chatbot_using_LSTM_pytorch.ipynb` | Đáp án notebook chatbot LSTM |
| `lstm/Chatbot_LSTM_giai_thich.html` | Giải thích từng bước notebook LSTM, mở bằng trình duyệt |

## Chạy

```bash
pip install -r requirements.txt
export AWS_ACCESS_KEY_ID=...        # key lớp do giảng viên phát
export AWS_SECRET_ACCESS_KEY=...
python app_todo.py                  # hoặc python app.py
```

Trên Windows (PowerShell), đặt key bằng:

```powershell
$env:AWS_ACCESS_KEY_ID="..."
$env:AWS_SECRET_ACCESS_KEY="..."
```

Mở http://127.0.0.1:7860 để chat.

Không viết key vào code, không commit key, không chụp màn hình có key. Key lớp chỉ có quyền gọi Nova Lite và chỉ dùng được trong thời hạn giảng viên đặt.

Đây là bài tập kỹ thuật, không phải công cụ tư vấn sức khoẻ tinh thần.
