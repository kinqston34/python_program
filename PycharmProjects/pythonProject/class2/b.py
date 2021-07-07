#rjust(幾個位置,空值捕的字元)
#ljust
id = 1
name = 'Mary'
fixed_length = str(id).rjust(4,'0')
fixed_length_1 = str(id).ljust(4,'0')
print(fixed_length)
print(fixed_length_1)