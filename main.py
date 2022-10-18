#Gabriel Montagni Domingues Filho - 11800903
arquivo =open("aula.txt", 'r')

#variaveis declaradas
dados = []
lst = []
contador = 0

#for para pegar as linhas e colocar numa lista
for lines in arquivo:
    lst=lines.split()
    dados.append(lst)

#for para abrir cada palavra de cada linha e conferir se a palavra tem "" e depois conferir letra por letra para trocar , por ;
for roll in dados:
    i=0
    for words in roll:
        j=0
        if words[0] == '"':
            i+=1
            continue   
        for letters in words:                       #avalia cada letra da palavra para conferir se é ,
            if letters == ',':
                string = list(dados[contador][i])
                string[j] = ';'
                string = ''.join(string)
                dados[contador][i] = string         #faz a troca da palavra com , pela palavra com ;
            j+=1
        i+=1        
    contador +=1            

#abre um novo arquivo
arquivo = open("novo.txt","w")
i = 0
#salva cada linha dos dados no arquivo
for lines in dados:
    x = " ".join(dados[i])
    x = x + "\n"
    i += 1
    arquivo.write(x)


