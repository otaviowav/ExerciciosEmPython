n = int(input())
countImpar = n
countPar = n
par = ''
impar = ''
while n > 0:
    countImpar -= 1
    countPar += 1
    if countImpar %2 == 1:
        impar = countImpar
    if countPar %2 == 0:
        par = countPar
    if par != '' and impar != '':
        print(impar,par)
        break
