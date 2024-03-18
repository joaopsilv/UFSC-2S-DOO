from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia, habilidade, velocidade,
                                resistencia, tipo)
        self.__personagens.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def jogada(self, mesa: Mesa) -> Jogador:
        valor_carta_jogador1 = mesa.carta_jogador1.valor_total_carta()
        valor_carta_jogador2 = mesa.carta_jogador2.valor_total_carta()

        if valor_carta_jogador1 > valor_carta_jogador2:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            if not mesa.jogador2.mao:
                return mesa.jogador1
        elif valor_carta_jogador1 < valor_carta_jogador2:
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            if not mesa.jogador1.mao:
                return mesa.jogador2
        else:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return None
