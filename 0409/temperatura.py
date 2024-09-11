import redis
import random

r = redis.Redis(host="localhost",port=6379,db=0,decode_responses=True)

for i in range(0,8):
    r.rpush("lista_temp",round(random.uniform(0,40),2))

print(r.lrange("lista_temp",0,-1))

soma= 0
for i in range(0,8):
    soma = soma + float(r.lindex("lista_temp",i))
    
media = soma/8
print("A média de temperatura de hoje é de: "+str(round(media,2)))
r.delete("lista_temp")