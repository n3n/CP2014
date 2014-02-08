lista,pos,listb=[int(x) for x in (file("lists.txt","r").read().replace(" ","").replace(",","").replace("\n",""))],0,{"00":[0,1,2,9,10,11,18,19,20],"01":[3,4,5,12,13,14,21,22,23],"02":[6,7,8,15,16,17,24,25,26],"10":[27,28,29,36,37,38,45,46,47],"11":[30,31,32,39,40,41,48,49,50],"12":[33,34,35,42,43,44,51,52,53],"20":[54,55,56,63,64,65,72,73,74],"21":[57,58,59,66,67,68,75,76,77],"22":[60,61,62,69,70,71,78,79,80]}
def check_row(pos,lista):
    for x in [(((int(pos)/9))*9)+x for x in xrange(9)]:
        if x!=pos and lista[pos]==lista[x]:return False
    return True
def check_col(pos,lista):
    for x in [((pos%9)+x*9) for x in xrange(9)]:
        if x!=pos and lista[x]==lista[pos]:return False
    return True
def check_box(pos,lista):
    for x in listb[str(pos/27)+str((pos/3)%3)]:
        if x!=pos and lista[x]==lista[pos]:return False
    return True
def check(pos,lista):
    if check_row(pos,lista) and check_col(pos,lista) and check_box(pos,lista):return True
list_to_operate_on=[x for x in xrange(81) if lista[x]==0]
while pos<len(list_to_operate_on):
    if int(lista[list_to_operate_on[pos]])==9:
        lista[list_to_operate_on[pos]],pos=0,pos-1
        continue
    if int(lista[list_to_operate_on[pos]])<9:lista[list_to_operate_on[pos]]+=1
    if check(list_to_operate_on[pos],lista)==True:pos+=1
for x in xrange(len(lista)):
    z=lista[x] if (x+1)%9!=0 else str(lista[x])+"\n"
    print z,
