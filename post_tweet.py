import oauth2
import json
import urllib.parse

consumer_key = 'key_do_consumer'
consumer_secret = 'secret_consumer'

token_key = 'key_token'
token_secret = 'secret_token'


#Informações que dão acesso a nossa conta no Twitter
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

#Junta as duas informações a cima
cliente = oauth2.Client(consumer, token)


pesquisa = input("Poste um Tweet aqui: ")
#Transforma para o caracter URL > % <
pesquisa_avancada = urllib.parse.quote(pesquisa, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_avancada, method='POST')

#Transformação para String
decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
print(objeto)

