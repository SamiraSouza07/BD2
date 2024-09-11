import redis
import time
r = redis.Redis(host="localhost",port=6379,db=0,decode_responses=True)
## Exercícios
## 1. Armazene uma string
# print("-"*20+"Exercício 1"+"-"*20)
# chave = input("Digite o nome da chave:\n")
# valor = input("Digite o valor da chave:\n")
# r.set(chave,valor)


# ## 2. Recupere o valor de uma chave
# print("-"*20+"Exercício 2"+"-"*20)
# print(r.get(chave))


# ## 3. Armazene e recupere uma lista
# print("-"*20+"Exercício 3"+"-"*20)
# def manipulaLista(nomeLista):
#     lista = r.lrange(nomeLista,0,-1)
#     if lista:
#         return lista
#     else:
#         qnt = int(input("Insira quantos valores irá inserir na lista:\n"))
#         for i in range(0,int(qnt)):
#             valor = input("Digite o valor:\n")
#             r.rpush(nomeLista,valor)
#         return "Valores inseridos com sucesso"

# print(manipulaLista(input("Digite o nome para uma lista:\n")))
# print(manipulaLista(input("Digite o nome da lista criada para recupera-la:\n")))


# ## 4. Adicione elementos em um conjunto
# print("-"*20+"Exercício 4"+"-"*20)
# nomeSet = input("Digite um nome para o conjunto:\n")
# qnt = int(input("Insira quantos valores irá inserir no conjunto:\n"))
# for i in range(0,int(qnt)):
#     valor = input("Digite o valor:\n")
#     r.sadd(nomeSet,valor)


# ## 5. Verifica se um elemento existe no conjunto
# print("-"*20+"Exercício 5"+"-"*20)
# elemento = input("Digite o nome do elemento que vc dejesa verificar se existe no sadd:\n")
# retorno = r.sismember(nomeSet,elemento)
# if retorno==1:
#     retorno="Existe"
# else:
#     retorno="Não existe"
# print(retorno)


# ## 6. Amarzena e recupera um dicionario
# print("-"*20+"Exercício 6"+"-"*20)
# nomeHash = input("Digite um nome para o dicionario:\n")
# qntCampos = int(input("Insira quantos campos vc inserir no dicionario:\n"))
# for i in range(0,int(qntCampos)):
#     chave = input("Digite o nome do campo:\n")
#     valor = input("Digite o valor deste campo:\n")
#     r.hset(nomeHash,chave,valor)
# print(r.hgetall(nomeHash))


# ## 7. Ultilize a expiração de chave
# print("-"*20+"Exercício 7"+"-"*20)
# chaveEx = r.setex("oiii",10,"expira em 10s")
# print(r.get('oiii'))
# time.sleep(11)
# print(r.get('oiii'))


# ## 8. Conte o números de elementos em um conjunto
# print("-"*20+"Exercício 8"+"-"*20)
# nomeSet = input("Digite o nome do conjunto:\n")
# print(r.scard(nomeSet))


# ## 9. Faça operações de incremento em uma chave numérica
# print("-"*20+"Exercício 9"+"-"*20)
# nomeChave = input("Digite um nome para a chave numérica:\n")
# valorChave = int(input("Digite seu valor:\n"))
# r.set(nomeChave,valorChave)
# r.incr(nomeChave)
# print("foi incrementado 1, novo valor: "+r.get(nomeChave))
# r.decr(nomeChave)
# r.decr(nomeChave)
# print("foi decrementado 2, novo valor: "+r.get(nomeChave))


# ## 10. Remove um elemento de um conjunto
# print("-"*20+"Exercício 10"+"-"*20)
# nomeSet = input("Digite o nome do conjunto:\n")
# print(r.smembers(nomeSet))
# remover = input("Digite o valor do elemento que vc dejesa deletar:\n")
# retorno =r.srem(nomeSet,remover)
# if retorno==1:
#     print("Excluido")
# else:
#     print("Não foi excluido")
# print(r.smembers(nomeSet))


## 11. Armazene e recupere uma lista de listas
print("-"*20+"Exercício 11"+"-"*20)
r.rpush("listaLista",*['[1,0]','[3,4]'])
print(r.lrange("listaLista",0,-1))


## 12. Armazene e recupere uma lista de elementos de tipos diferentes
print("-"*20+"Exercício 12"+"-"*20)
r.rpush("lista","Samira",17)
print(r.lrange("lista",0,-1))


## 13.  Realize uma transação com MULTI/EXEC
print("-"*20+"Exercício 13"+"-"*20)
with r.pipeline() as pipe:
    pipe.set("x","3")
    pipe.set("y","5")
    resp = pipe.execute()
    print("ex13",resp)


## 14. Defina e recupere um hash
print("-"*20+"Exercício 14"+"-"*20)
nomeHash = input("Digite um nome para o dicionario:\n")
qntCampos = int(input("Insira quantos campos vc inserir no dicionario:\n"))
for i in range(0,int(qntCampos)):
    chave = input("Digite o nome do campo:\n")
    valor = input("Digite o valor deste campo:\n")
    r.hset(nomeHash,chave,valor)
print(r.hgetall(nomeHash))


## 15. ultilize a operação de união de conjuntos
print("-"*20+"Exercício 15"+"-"*20)
r.sadd('conjunto1', 'a', 'b', 'c')
r.sadd('conjunto2', 'b', 'c', 'd')
r.sadd('conjunto3', 'c', 'd', 'e')

resultado = r.sunion('conjunto1', 'conjunto2', 'conjunto3')
print(list(resultado))


## 16. ultilize o comando sort em uma lista
print("-"*20+"Exercício 16"+"-"*20)
r.rpush('minha_lista', 5, 1, 3, 2, 4)
resultado = r.sort('minha_lista')
print(list(map(int, resultado)))


## 17. realize uma busca por padrão em chaves
print("-"*20+"Exercício 17"+"-"*20)
r.set('user:1000', 'Alice')
r.set('user:1001', 'Bob')
r.set('user:1002', 'Charlie')
r.set('admin:1003', 'Dave')

chaves = r.keys('user:*')
print("Chaves encontradas:", chaves)


## 18. Utilize a operação de interseccão de conjuntos
print("-"*20+"Exercício 18"+"-"*20)
r.sadd('set1', 'a', 'b', 'c')
r.sadd('set2', 'b', 'c', 'd')
r.sadd('set3', 'c', 'd', 'e')

result = r.sinter('set1', 'set2', 'set3')
result_list = list(result)
print("Interseção dos conjuntos:", result_list)


## 19. Armazene e recupere um valor de uma lista em uma posição específica
print("-"*20+"Exercício 19"+"-"*20)
lista_nome = 'listaaa'

r.rpush(lista_nome, 'valor1')
r.rpush(lista_nome, 'valor2')
r.rpush(lista_nome, 'valor3')

posicao = 1 
r.lset(lista_nome, posicao, 'novo_valor2') 
valor = r.lindex(lista_nome, posicao)

print(f"Valor na posição {posicao}")


## 20. Utilize a operação de diferença de conjuntos
print("-"*20+"Exercício 20"+"-"*20)
r.sadd('conjunto1', 'a', 'b', 'c', 'd')
r.sadd('conjunto2', 'c', 'd', 'e')
r.sadd('conjunto3', 'e', 'f')

resultado = r.sdiff('conjunto1', 'conjunto2', 'conjunto3')
resultado_lista = list(resultado)

print("Diferença dos conjuntos:", resultado_lista)