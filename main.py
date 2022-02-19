import urllib.request, json
def Scanner():
    print("------------------------------------")
    print("--------------SCANNER---------------")
    print("------------------------------------\n")
    print("    Por favor insira o endereço ip  \n")
    print("    Exemplo de endereço:1.1.1.1     \n")
    ip = input("Informe seu endereço: ")
    with urllib.request.urlopen(f"https://ipinfo.io/{ip}/json") as url:
        dados = json.loads(url.read().decode())
    
    print("Endereço ip: "+dados['ip'])
    print("Indentificação do host: "+dados['city']+"| Localidade: " + dados['region'] + "| Pais: " + dados['country'])
    print('Empresa da rede: ' + dados['org'])
    print('Endereço postal: ' + dados['postal'])
    print('TimeZone: ' + dados['timezone'])
Scanner()