import CodeWriter

def tester(input_file):

    asmCodeOut = []

    for line in input_file:
        accepted_command = ["C_PUSH","C_POP", "C_FUNCTION", "C_CALL"]
        words = line.strip().split()
        
        command_type = commandType(words)
        #print(command_type)

        first_argument = arg1(words)
        #print(first_argument)
        
        if command_type in accepted_command:
            second_argument = arg2(words)
        #print(second_argument)

        if command_type == "C_ARITHMETIC":
            asmCode = CodeWriter.writeArithmetic(words[0])
            #TODO
            #print(asmCode) 
            asmCodeOut.extend(asmCode)
            #print("\n".join(asmCode))

        elif command_type in ["C_PUSH","C_POP"]:
            CodeWriter.writePushPop(command_type, first_argument,second_argument)
        #print(line.strip())
        #print("\n".join(line))
        #print(CodeWriter.hello())

    return asmCodeOut

def commandType(command):
    
    arithmetic_commands= ["add","sub","neg", "eq", "gt", "lt", "and", "or", "not"]
    
    if len(command) == 1 and command[0] in arithmetic_commands:
        return "C_ARITHMETIC"
    elif len(command) == 3:
        if command[0] == "push":
            return "C_PUSH"
        elif command[0] == "pop":
            return "C_POP"
    #else: 
    #    print("NONE")

def arg1(word):
    if len(word) == 1:
        return word[0]
    elif len(word) == 3:
        return word[1]


def arg2(word):
    return word[2]
    