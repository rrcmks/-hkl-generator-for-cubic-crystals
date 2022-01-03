import math

two_theta=input("Enter 2-theta, in Degree :  ")
length=input ("Enter the maximum unit cell length (a) in Angstroms :  ")

two_theta=float(two_theta)
length=float(length)


lamda = 1.54059

theta =(two_theta/2)

sintheta = math.sin(math.radians(theta))            
d = lamda/(2*sintheta)

a=0
hmin=0
kmin=0
lmin=0
hmax=9
kmax=9
lmax=9
while a<=length:
    a=a + 0.0001
    x =(a**2)/(d**2)
    for h in range(hmin, hmax):
        h = h+1
        for k in range(kmin, kmax):
            k = k+1
            for l in range(lmin, lmax):
                l = l+1
                y = ((h**2)+(k**2)+(l**2))
                if round(x,4)== round(y,4):
                    print("a = ", round(a,4))
                    print("d-spacing = ", round (d,4))
                    print("{h, k, l} : ",h,k,l)
                    print("  ")

            


    

        


            
    

