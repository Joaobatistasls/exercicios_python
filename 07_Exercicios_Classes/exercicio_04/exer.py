# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque.

# Criando a Classe Pessoa
class Conta:
    
    # Criando o contrutor 
    def _init_(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        
    # Criando o método para alterar nome
    def set_alterar_nome(self, nome):
        self.nome = nome
        print(f"O nome do Conrrentista foi alterado para {self.nome}")
        
    # Criando o método para extrair o extrato
    def get_extrato(self):
        self.saldo
        print(f"O saldo da conta do titular {self.nome} é de {self.saldo}")
        
    # Criando o método para depositar
    def set_depositar(self, valor):
        self.saldo += valor
        print(f"O valor depositado foi de: {self.saldo}")
        
    # Criando o método para sacar
    def set_sacar(self, valor):
        self.saldo -= valor
        print(f"O valor sacado foi de: {self.saldo}")
        
# Criando a referência
conta = Conta("João", 77, 100.0)

# Imprimindo os métodos
print(conta.set_depositar(20.0))