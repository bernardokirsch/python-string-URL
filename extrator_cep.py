import re # Regular Expression - RegEx

endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

cep_padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = cep_padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)