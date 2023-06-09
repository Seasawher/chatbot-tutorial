import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

"""
# Hello World!
"""

with st.sidebar:
    st.title('🤗💬 HugChat')
    st.markdown('''
    ## About
    このアプリは LLM と会話できるチャットボットです．
    下記を使用しています:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM モデル

    💡: API キーは必要ありません！
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Data Professor](<https://youtube.com/dataprofessor>)')