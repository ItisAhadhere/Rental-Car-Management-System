print("~~~~~~~~~~~~~~~~~TG ENTERPRISES~~~~~~~~~~~~~~~~~")

#Vehicle Name and Quantity
Altis_Quantity=7
Juke_Quantity=2
Civic_Quantity=5
H6_Quantity=4

#Rent per day
Altis_Rent=6000
Juke_Rent=3500
Civic_Rent=7000
H6_Rent=10000

#Applying 5% Tax
Altis_Tax=Altis_Rent*0.05
Juke_Tax=Juke_Rent*0.05
Civic_Tax=Civic_Rent*0.05
H6_Tax=H6_Rent*0.05

#Insurance Type and Charges
Altis_Liability =500
Altis_Comprehensive=750
Juke_Liability=350
Juke_Comprehensive=600
Civic_Liability=400
Civic_Comprehensive=700
H6_Liability=600
H6_Comprehensive=1000

#Starting Totals
InsuranceTotal=0
totalTax=0
cTotal=0

def car_return(x,y):
    if x=='1':
        y+=1
        return y
    elif x=='2':
        y+=1
        return y
    elif x=='3':
        y+=1
        return y
    elif x=='4':
        y+=1
        return y
while True:
    option = input('\nPlease Select One\n1-Car Rental\n2-Car Return\n3-Print the totals\nOption no:')

    while option not in ['1', '2', '3']:
        print("Invalid Entry. Enter a valid Entry")
        option = input('\nPlease Select One\n1-Car Rental\n2-Car Return\n3-Print the totals\nOption no:')

    if option=='1':
            print("~~~~~~~~~~~~CAR RENTAL~~~~~~~~~~~~")
            print('Please select a vehicle from the Inventory below:\nModel\t\t\tAvailable\tPrice/day\tLiability Insurance/day\t\tComprehensive Insurance/day\n1-Toyota Altis\t\t',Altis_Quantity,'\t\t\t',Altis_Rent,'\t\t\t',Altis_Liability,'\t\t\t\t\t\t',Altis_Comprehensive,'\n2-Nissan Juke\t\t',Juke_Quantity,'\t\t\t',Juke_Rent,'\t\t\t',Juke_Liability,'\t\t\t\t\t\t',Juke_Comprehensive,'\n3-Honda Civic\t\t',Civic_Quantity,'\t\t\t',Civic_Rent,'\t\t\t',Civic_Liability,'\t\t\t\t\t\t',Civic_Comprehensive,'\n4-HAVAL H6\t\t\t',H6_Quantity,'\t\t\t',H6_Rent,'\t\t\t',H6_Liability,'\t\t\t\t\t\t',H6_Comprehensive,)
            Choosecar=input('\nEnter the Serial Number of the vehicle you want to rent: ')
            while True:
                #Checking if Vehicle is in stock
                if Choosecar in ['1','2','3','4']:
                    if (Choosecar=='1' and Altis_Quantity>0) or (Choosecar=='2' and Juke_Quantity>0) or (Choosecar=='3' and Civic_Quantity>0 ) or (Choosecar=='4' and H6_Quantity>0):
                        break
                    else:
                        print("This type of vehicle is unavailable right now.")
                        Choosecar=input("Enter Serial Number of vehicle again: ")
                else:
                    print('Invalid input.')
                    Choosecar=input('Enter the Serial Number again: ')

            #No. of days Vehicle is being rented for
            days=int(input('\nEnter the number of days you want to rent the vehicle for: '))
            #Choosing Type of Insurance
            insurance=input('\nEnter "L" for Liability Insurance or "F" for Full/Comprehensive Insurance: ')
            while True:
                if insurance=='l' or insurance=='L' or insurance=='F' or insurance=='f':
                    break
                else:
                    print('invalid input. Enter your preferred insurance type again')
                    insurance=input('enter "L" for Liability Insurance or "F" for Full/Comprehensive Insurance: ')
            if Choosecar=='1':
                Altis_Quantity=Altis_Quantity-1
                if insurance=='l' or insurance=='L':
                    total=(days*Altis_Rent)+Altis_Tax+Altis_Liability
                    InsuranceTotal+=Altis_Liability
                    totalTax+=Altis_Tax
                    print('\nToyota Altis\nRent/day:\t',Altis_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Altis_Tax,'\nInsurance:\t',Altis_Liability,'\n-----------------------\nTotal:\t\t',total)
                elif insurance=='F' or insurance=='f':
                    total=(days*Altis_Rent)+Altis_Tax+Altis_Comprehensive
                    InsuranceTotal+=Altis_Comprehensive
                    totalTax+=Altis_Tax
                    print('\nToyota Altis\nRent/day:\t',Altis_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Altis_Tax,'\nInsurance:\t',Altis_Comprehensive,'\n-----------------------\nTotal:\t\t',total)
            if Choosecar=='2':
                Juke_Quantity=Juke_Quantity-1
                if insurance=='l' or insurance=='L':
                    total=(days*Juke_Rent)+Juke_Tax+Juke_Liability
                    InsuranceTotal+=Juke_Liability
                    totalTax+=Juke_Tax
                    print('\nNissan Juke\nRent/day:\t',Juke_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Juke_Tax,'\nInsurance:\t',Juke_Liability,'\n-----------------------\nTotal:\t\t',total)
                elif insurance=='F' or insurance=='f':
                    total=(days*Juke_Rent)+Juke_Tax+Juke_Comprehensive
                    InsuranceTotal+=Juke_Comprehensive
                    totalTax+=Juke_Tax
                    print('\nNissan Juke\nRent/day:\t',Juke_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Juke_Tax,'\nInsurance:\t',Juke_Comprehensive,'\n-----------------------\nTotal:\t\t',total)
            if Choosecar=='3':
                Civic_Quantity= Civic_Quantity-1
                if insurance=='l' or insurance=='L':
                    total=(days*Civic_Rent)+Civic_Tax+Civic_Liability
                    InsuranceTotal+=Civic_Liability
                    totalTax+=Civic_Tax
                    print('\nHonda Civic\nRent/day:\t',Civic_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Civic_Tax,'\nInsurance:\t',Civic_Liability,'\n-----------------------\nTotal:\t\t',total)
                elif insurance=='F' or insurance=='f':
                    total=(days*Civic_Rent)+Civic_Tax+Civic_Comprehensive
                    InsuranceTotal+=Civic_Comprehensive
                    totalTax+=Civic_Tax
                    print('\nHonda Civic\nRent/day:\t',Civic_Rent,'\nDays:\t\t',days,'\nTax:\t\t',Civic_Tax,'\nInsurance:\t',Civic_Comprehensive,'\n-----------------------\nTotal:\t\t',total)
            if Choosecar=='4':
                H6_Quantity=H6_Quantity-1
                if insurance=='l' or insurance=='L':
                    total=(days*H6_Rent)+H6_Tax+H6_Liability
                    InsuranceTotal+=H6_Liability
                    totalTax+=H6_Liability
                    print('\nHAVAL H6\nRent/day:\t',H6_Rent,'\nDays:\t\t',days,'\nTax:\t\t',H6_Tax,'\nInsurance:\t',H6_Liability,'\n-----------------------\nTotal:\t\t',total)
                elif insurance=='F' or insurance=='f':
                    total=(days*H6_Rent)+H6_Tax+H6_Comprehensive
                    InsuranceTotal+=H6_Comprehensive
                    totalTax+=H6_Tax
                    print('\nHAVAL H6\nRent/day:\t',H6_Rent,'\nDays:\t\t',days,'\nTax:\t\t',H6_Tax,'\nInsurance:\t',H6_Comprehensive,'\n-----------------------\nTotal:\t\t',total)
            cTotal=total+cTotal
             #If user selects Option 2 in beginning
    elif option=='2':
        print("~~~~~~~~~~~~CAR RETURN~~~~~~~~~~~~")
        while True:
            #Checking if user input is valid or not
            carReturn=input('\n1-Toyota Altis\n2-Nissan Juke\n3-Honda Civic\n4-HAVAL H6\nEnter the serial number of the car you want to return: ')
            if carReturn == '1' or carReturn == '2' or carReturn == '3' or carReturn == '4':
                 break
            else:
                print("Invalid Input. Enter the Serial Number again.")
                carReturn=input('\n1-Toyota Altis\n2-Nissan Juke\n3-Honda Civic\n4-HAVAL H6\nEnter the serial number of the car you want to return: ')

        if carReturn=='1':
            Altis_Quantity=car_return(carReturn,Altis_Quantity)
        elif carReturn=='2':
            Juke_Quantity=car_return(carReturn,Juke_Quantity)
        elif carReturn=='3':
            Civic_Quantity=car_return(carReturn,Civic_Quantity)
        elif carReturn=='4':
            H6_Quantity=car_return(carReturn,H6_Quantity)


        print('\n---------------------------------------------------------------------------------------------------------------------------\nModel\t\t\tAvailable\t\tPrice/day\tLiability insurance/day\t\tComprehensive insurance/day\n---------------------------------------------------------------------------------------------------------------------------\n1-Toyota Altis\t\t',Altis_Quantity,'\t\t\t',Altis_Rent,'\t\t\t',Altis_Liability,'\t\t\t\t\t\t',Altis_Comprehensive,'\n2-Nissan Juke\t\t',Juke_Quantity,'\t\t\t',Juke_Rent,'\t\t\t',Juke_Liability,'\t\t\t\t\t\t',Juke_Comprehensive,'\n3-Honda Civic\t\t',Civic_Quantity,'\t\t\t',Civic_Rent,'\t\t\t',Civic_Liability,'\t\t\t\t\t\t',Civic_Comprehensive,'\n4-HAVAL H6\t\t\t',H6_Quantity,'\t\t\t',H6_Rent,'\t\t\t',H6_Liability,'\t\t\t\t\t\t',H6_Comprehensive,)

    #If user selects Option 3 in beginning
    elif option == '3':
        print("~~~~~~~~~~~~TOTAL~~~~~~~~~~~~")
        print('\nTotal Insurance Cost: ', InsuranceTotal, '\nTotal Tax: ', totalTax, '\nTotal Payable: ', cTotal + totalTax + InsuranceTotal)
    #Prompting user if they want further services or no
    ending = input('\nMore Operations[Y/N?]?\nEnter "Y" to continue or "N" to exit: ')
    if ending == 'N' or ending == 'n':
        print('\nThank You for choosing TG Enterprises.Looking forward to serving you again.\nGoodbye')
        break
    elif ending=='Y' or ending=='y':
        print()

    else:
        print("Invalid Entry. Kindly choose again.")
        ending=input('\nDo you wish to continue?\nEnter "Y" to continue or "N" to exit: ')

