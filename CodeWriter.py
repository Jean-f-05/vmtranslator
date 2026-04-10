def writeArithmetic(command, counter):
    print(f"ARITHMETIC: {command}")
    
    asmCodeArithmetic = []
    true_label = f"TRUE_{counter}"
    false_label = f"FALSE_{counter}"
    continue_label = f"CONTINUE_{counter}"
    
    def append_to_asm_aritchmetic(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCodeArithmetic.append(result)

    def increase_counter(counter):
        counter += 1
        return counter

    
    match command:
        case "add":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(addSPPointerToD)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)
            
        case "sub":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)

        case "neg":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadMintoD)
            append_to_asm_aritchmetic(negateOP)
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadDintoM)
        
        case "eq":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)  
            append_to_asm_aritchmetic(popSP)  
            append_to_asm_aritchmetic(reduceSP)  
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode,f"@{true_label}\nD;JEQ\n@{false_label}\nD;JNE")
            append_to_asm_aritchmetic(jumpTrueFalse,true_label,"1", continue_label)
            append_to_asm_aritchmetic(jumpFalse,false_label,"0", continue_label)
            append_to_asm_aritchmetic(declareContinue, continue_label)
            counter = increase_counter(counter)

        case "gt": 
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode, f"@{true_label}\nD;JGT\n@{false_label}\nD;JLE")
            append_to_asm_aritchmetic(jumpTrueFalse, true_label,"1", continue_label)
            append_to_asm_aritchmetic(jumpFalse, false_label,"0", continue_label)
            append_to_asm_aritchmetic(declareContinue, continue_label)
            counter = increase_counter(counter)
            
        case "lt":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode,f"@{true_label}\nD;JLT\n@{false_label}\nD;JGE")
            append_to_asm_aritchmetic(jumpTrueFalse,true_label,"1", continue_label)
            append_to_asm_aritchmetic(jumpFalse,false_label,"0", continue_label)
            append_to_asm_aritchmetic(declareContinue, continue_label)
            counter = increase_counter(counter)
            
        case "and":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(andOP)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)

        case "or":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(orOP)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)

        case "not":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(notOP)
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadDintoM)
            
        case _:
            print("ERROR IN CASE")    
                
    return (asmCodeArithmetic, counter)


def writePushPop(command, segment, index, file_name):
    print(f"PUSH/POP: {command, segment, index, file_name}")
    
    asmCodePushPop = []
    
    def append_to_asm_push_pop(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCodePushPop.append(result)

    if command == "C_PUSH":
        match segment:
            case "constant":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)
            
            case "local":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "LCL")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)
            
            case "argument":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "ARG")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)

            case "temp":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, 5)
                append_to_asm_push_pop(addConstantPlusD, index)
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)

            case "pointer":
                asmCodePushPop.append(f"//push {segment} {index}")
                thisOrThat = "THIS" if index == "0" else "THAT"
                
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(declarPointerSegment, thisOrThat)
                append_to_asm_push_pop(loadMintoD)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)
                
            case "static":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(popStaticToD, file_name, index)
                append_to_asm_push_pop(loadMintoD)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)

        return asmCodePushPop    
    
    
    elif command == "C_POP":
        match segment:
            case "local":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "LCL")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(pushDToRandom)
            
            case "argument":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "ARG")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(pushDToRandom)

            case "temp":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(getConstantToD, "5")
                append_to_asm_push_pop(addConstantPlusD, index)
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(pushDToRandom)

            case "pointer":

                asmCodePushPop.append(f"//pop {segment} {index}")
                thisOrThat = "THIS" if index == "0" else "THAT"
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(declarPointerSegment, thisOrThat)
                append_to_asm_push_pop(loadMintoD)
                append_to_asm_push_pop(loadDToSP)
        
            case "static":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(popStaticToD, file_name, index)
                append_to_asm_push_pop(loadDintoM)


        return asmCodePushPop    
    
    
####################
#AUXILIARY FUNCTIONS
def reduceSP():
    return """@SP\nM=M-1"""

def popSP():
    return """@SP\nA=M\nD=M"""

def addSPPointerToD():
    return """@SP\nA=M\nD=D+M"""

def increaseSP():
    return """@SP\nM=M+1"""

def subSPPointerToD():
    return """@SP\nA=M\nD=M-D"""

def tempReduceSP():
    return """@SP\nA=M-1"""

def loadMintoD():
    return """D=M"""

def negateOP():
    return """D=!D\nD=D+1"""

def loadDintoM():
    return """M=D"""

def returnAsmCode(asmString):
    return asmString

def jumpTrueFalse(name, value, label):
    return f"({name})\n@{value}\nD=A\nD=-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@{label}\n0;JMP"

def jumpFalse(name, value, label):
    return f"({name})\n@{value}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@{label}\n0;JMP"

def declareEnd():
    return """(END)\n@END\n0;JMP"""

def andOP():
    return """@SP\nA=M\nD=D&M"""

def loadDToSP():
    return """@SP\nA=M\nM=D"""

def goEnd():
    return """@END\n0;JMP"""

def orOP():
    return """@SP\nA=M\nD=D|M"""

def notOP():
    return """D=M\nD=!D"""

def declareContinue(label):
    return f"({label})\n"

def getConstantToD(index):
    return f"@{index}\nD=A"

def DPlusSegmentValue(segment):
    return f"@{segment}\nD=D+M"

def storeDinRandom():
    return """@random\nM=D"""

def popRandom():
    return """@random\nA=M\nD=M"""

def addConstantPlusD(index):
    return f"@{index}\nD=D+A"

def declarPointerSegment(pointer):
    return f"@{pointer}"

def popStaticToD(file_name, index):
    return f"@{file_name}.{index}"

def pushDToRandom():
    return """@random\nA=M\nM=D"""