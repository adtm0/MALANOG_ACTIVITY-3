    user_input = eval(input("Enter an integer for seconds: "))
minutes = user_input // 60
seconds = user_input % 60

print("500 seconds is", minutes,"minutes and", seconds, "seconds")