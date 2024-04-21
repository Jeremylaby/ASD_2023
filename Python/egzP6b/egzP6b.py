from egzP6btesty import runtests 

def jump ( M ):
    x,y=0,0
    szachownica={}
    szachownica.update({f"({x},{y})":(x,y)})

    for el in M:
        if el=="UL":
            y+=2
            x-=1
        elif el =="RD":
            y-=1
            x+=2
        elif el =="LU":
            x-=2
            y+=1
        elif el=="UR":
            y+=2
            x+=1
        elif el =="RU":
            y+=1
            x+=2
        elif el=="DR":
            y-=2
            x+=1
        elif el=="DL":
            y-=2
            x-=1
        elif el=="LD" :
            y-=1
            x-=2
        tmp=szachownica.get(f"({x},{y})")
        if tmp:
            szachownica.pop(f"({x},{y})")
        else:
            szachownica.update({f"({x},{y})":(x,y)})         
    #tutaj proszę wpisać własną implementację
    return len(szachownica)
    
runtests(jump, all_tests = True)