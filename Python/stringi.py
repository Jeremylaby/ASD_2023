string="ABCD"
print(string[0])
print(string[:-1])
tab=['A','AB','AAA','AA','B','BB']
tab=sorted(tab)
tab1=[]
tab2=['11','111','1111','1']
tab3=['1111','11','111111','11']
tab1=tab1+tab2
tab1=tab1+tab3
print(tab1)
print(tab)
print(max('0000','0001'))
tab4=['1111','11','100','11000','111111','11','000']
def radixSort(tab,x):
    while x!=-1:
        output_0=[]
        output_1=[]
        for i in tab:
            if len(i)<=x:
                output_0=[i]+output_0
            elif i[x]=="1":
                output_1.append(i)
            else:
                output_0.append(i)
        tab=output_0+output_1
        x-=1
    return tab
tab4=radixSort(tab4,6)
print(tab4)
tab5=['0', '001', '0011', '1011', '1111']
tab6=['', '1', '11', '0', '1011']
print(max('000000000000000001',tab6[3]+"2"))