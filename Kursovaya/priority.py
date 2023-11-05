from banksParams import banksParams as bs
from avgParams import avgParams as avg
from abcParams import abcParams as abc

class priority:
    
    def priority(inp_list): #Сравнивает значения ABC с средним значением
        param_list = bs.all_list(inp_list)
        table = [0,0,0]
        for a in range(len(param_list)):
            table[a] = [0 for i in range(len(inp_list))]
            
        for i in range(len(inp_list)):
            if (param_list[0][i] > avg.avgParams(param_list[0])):
                table[0][i] = 1
            else: table[0][i] = 0
            
            if (param_list[1][i] > avg.avgParams(param_list[1])):
                table[1][i] = 1
            else: table[1][i] = 0 

            if (param_list[2][i] > avg.avgParams(param_list[2])):
                table[2][i] = 1
            else: table[2][i] = 0                                
        return table
    
    def groupPriority(inp_list): #Строит группу-приоритет по ACB (на вход ABC)
        ptable = priority.priority(inp_list)
        table = [0 for i in range(len(inp_list))]
        
        for i in range(len(inp_list)):
            value = ptable[0][i] * 100 + ptable[2][i] * 10 + ptable[1][i] #Т.к. группа приоритет ACB, то сравнивать по столбцам 0 2 1
            match value:
                case 111: table[i] = 1
                case 110: table[i] = 2
                case 101: table[i] = 3
                case 100: table[i] = 4
                case 11: table[i] = 5
                case 10: table[i] = 6
                case 1: table[i] = 7
                case _: table[i] = 8
        return table
    
    def ranking(inp_list):          # Строит иерархический рейтинг IR
        inner_list = [0 for i in range(len(inp_list))]
        
        for i in range(len(inp_list)):
            inner_list[i] = abc.allParams(inp_list[i])
        gptable = (priority.groupPriority(inner_list))
        
        table = [0 for i in range(len(inp_list))]
        count = 1
        scount = 1
        for i in range(8):         
            flag = True
            for j in range(len(inp_list)):
                if ((gptable[j] == count)):
                    table[j] = scount
                    scount += 1                                
                elif (table[j] == 0):
                    table[j] = scount - 1
            count += 1
            
        for i in range(len(gptable)):     # Если есть повторные комбинации, то проверка по D параметру
            for j in range(i, len(gptable)):
                if (gptable[i] == gptable[j] and i != j):
                    if (inp_list[i][3] > inp_list[j][3] and table[i] > table[j]):
                        swap = table[i]
                        table[i] = table[j]
                        table[j] = swap
                    elif (inp_list[i][3] < inp_list[j][3] and table[i] < table[j]):
                        swap = table[i]
                        table[i] = table[j]
                        table[j] = swap
                       
        return gptable, table