import random
abcs = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
new_abcs = []
key_abcs = []


while len(abcs) > 0:
    word = abcs.pop(0).lower()
    new_abcs.append(word)    
print(new_abcs)

# for _ in range(6):
#     letter = random.randint(0,(len(abcs) - 1))
#     key_abcs.append(abcs[letter])
#     abcs.remove(abcs[letter])

# print(key_abcs,"\n",abcs)