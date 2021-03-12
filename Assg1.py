class BookStore:
    NoOfBooks=0
    def __init__(self,i,j):
        self.Name=i
        self.Author=j
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
        
    def Display(self):
        print("Name",self.Name)
        print("Author",self.Author)
        print("No Of Books",BookStore.NoOfBooks)
        
        
      
def main():
    
    Obj1=BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2=BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()
    
    
    

if __name__=="__main__":
    main()
