#In this chapter you’ll learn how to accept user input so your program can then work with it. 
#To do this, you’ll use the input() function.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


#name = input("Please enter your name: ")
#print(f"\nHello, {name}!")


prompt = "/nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = " "
while message != "quit": 
    message = input(prompt)
    print(message)