class BankAccount:
    ROI=10.5
    def __init__(self,i,j):
        self.Name=i
        self.Amount=int(j)
        
    def Display(self):
        print("Name",self.Name)
        print("Amount",self.Amount)

    def Deposit(self,amt):
        self.Amount=self.Amount+int(amt)
        return self.Amount
        
    def Withdraw(self,amt):
        self.Amount=self.Amount-int(amt)
        return self.Amount
        
    def CalculateInterest(self):
       return self.Amount*BankAccount.ROI
        

        
      
def main():
    
    Obj1=BankAccount("Snehal","10000")
    Obj1.Display()
    print("Amount deposited",Obj1.Deposit(10))
    print("Amount withdrawn",Obj1.Withdraw(10))
    print("ROI on Amount",Obj1.CalculateInterest())
    
    

if __name__=="__main__":
    main()
