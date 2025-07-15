username = input("Enter the username : ")
print("\n")
userName = username.lower()

password = input("Enter the password  : ")
print("\n")

if " " in password:
  c_password = password.replace(" ","_")
else:
  c_password = password  

if "@" not in c_password: 
  print("Wrong Password")
  print(f"🔴 {c_password} must include '@' symbol.")
  
elif len(c_password)<8:
  print("Wrong Password")
  print("🔴 length should be of 8")

elif c_password == "password":  
  print("Wrong Password")
  print(f"🔴 {c_password} must not contain the word 'password'.")
else:
        age = int(input("Enter the age : "))
        print("\n")
        
        if 18<=age<=60:
          print("Valid Age :", "True")
          print("  ✅  Login Successful")
        else:
          print("Valid Age :","False")  
          print(" ❌  Login Failed")  
  
print("\n")  
print("LOGIN_REPORT")  
print("Username: ",userName)
print(f"Formatted Password : {c_password}")
print("Password Length :", len(c_password))
   


































