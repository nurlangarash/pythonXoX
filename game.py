class Oyun():
    
    def __init__(self):   
        self.lovhe = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.info = True
        self.gedis = 0
    
    def oyna(self):
        if self.gedis%2==0:
            self.o1secim()
        else:
            self.o2secim()
        
        self.info = self.oyunYoxla()
        
        self.gedis +=1
    
    def o1secim(self):
        self.lovheGoster()
        print("X, birinci oyuncu:")
        setir = int(input("Setiri daxil edin: "))
        while setir <1 or setir>3:    
            setir = int(input("Setiri daxil edin: "))       
        sutun = int(input("Sutunu daxil edin: "))
        while sutun <1 or sutun>3:
            sutun = int(input("Sutunu daxil edin: "))
        self.doludurmu(setir,sutun)
        
        if self.doludurmu(setir,sutun):
            self.o1secim()
        else:                          
            self.lovhe[setir-1][sutun-1] = "x"
               
    def o2secim(self):
        self.lovheGoster()
        print("O, ikinci oyuncu:")
        setir = int(input("Setiri daxil edin: "))
        while setir <1 or setir>3:    
            setir = int(input("Setiri daxil edin: "))       
        sutun = int(input("Sutunu daxil edin: "))
        while sutun <1 or sutun>3:
            sutun = int(input("Sutunu daxil edin: "))
        self.doludurmu(setir,sutun)
        
        if self.doludurmu(setir,sutun):
            self.o2secim()
        else:
            self.lovhe[setir-1][sutun-1] = "o"
              
    def doludurmu(self,setir,sutun):
        if self.lovhe[setir-1][sutun-1] != "-":
            return True
        else:
            return False
    
    def lovheGoster(self):
        for i in self.lovhe:
            for j in i:
                print(j,end="")
            print("")
            
    def oyunYoxla(self):
        if [self.lovhe[0][0],self.lovhe[0][1],self.lovhe[0][2]] == ["x","x","x"] or [self.lovhe[0][0],self.lovhe[0][1],self.lovhe[0][2]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False
        if [self.lovhe[1][0],self.lovhe[1][1],self.lovhe[1][2]] == ["x","x","x"] or [self.lovhe[0][0],self.lovhe[0][1],self.lovhe[0][2]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False
        if [self.lovhe[2][0],self.lovhe[2][1],self.lovhe[2][2]] == ["x","x","x"] or [self.lovhe[0][0],self.lovhe[0][1],self.lovhe[0][2]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False
        if [self.lovhe[0][0],self.lovhe[1][0],self.lovhe[2][0]] == ["x","x","x"] or [self.lovhe[0][0],self.lovhe[1][0],self.lovhe[2][0]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False   
        if [self.lovhe[0][1],self.lovhe[1][1],self.lovhe[2][1]] == ["x","x","x"] or [self.lovhe[0][1],self.lovhe[1][1],self.lovhe[2][1]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False   
        if [self.lovhe[0][0],self.lovhe[1][1],self.lovhe[2][2]] == ["x","x","x"] or [self.lovhe[0][0],self.lovhe[1][1],self.lovhe[2][2]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False   
        if [self.lovhe[0][2],self.lovhe[1][1],self.lovhe[2][0]] == ["x","x","x"] or [self.lovhe[0][2],self.lovhe[1][1],self.lovhe[2][0]] == ["o","o","o"]:
            self.lovheGoster()
            print("Oyun bitdi!")

            return False 
        return True
    
oyun = Oyun()
