import oauth2
import json
import urllib.parse

#4 informações necessárias para utilização da API
consumer_key = 'aT0nKsBVycowoKTJ8TgAQx6eO'
consumer_secret = 'i3dGCJfmBajsNA8D5xhohAG8yb9EQQfQ9XY5cnYN2NgvySVoXk'

token_key = '1112724515497410560-TV7SQx8dqyQujsAi32YcdPUf8yioSG'
token_secret = 'QVefzIq6KYvQ4tZPHdE2A8S5NqzNmXlgsXMcWJFHYoZjN'


#Informações que dão acesso a nossa conta no Twitter
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

#Junta as duas informações a cima
cliente = oauth2.Client(consumer, token)

pesquisa = input('Escreva seu Tweet ou Hashtag (#): ')
#Transforma para o caracter URL > % 
pesquisa_avancada = urllib.parse.quote(pesquisa, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa_avancada)


#Transformação para String
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()