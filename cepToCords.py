import requests
from geopy.geocoders import Nominatim

#funcao principal
def acharEndereco(cep):
    #trata o cep antes de inserir na url
    cep = tratarCep(cep)
    #inseri o cep na url de requisição da api viaCEP
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    #verifica se a requisição foi feita sem problemas
    if response.status_code == 200:
        data = response.json()

        #print das informações devolvidas na api
        if 'erro' not in data:
            print(f'CEP: {data["cep"]}')
            print(f'Logradouro: {data["logradouro"]}')
            print(f'Complemento: {data["complemento"]}')
            print(f'Bairro: {data["bairro"]}')
            print(f'Cidade: {data["localidade"]}')
            print(f'Estado: {data["uf"]}')
            cord = geoLocalizar(data)
            print(cord)
            return cord
        else:
            print('CEP não encontrado')
    else:
        print('Erro na requisição')



#função que recebe um endereço e devolve imprime latitude e longitude
def geoLocalizar(data):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(f"{data['logradouro']}, {data['bairro']}, {data['localidade']}")
    latitude = location.latitude
    longitude = location.longitude

    cords = {"latitude" : latitude,
             "longitude" : longitude}
    return cords


#funcao que trata a string do cep
def tratarCep(cep):
    cep = cep.replace("-", "")
    cep.strip()
    return cep



cep = '09811-323'
acharEndereco(cep)
