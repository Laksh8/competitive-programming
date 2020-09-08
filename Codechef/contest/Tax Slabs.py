# Tax Slabs...
lst = []
for _ in range(int(input())):
    lst.append(int(input()))

for n in lst:
               
    tax = 0
    
    if n>250000 :
        if n > 500000:
            tax =+ 0.05*(500000 - 250000)
        else:
            tax += 0.05*(n-250000)

    if n> 500000:
        if n>750000:
            tax += 0.1*(750000-500000)

        else:
            tax+=0.1*(n-500000)

    if n> 750000:
        if n > 1000000:
            tax+= 0.15*(1000000-750000)

        else:
            tax+=0.15*(n-750000)

    if n>1000000:
        if n>1250000:
            tax+=0.2*(1250000-1000000)

        else:
            tax+=0.2*(n-1000000)

    if n> 1250000:
        if n>1500000:
            tax+=0.25*(1500000-1250000)
        else:
            tax+=0.25*(n-1250000)
    if n>1500000:
        tax+= 0.30(n-1500000)

    print("{}".format(n-tax))
