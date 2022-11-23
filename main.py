from string import ascii_letters, digits, punctuation
from random import choice


def gerador_chave():
    caracteres = ascii_letters + digits + punctuation + 'çÇ§°ª '
    key = []
    while len(key) < 100:
        caracter = choice(caracteres)
        if caracter not in key:
            key.append(caracter)
    return key


def encriptar(msg, chave, periodo):
    if periodo <=1:
        return
    index_chave = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 1],
                   [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3],
                   [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
                   [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7],
                   [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
                   [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1],
                   [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3],
                   [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5],
                   [9, 6], [9, 7], [9, 8], [9, 9]]

    # Identificando posição dos caracteres da mensagem dentro da chave.
    index_msg = []
    for caracter in msg:
        for index, c in enumerate(chave):
            if caracter == c:
                index_msg.append(index_chave[index])

    # Separando linhas das colunas de cada caracter
    linhas = []
    colunas = []
    for index in index_msg:
        linha, coluna = index
        linhas.append(linha)
        colunas.append(coluna)

    # embarralhando os numeros
    new_ordem = []
    while linhas or colunas:
        for c in range(periodo):
            if linhas:
                new_ordem.append(linhas[0])
                linhas.pop(0)
            else:
                break

        for c in range(periodo):
            if colunas:
                new_ordem.append(colunas[0])
                colunas.pop(0)
            else:
                break

    # arupando em 2 em 2
    new_agrupamento = []
    controle_rep = int((len(new_ordem) / 2))

    for c in range(controle_rep):
        grupo = [new_ordem[0], new_ordem[1]]
        new_agrupamento.append(grupo)
        new_ordem.pop(0)
        new_ordem.pop(0)

    # escrevendo nova mensagem
    new_msg = ''
    for grupo in new_agrupamento:
        for index, c in enumerate(index_chave):
            if c == grupo:
                new_msg += str(chave[index])
                break
    return new_msg


def desencriptar(msg, chave, periodo):
    if periodo <= 1:
        return
    index_chave = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 1],
                   [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3],
                   [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
                   [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7],
                   [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
                   [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1],
                   [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3],
                   [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5],
                   [9, 6], [9, 7], [9, 8], [9, 9]]

    # Identificando posição dos caracteres da mensagem dentro da chave.
    index_msg = []
    for caracter in msg:
        for index, c in enumerate(chave):
            if caracter == c:
                index_msg.append(index_chave[index])
    msg_desagrupada = []
    for grupo in index_msg:
        v1, v2 = grupo
        msg_desagrupada.append(v1)
        msg_desagrupada.append(v2)

    linhas = []
    colunas = []
    controle = 0
    new_periodo = False
    while msg_desagrupada:
        controle += 1
        if len(msg_desagrupada) >= periodo:
            if controle <= periodo:
                linhas.append(msg_desagrupada[0])
            if controle > periodo:
                colunas.append(msg_desagrupada[0])
        else:
            if not new_periodo:
                controle = 1
                periodo = (len(msg_desagrupada) / 2)
                print(periodo)
                new_periodo = True

            if controle <= periodo:
                linhas.append(msg_desagrupada[0])
            if controle > periodo:
                colunas.append(msg_desagrupada[0])

        if controle == (periodo*2):
            controle = 0
        msg_desagrupada.pop(0)
    print(len(linhas))
    print(len(colunas))

    # separando grupos
    index_msg_descript = []
    while linhas or colunas:
        index = [linhas[0], colunas[0]]
        index_msg_descript.append(index)
        linhas.pop(0)
        colunas.pop(0)

    # gerando mensagem descriptada
    msg_descriptada = ''
    for grupo in index_msg_descript:
        for index, c in enumerate(index_chave):
            if grupo == c:
                msg_descriptada += str(chave[index])
                break
    print(msg_descriptada)


if __name__ == "__main__":
    chave = ['b', ':', 'e', 'm', 'D', 'u', '0', ']', 'd', '5', '|', '(', 'G', '^', 'i', 'J', 'ª', 'c', '"', '@', 'C',
             'F', '2', '§', '4', 'p', '=', '_', 'A', "'", 'V', '`', 'z', 'f', 'S', 'h', 'Z', '°', 'Q', 'B', 'X', 'N',
             '\\', '&', ')', '!', 'y', 'k', '$', '[', 'l', '-', '7', '+', ' ', '9', '*', ',', 'n', '/', 'P', '}', 'K',
             '<', 'v', 'o', 'R', 'E', 'O', 'j', 't', 'U', 'g', '#', 'Ç', 'T', '?', '6', 'M', 'ç', 'a', 'I', '{', '1',
             '%', ';', 'H', '>', '8', 'r', 'Y', 'L', '~', 'w', '.', 'x', 'W', '3', 'q', 's']

    msg = 'defenda a parede leste do castelo'
    periodo = 5
    msg_encript = encriptar(msg, chave, periodo)
    desencriptar(msg_encript, chave, periodo)


