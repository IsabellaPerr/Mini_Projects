def convert(string):
    list1=[]
    list1[:]=string
    return list1

n = input('What is your word/num')
x = int(input('What position do you want'))
x = x -1
n = convert(n)

print(n[x])
