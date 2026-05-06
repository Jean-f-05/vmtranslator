import sys
import os
import Parser

file_name, file_extension = os.path.splitext(sys.argv[1])
in_file = file_name + ".vm"
out_file = file_name + ".asm"


if file_extension == "":
    counter_arithmetic = 0
    counter_call = 0
    for file in os.listdir(f"./{file_name}"):
        if file.endswith(".vm"):
            file = file.split(".")[0]
            with open(f"./{file_name}/{file}.vm", "r", encoding="utf-8", newline='') as input_file:
                asmCode, counter_arithmetic, counter_call = Parser.tester(input_file, file_name, file, counter_arithmetic, counter_call)

            with open(f"./{file_name}/{file_name}.asm", "a") as output_file:
                output_file.write("\n".join(asmCode))
else:
    counter_arithmetic = 0
    counter_call = 0
    with open(in_file, "r", encoding="utf-8", newline='') as input_file:
        asmCode, counter_arithmetic, counter_call  = Parser.tester(input_file, file_name, file_name, counter_arithmetic, counter_call)

    with open(out_file, "a") as output_file:
        output_file.write("\n".join(asmCode))