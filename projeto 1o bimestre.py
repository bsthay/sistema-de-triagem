def gravidadeFebre(temperatura):
    if temperatura < 37.5:
        return "Temperatura normal"
    elif temperatura >= 37.5 and temperatura <= 38.9:
        return "Febre moderada (Mantenha-se em observação)"
    else:
        return "Febre alta (Atenção Urgente, vá ao médico)"

def intensidadeDorCabeca(intensidade):
    if intensidade <= 4:
        return "Leve (Autocuidado)"
    elif intensidade <= 7:
        return "Moderada (Mantenha-se em repouso)"
    elif intensidade <= 10:
        return "Intensa (Realize uma consulta médica)"
    else:
        return "Número inválido"

def tosse(tem_tosse):
    if tem_tosse == "Com secreção" or tem_tosse== "com secreção":
        return "Possível Infecção"
    elif tem_tosse == "Seca" or tem_tosse == "seca":
        return "Hidratação"
    else:
        return "Resposta inválida"

#funções de diagnóstico combinado
def febre_dorCabeca():
    print("Você está apresentando sintomas de febre e dor de cabeça.")
    print("Recomendação: hidratação e repouso.")

def febre_tosse():
    print("Você está apresentando sintomas de febre e tosse.")
    print("Recomendação: hidratação, inalação, descanso e repouso com a cabeça elevada para aliviar a tosse.")

def dorCabeca_tosse():
    print("Você está apresentando sintomas de tosse e dor de cabeça.")
    print("Recomendação: hidratação, repouso e, se necessário, usar medicamentos para alívio sintomático, como analgésicos.")

def todosSintomas():
    print("Você está apresentando sintomas de febre, dor de cabeça e tosse.")
    print("Recomendação: hidratação, repouso, alimentação leve.")
    print("Atenção! No seu caso, é fundamental procurar um médico para obter um diagnóstico correto!")

#coleta de dados pessoais do usuário
input("Informe seu nome completo: ")
input("Informe a sua idade: ")
print()

#verificação dos sintomas e diagnóstico individual de cada um
febre = input("Você está com febre? (Sim/Não): ")
if febre == "Sim" or febre == "sim":
    temp = float(input("Informe sua temperatura em °C (graus celsius): "))
    print(gravidadeFebre(temp))
print()

dor_cabeca = input("Você está com dor de cabeça? (Sim/Não): ")
if dor_cabeca == "Sim" or dor_cabeca == "sim":
    intensidade = int(input("Classifique a intensidade da sua dor de cabeça de 0 a 10: "))
    print(intensidadeDorCabeca(intensidade))
print()

presenca_tosse = input("Você está com tosse? (Sim/Não): ")
if presenca_tosse == "Sim" or presenca_tosse == "sim":
    tipo_tosse = input("Sua tosse é com secreção ou seca? (Com secreção/Seca): ")
    tosse(tipo_tosse)
print()

#Diagnóstico combinado e recomendações
if (febre == "Sim" or febre == "sim") and (temp >= 37.5) and (dor_cabeca == "sim" or dor_cabeca == "Sim") and (presenca_tosse == "sim" or presenca_tosse == "Sim"):
    todosSintomas()
    print()
elif (febre == "Sim" or febre == "sim") and (temp >= 37.5) and (dor_cabeca == "sim" or dor_cabeca == "Sim"):
    febre_dorCabeca()
    print()
elif (febre == "Sim" or febre == "sim") and (temp >= 37.5) and (presenca_tosse == "Sim" or presenca_tosse == "sim"):
    febre_tosse()
    print()
elif (dor_cabeca == "Sim" or dor_cabeca == "sim") and (presenca_tosse == "sim" or presenca_tosse == "Sim"):
    dorCabeca_tosse()
    print()
else:
    print()

#Aviso
print("Lembre-se: essa é apenas uma orientação preliminar e a consulta com um profissional de saúde é indispensável para um diagnóstico preciso!")