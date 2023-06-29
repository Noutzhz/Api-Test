import requests

print ('''
 _____       _       _____            _   
|  _  | ___ |_| ___ |_   _| ___  ___ | |_ 
|     || . || ||___|  | |  | -_||_ -||  _|
|__|__||  _||_|       |_|  |___||___||_|  
       |_|                                
                Make a By: Noutz                

[火] https://github.com/Noutzhz

''')

def teste_api():
    url = input("Digite a URL da API: ")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Gera uma exceção se a resposta indicar um erro (status code >= 400)

        # Se a resposta estiver em formato JSON, você pode acessar os dados assim:
        # data = response.json()
        # Faça algo com os dados...

        print('Resposta da API:')
        print(response.text)  # Imprime o conteúdo da resposta
    except requests.exceptions.RequestException as e:
        print('Ocorreu um erro durante a solicitação:', e)

teste_api()
