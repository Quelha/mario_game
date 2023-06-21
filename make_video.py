import re

def separar_frases(texto):
    padrao = r"[A-Z][^.!?]*[.!?]"
    frases = re.findall(padrao, texto)
    return frases

def contar_caracteres(texto):
    return len(texto)

# Exemplo de uso
texto = """Em 1982, Chicago se tornou o palco de uma tragédia que abalou a cidade. Sete vidas foram ceifadas pelo veneno mortal contido em pílulas aparentemente inofensivas. Entre as vítimas, três pertenciam à mesma família, um fato ainda mais devastador. A investigação revelou um padrão alarmante: todas as embalagens dos medicamentos fatais eram provenientes do mesmo lote e exalavam um odor de amêndoas, sinalizando a presença de cianeto.

A notícia se espalhou como um incêndio, provocando uma onda de pânico que varreu os Estados Unidos. Hospitais foram invadidos por pessoas tomadas pelo medo e pela preocupação. Infelizmente, alguns criminosos aproveitaram a situação para imitar o envenenamento original, recorrendo a veneno de rato e até ácido clorídrico, aterrorizando ainda mais a população.

Apesar de uma intensa investigação, a polícia enfrentou inúmeras dificuldades para identificar o verdadeiro responsável pelos crimes. Ao longo do processo, três suspeitos surgiram, mas nenhum deles pôde ser conclusivamente ligado às mortes chocantes. A busca pela justiça foi frustrante, e a sombra do assassino permaneceu oculta, deixando a cidade em busca de respostas que pareciam inalcançáveis.

No entanto, mesmo diante do horror, um legado importante emergiu dessa tragédia. Como uma resposta direta aos eventos trágicos de Chicago, um sistema de segurança adicional foi implementado nas embalagens de medicamentos vendidos atualmente. O lacre de alumínio, hoje uma medida comum, foi desenvolvido como uma salvaguarda para proteger as pessoas de produtos adulterados e garantir sua segurança.

Embora o enigma dos envenenamentos de 1982 permaneça sem solução, o impacto dessas mortes trágicas levou a mudanças significativas na indústria farmacêutica. Um lembrete sombrio, mas importante, de como a busca pela justiça pode inspirar ações que visam proteger e preservar a vida. Que as vítimas descansem em paz, e que a memória de sua tragédia nos lembre constantemente da necessidade de vigilância e precaução."""
quantidade_caracteres = contar_caracteres(texto)
print("Quantidade de caracteres:", quantidade_caracteres)
frases_separadas = separar_frases(texto)
for frase in frases_separadas:
    print(frase.strip())  # strip() remove espaços em branco extras

