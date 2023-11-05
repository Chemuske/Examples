class avgParams: #Среднее значение из списка
    
    def avgParams(inp_list):
        sum_list = sum(inp_list)
        avg_list = sum_list / len(inp_list)
        return avg_list