def estado_atual(state):
    numK = int(state[0])
    moments = []
    parking = []
    time = int(state[len(state)-1])
    for i in range(1, len(state)-1):
        moments.append(state[i])
    for i in range(numK):
        parking.append(0)

    for i in range(1, time+1):
        for j in range(len(parking)-1, 0, -1):
            parking[j] = parking[j-1]
            parking[j-1] = 0
        
        for j in range(1, len(moments)+1):
            if (int(moments[j-1]) == int(i)):
                parking[0] = j
    print(parking)
        
inpu = input("Input: ")
inpu2 = inpu.replace("estado_atual(", "")
inpu3 = inpu2.replace(")", "")
inpu4 = inpu3.replace("[", "")
inpu5 = inpu4.replace("]", "")
state = inpu5.split(",")

estado_atual(state)