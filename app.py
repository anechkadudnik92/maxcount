alphabet = 'abcdefghijklmnopqrstuvwxyz'
str = 'abcyfgzOpqrsTux'
a = list(str)
two_symbols = []
count_in_alphabet = []

for i in range(len(a)-1):
    b = ''.join([a[i],a[i+1]])
    if b.lower() in alphabet:
        two_symbols.append(i)

count = 2
for i in range(len(two_symbols)-1):
    if two_symbols[i+1]-two_symbols[i] == 1:
        count += 1
    else:
        count = 2
    count_in_alphabet.append(count)

if len(two_symbols)>0:
    print max(count_in_alphabet)
else:
    print "No substring in alphabet order"
