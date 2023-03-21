def conta_economia(emails):
        contador = 0
        for i in range(1,len(emails)):
            for j in range(len(emails[i])):
                if (emails[i][j] != "@"): #para nao contabilizar o @usp.br
                    if (emails[i][j] == emails[i-1][j]):
                        contador += 1
                    else: #para nao contabilizar o resto se ja tiver encontrado uma diferença
                        break
                else:
                    break
        print("contador: " + str(contador))

inpu = input("Input: ")
inpu2 = inpu.replace("conta_economia([", "")
inpu3 = inpu2.replace("])", "")
inpu4 = inpu3.replace('"', "")
emails = list(inpu4.split(",")) 

conta_economia(emails)