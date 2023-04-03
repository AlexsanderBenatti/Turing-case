def estacionamento_ok(cars):
    numK = int(cars[0])
    instant = [] #carros que entram e saem no instante i
    parking = [] #ordena os carros que estao no estacionamento
    count = 0 #quantidade de carros no estacionamento
    sim = "sim"
    nao = "nao"
    for i in range(1, len(cars)):
        instant.append(cars[i])

    for i in range(len(instant)):
        if (int(instant[i]) > 0):
            if (count <= numK): #verifica se o estacionamento esta cheio
                count += 1
                parking.append(instant[i]) #"adiciona" o carro no estacionamento
            else:
                return nao
        elif (int(instant[i]) < 0):
            if (abs(int(instant[i])) == int(parking[len(parking)-1])): #verifica se o carro que esta saindo eh o mesmo que entrou por ultimo
                count -= 1
                parking.pop(len(parking)-1)
            else:
                if (count == 1): #verifica se o carro que saiu era o unico no estacionamento
                    count -= 1
                    parking.pop(len(parking)-1)
                else:
                    return nao
    if (count != 0): #verifica se o estacionamento esta vazio no final
        return nao

    return sim

a = input()
a = a.replace("estacionamento_ok(", "")
a = a.replace(")", "")
a = a.replace("[", "")
a = a.replace("]", "")
cars = a.split(",")

print(estacionamento_ok(cars))