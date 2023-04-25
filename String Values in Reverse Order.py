def reverse_list(string):
    modified_data = string[::-1]
    print("This are the reverse string: ", modified_data) 
    
def main():
    string_value1 = str(input("Please enter 1st word: "))
    string_value2 = str(input("Please enter 2nd word: "))
    string_value3 = str(input("Please enter 3rd word: "))
       
    string = (f"{string_value1} {string_value2} {string_value3}")

    print("These are the string: ", string)
    reverse_list(string)
    
        
if __name__ == "__main__":
    main()