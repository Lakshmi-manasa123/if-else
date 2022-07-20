# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)


square={1:2,2:3,4:5,7:2}
p={}
for i in square:
    p.update({i:square[i]*square[i]})
    i+=1
print(p)