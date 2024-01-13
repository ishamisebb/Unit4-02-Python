#created by ishami sebgoya
#date:december 12 2023

def main():
  try:
    #set factorial and counter
    loop_counter = 0
    factorial = 1
    # get user number
    user_number = int(input("Enter a positive number: "))
    print("")
#calculate the factorial of the user number using loop
    while True:
        loop_counter = loop_counter + 1
        factorial = loop_counter * factorial
        print("calculating {} times through the loop.".format (loop_counter))
        if loop_counter >= user_number:
          break
    print("")
    print ("{}! = {}.".format (user_number , factorial))
  except ValueError :
    print("invalid  input,please enter a valid number.")
if __name__ == "__main__":
    main()