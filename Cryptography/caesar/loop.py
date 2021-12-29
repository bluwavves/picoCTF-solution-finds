from secretpy import Caesar

text = "gvswwmrkxlivyfmgsrhnrisegl"

for i in range(1,25):
    i += 1
    print(Caesar().decrypt(text,i))
    
