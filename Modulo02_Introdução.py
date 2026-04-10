# Atividade: Saudação Personalizada com horario
print("\n=== MENU PRINCIPAL ===")

from datetime import datetime

#Mostrando a hora atual
agora: datetime = datetime.now()
hora: int = agora.hour

print("Hora atual:", agora.strftime("%H:%M:%S"))

#Definindo o nome do usuário
nome: str = input("Digite seu nome: ")

#Saudação personalizada com base na hora do dia
if hora < 12:
    saudacao = "Bom dia"
    complemento = "tenha uma ótima manhã"
elif hora < 18:
    saudacao = "Boa tarde"
    complemento = "tenha uma ótima tarde"
else:
    saudacao = "Boa noite"
    complemento = "tenha uma ótima noite"

# mensagem final
print(f"{saudacao}, {nome}! {complemento}!")