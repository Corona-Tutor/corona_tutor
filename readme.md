# Variables

* You want to create a variable when you are trying to keep track of something that will change sometime. It will represent the value in terms of a variable

  ```
  # If you want to keep track of the sum you create a variable sum
  
  sum = 0

  # If you want to keep track of the count you create a variable count
  
  count = 0
  
  # If you want to know whether you are adding or subtracting,
  # you can create a variable that represents that
  
  adding = False # Adding will be True if we are adding
  
  # If you want to know the sum of two numbers
  
  total = sum(1, 2)
  ```

  - You need to ask yourself when these variables will change and add it in the respective spots.

# Functions

* Functions are used when you are trying to streamline a certain "formula" for different variables.
  - Defining a function
  
    ```
    def function1(arguments1, arguments2):
      # ADD CODE HERE
    
    def function2():
      # ADD CODE HERE
      
    def function3(arguments1, arguments2 = False):
      # ADD CODE HERE
    ```
    
    * In order to call a function you want to write the function name and put in the all the arguments that it takes.
    
    > function1(1, 2)
    
    > function2()
    
    
    * Note that we do not need two arguments to this because by default arguments2 = False` so if do not put any value in for arguments2, the code chunk will use arguments2 as False.
    
    > function3(1) 
    
    > function3(1, 2)
    
  - Functions do not need to return anything. 
  
# If statements

* If statements are used when you want to do different things depending on different variables.

  - Structure
  ```
  If (statement1):
    # GO IN HERE if statement1 = True
  elif (statement2):
    # GO IN HERE if statement2 = True and Statement1 = False
  else:
    # GO IN HERE if statement1 and statement2 are both False
  ```
  * There can be as many elif chunks as you want. 
  * Note that you can only have an else statement and elif statement only if you have an else statement. 
  
# For Loops

* For loops are used for many reasons
  - To do something a certain amount of times.
  ```
  for var in range(10):
    # ADD CODE HERE
    
  # The code above will run 10 times. With var going from {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
  
  for var in range(5, 15):
    # ADD CODE HERE
  
  # The code above will run 10 times. With var going from {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
  
  # Both codes will run 10 times but if we do not care about var, both can be used. 
  ```
  
  - You need the numbers from a certain range
  ```
  for var in range(5, 20):
    # ADD CODE HERE
  
  # This code will run 15 times. With var going from 5 to 19. 
  
  for var in range(0, 10, 2):
    # ADD CODE HERE
  
  # This code will run 5 times. With var going from {0, 2, 4, 6, 8}
  ```

# While loops

* While loops are used to do something *WHILE* a certain statement is true

  - Structure
  
  ```
  while (statement):
    # ADD CODE HERE
  
  # You have to make sure that statement changes and will eventuall become FALSE so that you get out of the while loop
  ```
  
# Strings

* Strings are represented by double quotes
> "hello"

  - Adding strings
  > "hello" + " jason" --> "hello jason"
  
  - Length of a string
  > len("hello") --> 5
  
  - Indexing a string
  
    * Indexs of a string are represented by 0 to the length of the string.
    > "hello" # indexs go from 0 1 2 3 4 5
    
    > "hello"[0] --> "h"
    
    > "hello"[len(hello) - 1] --> "o"
    
  - Iterating through a string
    * If you don't need information about the indexes or the positions of the character then you can just do
    
    ``` 
    for character in "hello":
      # ADD CODE HERE
    
    # character will be {'h', 'e', 'l', 'l', 'o}
    ```
    
    * If you do need information about the indexes or the positions of the character then use range
    
    ```
    for index in range(0, len("hello")):
      character = "hello"[index]
      # ADD CODE HERE
   
    # index will be {0, 1, 2, 3, 4, 5} and character will be {'h', 'e', 'l', 'l', 'o}
    ```
    
    * As a while loop you have to use indexs
    ```
    indexs = 0
    while (indexs < len("hello")):
      character = "hello"[index]
      # ADD CODE HERE
      indexs += 1
    ```
    
# Steps in answering a function
  
  1. Know the arguments of the function and what the function should be returning/doing
  2. Try to go through the steps using a specific example and talk using such words like "this will increase when" "if this" "else" "for each of these" "while this is happening"
  3. Try to code using a specific example
  4. Replace the specific example with variable
  5. Input arguments and see if the return is the same as expected

  * EXAMPLE: Count the number of e's in the string

    ```
    def count_e(string):
      # ADD CODE HERE
    ```

    1. Know the arguments of the function and what the function should be returning/doing
    
      - Arguments will be a string and we will return the number of e's in this string

    2. Try to go through the steps using a specific example for the arguments and talk using such words like "this will increase when" "if this" "else" "for each of these" "while this is happening"
      
      - example is string = "hello"
      
      - *For each of the characters in string* we want to check *if* the character is "e", *if* it is then we increase *count* by 1

    3. Try to code using a specific example
    
    ```
     def count_e("hello"):
        count = 0
        for character in "hello":
          if character == "e":
            count += 1
        return count
    ```

    4. Replace the specific example with variable. Replace "hello" with the argument string
    
    ```
     def count_e(string):
        count = 0
        for character in string:
          if character == "e":
            count += 1
        return count
    ```

    5. Input arguments and see if the return is the same as expected
      
      - string = "hello"
      - count will be 0
      - we will iterate through the string
      - character will be "h" first, then we check if it is equal to "e"
        - it is not
      - character then becomes "e", it is "e" so we add one
      - continue steps 
      - count is 1 and it is expected value





