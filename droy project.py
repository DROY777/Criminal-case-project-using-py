
import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print()
    print('***********************************')
    print(            "     CRIMINAL CASE    "  )
    print("************************************")
    print()
    print()
    print("Data Analysis")
    print("      1.Reading file without index")
    print("      2.Reading file with new column names")
    print("Data Visualization")
    print("      3.Line plot")
    print("      4.Bar plot")
    print("Data Manupulation")
    print("      5.Reading few rows")
    print("      6.Read 3 records from top and 2 from bottom from table")
    print("      7.Duplicate file with new name")
    print("      8.read with specific colums ")
    print("      9.Create csv file with dataframe ")
    print("     10.Read csv file - sample ")
    print()
    print()      
    print("*******************************")
      
menu()

def no_index():
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv",index_col=0)
    print("without index")
    print(df)


def new_colnam():
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv",skiprows=1,names=['adm','name'])
    print(df)
    
    
def line_plot():
    print('line plot')
    NAME=['HARSHAT','VIJAY','RAHUL','AMIT','AJEY','SIVANSH','ANSH','YUVRAJ','RAJ','AYUSH','ABHINAV','VIRAT','VIVEK','GAMBHIR','SUJAL']
    AGE=[40,24,30,23,26,31,27,28,20,26,28,27,23,30,38,]
    plt.figure(figsize=(13,6))
    plt.xlabel("Age of criminals")
    plt.ylabel("Name of criminals")
    plt.title("Criminals Age chart")
    plt.plot(NAME,AGE)
    plt.show()
    
def bar_plot():
    print('bar plot')
    NAME=['HARSHAT','VIJAY','RAHUL','AMIT','AJEY','SIVANSH','ANSH','YUVRAJ','RAJ','AYUSH','ABHINAV','VIRAT','VIVEK','GAMBHIR','SUJAL','AKASH','VARUN','PARAS','ABISHEK']
    AGE=[40,24,30,23,26,31,27,28,20,26,28,27,23,30,38,40,31,23,27]
    plt.figure(figsize=(17,6))
    plt.bar(NAME,AGE)
    plt.xlabel("Age of criminals")
    plt.ylabel("Name of criminals")
    plt.show()

def read_rows():
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv",nrows=3)
    print(df)

def top_bottom():
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv")

    print('top 3 rows')
    print(df.head(3))
    print()
    print()
    print('last 2 rows')
    print(df.tail(2))
    
def dup():
    print(" duplicate file with new name as crime filenew")
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv")
    df.to_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv")      
    print(df)

def spec_col():
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv",usecols=['NAME','CRIME'])
    print(df)
                                                                                                    
def create_file():
    crimefile={'Sno':[],'NAME':[],'AGE':[],'BLOODGROUP':[],'DOB':[],'CRIME':[]}
    df1=pd.DataFrame(crimefile)
    print(df1)
    df1.to_csv("C:/Users/Droy/Desktop/prog/N/new crimefile.csv")

def csv():
    print('Reading file sample')
    df=pd.read_csv("C:/Users/Droy/Desktop/prog/New folder/crime file.csv")
    print(df)


opt=""
opt=int(input("enter your choice :"))
if opt==1:
    no_index()
elif opt==2:
    new_colnam()
elif opt==3:
    line_plot()
elif opt==4:
    bar_plot()
elif opt==5:
    read_rows()
elif opt==6:
    top_bottom()
elif opt==7:
     dup()
elif opt==8:    
     spec_col()
elif opt==9:
     create_file()
elif opt==10:
     csv()
else:
    print('invalid option') 
     


























    
