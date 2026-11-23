endereço_ip = input()
novo_endereço_ip = ""

for i in endereço_ip:
    if i == ".":
        
         novo_endereço_ip += "[.]"
    else:
         novo_endereço_ip += i

print(novo_endereço_ip)

# print(input().replace #jeito mais simples de rodar o mesmo código aprendido na aula.
# (".","[.]"))     

#Isso aí é o clássico defang de IP - pra deixar o IP seguro pra mandar no chat / relatório sem ele virar link clicável!
