'''
Try-except é uma exceção, algo inesperado no código ou apenas algo que não foi tratado diretamente no programa
Excessões são parte da biblioteca-padrão Python, mas podemos também criar nossas próprias exceções.

o Try permite delimitar o código que pode gerar uma exceção. Ele é completado pela declaração except. Se nenhum erro ocorrer,
o código dentro de except nem será executado. Dependendo do tipo da exceção, uma mensagem de erro diferente será exibida.

No exemplo o FOR não é interrompido, como aconteceria caso não tivéssemos tratado a exceção.

O bloco Try pode ter uma declaração finally

O finally executa o bloco, mesmo que aconteça uma exceção, com ou sem tratamento
'''

nomes = ["Ana", "Carlos", "Maria"]  #lista simples

# Tentativas para exibir um nome da lista

# exemplo 1
for tentativa in range(3):  
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])    
    except ValueError: # Erro no tipo do input
        print("Digite um número!")
    except IndexError: # Erro no indice da lista
        print("Valor inválido, digite entre -3 e 2")
'''
# exemplo 2            testes = (1, abc, 100 )

# Quando digitado o 1, não há exceção e o finally executa normalmente
# Ao digitar abc, geramos uma exceção ValueError que é tratada pelo bloco, imprimindo uma mensagem e executando o finally
# No ultimo teste, ao digitar 100 gera uma exceção do tipo IndexError, o finally é executado e só depois imprime o traceback
 
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])  
    except ValueError as e:
        print("Digite um número!")
    finally:
        print(f"Tentativa {tentativa + 1}")
'''   

# Boas práticas

# Ao usarmos exceções, evitamos retornar e verificar códigos de erro a cada chamada de função, 
# centralizando o tratamento de erros do bloco em um só lugar e faclitando o tratamento de error


    
