import random
import time
profissoes = ["Harry Potter e a pedra filosofal" , "Alice no país das maravilhas" , "Percy Jackson e o ladão de raios" , "Matrix"]
superheroes = ["Minecraft", "Free Fire", "Super Mario", "Roblox"]

print("Bem-vindo ao Charadas!")
w1 = input("Gostaria de ver os temas e as palavras que podem aparecer?")
if w1 == "Sim"  or w1 == "sim":
    print("Filmes: " , profissoes)        
    print("Jogos: " , superheroes)
time.sleep(3)
w2 = input("Caso queira adicionar algum item, diga o grupo que ele pertence. Caso não queria só diga ´não´ ")
if w2 == 'Filmes':
    n2 = input("Escreva o item:")
    profissoes.append(n2)
elif w2 == 'Jogos':
    n2 = input("Escreva o item:")
    superheroes.append(n2)

time.sleep(1)
w3 = input("Caso queira remover algum item, diga o grupo que ele pertence. Caso não queria só diga ´não´ ")
if w3 == 'Filmes':
    n3 = input("Escreva o item:")
    profissoes.remove(n3)
elif w3 == 'Jogos':
    n3 = input("Escreva o item:")
    superheroes.remove(n3)

time.sleep(2)

while True:
    w4 = input("Qual tema gostaria de jogar?")
    if w4 == "Filmes":
        print('O jogo irá começar!')
        print('Seu filme é...')
        time.sleep(2)
        
        # Criar uma lista randomizada
        prof = random.choice(profissoes)
        print(prof)
        print('Você tem 10 segundos para explicar o que você pegou a um amigo!')
        
       # Criar um timer
        for i in range(1, 11):
            print(i)
            time.sleep(1)
    
        print('O tempo acabou!')
        q1 = input('Você gostaria de continuar o jogo?')
        if q1 == 'Sim' or q1 == "sim":
            print('Ok, o jogo irá continuar.')
        else:
            break
            
    elif w4 == "Jogos":
        print('O jogo irá começar!')
        print('Seu jogo é...')
        time.sleep(2)
        
        # Criar uma lista randomizada
        heroi = random.choice(superheroes)
        print(heroi)
        print('Você tem 10 segundos para explicar o que você pegou a um amigo!')
        
       # Criar um timer
        for i in range(1, 11):
            print(i)
            time.sleep(1)
    
        print('O tempo acabou!')
        q1 = input('Você gostaria de continuar o jogo?')
        if q1 == 'Sim' or q1 == "sim":
            print('Ok, o jogo irá continuar.')
        else:
            break