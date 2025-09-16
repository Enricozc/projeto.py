import streamlit as st
import requests
import pandas as pd

st.markdown("""
    <style>
        /* Cor de fundo da página */
    body {
        background-color: #F0F8FF; /* Azul clarinho */
    }
            /* Cor e estilo do título principal */
    h1 {
        color: #2E86C1;  /* Azul mais forte */
        text-align: center;
    }
            /* Subtítulos */
    h2, h3 {
        color: #117864;  /* Verde escuro */
    }
    /* Texto da tabela */
    .stDataFrame {
        background-color: #ffffff;
        color: #1C2833;
    }
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="Loja de Produtos", page_icon="🛒", layout="wide")

st.title("🛒 Loja de Produtos - API Fake Store")
st.markdown("""
Esta aplicação consome a **[Fake Store API](https://fakestoreapi.com/)** para listar produtos de e-commerce.
Você pode escolher a categoria de produtos e ver informações como preço, título, descrição e imagem.
""")


categorias = ["electronics", "jewelery", "men's clothing", "women's clothing"]

categoria_selecionada = st.selectbox("Escolha uma categoria:", categorias)

if st.button("Buscar Produtos"):
    url = f"https://fakestoreapi.com/products/category/{categoria_selecionada}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        produtos = resposta.json()
        
        df = pd.DataFrame(produtos)[["title", "price", "description"]]
        df.rename(columns={
            "title": "Título",
            "price": "Preço",
            "description": "Descrição"
        }, inplace=True)
        st.subheader("Produtos encontrados:")
        st.dataframe(df)

        st.subheader("Imagens dos produtos:")
        for produto in produtos:
            st.write(f"**{produto['title']}** - R$ {produto['price']}")
            st.image(produto["image"], width=200)
    else:
        st.error("Erro ao acessar a API. Tente novamente.")
