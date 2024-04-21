def problem_plecakowy(item_list,capacity):
    P=[[0]*(capacity+1) for _ in range(len(item_list)+1)]
    for i in range(1,len(item_list)+1):
        for j in range(1,capacity+1):
            item_weight,item_val=item_list[i-1]
            if item_weight>j:
                P[i][j]=P[i-1][j]
            else:
                P[i][j]=max(P[i-1][j],P[i-1][j-item_weight]+item_val)
    return P[len(item_list)][capacity],P
item_list=[(4,50),(2,60),(4,20),(10,200),(5,70)]
val,P=problem_plecakowy(item_list,12)
print(val)
for i in range(len(item_list)+1):
    print(P[i])
def problem_plecakowy_zerowe_msc(item_list,capacity):
    P=[[0]*(capacity) for _ in range(len(item_list))]
    for i in range(len(item_list)):
        for j in range(capacity):
            item_weight,item_val=item_list[i]
            if i==0 and item_weight-1>j:
                P[i][j]=0
            elif i==0 and item_weight-1<=j:
                P[i][j]=item_val
            elif item_weight-1>j:
                P[i][j]=P[i-1][j]
            elif j-item_weight>=0:
                P[i][j]=max(P[i-1][j],P[i-1][j-(item_weight)]+item_val)
            else:
                P[i][j]=max(P[i-1][j],item_val)

    return P[len(item_list)-1][capacity-1],P
val,P=problem_plecakowy_zerowe_msc(item_list,12)
print(val)
for i in range(len(item_list)):
    print(P[i])