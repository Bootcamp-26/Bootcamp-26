import streamlit as st
import sys
import os

# Sistemin modülleri bulması için root dizinini ekliyoruz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from components.chat.chat_ui import chat_ui

st.set_page_config(page_title="IdeApp - Fikir Havuzu", layout="wide")

def main():
    # Chat arayüzünü çağırıyoruz
    chat_ui()

if __name__ == "__main__":
    main()