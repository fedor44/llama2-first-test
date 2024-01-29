import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q4_K_S.bin",
    model_type="llama"
)

st.title('인공지능 시인')
st.title('_시의_ is :blue[주제는?] :sunglasses:')
content = st.text_input('시의 주제를 제시해라')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 요청 중~~'):
        result = llm.predict("write a poem about " + content)
        st.write(result)
