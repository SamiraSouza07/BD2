import re
from pymongo import MongoClient
#conexão com o servidor
conexao = MongoClient("mongodb://localhost:27017/")
#criar um banco de dados
banco_do_sistema = conexao["dbGerminare"] #<- nome do banco no mongodb vai ser o valor da [chave]
#Criar colection
collection_alunos = banco_do_sistema["alunos"]

#(C) - Criar um documento 
aluno1 = {
    'nome':'Samira',
    'sobrenome':'Souza',
    'idade': 16,
    'media':9.9
}
aluno2 = {
    'nome':'Marcelo',
    'sobrenome':'Grilo',
    'idade': 30,
    'media':7.8
}
collection_alunos.insert_one(aluno2)

#(R) - Leitura de um documento
documentos = collection_alunos.find()# Cursor é uma estrutura de dados, precisa ser varrido
for doc in documentos: #para os documentos
    for chave in doc: #para os campos de um documento
        if doc['nome'] == 'Marcelo':
            print(chave,':',doc[chave])

# (U) - Atualizando um documento
filtro = {'nome':'Marcelo'}
resultado_update = collection_alunos.update_one(filtro,{'$set': {'media':8.5}})

if resultado_update.modified_count > 0:
    print('Um documento foi atualizado')
else:
    print('Nenhum documento foi atualizado')


# (D) - Deletar um documento
filtro2= {'nome':'Marcelo'}
resultado_delete = collection_alunos.delete_one(filtro2)
if resultado_delete.deleted_count > 0:
    print('Um documento foi deletado')
else:
    print('Nenhum documento foi deletado')

