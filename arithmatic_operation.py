def arithmatic_op(val1,val2):
    addition=val1+val2
    difference=val1-val2
    mul=val1*val2
    return addition,difference,mul
val1=int(input("Enter the Number : "))
val2=int(input("Enter the Number : "))
v1,v2,v3=arithmatic_op(val1, val2)
print(v1)
print(v2)
print(v3)

