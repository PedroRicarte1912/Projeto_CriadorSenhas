import random
import string

print("Bem vindo ao criador de senhas!")
    # Definição variáveis
    senha_def = ""
    total = []
    numeros_senha = []
    letras_senha = []
    carcespecial_senha = []
    alfabeto = list(string.ascii_letters)
    caracteres_especiais = ["@", "#", "$", "*"]
    
    # Entrada valores e testes
    quantidade_numeros = input("Insira a quantidade de números que quer na sua senha: ")
    while not quantidade_numeros.isnumeric():
        quantidade_numeros = input("Insira a quantidade de números que quer na sua senha: ")
    quantidade_numeros = int(quantidade_numeros)
    
    print("=" * 20)
    quantidade_letras = input("Insira a quantidade de letras que quer na sua senha: ")
    while not quantidade_letras.isnumeric():
        quantidade_letras = input("Insira a quantidade de letras que quer na sua senha: ")
    quantidade_letras = int(quantidade_letras)
    
    print("=" * 20)
    quantidade_caracespecial = input("Insira a quantidade de caracteres especiais que quer na sua senha: ")
    while not quantidade_caracespecial.isnumeric():
        quantidade_caracespecial = input("Insira a quantidade de caracteres especiais que quer na sua senha: ")
    quantidade_caracespecial = int(quantidade_caracespecial)
    print("=" * 20)
    
    # Criação letras, números e caracteres e adição direta em 'total'
    for i in range(quantidade_numeros):
        numero = str(random.randint(0, 9))
        numeros_senha.append(numero)
        total.append(numero)
        
    for i in range(quantidade_letras):
        letra = random.choice(alfabeto)
        letras_senha.append(letra)
        total.append(letra)
        
    for i in range(quantidade_caracespecial):
        carac = random.choice(caracteres_especiais)
        carcespecial_senha.append(carac)
        total.append(carac)
        
    # Embaralha todos os elementos da lista total
    random.shuffle(total)
    
    # Transforma a lista embaralhada em uma string final
    senha_def = "".join(total)
    
    print(f"Sua senha gerada é: {senha_def}")