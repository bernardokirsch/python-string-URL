# URL
url = 'bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar'

# Sanitização da URL
url = url.replace(' ', '')
url = url.strip()

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia')

# Separa a base e os parâmetros
index_interrogacao = url.find('?')
url_base = url[0:index_interrogacao]
url_parametros = url[index_interrogacao+1:]

# Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
index_parametro = url_parametros.find(parametro_busca)
index_valor = index_parametro + len(parametro_busca) + 1
index_e_comercial = url_parametros.find('&', index_valor)
if index_e_comercial == -1:
    valor = (url_parametros[index_valor:])
else:
    valor = (url_parametros[index_valor:index_e_comercial])
print(valor)







