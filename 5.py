string = input("Enter a text: ") 

  

text = string.upper() 

  

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 

    count = text.count(char) 

     

    if count > 0: 

        print(char, count) 