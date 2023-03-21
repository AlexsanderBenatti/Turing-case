def estacionamento_ok(cars):
    numK = int(cars[0])
    instant = []
    parking = []
    count = 0
    for i in range(1, len(cars)):
        instant.append(cars[i])

    for i in range(len(instant)):
        if (int(instant[i]) > 0):
            if (count <= numK):
                count += 1
                parking.append(instant[i])
            else:
                print("nao")
                exit()
        elif (int(instant[i]) < 0):
            if (abs(int(instant[i])) == int(parking[len(parking)-1])):
                count -= 1
                parking.pop(len(parking)-1)
            else:
                if (count == 1):
                    count -= 1
                    parking.pop(len(parking)-1)
                else:
                    print("nao")
                    exit()
    if (count != 0):
        print("nao")
        exit()
    print("sim")

inpu = input("Input: ")
inpu2 = inpu.replace("estacionamento_ok(", "")
inpu3 = inpu2.replace(")", "")
inpu4 = inpu3.replace("[", "")
inpu5 = inpu4.replace("]", "")
cars = inpu5.split(",")

estacionamento_ok(cars)