def increase_counter(counter):
    counter += 1
    print("INC_COUNTER", counter)
    return counter
    

def writeArithmetic(command, counter):
    print(f"ARITHMETIC: {command}")
    
    asmCodeArithmetic = []
    true_label = f"TRUE_{counter}"
    false_label = f"FALSE_{counter}"
    continue_label = f"CONTINUE_{counter}"
    
    def append_to_asm_aritchmetic(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCodeArithmetic.append(result)
    
    match command:
        case "add":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(addSPPointerToD)
            append_to_asm_aritchmetic(loadDToPointer, "SP")
            append_to_asm_aritchmetic(increaseSP)
            
        case "sub":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(loadDToPointer, "SP")
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
            append_to_asm_aritchmetic(loadDToPointer, "SP")
            append_to_asm_aritchmetic(increaseSP)

        case "or":
            asmCodeArithmetic.append(f"//{command}")
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(orOP)
            append_to_asm_aritchmetic(loadDToPointer, "SP")
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
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)
            
            case "local":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "LCL")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)
            
            case "argument":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "ARG")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)

            case "this":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "THIS")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)

            case "that":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "THAT")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)

            case "temp":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(getConstantToD, 5)
                append_to_asm_push_pop(addConstantPlusD, index)
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(popRandom)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)
            
            case "pointer":
                asmCodePushPop.append(f"//push {segment} {index}")
                thisOrThat = "THIS" if index == "0" else "THAT"
                
                append_to_asm_push_pop(popThisThatToD, thisOrThat)
                append_to_asm_push_pop(loadDToPointer, "SP")
                append_to_asm_push_pop(increaseSP)
                
            case "static":
                asmCodePushPop.append(f"//push {segment} {index}")
                append_to_asm_push_pop(popStaticToD, file_name, index)
                append_to_asm_push_pop(loadMintoD)
                append_to_asm_push_pop(loadDToPointer, "SP")
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

            case "this":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "THIS")
                append_to_asm_push_pop(storeDinRandom)
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(pushDToRandom)

            case "that":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(DPlusSegmentValue, "THAT")
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
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(popThisThatToM,thisOrThat)
        
            case "static":
                asmCodePushPop.append(f"//pop {segment} {index}")
                append_to_asm_push_pop(reduceSP)
                append_to_asm_push_pop(popSP)
                append_to_asm_push_pop(popStaticToD, file_name, index)
                append_to_asm_push_pop(loadDintoM)


        return asmCodePushPop    

def writeLabel(command):
    asmLabel = []

    label = f"({command.upper()})"
    asmLabel.append(f"//label {command}")
    asmLabel.append(label)

    return asmLabel

def writeGoto(label):
    asmGoto = []
    asmGoto.append(f"//goto {label}")
    asmGoto.append(f"@{label}\n0;JMP")
    return asmGoto

def writeIfGoto(label):
    asmIfGoto = []

    def append_to_asm_ifGoto(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmIfGoto.append(result)

    asmIfGoto.append(f"//if-goto {label}")
    append_to_asm_ifGoto(reduceSP)
    append_to_asm_ifGoto(popSP)
    append_to_asm_ifGoto(gotoLabel, label)

    return asmIfGoto


def writeCall(funcName, argNum, counter):
    asmCallFunc = []

    def append_to_asm_callFunc(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCallFunc.append(result)
        
    asmCallFunc.append(f"//call {funcName} {argNum}")
    counter = increase_counter(counter)
    append_to_asm_callFunc(generateLabel, funcName, counter)
    append_to_asm_callFunc(assignAtoD)
    append_to_asm_callFunc(loadDToPointer, "SP")
    append_to_asm_callFunc(increaseSP)
    append_to_asm_callFunc(storeIndexInSP, "LCL")
    append_to_asm_callFunc(storeIndexInSP, "ARG")
    append_to_asm_callFunc(storeIndexInSP, "THIS")
    append_to_asm_callFunc(storeIndexInSP, "THAT")
    append_to_asm_callFunc(readIndex, "SP")
    append_to_asm_callFunc(subtractXfromD, "5")
    append_to_asm_callFunc(subtractXfromD, argNum)
    append_to_asm_callFunc(pushDtoIndex, "ARG")
    append_to_asm_callFunc(readIndex, "SP")
    append_to_asm_callFunc(pushDtoIndex, "LCL")
    append_to_asm_callFunc(gotoFunction, funcName)


    return (asmCallFunc, counter)


def writeFunction(funcName, argNum):
    #print(funcName, argNum)
    asmFunc = []

    def append_to_asm_Func(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmFunc.append(result)
        
    asmFunc.append(f"// function {funcName} {argNum}")       
    append_to_asm_Func(declareContinue, funcName)
    for arg in range(int(argNum)):
        append_to_asm_Func(getConstantToD, 0)
        append_to_asm_Func(loadDToPointer, "SP")
        append_to_asm_Func(increaseSP)

    return asmFunc


def writeReturn():
    asmReturn = []

    def append_to_asm_Return(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmReturn.append(result)

    asmReturn.append("// return")
    append_to_asm_Return(readIndex, "LCL")
    append_to_asm_Return(pushDtoIndex, "R13")
    #append_to_asm_Return(loadAddressToD, "R13")
    append_to_asm_Return(subtractXfromD, "5")
    append_to_asm_Return(subtractValueToD)

    append_to_asm_Return(pushDtoIndex, "R14")
    append_to_asm_Return(reduceSP)
    append_to_asm_Return(popSP)


    append_to_asm_Return(loadDToPointer, "ARG")
    append_to_asm_Return(pushIndexPlusOnetoD, "ARG")
    
    append_to_asm_Return(pushDtoIndex, "SP")
    append_to_asm_Return(readIndex, "R13")
    append_to_asm_Return(subtractXfromD, "1")
    append_to_asm_Return(subtractValueToD)


    append_to_asm_Return(pushDtoIndex, "THAT")
    append_to_asm_Return(readIndex, "R13")
    append_to_asm_Return(subtractXfromD, "2")
    append_to_asm_Return(subtractValueToD)

    
    append_to_asm_Return(pushDtoIndex, "THIS")
    append_to_asm_Return(readIndex, "R13")
    append_to_asm_Return(subtractXfromD, "3")
    append_to_asm_Return(subtractValueToD)
    
    append_to_asm_Return(pushDtoIndex, "ARG")
    append_to_asm_Return(readIndex, "R13")
    append_to_asm_Return(subtractXfromD, "4")
    append_to_asm_Return(subtractValueToD)

    append_to_asm_Return(pushDtoIndex, "LCL")
    append_to_asm_Return(jumpToTempAddress)
    
    return asmReturn


def writeBoot():
    asmBoot = []

    def append_to_asm_Boot(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmBoot.append(result)

    asmBoot.append("//set SP = 256")
    append_to_asm_Boot(getConstantToD, "256")
    append_to_asm_Boot(pushDtoIndex, "SP")
    asmBoot.append("//call Sys.init")
    append_to_asm_Boot(generateLabel, "Sys.init", "1")
    append_to_asm_Boot(assignAtoD)
    append_to_asm_Boot(loadDToPointer, "SP")
    append_to_asm_Boot(increaseSP)
    append_to_asm_Boot(storeIndexInSP, "LCL")
    append_to_asm_Boot(storeIndexInSP, "ARG")
    append_to_asm_Boot(storeIndexInSP, "THIS")
    append_to_asm_Boot(storeIndexInSP, "THAT")
    append_to_asm_Boot(readIndex, "SP")
    append_to_asm_Boot(subtractXfromD, "5")
    append_to_asm_Boot(pushDtoIndex, "ARG")
    append_to_asm_Boot(readIndex, "SP")
    append_to_asm_Boot(pushDtoIndex, "LCL")
    append_to_asm_Boot(gotoFunction, "Sys.init")

    return asmBoot


####################
#AUXILIARY FUNCTIONS
def reduceSP():
    return """@SP\nM=M-1"""

def popSP():
    return """@SP\nA=M\nD=M"""

def popThisThatToM(thisthat):
    return f"@{thisthat}\nM=D"

def popThisThatToD(thisthat):
    return f"@{thisthat}\nD=M"

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

def loadDToPointer(index):
    return f"@{index}\nA=M\nM=D"

def goEnd():
    return """@END\n0;JMP"""

def orOP():
    return """@SP\nA=M\nD=D|M"""

def notOP():
    return """D=M\nD=!D"""

def declareContinue(label):
    return f"({label})"

def getConstantToD(index):
    return f"@{index}\nD=A"

def DPlusSegmentValue(segment):
    return f"@{segment}\nD=D+M"

def storeDinRandom():
    return """@R13\nM=D"""

def popRandom():
    return """@R13\nA=M\nD=M"""

def addConstantPlusD(index):
    return f"@{index}\nD=D+A"

def declarPointerSegment(pointer):
    return f"@{pointer}"

def popStaticToD(file_name, index):
    return f"@{file_name}.{index}"

def pushDToRandom():
    return """@R13\nA=M\nM=D"""

def gotoLabel(label):
    return f"@{label}\nD;JNE"

def generateLabel(functionName, counter):
    return f"@{functionName}$ret.{counter}"

def assignAtoD():
    return "D=A"

def storeIndexInSP(index):
    return f"@{index}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"

def subtractXfromD(value):
    return f"@{value}\nD=D-A"

def pushDtoIndex(index):
    return f"@{index}\nM=D"

def loadAddressToD(index):
    return f"@{index}\nA=M\nD=A"

def gotoFunction(label):
    return f"@{label}\n0;JMP"

def subtractValueToD():
    return "A=D\nD=M"

def pushIndexPlusOnetoD(label):
    return f"@{label}\nD=M+1"

def jumpToTempAddress():
    return "@R14\nA=M\n0;JMP"

def readIndex(index):
    return f"@{index}\nD=M"