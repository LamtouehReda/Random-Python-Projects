from itertools import cycle

#check if a number is two power or not
def isTwoPower(n):
    return (n!=0) and (n&(n-1)==0)

'''
calculate the control bit value
a:the list of bits
k:the bit index
n:the message legnth
'''
def ControlBitSum(a,k,n):
    s=0
    for i in range(k,n+1,2*k):
        for j in range(i,i+k):
            if not isTwoPower(j):
                s+=a[j-1]
    return s%2

#The main algorithme while bits are the bits you wnt to send and n is the message's length that will be send
def hamming(bits,n):
    a=[None for x in range(n)]
    bits_cycle=cycle(bits)
    
    for i in range(n):
        if not isTwoPower(i+1):
            a[i]=next(bits_cycle)
    
    for i in range(n):
        if isTwoPower(i+1):
            a[i]=ControlBitSum(a,i+1,n)
    
    return a

def ErrorHamming(messageRecieved):
    n=len(messageRecieved)
    for i in range(n):
        if isTwoPower(i+1):
            if messageRecieved[i]!=ControlBitSum(messageRecieved,i+1,n):
                return i+1
    return False

bits=[1,0,0,0,0,1,0,0,1,1,1]
msgTosend=hamming(bits,15)
print('The sent message     : ',msgTosend)
msgRecieved=[1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
print('The Recieved message : ',msgRecieved)
res=ErrorHamming(msgRecieved)
if res==False:
    print('There is no error')
else:
    print('The error position is : ',res)