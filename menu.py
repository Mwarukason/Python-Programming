## Text menu in Python
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. WALI NYAMA KUKU (RICE CHIKEN) 1"
    print "2. NDIZI NYAMA YA KUKU (BANANA CHIKEN) 2"
    print "3. BIRIAN KUKU (BIRIAN CHIKEN) 3"
    print "4. MBOGA ZA MAJANI (VEGETABLES) 4"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        print "Menu 1 WALI NYAMA KUKU (RICE CHIKEN) has been selected"
        ## You can add your code or functions here
    elif choice==2:
        print "Menu 2 NDIZI NYAMA YA KUKU (BANANA CHIKEN) has been selected"
        ## You can add your code or functions here
    elif choice==3:
        print "Menu 3 BIRIAN KUKU (BIRIAN CHIKEN) has been selected"
        ## You can add your code or functions here
    elif choice==4:
        print "Menu 4 MBOGA ZA MAJANI (VEGETABLES) has been selected"
        ## You can add your code or functions here
    elif choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Print an Message Error when integer above or lower than 1-5
        raw_input("Wrong option selection. Enter any key to try again..")
