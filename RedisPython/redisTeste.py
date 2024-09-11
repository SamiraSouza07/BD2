import redis

#Conectar ao servidor redis
r = redis.Redis(host = 'localhost',port=6379,db=0,decode_responses=True)

r.set('name','Alice')

name = r.get('name')
print(name)

# LPUSH: Adicionar elementos à lista
r.lpush('fruta', 'maçã', 'fruta', 'banana')
 
# LLEN: Contar elementos da lista
print(r.llen('fruta'))
 
# LRANGE: Recuperar todos os elementos da lista
print(r.lrange('fruta', 0, -1))
 
# LPOP: Remover elemento do começo da lista
print(r.lpop('fruta'))
