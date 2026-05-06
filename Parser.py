import CodeWriter

def tester(input_file, file_name, class_name, counter_arithmetic, counter_call): #FIXME classname isn't used when translating single file

    asmCodeOut = []
    
    if counter_arithmetic == 0 and counter_call == 0:
        (asmCode, returned_call_counter) = CodeWriter.writeBoot(counter_call)
        asmCodeOut.extend(asmCode)
        counter_call = returned_call_counter
    
    for line in input_file:
        accepted_command = ["C_PUSH","C_POP", "C_FUNCTION", "C_CALL"]
        line = line.split("//")[0]
        words = line.strip().split()
        command_type = commandType(words)

        first_argument = arg1(words)
        
        if command_type in accepted_command:
            second_argument = arg2(words)

        if command_type == "C_ARITHMETIC":
            (asmCode, returned_counter) = CodeWriter.writeArithmetic(words[0], counter_arithmetic)
            asmCodeOut.extend(asmCode)
            counter_arithmetic = returned_counter

        if command_type in ["C_PUSH","C_POP"]:
            asmCode = CodeWriter.writePushPop(command_type, first_argument, second_argument, file_name, class_name)
            asmCodeOut.extend(asmCode)

        if command_type == "LABEL":
            asmCode = CodeWriter.writeLabel(words[1])
            asmCodeOut.extend(asmCode)

        if command_type == "GOTO":
            asmCode = CodeWriter.writeGoto(words[1])
            asmCodeOut.extend(asmCode)
    
        if command_type == "IF-GOTO":
            asmCode = CodeWriter.writeIfGoto(words[1])
            asmCodeOut.extend(asmCode)

        if command_type == "C_CALL":
            (asmCode, returned_call_counter) = CodeWriter.writeCall(first_argument, second_argument, counter_call)
            asmCodeOut.extend(asmCode)
            counter_call = returned_call_counter

        if command_type == "C_FUNCTION":
            asmCode = CodeWriter.writeFunction(first_argument, second_argument )
            asmCodeOut.extend(asmCode)

        if command_type == "RETURN":
            asmCode = CodeWriter.writeReturn()
            asmCodeOut.extend(asmCode)

    return asmCodeOut, counter_arithmetic, counter_call

def commandType(command):
    
    arithmetic_commands= ["add","sub","neg", "eq", "gt", "lt", "and", "or", "not"]
    
    if len(command) == 1 and command[0] in arithmetic_commands:
        return "C_ARITHMETIC"
    
    elif len(command) == 1 and command[0] == "return":
        return "RETURN"

    elif len(command) ==2:
        if command[0] == "label":
            return "LABEL"
        elif command[0] == "goto":
            return "GOTO"
        elif command[0] == "if-goto":
            return "IF-GOTO"
        elif command[0] == "call":
            return "C_CALL"

    elif len(command) == 3:
        if command[0] == "push":
            return "C_PUSH"
        elif command[0] == "pop":
            return "C_POP"
        elif command[0] == "call":
            return "C_CALL"
        elif command[0] == "function":
            return "C_FUNCTION"

def arg1(word):
    if len(word) == 1:
        return word[0]
    elif len(word) == 3:
        return word[1]


def arg2(word):
    return word[2]