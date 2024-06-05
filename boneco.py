"""personagem enforcado"""

stages = [
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """
]


# Função para mostrar o estágio atual do jogo
def enforcado(tries):
    print(stages[tries])
