# 1

name = input('enter your full name')
name = name.split()
name1 = name[0][0]
name2 = name[1][0]

print(f"initial {name1.upper()}.{name2.upper()}")



# 2
word = input('any word')
print(word[::-1])

#3
sentence = input('write sentence')
change = input('write two word.\n first word will be sentence secend word will be \n what you want to be replaced')
change = change.split()
change1 = change[0]
change2 = change[1]
sentence = sentence.replace(change1, change2)
print(sentence)
