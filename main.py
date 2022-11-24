from string import ascii_letters, digits, punctuation
from random import choice


def gerador_chave():
    caracteres = ascii_letters + digits + punctuation + 'çÇº°ª '
    key = []
    while len(key) < 100:
        caracter = choice(caracteres)
        if caracter not in key:
            key.append(caracter)
    return key


def encriptar(msg, chave, periodo):
    if len(chave) != 100 or periodo <2:
        return
    posicao_relativa_chave = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0],
                              [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1],
                              [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2],
                              [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3],
                              [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4],
                              [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5],
                              [6, 6], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                              [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7],
                              [8, 8], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8],
                              [9, 9]]

    linhas = []
    colunas = []
    for caracter in msg:
        for index, c in enumerate(chave):
            if caracter == c:
                linha, coluna = posicao_relativa_chave[index]
                linhas.append(linha)
                colunas.append(coluna)
                break

    agrupamento = []
    # agrupar linhas e colunas em periodos
    while linhas or colunas:
        if len(linhas) >= periodo:
            for c in range(periodo):
                agrupamento.append(linhas[0])
                linhas.pop(0)
        else:
            for c in range(int(len(linhas))):
                agrupamento.append(linhas[0])
                linhas.pop(0)
        if len(colunas) >= periodo:
            for c in range(periodo):
                agrupamento.append(colunas[0])
                colunas.pop(0)
        else:
            for c in range(int(len(colunas))):
                agrupamento.append(colunas[0])
                colunas.pop(0)

    index_nova_msg = []
    for c in range(int(len(agrupamento)/2)):
        grupo = [agrupamento[0], agrupamento[1]]
        index_nova_msg.append(grupo)
        agrupamento.pop(0)
        agrupamento.pop(0)

    msg_encriptada = ''
    for grupo in index_nova_msg:
        for index, c in enumerate(posicao_relativa_chave):
            if grupo == c:
                msg_encriptada += chave[index]
                break

    return msg_encriptada


def desencriptar(msg, chave, periodo):
    if len(chave) != 100 or periodo <2:
        return

    posicao_relativa_chave = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0],
                              [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1],
                              [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2],
                              [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3],
                              [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4],
                              [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5],
                              [6, 6], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
                              [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7],
                              [8, 8], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8],
                              [9, 9]]

    linhas = []
    colunas = []
    for caracter in msg:
        for index, c in enumerate(chave):
            if caracter == c:
                linha, coluna = posicao_relativa_chave[index]
                linhas.append(linha)
                colunas.append(coluna)
                break

    msg_desagrupada = []
    while linhas or colunas:
        if linhas:
            msg_desagrupada.append(linhas[0])
            linhas.pop(0)
        if colunas:
            msg_desagrupada.append(colunas[0])
            colunas.pop(0)
    while msg_desagrupada:
        if len(msg_desagrupada) >= periodo*2:
            for c in range(periodo):
                linhas.append(msg_desagrupada[0])
                msg_desagrupada.pop(0)
            for c in range(periodo):
                colunas.append(msg_desagrupada[0])
                msg_desagrupada.pop(0)
        else:
            for c in range(int(len(msg_desagrupada)/2)):
                linhas.append(msg_desagrupada[0])
                msg_desagrupada.pop(0)
            for c in range(int(len(msg_desagrupada))):
                colunas.append(msg_desagrupada[0])
                msg_desagrupada.pop(0)

    index_desencriptado = []
    while linhas or colunas:
        grupo = [linhas[0], colunas[0]]
        index_desencriptado.append(grupo)
        linhas.pop(0)
        colunas.pop(0)
        if not colunas or not linhas:
            break
    msg_desencriptada = ''
    for index in index_desencriptado:
        for i, c in enumerate(posicao_relativa_chave):
            if index == c:
                msg_desencriptada += str(chave[i])

    return msg_desencriptada
