import redis
r = redis.Redis(host = 'localhost',port=6379,db=0,decode_responses=True)

def getSet(chave):
    valor = r.get(chave)
    if valor:
        return "valor: "+valor
    else:
        valor = input("Insira um valor:\n")
        r.set(chave,valor)
        return "chave inserida com sucesso"

# print(getSet(input("Digite o nome de uma chave:\n")))

def manipulaLista(nomeLista):
    lista = r.lrange(nomeLista,0,-1)
    if lista:
        return lista
    else:
        qnt = int(input("Insira quantos valores irá inserir na lista:\n"))
        for i in range(0,int(qnt)):
            valor = input("Digite o valor:\n")
            r.rpush(nomeLista,valor)
        return "Valores inseridos com sucesso"

print(manipulaLista(input("Digite o nome de uma lista:\n")))