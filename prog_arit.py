"""
Programa: prog_arit
Descrição: Este programa calcula uma progressão aritmética à escolha do usuário
Autor: Filipe Eich
Data: 25/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

n=""
razao=""
nesimo=""
termo=""


#Entrada de dados

termo = float(input("\nOlá! Vamos calcular uma progressão aritmética? Comece digitando o primeiro termo da P.A.: "))

razao = float(input("\nAgora, diga a razão: "))


n = float(input("\nPor fim, defina o valor de n para calcularmos qual será o n-ésimo termo: "))




# Processamento de dados

nesimo=termo+((n-1)*razao)



#Saida de dados


print(f"\nAqui está o valor do n-ésimo termo: {nesimo}")






