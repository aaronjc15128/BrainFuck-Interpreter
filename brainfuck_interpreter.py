def main():
    from os import system
    from sys import exit
    from time import time
    
    # create memory
    global memorysize
    memorysize = 30000
    
    def mainmenu():
        title = "BRAINFUCK INTERPRETER\nby Aaron Chauhan\n"
        
        # mainmenu
        system("clear")
        print(title)
        print("What would you like to do?\n1. Interpret\n2. Config")
        userinput = int(input(">>>  "))
        
        # interpret
        if userinput == 1:
            system("clear")
            print(title)
            filepath = input("Enter .bf file path: ")

            start_time = time()

            # create memory
            memory = [0] * memorysize
            pointer = 0
        
            # get brainfuck file
            file = open(filepath, "r")

            # convert file to string
            brainfuck = ""
            for line in file:
                brainfuck += line.strip()


            currentprint, jumptoCB = "", False
            
            # loop through each character of brainfuck using while loop
            i = 0
            while i < len(brainfuck):
                char = brainfuck[i]
                
                if jumptoCB == True:
                    if char == "]":
                        jumptoCB = False

                elif char == ">":
                    pointer += 1

                elif char == "<":
                    pointer -= 1

                elif char == "+":
                    if memory[pointer] == 255:
                        memory[pointer] = 0
                    else:
                        memory[pointer] += 1

                elif char == "-":
                    if memory[pointer] == 0:
                        memory[pointer] = 255
                    else:
                        memory[pointer] -= 1

                elif char == ".":
                    currentprint += chr(memory[pointer])

                elif char == ",":
                    pass

                elif char == "[":
                    # get index of open bracket
                    indexOB = i
                    
                    # check if loop should not be executed
                    if memory[pointer] == 0:
                        jumptoCB = True

                elif char == "]":
                    # jump to last open bracket
                    # -1 because we are going to +1 straight after
                    i = indexOB - 1

                i += 1


            end_time = time()

            # print currentprint, memory
            print(f"\nOutput:\n{currentprint}\n\nInterpreted in {(end_time-start_time)*1000} ms")
            input()
            exit()
        
        # config
        elif userinput == 2:
            def config():
                global memorysize
                
                system("clear")
                print(title)

                print(f"PARAMETERS:\n1. Memory Size: {memorysize}")

                print("\nType the parameter number followed by a dot, space, and then the value")
                print("Type 'BACK' to go back to mainmenu")
                userinput = input(">>>  ")
                if userinput == "BACK":
                    mainmenu()
                else:
                    userinput = userinput.split(". ")
                    
                    if int(userinput[0]) == 1:
                        memorysize = int(userinput[1])

                config()
            
            config()

    mainmenu()


if __name__ == "__main__":
    main()