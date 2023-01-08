import math
d =[ 100000, 200000 , 300000]
rent = 1000
FLtax = -150    
ultities = -250
Hoa = -25
lawn = -75
copex = -100
repairs = -100
mortgage1 = rent * 0.16-+rent-repairs-copex-ultities-Hoa-FLtax+rent*0.05+100000*0.0743//12
mortgage2 = rent*2 * 0.16-+rent*2-repairs-copex-ultities-Hoa-FLtax+rent*2*0.05+200000*0.0743//12
mortgage3 = rent*4 * 0.16-+rent*2-repairs-copex-ultities-Hoa-FLtax+rent*4*0.05+300000*0.0743//12 
fcash1 =rent -mortgage1
fcash2 = rent*2 - mortgage2
fcash3 = rent*4 - mortgage3
ti1 =int(100000 *0.2+3000+7000 )
ti2 =int(200000 *0.2+3000+7000 )
ti3 =int(300000 *0.2+3000+7000 )
cci=fcash1*12/ti1*100
cci2=fcash2*12/ti2*100
cci3=fcash3*12/ti3*100


rc = print("We have only apartments ranging" , list(d))
br =int(input(" What in you budget:  100000, 200000 , 300000 "))

class RentalProperties():
    def __init__(self):
        self=self
       
    def income(self):
        
        if br == 100000:
            print(f'This {d[0]} budget range has no available amenties income will be : {rent}')
        elif br == 200000:
            print(f'This {d[1]} property has laundry included in, your income will be {rent*2} ') 
        elif br == 300000:
                 print(f'This {d[2]} property has storage and laundry , your income will be {rent*4} ')      
        else:
            print("invailed no properties within this budget")


  

    def expense(self):

            if br == 100000:
                print(" This property has no Hoa fee nor lawn. The renters will also be paying the ultities")
                print(f'{mortgage1} is your monthly expenses')
                
            elif br == 200000:
                print(" This property has Hoa fee no lawn. property owner will be paying the ultities")
                print(f'{mortgage2} is your monthly expenses')

            elif br == 300000:
                print(" This property has Hoa fee and lawn. property owner will be paying the ultities")
                print(f'{mortgage3} is your monthly expenses')
                
            else:
                print("invailed entry")
    def Cashflow(self):
        if br == 100000:
            print(f' This is your cash flow for this property {fcash1}')
        elif br == 200000:
            print(f' This is your cash flow for this property {int(fcash2)}')
        elif br == 300000:
            print(f' This is your cash flow for this property {int(fcash3)}')
        else:
            print("invailed")

    def CashonCashroi(self):
        if br == 100000:
            print(f'Your cash return is {int(cci)}%')
        elif br == 200000:
            print(f'Your cash return is{int(cci2)}%')
        elif br == 300000:
            print(f'Your cash return is {int(cci3)}%')
        
 
florida = RentalProperties()
florida.income()
florida.expense()
florida.Cashflow()
florida.CashonCashroi()
