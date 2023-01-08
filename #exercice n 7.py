#exercice n 7
price= int(input("enter price "))
if price<=500:
    disc = price*0.5
elif 200<price<=500:
    disc=price*0.3
else:
    disc=price*0.1
nprice=price-disc
print(nprice)

