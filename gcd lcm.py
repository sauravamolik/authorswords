m=6
n=9
c=m*n
for i in range(1,c+1):
    if(m%i==0 and n%i==0):
        gcd=i
print("gcd of num is",gcd)
lcm=c/gcd
print("lcm of num is",lcm)
    
