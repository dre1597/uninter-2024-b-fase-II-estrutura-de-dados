class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None


def funcao_hash(sigla):
    if sigla == 'DF':
        return 7
    else:
        a, b = pegar_valor_na_tabela_asc(sigla[0]), pegar_valor_na_tabela_asc(sigla[1])
        return (a * b) % 10


def pegar_valor_na_tabela_asc(valor):
    return ord(valor)


class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def inserir(self, sigla, nome_estado):
        indice = funcao_hash(sigla)
        nodo = Nodo(sigla, nome_estado)
        nodo.proximo = self.tabela[indice]
        self.tabela[indice] = nodo

    def imprimir(self):
        for i in range(10):
            print(f'Posição {i}: ', end='')
            atual = self.tabela[i]
            if atual is None:
                print('None')
            else:
                while atual:
                    print(f'{atual.sigla} ({atual.nomeEstado}) -> ', end='')
                    atual = atual.proximo
                print('None')


tabela = TabelaHash()

estados = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
    ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
    ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
    ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

print('Impressão inicial da tabela Hash:')
tabela.imprimir()

for sigla, nome in estados:
    tabela.inserir(sigla, nome)

print('\nImpressão da Tabela Hash após inserir os 26 estados e o DF:')
tabela.imprimir()

estado_ficticio_sigla = 'DP'
estado_ficticio_nome = 'Dré Pereira'

tabela.inserir(estado_ficticio_sigla, estado_ficticio_nome)

print('\nImpressão da Tabela Hash após inserir os estados, DF e estado fictício:')
tabela.imprimir()
