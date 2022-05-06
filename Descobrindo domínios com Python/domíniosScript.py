import whois #Whois é um servidor ou protocolo para consulta de informações de contato, domínios e DNS
dominio = input("Alvo:") 
consulta_whois = whois.whois(dominio) #chamando a função whois e passando para ela, que queremos fazer o Scan de dominio, que será o valor que nós iremos colocar no Input. 

#print consulta_whois.fone..., text, firstdate, há diversas opções, para ver uma lista completa, deixe em aberto consulta_whois.
print (consulta_whois.text) #Será printado o resultado do código acima.

#https://pypi.org/project/python-whois/ caso não consiga instalar usando o comando: pip install python-whois