def estado_atual(state):
    numK = int(state[0])
    moments = [] #momentos em que os carros entram e saem
    parking = [] #ordena os carros que estao no estacionamento
    time = int(state[len(state)-1])
    for i in range(1, len(state)-1):
        moments.append(state[i])
    for i in range(numK):
        parking.append(0)

    for i in range(1, time+1):
        for j in range(len(parking)-1, 0, -1): #ordena os carros no estacionamento
            parking[j] = parking[j-1]
            parking[j-1] = 0
        
        for j in range(1, len(moments)+1):
            if (int(moments[j-1]) == int(i)): #Adiciona o carro no estacionamento se ele entrou no momento i
                parking[0] = j
    return parking
        
a = input()
a = a.replace("estado_atual(", "")
a = a.replace(")", "")
a = a.replace("[", "")
a = a.replace("]", "")
state = a.split(",")

print(estado_atual(state))