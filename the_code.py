    import mysql.connector

#Connecting to the LETSPLAY DB in mysql
myDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'achyut',
    database = 'letsplay'
)

DBcursor = myDB.cursor()




#CLASS TO COLLECT ALL THE USER INFO

class UserDetails:
    def __init__(self,uid,name,f_name,l_name,email,password):
        self.uid = uid
        self.name = name
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        

#Function to input data and insert it in the user_details table
        
def user_signup(uid,name,f_name,l_name,email,password,re_entry):
    name = input("Enter your username >>> ")
    f_name = input("Enter your first name  >>> ")
    l_name = input("Enter your last name >>> ")

    #check if the email is valid
    while True:
        email = input("Enter your email address >>> ")
        
        check = "!@#$%^&*(){}-[]|\\;:'\"><,?/~`"

        valid = False

        if email.find("@gmail.com", len(email)-10,len(email)) != -1:
            for i in email[0:len(email)-10]:
                if i in check:
                    valid = False
                else:
                    valid = True

        if valid == True:
            break
        else:
            print("Enter valid gmail address")
            continue
        
    #check if the passwords match
    while True:
        
        password = input("Enter a password >>> ")
        re_entry = input("Re-enter the password >>> ")
        if password == re_entry:
            password = password
            break
        else:
            print ("Passwords DONT match")
            continue
        
    print ('usesr ID:',uid,"\n","name:",name,"\n","father's name:",f_name,"\n","last name:",l_name,"\n","email:",email)
    prpass=input("do you want to view password? (y/n)")
    if prpass=="y":
        print ("password:",passsword)

    user = UserDetails(uid,name,f_name,l_name,email,password)
    
    #query to insert the details of the user in the db
    ud_insert = "insert into user_details values(%s,%s,%s,%s,%s,%s)"
    ud_val = (user.uid,user.name, user.f_name, user.l_name, user.email ,user.password)
    DBcursor.execute(ud_insert,ud_val)  

    myDB.commit()

    print ("Sign Up Successful")
    

'''    #printing the user details 
    print ("User details :")

    ud = "select * from user_details where user_name = %s ;"
    ud_val = (str(user.name),)
    DBcursor.execute(ud, ud_val)
    
     

    result_ud = DBcursor.fetchall()


    for x in result_ud:
        print(x)
'''    

    
            

def user_signin(name,password):
    name = input("Enter your username >>> ")
    password=input("Enter your password >>> ")
    zero=0
    u_pass_get = "select user_name,password from user_details;"

    DBcursor.execute(u_pass_get)

    result_pass_get = DBcursor.fetchall()
    
    for i in result_pass_get:
        if name == result_pass_get[zero][0] and password == result_pass_get[zero][1]:
            print ("SIGN IN SUCCESSFULL")
            break
        zero+=1
    else:
        print ("Not successful , Invalid username or password")
        

def manager_signin(mid,password):
    mid = input("Enter the Manager ID >>> ")
    password=input("Enter your password >>> ")
    zero=0
    u_pass_get = "select manager_ID, password from manager_details;"

    DBcursor.execute(u_pass_get)

    result_pass_get = DBcursor.fetchall()
    
    for i in result_pass_get:
        if mid == result_pass_get[zero][0] and password == result_pass_get[zero][1]:
            print ("SIGN IN SUCCESSFULL")
            break
        zero+=1
    else:
        print ("Not successful , Invalid username or password")
        
            

home_pg = str(input("Enter u for User, m for Managers >>> "))
if home_pg == 'U' or home_pg == 'u':
    
    login_pg = int(input("Enter 1 for Sign-In, 2 for Sign-Up >>> "))

    if login_pg == 1:
        username = ""
        password = ""

        user_signin(username,password)
        
    elif login_pg == 2:
        name = ""
        f_name = ""
        l_name = ""
        email = ""
        password = ""
        re_entry = ""
        userid = ""


        #getting all the user_id
        DBcursor.execute("select user_id from user_details;")

        all_users= DBcursor.fetchall()
        
        if len(all_users)==0:
            userid = "ud1"

        else:
            #last user id created
            u_p = all_users[len(all_users)-1][0]
        
            userid = "ud" + str(int(u_p[2::])+1)
            
            
        user_signup(userid,name,f_name,l_name,email,password,re_entry)

elif home_pg == 'M' or home_pg == 'm':
    #manager signin
    m_un = ""
    m_pw=""
    

    manager_signin(m_un,m_pw)





    
    
