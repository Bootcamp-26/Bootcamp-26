import json
import os

STORAGE_FILE = "chat_storage.json"

def load_user_chats(username: str) -> dict:
    """
    Load chat sessions for a given username from persistent storage.
    """
    if not os.path.exists(STORAGE_FILE):
        return {}
    
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get(username, {}).get("chat_sessions", {})
    except Exception:
        return {}

def save_user_chats(username: str, chat_sessions: dict) -> None:
    """
    Save chat sessions for a given username to persistent storage.
    """
    data = {}
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
            
    if username not in data:
        data[username] = {}

    # 1 veya daha az mesaja sahip boş sohbet oturumlarını kaydetmeyelim
    filtered_sessions = {}
    for sid, sdata in chat_sessions.items():
        if len(sdata.get("messages", [])) > 1:
            filtered_sessions[sid] = sdata

    data[username]["chat_sessions"] = filtered_sessions
    
    try:
        with open(STORAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving chat storage: {e}")
