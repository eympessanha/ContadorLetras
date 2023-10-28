import funcoes
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

print("Contagem de letras!")
print("Para encerrar a adição de palavras, basta inserir X")
palavra = str(input("Insira a palavra: ")).upper()
while palavra != "X":
    for letra in palavra:
        if letra == "A":
            a += 1
        elif letra == "B":
            b += 1
        elif letra == "C":
            c += 1
        elif letra == "D":
            d += 1
        elif letra == "E":
            e += 1
        elif letra == "F":
            f += 1
        elif letra == "G":
            g += 1
        elif letra == "H":
            h += 1
        elif letra == "I":
            i += 1
        elif letra == "J":
            j += 1
        elif letra == "K":
            k += 1
        elif letra == "L":
            l += 1
        elif letra == "M":
            m += 1
        elif letra == "O":
            o += 1
        elif letra == "P":
            p += 1
        elif letra == "Q":
            q += 1
        elif letra == "R":
            r += 1
        elif letra == "S":
            s += 1
        elif letra == "T":
            t += 1
        elif letra == "U":
            u += 1
        elif letra == "V":
            v += 1
        elif letra == "W":
            w += 1
        elif letra == "X":
            x += 1
        elif letra == "Y":
            y += 1
        elif letra == "Z":
            z += 1
    # funcoes.verificarLetras(palavra,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
    palavra = str(input("Insira a palavra: ")).upper()
funcoes.exibirLetras(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)


