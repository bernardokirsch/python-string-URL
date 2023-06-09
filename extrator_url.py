import re
import requests

request = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
request_dict = request.json()

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            url = url.replace(' ', '')
            url = url.strip()
            return url
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        index_interrogacao = self.url.find('?')
        url_base = self.url[0:index_interrogacao]
        return url_base

    def get_url_parametros(self):
        index_interrogacao = self.url.find('?')
        url_parametros = self.url[index_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        index_parametro = self.get_url_parametros().find(parametro_busca)
        index_valor = index_parametro + len(parametro_busca) + 1
        index_e_comercial = self.get_url_parametros().find('&', index_valor)
        if index_e_comercial == -1:
            valor = (self.get_url_parametros()[index_valor:])
        else:
            valor = (self.get_url_parametros()[index_valor:index_e_comercial])
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "" + self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base() # colocar qualquer coisa para impressão ao printar o objeto

    def __eq__(self, other):
        return self.url == other.url

quantidade = 100
origem = 'dolar'
destino = 'real'

url = f'bytebank.com/cambio?quantidade={quantidade}&moedaOrigem={origem}&moedaDestino={destino}'
extrator_url = ExtratorURL(url)

# print('O tamanho da URL é: ', len(extrator_url))
# print(extrator_url)

# extrator_url_2 = ExtratorURL(url)
# print(extrator_url == extrator_url_2)

# print(id(extrator_url))
# print(id(extrator_url_2))

valor_dolar = float(request_dict['USDBRL']['bid'])
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
moeda_quantidade = int(extrator_url.get_valor_parametro('quantidade'))

if moeda_origem == 'dolar':
    conversao = valor_dolar * moeda_quantidade
elif moeda_origem == 'real':
    conversao = moeda_quantidade / valor_dolar

print(f'A conversão de {moeda_quantidade}, de {moeda_origem} para {moeda_destino}, é de {round(conversao, 2)}')


