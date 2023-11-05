class abcParams:

    def aParam(own, assets): #Считает параметр А
        return own / assets

    def bParam(cash, assets): #Считает параметр B
        return cash / assets

    def cParam(profit, own): #Считает параметр C
        return profit / own
    
    def allParams(inp_list): #Все параметры для данного банка
        own = inp_list[0] 
        assets = inp_list[1]
        cash = inp_list[2] 
        profit = inp_list[3]
        return abcParams.aParam(own, assets), abcParams.bParam(cash, assets), abcParams.cParam(profit, own)