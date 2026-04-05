def writeArithmetic(command):
    #print(f"ARITHMETIC: {command}")
    
    asmCodeArithmetic = []
    
    def append_to_asm_aritchmetic(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCodeArithmetic.append(result)


    match command:
        case "add":
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(addSPPointerToD)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(increaseSP)
            
        case "sub":
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(increaseSP)

        case "neg":
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadMintoD)
            append_to_asm_aritchmetic(negateOP)
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadDintoM)
        
        case "eq":
            append_to_asm_aritchmetic(reduceSP)  
            append_to_asm_aritchmetic(popSP)  
            append_to_asm_aritchmetic(reduceSP)  
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode,"@TRUE\nD;JEQ\n@FALSE\nD;JNE")
            append_to_asm_aritchmetic(jumpTrueFalse,"TRUE","1")
            append_to_asm_aritchmetic(jumpTrueFalse,"FALSE","0")
            append_to_asm_aritchmetic(declareContinue)

        case "gt": 
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode, "@TRUE\nD;JGT\n@FALSE\nD;JLE")
            append_to_asm_aritchmetic(jumpTrueFalse, "TRUE","1")
            append_to_asm_aritchmetic(jumpTrueFalse, "FALSE","0")
            append_to_asm_aritchmetic(declareContinue)

        case "lt":
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(subSPPointerToD)
            append_to_asm_aritchmetic(returnAsmCode,"@TRUE\nD;JLT\n@FALSE\nD;JGE")
            append_to_asm_aritchmetic(jumpTrueFalse,"TRUE","1")
            append_to_asm_aritchmetic(jumpTrueFalse,"FALSE","0")
            append_to_asm_aritchmetic(declareContinue)
        
        case "and":
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(andOP)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)
            #append_to_asm_aritchmetic(goEnd)
            #append_to_asm_aritchmetic(declareEnd)

        case "or":
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(popSP)
            append_to_asm_aritchmetic(reduceSP)
            append_to_asm_aritchmetic(orOP)
            append_to_asm_aritchmetic(loadDToSP)
            append_to_asm_aritchmetic(increaseSP)
            #append_to_asm_aritchmetic(goEnd)
            #append_to_asm_aritchmetic(declareEnd)

        case "not":
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(notOP)
            append_to_asm_aritchmetic(tempReduceSP)
            append_to_asm_aritchmetic(loadDintoM)
            #append_to_asm_aritchmetic(goEnd)
            #append_to_asm_aritchmetic(declareEnd)
        case _:
            print("ERROR IN CASE")    
    
         
    return asmCodeArithmetic


def writePushPop(command, segment, index):
    print(f"PUSH/POP: {command, segment, index}")
    
    asmCodePushPop = []
    
    def append_to_asm_push_pop(func, *args, **kwargs):
        result = func(*args, **kwargs)
        asmCodePushPop.append(result)

    if command == "C_PUSH":
        match segment:
            case "constant":
                append_to_asm_push_pop(getConstantToD, index)
                append_to_asm_push_pop(loadDToSP)
                append_to_asm_push_pop(increaseSP)
    
        return asmCodePushPop    
    
    
    elif command == "C_POP":
        ...
        return asmCodePushPop    
    
    
    #TODO
    
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

def jumpTrueFalse(name, value):
    return f"({name})\n@{value}\nD=A\nD=-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@CONTINUE\n0;JMP"

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

def declareContinue():
    return """(CONTINUE)\n"""

def getConstantToD(index):
    return f"@{index}\nM=A\nD=M"


