import re

def my_function 
  value = 0
  my_pass = "CyberDefenders$14"
if re.search('[a-z]', my_pass):
  value = value + 1 #Add 1 to the variable if the password has Lower case 
if re.search('[A-Z]', my_pass):
  value = value + 1 #Add 1 to the variable if the password has Upper case 
if re.search('[0-9]', my_pass):
  value = value + 1 #Add 1 to the variable if the password has numbers
if re.search('[!@#$$%^&*()~_+":?><.,;=-]', my+pass): 
  value = value + 1 #Add 1 to the variable if the password has symbols
if len(my_pass) < 6:
  print("The password should have more than 6 characters")
if value == 4:
  print("Strong password")
if value == 3:
  print("Medium password")
if value == 2:
  print("Weak pssword")
if value == 1:
  print("Very Weak password")
return 0

my_function()
  
 
