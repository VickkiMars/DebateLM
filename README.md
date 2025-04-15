# DebateLM
An attempt to make LLM's go at each other....forever...or until they run out of context length.

This project explores multiple iterations of a chat interface with the aim to achieve a `standard` ui for the debateLM idea.

## 📂 File Overview

### 🧪 `test_chat_area.py`
- **Purpose:** A test runner script to validate the chat area logic.
- **Usage:** Good for quick verification of layout or LLM integration.
- **Run with:**  
  ```bash
  python test_chat_area.py
  ```
### 🖥️ `app_main.py`
- **Purpose:** Main PyQt application that integrates UI and LLM logic.
- **Features:** Full working demo of the debate/chat interface.
- **Run with:**  
```bash
python app_main.py
```

### 🧱   chat_area_base.py  
- **Purpose**: The original core implementation of the chat area.
- **Notes**: Can be used as a base class or reference point for newer versions.
- **Run with:**  
```bash
python chat_area_base.py
```

### 📜 chat_area_scroll.py
- **Purpose**: Enhanced chat area with scrollable message area.
- **Improvements**: Fixes layout overflow, improves usability for long chats.
```bash
python chat_area_scroll.py
```

### 🧠 llm_response.py
- **Purpose**: A minimal LLM logic unit for generating responses in a debate-style interaction.
- **Usage**: Build on implementation logic in other files like app_main.py.
```bash
python llm_response.py
```

### ⚠️ chat_area_faulty.py
- **Purpose**: A broken version of the chat area.
- **Use for**: Debugging or comparing with working versions.
```bash
python chat_area_faulty.py
```

## ✅ Requirements

- Python 3.8+
- PyQt5 or PyQt6
- `transformers`
- `qasync`
- 'hugging face api_key'
---

## ▶️ Running the App
Install dependencies:

```bash
pip install pyqt5 transformers qasync
```

Then run the main application:

```bash
python app_main.py
```

---

## 💡 Contribution

Feel free to experiment by swapping in different LLM response logic or UI layouts. Each file is modular to help with quick prototyping.

---

## 📃 License

MIT License

