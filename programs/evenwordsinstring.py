def evenwords(s):
    s = s.split()
    for word in s:
        if len(word)%2==0:
            print(word, end=' ')
s = str(input('enter a string : '))
evenwords(s)