from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

def get_llm_response(input_message: str, selected_expert: str) -> str:
    """
    LLMから回答を取得する関数
    
    Args:
        input_message (str): ユーザーからの質問内容
        selected_expert (str): 選択された専門家
    
    Returns:
        str: LLMからの回答
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    
    messages = [
        SystemMessage(content=f"あなたは{selected_expert}です。質問に答えてください。"),
        HumanMessage(content=input_message),
    ]
    
    result = llm(messages)
    return result.content

import streamlit as st

st.title("LLM機能を搭載したWebアプリ")

# アプリの概要と操作方法を説明
st.markdown("""
## アプリについて
このWebアプリは、AI（LLM）を活用した専門家相談システムです。
栄養や運動に関する質問に、それぞれの専門家の立場からAIが回答します。

## 使い方
1. **質問を入力**: 下のテキストボックスに相談したい内容を入力してください
2. **専門家を選択**: 回答してもらいたい専門家をラジオボタンで選択してください
3. **送信ボタンをクリック**: 「送信」ボタンを押すとAIが回答を生成します

---
""")

input_message = st.text_input(label="質問したい内容を入力してください。")

selected_item = st.radio(
    "質問をする専門家を選択してください。",
    ["栄養の専門家", "運動の専門家"]
)

# 送信ボタンを配置
submit_button = st.button("送信")

# ボタンがクリックされ、かつ入力がある場合のみLLMを呼び出す
if submit_button and input_message:
    response = get_llm_response(input_message, selected_item)
    st.write("回答:", response)
elif submit_button and not input_message:
    st.warning("質問内容を入力してください.")