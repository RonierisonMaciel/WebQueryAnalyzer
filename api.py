import streamlit as st
import requests
import json
from collections import Counter

# Função para buscar no Google
def buscar_no_google(query, api_key, cx):
    endpoint = "https://www.googleapis.com/customsearch/v1"
    parametros = {
        'q': query,
        'key': api_key,
        'cx': cx
    }

    resposta = requests.get(endpoint, params=parametros)

    if resposta.status_code == 200:
        resultados = json.loads(resposta.text)
        return resultados
    else:
        return None

# Função para inferir o país (usando a abordagem anterior)
def inferir_pais(domain):
    IPSTACK_API_KEY = 'f86f03244dc5897b873822ddc91f5f10'
    endpoint = f"http://api.ipstack.com/{domain}?access_key={IPSTACK_API_KEY}"
    resposta = requests.get(endpoint)
    
    if resposta.status_code == 200:
        data = resposta.json()
        return data.get('country_name', 'Desconhecido')
    else:
        return "Desconhecido"

# Configurações da API
API_KEY = 'AIzaSyDkh5qhexNaTKtFmccFgJUXQ4q164p-bjA'
CX = 'd2a5e6a13741541ca'

# Interface Streamlit
st.title("Análise de Startups")

# Entrada de texto para as consultas
queries_input = st.text_area("Digite os campos de busca (um por linha):")
queries = queries_input.split("\n")

# Botão para iniciar a busca
if st.button("Buscar"):
    paises = []
    resultados_totais = {
        'listings': 0,
        'results': [],
        'top_countries': {}
    }

    for query in queries:
        st.write(f"Buscando por: {query}...")
        resultados = buscar_no_google(query, API_KEY, CX)
        
        if resultados:
            for item in resultados.get('items', []):
                domain = item['displayLink']
                pais = inferir_pais(domain)
                paises.append(pais)
                resultados_totais['results'].append({
                    'title': item['title'],
                    'link': item['link'],
                    'snippet': item.get('snippet', ''),
                    'country': pais
                })
            resultados_totais['listings'] += len(resultados.get('items', []))
    
    # Mostrar os resultados
    st.subheader("Resultados")
    for result in resultados_totais['results']:
        st.write(f"**Título:** {result['title']}")
        st.write(f"**Link:** {result['link']}")
        st.write(f"**Snippet:** {result['snippet']}")
        st.write(f"**País:** {result['country']}")
        st.write("---")

    # Mostrar os países mais frequentes
    st.subheader("Top Países")
    contagem_paises = Counter(paises)
    for country, count in contagem_paises.most_common():
        st.write(f"{country}: {count}")
