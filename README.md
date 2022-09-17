## 🦸‍♂️ Consuming-Marvel-API
Consumindo a **API da Marvel**,  trazendo os nomes e descrições dos heróis em um arquivo csv.

<br>

API da Marvel está em https://developer.marvel.com/docs

Leia também https://developer.marvel.com/documentation/authorization

<br>

### Arquivo csv após a consumação da API: 

```bash
NAME,DESCRIPTION
3-D Man,
A-Bomb (HAS),"Rick Jones has been Hulk's best bud since day one, but now he's more than a friend...he's a teammate! Transformed by a Gamma energy explosion, A-Bomb's thick, armored skin is just as strong and powerful as it is blue. And when he curls into action, he uses it like a giant bowling ball of destruction! "
A.I.M.,AIM is a terrorist organization bent on destroying the world.
Aaron Stack,
Abomination (Emil Blonsky),"Formerly known as Emil Blonsky, a spy of Soviet Yugoslavian origin working for the KGB, the Abomination gained his powers after receiving a dose of gamma radiation similar to that which transformed Bruce Banner into the incredible Hulk."
Abomination (Ultimate),
Absorbing Man,
Abyss,
Abyss (Age of Apocalypse),
Adam Destine,
Adam Warlock,Adam Warlock is an artificially created human who was born in a cocoon at a scientific complex called The Beehive.
Aegis (Trey Rollins),
Aero (Aero),
Agatha Harkness,
Agent Brand,
Agent X (Nijo),"Originally a partner of the mind-altering assassin Black Swan, Nijo spied on Deadpool as part of the Swan's plan to exact revenge for Deadpool falsely taking credit for the Swan's assassination of the Four Winds crime family, which included Nijo's brother."
Agent Zero,
Agents of Atlas,
Aginar,
Air-Walker (Gabriel Lan),
```

##

### 🔨 Como executar:

* Clone o repositório e vá para a sua pasta:
```
$ git clone https://github.com/RakelMacedo/Consuming-Marvel-API.git

$ cd Consuming-Marvel-API.git/
```

* Agora, vamos criar o nosso ambiente virtual e ativa-lo:
```bash
$ python3 -m venv venv

$ source venv/bin/activate
```

* Em seguida, vamos baixar nossas bibliotecas com:
```bash
$ pip install -r requirements.txt
```
##

### ⚙️ Requisitos: 

* Crie uma conta em Developer Marvel acessando: 
```bash
https://www.marvel.com/signin
```

* Após o Login, clique em **My Developer Account** e copie sua *chave pública* e *chave privada*, e cole no arquivo .env: 
```bash
PUBLIC_KEY=***COLE AQUI***
PRIVATE_KEY=***COLE AQUI***
```
* Agore rode o código e veja o resultado em heros.csv :) 
```bash
$ python code.py
```

✅ Prontinho! =)
