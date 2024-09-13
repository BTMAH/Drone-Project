#define constants
pi=3.14159265358979

# Ensure positive input for diameter
while True:
    try:
        diameter = float( input("Enter the diameter in cm: "))
        if diameter > 0:
            break
        else:
            print("Please enter a positive number (diameter can't be a negative number)")
    except ValueError:
        print("Invalid input. Please enter a valid number")
        
# define radius
radius = diameter/2

# calculate the area
area = round(pi*(radius)**2, 2)
area_output = str(area)+ " cm\u00b2"

# calculate the circumference
circumference = round(2*pi*radius, 2)
circumference_output = str(circumference)+ " cm"

#output the results
print("The circle area, to the nearest hundredth, is",(area_output))
print("The circle cirumference, to the nearest hundredth, is", (circumference_output))

# Add some print statements while making code to check if code is working properly at certain checkpoints
# print("The circle area, to the nearest hundredth is" + str(area)+" cm^2")
# make you convert the area from a float to string (or vice versa) or else you will get an error
# look into the \n for special characters or /m
# to practice:
# Google Colab
# w3schools.com
# Make sure you watch the lecture videos before Studio Sessions tomorrow