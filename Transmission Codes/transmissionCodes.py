def RZ(s,volte):
    c=[]
    for i in range(0,len(s)):
        if s[i]=='0': 
            c.append(-volte)
            c.append(0)
        if s[i]=='1':
            c.append(volte)
            c.append(0)
    return c

def RZdecode(c):
    chaine=''
    for i in range(0,len(c)-1):
        if c[i]>0:
            chaine+='1'
        if c[i]<0:
            chaine+='0'
    return chaine


def NRZ(s,volte):
    c=[]
    for i in range(0,len(s)):
        if s[i]=='0' :
            c.append(-volte)
        if s[i]=='1':
            c.append(volte)
    return c

def NRZdecode(c):
    chaine=''
    for i in range(0,len(c)):
        if c[i]>0:
            chaine+='1'
        if c[i]<0:
            chaine+='0'
    return chaine

def NRZI(s,volte):
    c=[]
    if s[0]=='0':
        c.append(-volte)
    else:
        c.append(volte)
    for i in range(1,len(s)):
        if s[i]=='1':
            c.append(c[i-1])
        if s[i]=='0':
            c.append(-c[i-1])
    return c

def NRZIdecode(c):
    if c[0]<0:
        chaine='0'
    else:
        chaine='1'
    for i in range(1,len(c)):
        if c[i-1]==c[i]:
            chaine+='1'
        else:
            chaine+='0'
    return chaine 

def Manchester(s,volte):
    c=[]
    for i in range(0,len(s)):
        if s[i]=='0':
            c.append(-volte)
            c.append(volte)
        if s[i]=='1':
            c.append(volte)
            c.append(-volte)
    return c

def ManchesterDecode(c):
    chaine=''
    for i in range(0,len(c),2):
        if c[i]<0:
            chaine+='0'
        else:
            chaine+='1'
    return chaine

def Manchester_diff(s,volte):
    c=[]
    if s[0]=='0':
        c.append(-volte)
        c.append(volte)
    else:
        c.append(volte)
        c.append(-volte)
        j=2
    for i in range(1,len(s)):
        if s[i]=='0':
            c.append(c[j-2])
            c.append(c[j-1])
        if s[i]=='1':
            c.append(-c[j-2])
            c.append(-c[j-1])
        j+=2
    return c

def Manchester_diff_decode(ls):
    chaine=''
    if ls[0]<0:
        chaine+='0'
    else:
        chaine+='1'
    for i in range(2,len(ls),2):
        if ls[i-2]==ls[i]:
            chaine+='0'
        if ls[i-2]!=ls[i]:
            chaine+='1'
    return chaine

def Miller(chaine,volte):
    ls=[]
    if chaine[0]=='0':
        ls.append(-volte)
        ls.append(-volte)
    else:
        ls.append(volte)
        ls.append(-volte)
    j=2
    for i in range(1,len(chaine)):
        if chaine[i]=='0':
            if chaine[i-1]=='0':
                ls.append(-ls[j-2])
                ls.append(-ls[j-2])
            else:
                ls.append(ls[j-1])
                ls.append(ls[j-1])
        else:
            ls.append(ls[j-1])
            ls.append(-ls[j-1])
        j+=2
    return ls

def MilerDecode(c):
    chaine=''
    for i in range(0,len(c)-1,2):
        if c[i]==c[i+1]:
            chaine+='0'
        elif c[i]!=c[i+1]:
            chaine+='1'
    return chaine

def CMI(s,volte):
    c=[]
    j=0
    if s[0]=='0':
        c.append(-volte)
        c.append(-volte)
    elif s[0]=='1':
        c.append(-volte)
        c.append(volte)
    j+=2

    for i in range(1,len(s)):
        if(s[i]=='1'):
            c.append(-volte)
            c.append(volte)
            j+=2
        elif s[i]=='0':
            if s[i-1]!='0':
                c.append(c[j-1])
                c.append(c[j-1])
            elif s[i-1]=='0':
                c.append(-c[j-2])
                c.append(-c[j-2])
            j+=2
    
    return c

def CMIdecode(c):
    chaine=''
    for i in range(0,len(c),2):
        if c[i]==c[i+1]:
            chaine+='0'
        elif c[i]!=c[i+1]:
            chaine+='1'
    return chaine

def AMI(s,volte):
    c=[]
    u=0
    for i in range(0,len(s)):
        if s[i]=='0':
            c.append(0)
        if s[i]=='1':
            if u%2==0:
                c.append(volte)
            if u%2!=0:
                c.append(-volte)
            u+=1
    return c
def AMIdecode(c):
    chaine=''
    for x in c:
        if x==0:
            chaine+='0'
        else:
            chaine+='1'
    return chaine

def MLT3(s,volte):
    c=[]
    if s[0]==0:
        c.append(0)
    else:
        c.append(volte)
        u=volte
        prec=volte
    for i in range(1,len(s)):
        if s[i]=='0':
            c.append(c[i-1])
        if s[i]=='1':
            if u==volte:
                c.append(0)
                prec=u
                u=0
            elif u==0 and prec==-volte:
                c.append(volte)
                prec=u
                u=volte
            elif u==0 and prec==volte:
                c.append(-volte)
                prec=u
                u=-volte
            elif u==-volte:
                c.append(0)
                prec=u
                u=0
    return c

def MLT3decode(c):
    if c[0]==0:
        chaine='0'
    else:
        chaine='1'
    for i in range(1,len(c)):
        if c[i]==c[i-1]:
            chaine+='0'
        else:
            chaine+='1'
    return chaine

def _2B1Q(s,info):
    return [info[s[i]+s[i+1]] for i in range(0,len(s)-1,2) if s[i]+s[i+1] in info.keys() ]

def _2B1Qdecode(c,info):
    chaine=''
    switch=dict([(y,x) for (x,y) in info.items() ])
    for x in c:
        if x in info.values():
            chaine+=switch[x]
    return chaine

