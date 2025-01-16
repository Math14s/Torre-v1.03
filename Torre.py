import time
import random
import os
import threading

class JogoIncremental:
    def __init__(self):
        self.vida = 500
        self.forca = 100
        self.agilidade = 25
        self.ouro = 10
        self.pontos_disponiveis = 10
        self.arma_equipada = None
        self.bota_equipada = None
        self.colete_equipado = None
        self.maior_andar = 0
        self.vitorias = 0
        self.derrotas = 0
        self.recordes_ouro = 0
        self.andar_atual = 1  # Andar atual, diferente do maior_andar

    def limpar_tela(self):
        os.system('clear')  # Limpa a tela no Termux

    def inventario(self):
        self.limpar_tela()
        print("==== INVENTARIO ====")
        if self.arma_equipada:
            print(f"Arma: {self.arma_equipada[0]} (multiplicador {self.arma_equipada[1]}x)")
        if self.bota_equipada:
            print(f"Bota: {self.bota_equipada[0]} (multiplicador {self.bota_equipada[1]}x)")
        if self.colete_equipado:
            print(f"Colete: {self.colete_equipado[0]} (multiplicador {self.colete_equipado[1]}x)")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")
        if escolha == "4":
            return

    def distribuir_status(self):
        self.limpar_tela()
        print(f"==== DISTRIBUIR ====")
        print(f"PONTOS DISPONIVEIS: {self.pontos_disponiveis}")
        print("1. Vida")
        print("2. Força")
        print("3. Agilidade")
        print("4. Voltar")
        
        escolha = input("Escolha um status para colocar pontos: ")
        if escolha == "4":
            return
        
        pontos = int(input("Quantos pontos? "))
        if pontos > self.pontos_disponiveis:
            print("Você não tem pontos suficientes!")
            return
        
        if escolha == "1":
            self.vida += pontos
        elif escolha == "2":
            self.forca += pontos
        elif escolha == "3":
            self.agilidade += pontos
        
        self.pontos_disponiveis -= pontos
        print(f"Status atualizado! Vida: {self.vida}, Força: {self.forca}, Agilidade: {self.agilidade}")
        time.sleep(1)

    def loja(self):
        while True:
            self.limpar_tela()
            print("==== LOJA ====")
            print("Escolha uma categoria:")
            print("1. Armas")
            print("2. Botas")
            print("3. Coletes")
            print("4. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.loja_armas()
            elif opcao == "2":
                self.loja_botas()
            elif opcao == "3":
                self.loja_coletes()
            elif opcao == "4":
                return
            else:
                print("Opção inválida!")
                time.sleep(1)

    def mostrar_recordes(self):
        self.limpar_tela()
        print("==== SEUS RECORDES ====")
        print(f"Maior Andar Alcançado: {self.maior_andar}")
        print(f"Vitórias: {self.vitorias}")
        print(f"Derrotas: {self.derrotas}")
        input("Pressione Enter para voltar ao menu.")

    def loja_armas(self):
        self.limpar_tela()
        print("==== LOJA DE ARMAS ====")
        print("1. 10 Ouro - Espada de madeira (1.5x força)")
        print("2. 50 Ouro - Espada de pedra (3x força)")
        print("3. 200 Ouro - Espada de ferro (5x força)")
        print("4. 500 Ouro - Sabre Comum (10x força)")
        print("5. 800 Ouro - Sabre de Aço (20x força)")
        print("6. 1200 Ouro - Sabre de Luz (50x força)")
        print("7. 2000 Ouro - Excalibur (100x força)")
        print("8. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "8":
            return

        if escolha == "1" and self.ouro >= 10:
            self.ouro -= 10
            self.arma_equipada = ("Espada de madeira", 1.5)
        elif escolha == "2" and self.ouro >= 50:
            self.ouro -= 50
            self.arma_equipada = ("Espada de pedra", 3)
        elif escolha == "3" and self.ouro >= 200:
            self.ouro -= 200
            self.arma_equipada = ("Espada de ferro", 5)
        elif escolha =="22042008" and self.ouro>= 0:
            self.arma_equipada = ("Dragon Slayer", 200)
        elif escolha == "4" and self.ouro >= 500:
            self.ouro -= 500
            self.arma_equipada = ("Sabre Comum", 10)
        elif escolha == "5" and self.ouro >= 500:
            self.ouro -= 500
            self.arma_equipada = ("Sabre De Aço", 20)
        elif escolha == "6" and self.ouro >= 800:
            self.ouro -= 800
            self.arma_equipada = ("Sabre de Luz", 50)
        elif escolha == "7" and self.ouro >= 2000:
            self.ouro -= 2000
            self.arma_equipada = ("Excalibur", 100)
        else:
            print("Ouro insuficiente ou opção inválida.")
            return

        print(f"Arma equipada: {self.arma_equipada[0]} com multiplicador {self.arma_equipada[1]}x de força.")
        time.sleep(1)

    def loja_botas(self):
        self.limpar_tela()
        print("==== LOJA DE BOTAS ====")
        print("1. 70 Ouro - Bota Ágil (2x Agi)")
        print("2. 150 Ouro - Bota Booster (4x Agi)")
        print("3. 300 Ouro - Bota Sonica (10x Agi)")
        print("4. 500 Ouro - Bota de aquiles (25x Agi)")
        print("5. 777 Ouro - Bota Speed Light (60x Agi)")
        print("6. 1000 Ouro - Bota Teleport (100x Agi)")
        print("7. 4500 Ouro - Tênis da Nike (300x Agi)")
        print("8. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "8":
            return

        if escolha == "1" and self.ouro >= 70:
            self.ouro -= 70
            self.bota_equipada = ("Bota Ágil", 2)
        elif escolha == "2" and self.ouro >= 150:
            self.ouro -= 150
            self.bota_equipada = ("Bota Booster", 4)
        elif escolha == "3" and self.ouro >= 300:
            self.ouro -= 300
            self.bota_equipada = ("Bota Sonica", 10)
        elif escolha == "4" and self.ouro >= 500:
            self.ouro -= 500
            self.bota_equipada = ("Bota de Aquiles", 25)
        elif escolha == "5" and self.ouro >= 777:
            self.ouro -= 777
            self.bota_equipada = ("Bota Light Speed", 60)
        elif escolha == "6" and self.ouro >= 1000:
            self.ouro -= 1000
            self.bota_equipada = ("Bota teleport", 100)
        elif escolha == "7" and self.ouro >= 4500:
            self.ouro -= 4500
            self.bota_equipada = ("Tênis da Nike", 300)
        elif escolha == "22042008" and self.ouro >= 0:
             self.bota_equipada = ("Salto Alto Rosa", 777)
        else:
            print("Ouro insuficiente ou opção inválida.")
            return

        print(f"Bota equipada: {self.bota_equipada[0]} com multiplicador {self.bota_equipada[1]}x de agilidade.")
        time.sleep(1)

    def loja_coletes(self):
        self.limpar_tela()
        print("==== LOJA DE COLETES ====")
        print("1. 100 Ouro - Colete Kevlar (3x Vida)")
        print("2. 300 Ouro - Colete Anti tanque (6x Vida)")
        print("3. 800 Ouro - Colete de Vibranium (20x Vida)")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "4":
            return

        if escolha == "1" and self.ouro >= 100:
            self.ouro -= 100
            self.colete_equipado = ("Colete Kevlar", 3)
        elif escolha == "2" and self.ouro >= 300:
            self.ouro -= 300
            self.colete_equipado = ("Colete Anti tanque", 6)
        elif escolha == "3" and self.ouro >= 800:
            self.ouro -= 800
            self.colete_equipado = ("Colete de Vibranium", 20)
        else:
            print("Ouro insuficiente ou opção inválida.")
            return

        print(f"Colete equipado: {self.colete_equipado[0]} com multiplicador {self.colete_equipado[1]}x de vida.")
        time.sleep(1)

    def mostrar_sequencia(self, sequencia):
        # Exibe a sequência por 3 segundos
        for letra in sequencia:
            print(letra, end=' ', flush=True)
            time.sleep(0.5)
        time.sleep(2)
        self.limpar_tela()  # Limpa a tela

    def minigame_memoria(self):
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def temporizador(resposta_event):
            time.sleep(5)  # 5 segundos para responder
            if not resposta_event.is_set():  # Verifica se a resposta foi dada
                print("\nTempo esgotado! Você perdeu!")
                resposta_event.set()  # Marca como respondido para finalizar
                return False

        for fase in range(1, 4):  # Três fases
            # Gerar uma sequência diferente para cada fase
            tamanho_sequencia = 5 + fase  # Aumenta o tamanho a cada fase
            sequencia = random.choices(letras, k=tamanho_sequencia)

            print(f"\nFase {fase}: Memorize a sequência!")
            self.mostrar_sequencia(sequencia)

            # Preparar o temporizador e capturar a resposta
            resposta_event = threading.Event()
            thread_tempo = threading.Thread(target=temporizador, args=(resposta_event,))
            thread_tempo.start()

            tentativa = input("Digite a sequência que você viu: ").upper()
            resposta_event.set()  # Indica que o jogador respondeu a tempo

            thread_tempo.join()  # Aguarda o fim do temporizador

            if tentativa != ''.join(sequencia):
                print("Você errou a sequência! O jogo terminou!")
                time.sleep(3)
                return False

            print(f"Fase {fase} completa! Prepare-se para a próxima fase." if fase < 3 else "Você venceu o boss!")
            time.sleep(2)

        return True  # Venceu todas as fases

    def torre(self):
        while True:
            self.limpar_tela()
            print(f"==== ANDAR {self.andar_atual} ====")
            print("Lutando...")
            time.sleep(1)

            if self.arma_equipada:
                dano = self.forca * self.arma_equipada[1]
            else:
                dano = self.forca
            if self.bota_equipada:
                agilidade = self.agilidade * self.bota_equipada[1]
            else:
                agilidade = self.agilidade

            if self.colete_equipado:
                vida = self.vida * self.colete_equipado[1]
            else:
                vida = self.vida

            chance_vitoria = random.random()
            dificuldade = 0.1 * self.andar_atual * 2
            chance_de_vencer = (vida / 200) + (agilidade / 100) + (dano / 100) - dificuldade

            if chance_vitoria < chance_de_vencer:
                print("VITÓRIA! SUBINDO UM ANDAR")
                self.ouro += self.andar_atual
                self.pontos_disponiveis += 3
                self.vitorias += 1
                self.maior_andar = max(self.maior_andar, self.andar_atual)
                self.andar_atual += 1

                if self.andar_atual % 10 == 0:
                    print("BOSS ENCONTRADO!")
                    if not self.minigame_memoria():  # Se o minigame for perdido
                        print("Você perdeu o desafio e será derrotado!")
                        self.derrotas += 1
                        self.andar_atual = 1  # Reseta para o andar 1 após derrota no boss
                        break
                    time.sleep(2)
            else:
                print("DERROTA! Você perdeu e voltará para o primeiro andar.")
                self.derrotas += 1
                self.andar_atual = 1  # Resetando para o andar 1 após derrota
                time.sleep(3)
                break

            print(f"RECOMPENSAS: {self.ouro} OURO e 3 PONTOS")
            time.sleep(3)

    def menu(self):
        while True:
            self.limpar_tela()
            print(f"==== INICIO ====")
            # Exibe a vida com o multiplicador do colete equipado, se houver
            if self.colete_equipado:
                vida_com_buff = self.vida * self.colete_equipado[1]
                print(f"Vida: {vida_com_buff} (buff do colete: {self.colete_equipado[1]}x)")
            else:
                print(f"Vida: {self.vida}")
            
            # Exibe a força com o multiplicador da arma equipada, se houver
            if self.arma_equipada:
                forca_com_buff = self.forca * self.arma_equipada[1]
                print(f"Força: {forca_com_buff} (buff da arma: {self.arma_equipada[1]}x)")
            else:
                print(f"Força: {self.forca}")
            
            # Exibe a agilidade com o multiplicador da bota equipada, se houver
            if self.bota_equipada:
                agilidade_com_buff = self.agilidade * self.bota_equipada[1]
                print(f"Agilidade: {agilidade_com_buff} (buff da bota: {self.bota_equipada[1]}x)")
            else:
                print(f"Agilidade: {self.agilidade}")

            print(f"Ouro: {self.ouro}")
            print(f"Pontos Disponíveis: {self.pontos_disponiveis}")
            print("-----Menu-----")
            print("1. Loja")
            print("2. Inventário")
            print("3. Distribuir status")
            print("4. Torre")
            print("5. Seus Recordes")
            print("6. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.loja()
            elif opcao == "2":
                self.inventario()
            elif opcao == "3":
                self.distribuir_status()
            elif opcao == "4":
                self.torre()
            elif opcao == "5":
                self.mostrar_recordes()
            elif opcao == "6":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida.")
                time.sleep(1)


if __name__ == "__main__":
    jogo = JogoIncremental()
    jogo.menu()
