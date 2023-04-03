def conta_economia(emails):
    counter = 0
    for i in range(1,len(emails)):
        for j in range(len(emails[i])):
            if (emails[i][j] != "@"): #contabilizar ate o @
                if (emails[i][j] == emails[i-1][j]):
                    counter += 1
                else: #para nao contabilizar o resto se ja tiver encontrado uma diferença
                    break
            else:
                break
    return counter

a = input("Input: ")
a = a.replace("conta_economia([", "")
a = a.replace("])", "")
a = a.replace('"', "")
emails = list(a.split(",")) 

print(conta_economia(emails))