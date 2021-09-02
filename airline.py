import mysql.connector
from datetime import datetime
import datetime

mydb = mysql.connector.connect(host = 'localhost',username = 'root',password = '',database = 'qantas_airways')

def option():
    while(True):
        print("\t\t\t \t\t **Heartest Welcome to Qantas** \n")
        
        #input number accoding to requirement        
        print("Please choose one of the following option")
        print("1.Add New Customer Record")
        print("2.View Customer Record")
        print("3.Edit Customer Record")
        print("4.Ticket Reservation")
        print("5.Cancel Reservation")
        print("6.All Passangers Record")
        print("7.Add  Flight Details")
        print("8.View Flight Details")
        print("9.Edit Flight Details")
        print("10.Delete Flight Details")
        
        option = int(input("Your Option --> "))
    
    
        if option==1:
            newclient()
        
        elif option==2:
            viewclient()
        
        elif option==3:
            updateclient()

        elif option==4:
            reservation()

        elif option==5:
            reservationcancel()

        elif option==6:
            allreservation()

        elif option==7:
            newflight()
        
        elif option==8:
            viewflight()
        
        elif option==9:
            editflight()
        
        elif option==10:
            deleteflight()
    
        else:
            option()
        
    

#option 1 used to add details of new client
def newclient():
    name = input("Clients Good Name : ")
    code = input("Create Code       : ")
    email = input("Email Address    : ")
    phone = input("Contact Number   : ")
    pincode = input("Area Pincode   : ")
    street = input("Street Address  : ")
    city = input(" City             : ")
    state = input(" State           : ")
    country = input(" country       : ")

    qry1 = "insert into clients(name,clientcode,email,phone,pincode,street,city,state,country) values('{}','{}','{}',{},'{}','{}','{}','{}','{}')".format(name,code,email,phone,pincode,street,city,state,country)

    mycursor = mydb.cursor()
    mycursor.execute(qry1)
    mydb.commit()

    #Message after saving record to database
    print("Data Inserted")
            
  

#option 2 used to view details of new client
def viewclient():
    code = input("Clients code : ")
    qry2 = "select * from clients where clientcode = '{}'".format(code)
                
    mycursor = mydb.cursor()
    mycursor.execute(qry2)
    myresult = mycursor.fetchall()
        
    #for loop to fetch records from database    
    for row in myresult:
        code = row[0]
        name = row[1]
        email = row[2]
        phone = row[3]
        pincode = row[4]
        street = row[5]
        city = row[6]
        state = row[7]
        country = row[8]
                    
        print("Client Code :  " ,code)
        print("Name        :  " ,name)
        print("Email       :  " ,email)
        print("Contact     :  " ,phone)
        print("Pincode     :  " ,pincode)
        print("Street      :  " ,street)
        print("city        :  " ,city)
        print("State       :  " ,state)
        print("County      :  " ,country)
        print("\n\n")
           



#option 3 used to update details of client
def updateclient():
    while(True):
        code = input("\n\nEnter Client's Code : ")
        while(True):
            print("\nPlease choose one of the following option which you want to edit")
            print("1.Name ")
            print("2.Email Address ")
            print("3.Phone Number ")
            print("4.Pincode ")
            print("5.Address ")
            print("6.City ")
            print("7.State ")
            print("8.Country ")
            update = int(input("Enter your option : ")) 
                    
            if update ==1:
                newname = input("Enter New Name : ")
                qry3 = "update clients set name='{}' where clientcode='{}'".format(newname,code)
                break
                    
            elif update ==2:
                newmail = input("Enter New Email Address : ")
                qry3 = "update clients set email='{}' where clientcode='{}'".format(newmail,code)
                break
                    
            elif update ==3:
                newphone = input("Enter New Contact Number : ")
                qry3 = "update clients set phone='{}' where clientcode='{}'".format(newphone,code)
                break
                    
            elif update ==4:
                newpin = input("Enter New Pincode : ")
                qry3 = "update clients set pincode='{}' where clientcode='{}'".format(newpin,code)
                break
                    
            elif update ==5:
                newaddress = input("Enter New Address : ")
                qry3 = "update clients set street='{}' where clientcode='{}'".format(newaddress,code)
                break
                    
            elif update ==6:
                newcity = input("Enter New City  : ")
                qry3 = "update clients set city='{}' where clientcode='{}'".format(newcity,code)
                break
                    
            elif update ==7:
                newstate = input("Enter New State : ")
                qry3 = "update clients set state='{}' where clientcode='{}'".format(newstate,code)
                break
                    
            elif update ==8:
                newcountry = input("Enter New Country : ")
                qry3 = "update clients set country='{}' where clientcode='{}'".format(newcountry,code)
                break
                    
            else:
                print("\n*Please choose valid option*\n\n")
                        
        mycursor = mydb.cursor()
        mycursor.execute(qry3)
        mydb.commit()
                        
        print("Data Update Successfully\n")
                        
        #asking user weather they want to enter more values or not
        more = input("Want to Edit more : ")
        more = more.lower()
        if (more=='n'):
            print("\t\t\t\t\t\tThankyou ! \n\n  ")
            break



#option 4 used for flight reservation
def reservation():
    custid = input("Clients Unique Id : ")
    flightcode = input("Flight  Code : ")
    meat = input("Weather they wan to add halal meat in thier meal{y/n} : ")
    

    qry4 = "insert into booking(custid,flightcode,halal_meat) values('{}','{}','{}')".format(custid,flightcode,meat)
    mycursor = mydb.cursor()
    mycursor.execute(qry4)
    mydb.commit()

    #Message after saving record to database
    print("Ticket Booked ! Happy Travelling ")

    query41 = "update flights set filledup = filledup+1 where flightcode= '{}'".format(flightcode) 
    mycursor = mydb.cursor()
    mycursor.execute(query41)
    mydb.commit()
    
    query42 = "update flights set free = totalseats - filledup where flightcode= '{}'".format(flightcode)
    mycursor = mydb.cursor()
    mycursor.execute(query42)
    mydb.commit()
  

#option 5 used for cancel flight reservation
def reservationcancel():
    custid = input("Clients Unique Id : ")
    flightcode = input("Flight  Code : ")
    
    qry5 = "select * from flights where flightcode = '{}'".format(flightcode)
                
    mycursor = mydb.cursor()
    mycursor.execute(qry5)
    myresult = mycursor.fetchall()
        
    #for loop to fetch records from database    
    for row in myresult:
        date2 = row[2]
        datetimeFormat = '%H:%M:%S'
        date1 = datetime.datetime.now()

        diff = datetime.datetime.strptime(date2, datetimeFormat) - date1
 
        sec = diff.seconds
        minute = sec / 60
        hour = minute / 60 


        if hour >=2:
            query50 = "delete from booking where flightcode = '{}' and custid = '{}'".format(flightcode,custid)
            mycursor = mydb.cursor()
            mycursor.execute(query50)
            mydb.commit()
            print("Your Reservation is cancelled")

            query51 = "update flights set filledup = filledup-1 where flightcode= '{}'".format(flightcode) 
            mycursor = mydb.cursor()
            mycursor.execute(query51)
            mydb.commit()
    
            query52 = "update flights set free = totalseats + filledup where flightcode= '{}'".format(flightcode)
            mycursor = mydb.cursor()
            mycursor.execute(query52)
            mydb.commit()


        else:
            print("Sorry its less than 2 hours to flight . You can't cancel it now")
            



#option 6 used to view details of flight with schedule
def allreservation():
    flightcode = input("Flight  Code : ")
    
    qry61 = "select * from flights where flightcode = '{}'".format(flightcode)
    qry62 = "SELECT COUNT(halal_meat) FROM booking WHERE halal_meat='y'"

    mycursor = mydb.cursor()
    mycursor.execute(qry61)
    myresult = mycursor.fetchall()

    mycursor = mydb.cursor()
    mycursor.execute(qry62)
    myresult2 = mycursor.fetchall()

    #for loop to fetch records from database    
    for row in myresult:
        code = row[0]
        origin = row[1]
        origin_time = row[2]
        departure = row[3]
        departure_time = row[4]
        luggage = row[5]
        seats = row[6]
        seats_free = row[8]
        seats_occupied = row[7]


        print("\n\n")            
        print("{:30}{:>30}".format("FLight Code" , code))
        print("{:30}{:>30}".format("Origin" , origin))
        print("{:30}{:>30}".format("Origin Time" , origin_time))
        print("{:30}{:>30}".format("Departure", departure))
        print("{:30}{:>30}".format("Departure Time" , departure_time))
        print("{:30}{:>30}".format("Luggage Allowed" , luggage))
        print("{:30}{:>30}".format("Total Seats" , seats))
        print("{:30}{:>30}".format("Luggage Allowed" , seats_free))
        print("{:30}{:>30}".format("Seats Occupied" , seats_occupied))

        for row in myresult2:
            meat = row[0]
            print("{:30}{:>30}".format("Halal Meat Requirement " , meat))

        print("\n\n")



#option 7 used to add details of new flight with schedule
def newflight():
    code = input("Flight Code               : ")
    origin = input("Flight Origin           : ")
    origin_time = input("Flight Origin Time {09:56:28} : ")
    departure = input("Flight Departure     : ")
    departure_time = input("Flight Departure Time{09:56:28}  : ")
    luggage = input("Total Luggage Allowed  : ")
    total_seats = int(input("Total Number of Seats    : "))

    qry7 = "insert into flights(flightcode,origin,origintime,destination,depttime,luggage,totalseats) values('{}','{}','{}','{}','{}','{}',{})".format(code,origin,origin_time,departure,departure_time,luggage,total_seats)

    mycursor = mydb.cursor()
    mycursor.execute(qry7)
    mydb.commit()

    #Message after saving record to database
    print("Data Inserted")
            





#option 8 used to view details of flight
def viewflight():
    code = input("Flight Code : ")

    
    qry8 = "select * from flights where flightcode = '{}'".format(code)

    mycursor = mydb.cursor()
    mycursor.execute(qry8)
    myresult = mycursor.fetchall()
        
    #for loop to fetch records from database    
    for row in myresult:
        code = row[0]
        origin = row[1]
        origin_time = row[2]
        departure = row[3]
        departure_time = row[4]
        luggage = row[5]
        seats = row[6]
        seats_free = row[8]
        seats_occupied = row[7]
                    
        print("** Flight Number  :  " ,code , "**\n")
        print("{:30}{:>30}".format("Origin" , "Departure"))
        print("{:30}{:>30}".format(origin , departure))
        print("{:30}{:>30}".format(origin_time , departure_time))
        print("\nLuggage Allowed :  " ,luggage)
        print("Total Seats     :  " ,seats)
        print("Seats Free      :  " ,seats_free)
        print("seats_occupied  :  " ,seats_occupied)
        print("\n\n\n")
           





#option 9 used to update details of flight
def editflight():
    while(True):
        code = input("\n\nEnter Flight's Code : ")
        while(True):
            print("\nPlease choose one of the following option which you want to edit")
            print("1.Origin : ")
            print("2.Origin Time : ")
            print("3.Destination : ")
            print("4.Destination Time : ")
            print("5.Luggage Allowed : ")
            print("6.Total Seats : ")
            update = int(input("Enter your option : ")) 
                    
            if update ==1:
                neworigin = input("Enter New Origin Location : ")
                qry9 = "update flights set origin='{}' where flightcode='{}'".format(neworigin,code)
                break

            elif update ==2:
                neworigintime = input("Enter New Origin Time : ")
                qry9 = "update flights set origintime='{}' where flightcode='{}'".format(neworigintime,code)
                break

            elif update ==3:
                newdestination = input("Enter New Destination Location : ")
                qry9 = "update flights set destination='{}' where flightcode='{}'".format(newdestination,code)
                break

            elif update ==4:
                newdestinationtime = input("Enter New Destination time : ")
                qry9 = "update flights set depttime='{}' where flightcode='{}'".format(newdestinationtime,code)
                break

            elif update ==5:
                newluggage = input("Enter New Luggage Allowed : ")
                qry9 = "update flights set luggage='{}' where flightcode='{}'".format(newluggage,code)
                break

            elif update ==6:
                newtotalseats = int(input("Enter New Luggage Allowed : "))
                qry9 = "update flights set totalseats={} where flightcode='{}'".format(newtotalseats,code)
                break

            else:
                print("\n*Please choose valid option*\n\n")
                        
        mycursor = mydb.cursor()
        mycursor.execute(qry9)
        mydb.commit()
                        
        print("Data Update Successfully\n")
                        
        #asking user weather they want to enter more values or not
        more = input("Want to Edit more : ")
        more = more.lower()
        if (more=='n'):
            print("\t\t\t\t\t\tThankyou ! \n\n  ")
            break




def deleteflight():
    code = input("Flight Code : ")

    
    qry10 = "delete from flights where flightcode = '{}'".format(code)

                
    mycursor = mydb.cursor()
    mycursor.execute(qry10)
    mydb.commit()

    
    #Message after saving record to database
    print("Flight Deleted from record")



               
#calling main function
def main():
    option()

if __name__ == "__main__":
    main()
