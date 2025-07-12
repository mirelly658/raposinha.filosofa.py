import random

class RaposinhaFilosofa:
    def __init__(self):
        self.frases = [
            "Se o código compila na primeira tentativa, desconfie: ou você é um gênio, ou o universo está te trollando.",
            "A vida é um algoritmo recursivo sem condição de parada. Cuidado com o stack overflow da existência!",
            "Debugar a própria mente é mais difícil que encontrar um bug em código legado de 20 anos.",
            "O paradoxo do nerd: quanto mais você sabe, mais percebe que o Dunning-Kruger está em *commit* na sua branch.",
            "Ser ou não ser? Eis a questão. Mas, em binário, é só 1 ou 0. Simplifique, humano!",
            "A entropia do universo é apenas o backlog de um sprint cósmico mal planejado.",
            "Se Descartes dissesse 'Penso, logo existo' hoje, o servidor da consciência já teria caído por DDoS.",
            "A matrix não é um filme, é o deploy da realidade em um cluster mal configurado.",
            "O sentido da vida é 42? Só se você acredita que o compilador da existência usa base decimal.",
            "Nietzsche disse que Deus está morto, mas ele só esqueceu de atualizar o driver da divindade."
        ]

    def falar(self):
        return random.choice(self.frases)

def main():
    raposinha = RaposinhaFilosofa()
    print("🦊 Raposinha Filósofa está pronta! Pressione Enter para uma frase ou 'sair' para encerrar.")
    
    while True:
        user_input = input()
        if user_input.lower() == 'sair':
            print("🦊 Raposinha Filósofa se despede: 'Que seus bugs sejam fáceis de rastrear!'")
            break
        print("🦊 Raposinha Filósofa diz:")
        print(raposinha.falar())
        print("\nPressione Enter para outra frase ou digite 'sair' para encerrar.")

if __name__ == "__main__":
    main()