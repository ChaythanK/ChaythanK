import random
AY=str(random.randint(1,3))
YA=AY+'A'
a="A1"
b="A2"
c="A3"
exec("%s = %d" % (a,"rock"))
exec("%s = %d" % (b,"paper"))
exec("%s = %d" % (c,"sissors"))
#rock, paper, sissors shoot!
print(YA)
