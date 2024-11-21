import streamlit as st 
from openai import OpenAI

openai_api_key = st.secrets['OPENAI-APIKEY']
client = OpenAI(api_key=openai_api_key)

st.set_page_config(
    page_title="Pessoa Especial",
    page_icon= '💖',
    layout="centered")


st.markdown("""
# Olá! 

Se você está aqui, é porque você é uma ✨**pessoa especial**✨ para mim!

Então, eu tenho uma mensagem para você!
Quando estiver preparado(a), clique no botão abaixo!

"""
)



instrucoes = """
Você é um assistente encarregado de gerar uma mensagem motivadora.
Siga as seguintes instruções:
- Faça uma mensagem com 20 a 30 palavras
- Seja sempre positivo e inspirador 
- Use formatação (negrito, italicos, emojis)
- Use um tom alegre. Transmita felicidade em sua mensagem. 
- Mencione que a mensagem é para uma 'pessoa especial'.
- Use frases que enalteçam a pessoa. 
- Se der, seja engraçado também!
"""

def gerar_mensagem(prompt):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": instrucoes},
                  {"role": "user", "content": prompt}],
    )
    return resposta.choices[0].message.content

if st.button('Quero uma mensagem!', icon = '🙋',
    type="primary", use_container_width = True):
    msg = gerar_mensagem('Gere uma nova mensagem especial')
    st.info(msg)
    st.balloons()