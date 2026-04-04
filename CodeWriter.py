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
            asmCode.append(negateOP())
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
            asmCode.append(declareEnd())

        case "gt": 
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(subSPPointerToD())
            asmCode.append(returnAsmCode("@TRUE\nD;JGT\n@FALSE\nD;JLE"))
            asmCode.append(jumpTrueFale("TRUE","1"))
            asmCode.append(jumpTrueFale("FALSE","0"))
            asmCode.append(declareEnd())

        case "lt":
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(subSPPointerToD())
            asmCode.append(returnAsmCode("@TRUE\nD;JLT\n@FALSE\nD;JGE"))
            asmCode.append(jumpTrueFale("TRUE","1"))
            asmCode.append(jumpTrueFale("FALSE","0"))
            asmCode.append(declareEnd())
        
        case "and":
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(andOP())
            asmCode.append(loadDToSP())
            asmCode.append(increaseSP())
            asmCode.append(goEnd())
            asmCode.append(declareEnd())
        case "or":
            asmCode.append(reduceSP())
            asmCode.append(popSP())
            asmCode.append(reduceSP())
            asmCode.append(orOP())
            asmCode.append(loadDToSP())
            asmCode.append(increaseSP())
            asmCode.append(goEnd())
            asmCode.append(declareEnd())
        case "not":
            asmCode.append(tempReduceSP())
            asmCode.append(notOP())
            asmCode.append(tempReduceSP())
            asmCode.append(loadDintoM())
            asmCode.append(goEnd())
            asmCode.append(declareEnd())
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

def negateOP():
    return """D=!D\nD=D+1"""

def loadDintoM():
    return """M=D"""

def returnAsmCode(asmString):
    return asmString

def jumpTrueFale(name, value):
    return f"({name})\n@{value}\nD=A\nD=-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@END\n0;JMP"

def declareEnd():
    return """(END)\n@END\n0;JMP"""

def andOP():
    return """@SP\nA=M\nD=D&M"""

def loadDToSP():
    return """@SP\nA=M\nM=D"""

def goEnd():
    return """@END\n0;JMP"""

def orOP():
    return """@SP\nA=M\nD=D&M"""

def notOP():
    return """D=M\nD=!D"""