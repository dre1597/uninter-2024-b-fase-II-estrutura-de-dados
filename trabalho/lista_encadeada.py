class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class FilaTriagem:
    def __init__(self):
        self.head = None
        self.numero_amarelo = 201
        self.numero_verde = 1

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
        if cor == 'A':
            nodo = Nodo(self.numero_amarelo, cor)
            self.numero_amarelo += 1
            self.inserirSemPrioridade(nodo)
        elif cor == 'V':
            nodo = Nodo(self.numero_verde, cor)
            self.numero_verde += 1
            self.inserirSemPrioridade(nodo)
        else:
            print("Cor inválida!")

    def imprimirListaEspera(self):
        atual = self.head
        if not atual:
            print("Nenhum paciente na fila.")
        else:
            while atual:
                print(f"Cartão {atual.cor} número {atual.numero}")
                atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            print(f"Chamando paciente com cartão {self.head.cor} número {self.head.numero}")
            self.head = self.head.proximo


def menu():
    fila = FilaTriagem()
    while True:
        print("\n1 – Adicionar paciente a fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            fila.inserir()
        elif opcao == '2':
            fila.imprimirListaEspera()
        elif opcao == '3':
            fila.atenderPaciente()
        elif opcao == '4':
            break
        else:
            print("Opção inválida!")


menu()
