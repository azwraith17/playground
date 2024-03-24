al="abcdefghi jklmnopqrstuvwxyz"
while(True):
    key=13
    c = input("en or de?")
    if c=="en":
        x=input("give the text:")
        x=list(x)
        for i in range(len(x)):
            if x[i]in al:
                x[i]=al[al.index(x[i])-key]

        r=''.join(x)
        print(r)
    elif c=="de":
        x=input("give the c-text:")
        x=list(x)
        for i in range(len(x)):
            if x[i] in al:
                x[i]=al[al.index(x[i])-(len(al)-key)]
        r=''.join(x)
        print(r)
    else:
        break
