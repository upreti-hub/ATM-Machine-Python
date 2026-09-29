password = 12345
amount = 4000
pin = int(input("Enter your pin: "))

if pin == password:
   print("\n") 
   print("1 for checking amount \n" \
  "2 for withdrawing \n" \
  "3 for changing pin \n")
   option = int(input("Choose your option: "))

  #Option 1 for checking balance
   if option == 1:
    print(f"Your account has Rs{amount}")

  #Option 2 for Withdrawing Cash
   elif option == 2:
     balance = int(input("Amount: "))
     if balance <= amount :
       amount = amount - balance
       print(f"You Withdraw {balance}\n")
       print(f"Your Remaining balance is {amount}\n")
       print(f"Thank you for visiting us!")
     else:
       print("Sorry Insufficent Balance") 

  #Option 3 for changing pin
   elif option == 3:
     Old_Pin = int(input("Enter your Old Pin "))
     if Old_Pin ==  password :
        password = input("Enter your new pin: ")
        if password != Old_Pin :
            print("Pin change Sucessfully!!")
   
     
    
else :
   print("Incorect Pin!! Try again") 