import pandas as pd
from entries import file,column

# reading the csv file using pandas NB
data=pd.read_csv(file)

#converting to string make sure no country code is provided
Phone_Numbers = [str(number) for number in data[column]]

if not Phone_Numbers:
    print("Phone Numbers did not read sucessfully")
else:
     # check if correct column is readed by example ,else re run the program by correct column
    print("Phone Numbers read sucessfully","\nEg:",Phone_Numbers[0])