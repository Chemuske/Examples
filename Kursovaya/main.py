from priority import priority as pr 
from abcParams import abcParams as abc
import pandas as pd
import os

class main:
    
    def main():      
        a = (1241923682, 14020428211, 1264097488, 219697463)
        b = (412432343, 3626642697, 386981520, 51052467)
        c = (657916496, 6407829972, 486846068, 46338254)
        d = (371871041, 2315956863, 111803518, 47168031)
        f = (161611821, 1372200534, 79476957, 12241077)  
        list = [a,b,c,d,f]
        ss = pr.ranking(list)        
        for i in range(len(list)):
            print(" Параметры ABC для", i + 1, "банка =", abc.allParams(list[i])) 
        print(" Группа - приоритет ACB =", ss[0], '\n', "Иерархический рейтинг IR =", ss[1])      
        os.system("pause")
        return 0
    
    def inpExcel():
        
        file = 'banks.xlsx'
        xl = pd.ExcelFile(file)
        df = pd.DataFrame({'Bank': ['Первый', 'Второй', 'Третий', 'Четвертый'],
                           'Параметр A':['1241923682', '14020428211', '1264097488', '219697463'],
                           'Параметр B':['412432343', '3626642697', '386981520', '51052467'],
                           'Параметр C':['657916496', '6407829972', '486846068', '46338254'],
                           'Параметр D':['371871041', '2315956863', '111803518', '47168031'],
                           'Параметр F':['161611821', '1372200534', '79476957', '12241077']})
        df.to_excel('./banks.xlsx',sheet_name='banks')

    def outExcel():
    
        file = 'banks.xlsx'
        xl = pd.ExcelFile(file)

        aParam = pd.read_excel(file, usecols = 'C')
        bParam = pd.read_excel(file, usecols = 'D')
        cParam = pd.read_excel(file, usecols = 'E')
        dParam = pd.read_excel(file, usecols = 'F')
        fParam = pd.read_excel(file, usecols = 'G')
        #print(aParam)
        list(aParam)
        print(aParam)
        df = pd.DataFrame(aParam)
        df.to_excel('./banks.xlsx', startcol=7,header='aParam')
        #print(xl.head())

    
main.inpExcel() 
#main.outExcel()   
#main.main()