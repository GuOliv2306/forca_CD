import forca_gpt
import jogo
print("Bem vindo ao jogo da forca!!!!")
print('==================================================')
print("realize suas escolhas: ")
dificuldade= input("Escolha a dificuldade: ")
lingua= input("Escolha agora o idioma: ")
tamanho= input("Quantas palavras você deseja?: ")
genero= input ("Escolha o gênero de sua preferência: ")

palavra_escolhida= forca_gpt.palavra_gpt(dificuldade,lingua,tamanho,genero)
jogo.game(palavra_escolhida)