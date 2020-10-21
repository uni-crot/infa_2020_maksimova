import turtle
turtle.shape('turtle')
number=input()
f= open('indexText.txt', 'r')
s1=[i.rstrip() for i in f.readlines()]
f.close()
s1=[i.split('|') for i in s1]
s=[]
for i in (s1):
    s.append([j.split(',') for j in i])
for i in range(0,len(number)):
    turtle.penup()
    turtle.goto(int(s[int(number[i])][0][0])+i*40,int(s[int(number[i])][0][1]))
    turtle.pendown()
    for j in range (0,len(s[int(number[i])])):
        turtle.goto(int(s[int(number[i])][j][0])+i*40,int(s[int(number[i])][j][1]))
input()
