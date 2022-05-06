import time

def cuenta_atras(seg):
    seg -= 1
    if seg > 0:
        print (seg)
        time.sleep(1)
        cuenta_atras(seg)
    else:
        print ("La cuenta terminó")

cuenta_atras(10)