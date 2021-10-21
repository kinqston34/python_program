a = 0.1 + 0.1 + 0.1 #採二進為逼近
print(a)
import decimal
a = decimal.Decimal('0.1')
a = a+a+a
print(a)
b = decimal.Decimal('0.3')
print(a==b)