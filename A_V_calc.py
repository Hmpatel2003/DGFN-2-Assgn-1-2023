'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
import math

def calculate_area_circle(radius):# Test cases for calculate_area_circle function
    return math.pi * radius**2

def calculate_volume_sphere(radius):
    return 4/3 * math.pi *radius**3

def calculate_area_rectangle(length,breadth):
    return length * breadth
   
def calculate_area_square(length):
    return length * length

def calculate_volume_cylinder(radius,height):
    return math.pi * radius**2 * height

def main():
    display_equation = False # setting calculation in default 
    while True: # loop for level 0 options
        print("A/V Calculator Menu")
        print("Enter Q/q to quit")
        print("Enter V/v to change the calculated view or D/d for default view")
        option = input("Enter your choice: ")
        option = option.lower() #convert input to lower case
        
        if option == 'q': #loop for level 1 options
            print("end")
            break
        elif option == 'v': # sets equation to show general formula
            display_equation = True
        elif option == 'd': # sets equation to default view
            display_equation = False
        else:
            print("Invalid option. Please try again.")
            continue

        print("1. First Area/Volume calculation")
        print("2. Second Area/Volume calculation")
        print("3. Third Area/Volume calculation")
        print("4. Fourth Area/Volume calculation")
        print("5. Fifth Area/Volume calculation")
        
        option = input("Enter your choice: ")
        
        if option.isdigit() and 1 <= int(option) <= 5:
            if option == '1':
                radius = float(input("Enter the radius: ")) # asks for user input for radius
                result = calculate_area_circle(radius) # calculte function
                equation = f"{radius} * {radius} = {result}" # display answer with calculation step
                print("(math.pi * r^2)") if display_equation else '' # prints formula if calculated view is selected
                
            elif option == '2':
                radius = float(input("Enter the radius: "))
                result = calculate_volume_sphere(radius)
                equation = f"{4/3} * {math.pi} * {radius**2} = {result}" 
                print("(4/3 * math.pi * r^3)") if display_equation else ''
                
            elif option == '3':
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                result = calculate_area_rectangle(length, breadth)
                equation = f"{length} * {breadth} = {result}" 
                print("(l * b)") if display_equation else ''
                
            elif option == '4':
                length = float(input("Enter the length: "))
                result = calculate_area_square(length)
                equation = f"{length} * {length} = {result}" 
                print("(l * l)") if display_equation else ''
                
            elif option == '5':
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: "))
                result = calculate_volume_cylinder(radius, height)
                equation = f"{math.pi} * {radius**2} * {height} = {result}" 
                print("(math.pi * r^2 * h)") if display_equation else ''
            
            print(f"Equation: {equation}")# display answer
        else:
            print("Invalid option. Please try again.")# display error for any other inputs other than asked

if __name__ == "__main__":
    main()

    
    

