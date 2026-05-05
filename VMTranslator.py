import sys
import os
import Parser

file_name, file_extension = os.path.splitext(sys.argv[1])
#print(file_name)
in_file = file_name + ".vm"
out_file = file_name + ".asm"

if file_extension == "":
    for file in os.listdir(f"./{file_name}"):
        if file.endswith(".vm"):
            print(file)
            file = file.split(".")[0]
            with open(f"./{file_name}/{file}.vm", "r", encoding="utf-8", newline='') as input_file:
                #inputFile = input_file.read()
                #print(inputFile)
                asmCode = Parser.tester(input_file, file_name, file)
                #print("HERE WE ARE!")
                #print("\n".join(asmCode))


            with open(f"./{file_name}/{file_name}.asm", "a") as output_file:
                output_file.write("\n".join(asmCode))
else:
    with open(in_file, "r", encoding="utf-8", newline='') as input_file:
        #inputFile = input_file.read()
        #print(inputFile)
        asmCode = Parser.tester(input_file, file_name)
        #print("HERE WE ARE!")
        #print("\n".join(asmCode))


    with open(out_file, "a") as output_file:
        output_file.write("\n".join(asmCode))