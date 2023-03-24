def corrige_emails(emails):
    backup = emails.copy()
    domain = "usp.br"
    for i in range(len(emails)):
        emails[i] = list(emails[i]) #transformar em lista para poder alterar os caracteres
        for j in range(len(emails[i])):
            if (j <= int(len(emails[i])/2)-1): #precisa do -1 pois j começa do 0
                emails[i][j] = backup[i][int(len(emails[i])/2)-j-1] #usa o backup para não alterar o email original
            elif (j >= int(len(emails[i])/2)):
                emails[i][j] = backup[i][int(len(emails[i])/2)-j-1]
        
        emails[i] = "".join(emails[i])
        if domain not in emails[i]: #verifica se o dominio esta correto
            emails[i] = "ERRO"

    print("Output: " + str(emails))

a = input("Input: ")
a = a.replace("corrige_emails([", "")
a = a.replace("])", "")
a = a.replace('"', "")
emails = list(a.split(",")) 

corrige_emails(emails)