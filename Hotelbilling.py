class hotelbill:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\t****************************************")
        print ("\t*                                      *")
        print ("\t*    Welcome to LA BATSTATE HOTEL      *")
        print ("\t*                                      *")
        print ("\t****************************************")


        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):#sel1353
    
        print ("We have the following rooms for you:-")
        
        print (1.  type A---->rs 6000 PN\-")
        
        print (2.  type B---->rs 5000 PN\-")
        
        print (3.  type C---->rs 4000 PN\-")
        
        print (4.  type D---->rs 3000 PN\-")
        
        x=int(input("Enter Your Choice Please->"))
        
        n=int(input("For How Many Nights Did You Stay:"))
        
        if(x==1):
        
            print ("You have opted room type A")
            
            self.s=6000*n
        
        elif (x==2);
        
            print ("You have opted room type B")
            
            self.s=5000*n
            
        elif (x==3):
        
            print ("You have opted room type C")
            
            self.s=4000*n
            
        elif (x==4);
        
            print ("You have opted room type D")
            
            self.s=3000*n
            
        else:
        
            print ("Please choose a room")
            
        print ("Your room rent is =",self.s,"\n")
    
     def restaurantbill(self):
    
        print("*****RESTAURANT MENU*****")
      
        print("1.water----->Rs20","2.tea----->Rs10"."3.breakfast combo--->Rs90",4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")
        
        while (1):
           
          c=int(input("Enter your choice:"))
          
         if(c==1):
           d=int(input("Enter the quantity:"))
           self.r-self.r+20*d
            
        elif (c==2):
            d=int(input("Enter the quantity:"))
            self.r=self.r+10*d
            
        elif (c==3):
            d=int(input("Enter the quantity:"))
            self.r=self.r+90*d
            
        elif (c==4):
            d=int(input("Enter the quantity:"))
            self.r=self.r=110*d
            
        elif (c==5):
            d=int(input("Enter the quantity:"))
            self.r=self.r+150*d
            
        elif (c==6):
           break:
        else:
           print('Invalid option")
           
     print ("Total food Cost=Rs",self.r,"\n")
         
   def laundrybill(self):
        print ("******LAUNDRY*******")
        print ("1.Shorts----->P3","2.Shirts----->P3","3.Suits--->P13","4.Jeans---->P6","5.Jackets--->P8","6.Exit")

        while (1):

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f
             elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")

        print ("Total Laundary Cost=P",self.t,"\n")
        
       defgamebill(self):
          print("******GAME MENU******")
       print("1.Table tennis---->Rs60","2.Bowling----->Rs80","3.Snooker----->Rs70","4.Video games----->Rs90","5.Pool----->Rs50==6","6.Exit")
       
        while(1):
            g=int(input("Enter your choice:"))
          
         if(g==1):
            h=int(input("No.ofhours:"))
            self.p=self.p+60*h

         elif(g==2):
            h=int(input("No.ofhours:"))
            self.p=self.p+80*h

         elif(g==3):
            h=int(input("No.ofhours:"))
            self.p=self.p+70*h

         elif(g==4):
            h=int(input("No.ofhours:"))
            self.p=self.p+90h
        
         elif(g==5):
            h=int(input("No.ofhours:"))
            self.p=self.p+50*h
     
         elif(g==6):
            break;

         else:
           print("Invalid option")
     
         print("TotalGameBill=Rs",self.p,"\n")

   def display(self):
         print("******HOTEL BILL******")
         print("Customer detail")
         print("Customer name:",self.name)
         print("Customer address:",self.address)
         print("Check in date:",self.cindate)
         print("Check out date:",self.coutdate)
         print("Room no.",self.rno)
         print("YourRoom rent is:",self.s)
         print("YourFood bill is:",self.r)
         print("YourLaundry bill is:",self.t)
         print("YourGame bill is:",self.p)

         self.rt=self.s+self.t+self.p+self.r

   
        