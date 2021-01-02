import sqlite3
import os

db = sqlite3.connect("skillapp.db")
cr = db.cursor()
input_message = """
"l" => "Login"
"s" => "Sign Up" 
"""
print(input_message)
FirstInput = input("please chosse one: ").strip().lower()
def Login():
    global username
    username = input("enter your username: ")
    cr.execute("SELECT * FROM users WHERE name = ?", [(username)])
    result = cr.fetchall()
    if result:
        #print it after the password
        pass
    else:
        print("sorry user name is not found")
        exit()

    password = input("enter your password: ")
    cr.execute("SELECT * FROM users WHERE password = ?", [(password)])
    result = cr.fetchall()
    if result:
        #print it after the password
        pass
    else:
        print("sorry your password is incoract")
        exit()

def SignUp():
    global username
    username = input("enter your username: ")
    cr.execute("SELECT * FROM users")
    result = cr.fetchall()

    for i in result:
        if i[0] == username:
            print("the username is already used")
            exit()
    password = input("enter your password: ")
    re_password = input("re-enter your password: ")
    if password != re_password:
            print("your password is incorrect")
            exit()
    
    else:
        cr.execute("INSERT INTO users (name, password) VALUES(?,?)", [(username), (password)])
        db.commit()

input_list = ["l", "s"]

if FirstInput in input_list:
    if FirstInput == "l":
        Login()
    elif FirstInput == "s":
        SignUp()
else:
    print("enter one of those character \"l\" \"s\" " )
    quit()


input_list2 = ["s", "a", "d", "u", "q"]
cr.execute("SELECT user_id FROM users WHERE name=:name", [(username)])
results = cr.fetchall()
strings = [str(result) for result in results]
a_string = "".join(strings)
i = ''.join(str(x) for x in a_string)
result2 = int(i[1:2])

def showSkills():
    cr.execute("SELECT skillName,prograss FROM skills WHERE skills.user_id = ? ", [(result2)])
    result = cr.fetchall()
    if result == []:
        print("you dont have any skill")
        exit()
    else:
        print(result)
    
    db.commit()
def addSkill():
    sk = input("enter your skill name: ")
    prog = input("enter your skill prograss: ")
    cr.execute("INSERT INTO skills(skillName, prograss, user_id) VALUES(?, ?, ?)", [(sk), (prog), (result2)])
    db.commit()
    
def deleteSkill():
    showSkills()
    input1 = input("the name of the skill you want to delete: ")
    cr.execute("DELETE FROM skills WHERE user_id = ? AND skillName = ? ", [(result2),(input1)])
    db.commit()
    print("ok")

def updateSkill():
    showSkills()
    input1 = input("the name of the skill you want to Edit: ")
    input2 = input("what is your prograss: ")
    cr.execute("UPDATE skills SET prograss = ?  WHERE user_id = ? AND skillName = ? ", [(input2),(result2),(input1)])
    db.commit()
def quit():
     exit()

input_message2 = f"""
What Do you Want ? 
"s" => Show All Skills
"a" => Add a New Skill
"d" => Delete a Skill
"u" => Update Skill prograss
"q" => Quit The App

Chosse a Option please:
"""
print(input_message2)
SecoundInput = input("please chosse one: ").strip().lower()
if SecoundInput in input_list2:
    if SecoundInput == "s":
        showSkills()
    if SecoundInput == "a":
        addSkill()
    if SecoundInput == "d":
        deleteSkill()
    if SecoundInput == "u":
        updateSkill()
    else:
        quit()
else:
    print("Flase")

db.close()

