irq = open('sample.txt','r')
for line in irq:
    print(line,end='hoi')
o = open('sample_output.txt','w')
a = irq.read()
o.write("vc é ação para nós")

print(o)
