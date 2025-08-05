import streamlit as st
from openai import OpenAI

# Set up OpenAI client for Upstage Solar Pro2
client = OpenAI(
    api_key=st.secrets["up_rO5kNk8a7MIDb2bhDfLcs3br0ZRx7"],
    base_url="https://api.upstage.ai/v1"
)

st.set_page_config(page_title="학생 심리상담 챗봇", page_icon="🧑‍🎓")
st.title("🧑‍🎓 학생 심리상담 챗봇")
st.write("안녕하세요! 저는 학생들의 심리상담을 도와주는 챗봇입니다. 고민이나 궁금한 점을 자유롭게 입력해 주세요.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "당신은 학생들의 심리상담을 도와주는 친절한 상담사입니다. 학생의 고민을 경청하고, 공감하며, 따뜻하게 조언해 주세요."}
    ]

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

user_input = st.chat_input("고민이나 궁금한 점을 입력해 주세요.")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("assistant"):
        response = ""
        stream = client.chat.completions.create(
            model="solar-pro2",
            messages=st.session_state["messages"],
            stream=True,
        )
        message_placeholder = st.empty()
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
                message_placeholder.markdown(response + "▌")
        message_placeholder.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})
