def writeArithmetic(command):
    print(f"ARITHMETIC: {command}")
    
    asmCode = []
    
    match command:
        case "add":
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(addSPPointerToD())
            asmCode.append(popSP())
            asmCode.append(increaseSP())
            
        case "sub":
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(subSPPointerToD())
            asmCode.append(popSP())
            asmCode.append(increaseSP())

        case "neg":
            asmCode.append(tempReduceSP())
            asmCode.append(loadMintoD())
            asmCode.append(negate())
            asmCode.append(tempReduceSP())
            asmCode.append(loadDintoM())
        
        case "eq":
            asmCode.append(reduceSP())  
            asmCode.append(popSP())  
            asmCode.append(reduceSP())  
            asmCode.append(subSPPointerToD())
            asmCode.append(returnAsmCode("@TRUE\nD;JEQ\n@FALSE\nD;JNE"))
            asmCode.append(jumpTrueFale("TRUE","1"))
            asmCode.append(jumpTrueFale("FALSE","0"))
            asmCode.append(end())

        case "gt":
            ...    
        case "lt":
            ...    
        case "and":
            ...    
        case "or":
            ...    
        case "not":
            ...
        case _:
            print("ERROR IN CASE")    
    
         
    return asmCode



####################
#AUXILIARY FUNCTIONS

def writePushPop(command, segment, index):
    print(f"PUSH/POP: {command, segment, index}")
    
def reduceSP():
    return """@SP\nM=M-1"""

def popSP():
    return """@SP\nA=M\nD=M"""

def addSPPointerToD():
    return """@SP\nA=M\nD=D+M"""

def increaseSP():
    return """@SP\nM=M+1"""

def subSPPointerToD():
    return """@SP\nA=M\nD=D-M"""

def tempReduceSP():
    return """@SP\nA=M-1"""

def loadMintoD():
    return """D=M"""

def negate():
    return """D=!D\nD=D+1"""

def loadDintoM():
    return """M=D"""

def returnAsmCode(asmString):
    return asmString

def jumpTrueFale(name, value):
    return f"({name})\n@{value}\nD=A\nD=-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@END\n0;JMP"

def end():
    return """(END)\n@END\n0;JMP"""