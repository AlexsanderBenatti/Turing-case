def corrige_emails(emails):
    backup = emails.copy()
    word = "usp.br"
    for i in range(len(emails)):
        emails[i] = list(emails[i]) #transformar em lista para poder alterar os caracteres
        for j in range(len(emails[i])):
            if (j <= int(len(emails[i])/2)-1): #precisa do -1 pois j começa do 0
                emails[i][j] = backup[i][int(len(emails[i])/2)-j-1]
            elif (j >= int(len(emails[i])/2)):
                emails[i][j] = backup[i][int(len(emails[i])/2)-j-1]
        
        emails[i] = "".join(emails[i])
        if word not in emails[i]:
            emails[i] = "ERRO"

    print(emails)

inpu = input("Input: ")
inpu2 = inpu.replace("corrige_emails([", "")
inpu3 = inpu2.replace("])", "")
inpu4 = inpu3.replace('"', "")
emails = list(inpu4.split(",")) 

corrige_emails(emails)