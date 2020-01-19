from random import randint
a = 6 # Length of password
с = 20 # Number of password
for k in range(0,с): # Cycle with c
    for i in range(0,a): # Cycle with a
        b = randint(0,1) # Choose number or letter
        if b == 0:
            if i == 0:
                psw = chr(48+randint(0,9))
            else:
                psw +=chr(48+randint(0,9))
        elif b == 1:
            if i == 0:
                psw = chr(97+randint(0,25))
            else:
                psw +=chr(97+randint(0,25))
    l = str(k+1)
    print(l+"."+psw) # Print password formatting "sn.password"
    del(psw) # clear string for next password
