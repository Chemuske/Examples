class banksParams:
    
    def a_list(banks_listslist): #Список а-параметров всех банков
        param = [0 for i in range(len(banks_listslist))]
        for a in range(len(banks_listslist)):
            param[a] = banks_listslist[a][0]
        return param

    def b_list(banks_listslist): #Список b-параметров всех банков
        param = [0 for i in range(len(banks_listslist))]
        for a in range(len(banks_listslist)):
            param[a] = banks_listslist[a][1]
        return param

    def c_list(banks_listslist): #Список c-параметров всех банков
        param = [0 for i in range(len(banks_listslist))]
        for a in range(len(banks_listslist)):
            param[a] = banks_listslist[a][2]
        return param
    
    def all_list(banks_listslist): #Список а-параметров b-параметров c-параметров для всех банков [банк][параметр] 
        param = [0,0,0] 
        param[0] = banksParams.a_list(banks_listslist)
        param[1] = banksParams.b_list(banks_listslist)
        param[2] = banksParams.c_list(banks_listslist)
        return param