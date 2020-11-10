xh = input( "Enter Hours:")
xr = input("Enter Rate:")
xp = float(xh) * float (xr)
print("Pay:",xp)


def computepay(h,r):
    if h > 40:
        norm = h * r
        ot = (h - 40.0) *(r * .5)
        pay = norm + ot
    else:
    	pay = h * r
    return pay
h = input("Enter Hours:")
r = input ("Enter Rate:")
h = float (h)
r = float (r)
p = computepay(10,20)
print("Pay",p)
