#z poleceniem ht(), które po wykonaniu rysunku ukrywa żółwia

from turtle import *
#fasada
fillcolor("gold")
begin_fill()
for i in range(4):
    fd(120); rt(90)
end_fill()
#dach
fillcolor("tomato")
begin_fill()
for i in range(3):
    fd(120); lt(120)
end_fill()
#okno
pu(); fd(40); rt(90); fd(40); pd()
fillcolor("gray")
begin_fill()
for i in range(4):
    fd(40); lt(90)
end_fill()
#ukrycie żółwia
ht()
