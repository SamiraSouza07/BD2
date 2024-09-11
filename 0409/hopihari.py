import redis
import time
r = redis.Redis(host="localhost",port=6379,db=0,decode_responses=True)

def montanha():
    if r.get("montanha-russa"):
        time.sleep(1)
        r.incr("montanha-russa")
    else:
        r.set("montanha-russa",1)

    print("Montanha-russa: "+r.get("montanha-russa"))

def roda():
    if r.get("roda-gigante"):
        time.sleep(3)
        r.incr("roda-gigante")
    else:
        r.set("roda-gigante",1)
    print("Roda-gigante: "+r.get("roda-gigante"))

def carrossel():
    if r.get("carrossel"):
        time.sleep(4)
        r.incr("carrossel")
    else:
        r.set("carrossel",1)
    print("Carrossel: "+r.get("carrossel"))


while(True):
    montanha()
    roda()
    carrossel()

