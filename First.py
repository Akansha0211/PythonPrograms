hrs = input("Enter Hours:")
rate = input("Enter Rate")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error . please enter numeric input")
    quit()
print(h,r)

# h = float(hrs)
# r = float(rate)

if(h>40):
    grossPay = h * r + (h-40) * 1.5 * r;

else:grossPay = h*r

print(grossPay)
