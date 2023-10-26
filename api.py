import streamlit as st
import requests
import json
from collections import Counter
import configparser
import logging

# Configuração
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['API']['GoogleAPIKey']
CX = config['API']['CX']
IPSTACK_API_KEY = config['API']['IPStackAPIKey']

# Configuração de Log
logging.basicConfig(filename='app.log', level=logging.INFO)

# Função para buscar no Google
def buscar_no_google(query, api_key, cx):
    endpoint = "https://www.googleapis.com/customsearch/v1"
    parametros = {
        'q': query,
        'key': api_key,
        'cx': cx
    }

    try:
        resposta = requests.get(endpoint, params=parametros)
        resposta.raise_for_status()
        resultados = json.loads(resposta.text)
        return resultados
    except requests.RequestException as e:
        logging.error(f"Erro ao buscar no Google: {e}")
        st.error("Erro ao buscar no Google. Por favor, tente novamente.")
        return None

# Função para inferir o país
def inferir_pais(domain):
    endpoint = f"http://api.ipstack.com/{domain}?access_key={IPSTACK_API_KEY}"
    
    try:
        resposta = requests.get(endpoint)
        resposta.raise_for_status()
        data = resposta.json()
        return data.get('country_name', 'Desconhecido')
    except requests.RequestException as e:
        logging.error(f"Erro ao inferir país: {e}")
        return "Desconhecido"

# Interface Streamlit
def main():
    st.title("Análise de Consultas Web")

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
            if query:  # verifica se a consulta não está vazia
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

if __name__ == "__main__":
    main()
