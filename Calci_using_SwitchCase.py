import math
import requests
import datetime
def logging(*arguments):
    with open("Log_File.txt","a+") as f:
        for item in arguments:
            f.write(str(item) + " ")
        f.write("\n")
def get_two_var():
    first_num=int(input("\n\t Enter the first Number : "))
    second_num=int(input("\n\t Enter the second Number : "))    
    return first_num,second_num    

def get_single_var():
    num=int(input("\n\t Enter the Number : "))
    return num
def error_handling():
    print("\n\t Invalid Input : Please enter the correct chiuce number")
class Calculator:
   

    
    # 1) Method for addition of two numbers
    def addition():
        first_num,second_num=get_two_var()
        result=first_num+second_num
        print("\n\t Addition of {} and {} is = {} ".format(first_num,second_num,result))
        format=[" Addition of ","and"," is = "]
        logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        
        flag=True
        while flag:
            print("\n\t 1. To add next number","\n\t 2. Exit")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                
                print("\n\t Addition of {} and {} is = {} ".format(result,next_number,new_result) )
                logging(datetime.datetime.now(),format[0],result,format[1],next_number,format[2],new_result)
                result=new_result
            else:
                flag=False
    
    # 2) Method for Subtraction of two numbers
    def subtraction():
        first_num,second_num=get_two_var()
        format=[" Subtraction of ","and"," is = "]
        if first_num > second_num:
            result= first_num-second_num
            print("\n\t subtraction of {} and {} is = {} ".format(first_num,second_num,result))
            logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        else:
            result= second_num-first_num
            print("\n\t subtraction of {} and {} is = {} ".format(second_num,first_num,result))
            logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        
        flag=True
        while flag:
            print("\n\t 1. To Substract next number","\n\t 2. Exit")
            sub_input=int(input("\n\tSelect Option :",))
            if sub_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                if result > next_number:
                    new_result= result - next_number
                    
                    print("\n\t subtraction of {} and {} is = {} ".format(result,next_number,new_result))
                    logging(datetime.datetime.now(),format[0],result,format[1],next_number,format[2],new_result)
                    result=new_result
                else:
                    new_result= next_number - result
                    
                    print("\n\t subtraction of {} and {} is = {} ".format(result,next_number,new_result))
                    logging(datetime.datetime.now(),format[0],result,format[1],next_number,format[2],new_result)
                    result=new_result
            else:
                flag=False         
            
    
    # 3) Method for addition of two numbers
    def multiplication():
        format=[" Multiplication of ","and"," is = "]
        first_num,second_num=get_two_var()
        result= first_num * second_num
        print("\n\t Multiplication of {} and {} is = {} ".format(first_num,second_num,result))
        logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        flag=True
        while flag:
            print("\n\t 1. To multiply with next number","\n\t 2. Exit")
            add_input=int(input("\n\tSelect Option :",))
            
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                print("\n\t Multiplication of {} and {} is = {} ".format(result,next_number,new_result) )
                logging(datetime.datetime.now(),format[0],result,format[1],next_number,format[2],new_result)
                result=new_result
            else:
                flag=False
    
    # 4) Method for Division of two numbers
    def division():
        format=[" Division of ","and"," is = "]
        first_num,second_num=get_two_var()
        result= first_num / second_num
        print("\n\t Division of {} and {} is = {} ".format(first_num,second_num,result))
        logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        flag=True
        while flag:
            print("\n\t 1. To divide with next number","\n\t 2. Exit")
            add_input=int(input("\n\tSelect Option :",))
            if add_input==1:
                next_number=int(input("\n\t Enter the Next Number : "))
                new_result= result + next_number
                print("\n\t Division of {} and {} is = {} ".format(result,next_number,new_result) )
                logging(datetime.datetime.now(),format[0],result,format[1],next_number,format[2],new_result)
                result=new_result
            else:
                flag=False
    
    # 5) Method for finding remainder of two numbers
    def find_remainder():
        format=[" Remainder of ","and"," is = "]
        first_num,second_num=get_two_var()
        result=first_num % second_num
        if first_num > second_num:
            print("\n\t Remainder of {} and {} is = {} ".format(first_num,second_num,result))
            logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)
        else:
            print("\n\t Remainder of {} and {} is = {} ".format(second_num,first_num,second_num % first_num))
            logging(datetime.datetime.now(),format[0],second_num,format[1],first_num,format[2],result)
         
    # 6) Method for floor Division of two numbers
    def floor_division():
        format=[" Floor Division of ","and"," is = "]
        first_num,second_num=get_two_var()
        result=first_num // second_num
        print("\n\t Division of {} and {} is = {} ".format(first_num,second_num,result))
        logging(datetime.datetime.now(),format[0],first_num,format[1],second_num,format[2],result)

    # 7) Method for finding square
    def find_square():
        format=[" Square of "," is = "]
        num=get_single_var()
        result=pow(num,2)
        print("\n\t Square of {} is = {} ".format(num,result))
        logging(datetime.datetime.now(),format[0],num,format[1],result)

    # 8) Method for finding square root
    def find_square_root():
        format=[" Square Root of "," is = "]
        num=get_single_var()
        result=math.sqrt(num)
        print("\n\t Square Root of {} is = {} ".format(num,result ))
        logging(datetime.datetime.now(),format[0],num,format[1],result)
    
    # 9) Method for finding cube
    def find_cube():
        num=get_single_var()
        format=[" Cube of "," is = "]
        result=pow(num,3)
        print("\n\t Cube of {} is = {} ".format(num,result))
        logging(datetime.datetime.now(),format[0],num,format[1],result)
    # 10) Method for finding cube root
    def find_cube_root():
        format=[" Cube Root of "," is = "]
        num=get_single_var()
        result=pow(num,(1/3))
        print("\n\t Cube Root  of {} is = {} ".format(num,result))
        logging(datetime.datetime.now(),format[0],num,format[1],result)
    
    # 11) Method for currency converter
    def currency_converter():
        format=[" Conversion of ", "to"," is = "]
        from_currency=str(input("\n\t Enter the currency you would like to convert from : ")).upper()
        to_currency=str(input("\n\t Enter the currency you would like to convert to : ")).upper()
        amount=int(input("\n\t Enter the amount : "))
        response= requests.get(
            f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        )
        #print(response.status_code)
        result=response.json()['rates'][to_currency]
        print(f"\n {amount} {from_currency} is {result} {to_currency}")
        logging(datetime.datetime.now(),format[0],from_currency,format[1],to_currency,format[2],result)
        
    # 12) Method for finding the area of triangle
    
    def area_of_triangle():
        format=[" Area of triangle with 3 sides "," is = "]
        a=int(input("\n\t Enter the length of 1st side of triangle : "))
        b=int(input("\n\t Enter the length of 2nd side of triangle : "))
        c=int(input("\n\t Enter the length of 3rd side of triangle : "))
        s=(a+b+c)/2
        area_of_tri=(s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("\n\t Area of Triangle with sides {} {} and {} is = {} ".format(a,b,c,area_of_tri))
        logging(datetime.datetime.now(),format[0],a,b,c,format[1],area_of_tri)
    
    # 13) Method for finding the area of circle
    def area_of_circle():
        format=[" Area of Circle with radius "," is = "]
        radius=int(input("\n\t Enter the Radius of Circle : "))
        result=3.14 * pow(radius,2)
        print("\n\t Area of circle of radius {} is = {} ".format(radius,result))
        logging(datetime.datetime.now(),format[0],radius,format[1],result)


    # 14) Method for finding the area of rectangle
    def area_of_rectangle():
        format=[" Area of Rectangle with breadth","and height"," is = "]
        breadth=int(input("\n\t Enter the breadth of rectangle : "))
        height=int(input("\n\t Enter the height of rectangle : "))
        result=breadth * height
        print("\n\t Area of Rectangle with breadth {} and height {} is = {} ".format(breadth,height,result))
        logging(datetime.datetime.now(),format[0],breadth,format[1],height,result)
    
    # 15) Method for finding the area of square
    def area_of_square():
        format=[" Area of Square with side","is = "]
        side=int(input("\n\t Enter the side of square: "))
        print("\n\t Area of square with side {} is = {} ".format(side,pow(side,2)))
        logging(datetime.datetime.now(),format[0],side,format[1],pow(side,2))

    # 16) Method for finding the percentage
    def find_percentage():
        format=[" Percenatge with Maximum Marks","and","is = "]
        maximum=int(input("\n\t Enter the Maximum Marks : "))
        Total=int(input("\n\t Enter the Total Marks : "))
        result=(maximum/Total) * 100
        print("\n\t The percentage is = {} % ".format(result))
        logging(datetime.datetime.now(),format[0],maximum,format[1],Total,result)
    
    # 17) Method for finding the Nth degree
    def nth_degree():
        format=[" th degree of ","is = "]
        first_num,second_num=get_two_var()
        result=first_num ** second_num
        print("\n\t The {} degree of {} is = {}".format(second_num,first_num,result))
        logging(datetime.datetime.now(),second_num,format[0],first_num,format[1],result)
    
    # 18) Method for finding the Nth root of a number
    def nth_root():
        format=[" th of root of","is = "]
        first_num,second_num=get_two_var()
        result=first_num **(1/second_num)
        print("\n\t The {} root of {} is = {}".format(second_num,first_num,result))
        logging(datetime.datetime.now(),second_num,format[0],first_num,format[1],result)


    # 19) Method for spliiting expenses amongst friends
    def split_expense():
        # Rohan paid Rs. 500 for cab and split_with nedd to pay Rs. split_amount to Rohan.
        format=[" paid Rs."," for "," and "," need to pay Rs.","to"]
        amount=int(input("\n\t Enter the amount : "))
        for_what=input("\n\t This is for what? : ").upper()
        who_paid=input("\n\t Paid By : ").upper()
        print("\n\t Choose with whom you want to split ")
        print("\n\t 1. Shubham", "\n\t 2. Palkesh", "\n\t 3. Anuj", "\n\t 4. Balaji","\n\t 5. Virendra","\n\t 6. Rohan" )
        split_with=input("\n\t Enter the names : ").upper().split()
        split_amount= amount/len(split_with)
        for name in split_with:
            if name!=who_paid:
                print("\n\t{} you need to pay Rs.{} to {} for {}".format(name,split_amount,who_paid,for_what))
        logging(datetime.datetime.now(),who_paid,format[0], amount,format[1], for_what,format[2],split_with,format[3],split_amount,format[4],who_paid)
                
    # 20) Method to print Log File
    def print_log_file():
        with open("Log_File.txt","r") as f:
            for line in f:
                print("\n\t",line,"\n")   

# Driver Code
if __name__=="__main__":
    # For printing the choices
    print("\n 1.  Addition","\n 2.  Substraction","\n 3.  Multiplication","\n 4.  Division",
    "\n 5.  Find Remainder","\n 6.  Floor Division","\n 7.  Find Square","\n 8.  Find Square Root",
    "\n 9.  Find Cube","\n 10. Find Cube Root","\n 11. Currency Converter",
    "\n 12. Find Area of Triangle","\n 13. Find Area of Circle","\n 14. Find Area of Rectangle",
    "\n 15. Find Area of Square""\n 16. Find Percentage","\n 17. Nth Degree of a number",
    "\n 18. Nth root of number","\n 19. Split Expenses","\n 20. Print Logs","\n")
    
    flag = True
    while flag:
        choice=int(input("\n Enter the number which functionality you want to use : "))
        Operations={    1:Calculator.addition,
                        2:Calculator.subtraction,
                        3:Calculator.multiplication,
                        4:Calculator.division,
                        5:Calculator.find_remainder,
                        6:Calculator.floor_division,
                        7:Calculator.find_square,
                        8:Calculator.find_square_root,
                        9:Calculator.find_cube,
                        10:Calculator.find_cube_root,
                        11:Calculator.currency_converter,
                        12:Calculator.area_of_triangle,
                        13:Calculator.area_of_circle,
                        14:Calculator.area_of_rectangle,
                        15:Calculator.area_of_square,
                        16:Calculator.find_percentage,
                        17:Calculator.nth_degree,
                        18:Calculator.nth_root,
                        19:Calculator.split_expense,
                        20:Calculator.print_log_file }
        
        Operations.get(choice,error_handling)()
        # repeatation code
        repeat = input("\n Do you want to go with other choices, if yes then type Y or type N : ")
        if repeat=='N'or repeat=='n':
            flag = False 
            print()