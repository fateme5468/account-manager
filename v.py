def validation(id,username,password):
    assert username.count("@")==1,'username wrong'
    assert len(password)>=8,'password wrong'

    d1={'upper':0,'lower':0,'digit':0,'sp':0}

    for i in password:
        if i.isupper():
            d1['upper']+=1
        elif i.islower():
            d1['lower']+=1
        elif i.isdigit():
            d1['digit']+=1
        else:
            d1['sp']+=1
    assert d1['upper']!=0 and d1['lower']!=0 and d1['digit']!=0 and d1['sp']!=0,'password wrong'
    d2={}
    d2[1]=[username,password]
    
    f1=open(r'C:\Users\NORI\Desktop\save.taxt','a')
    f1.write(f'{id}:{username}:{password}\n')
    f1.close()


print(validation(input('username:'),input('password:')))



