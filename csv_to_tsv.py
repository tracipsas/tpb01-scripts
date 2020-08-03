import sys

input_file_path = sys.argv[1]
output_file_path = input_file_path.replace(".csv", ".tsv")

with open(input_file_path, "r", encoding="utf-8") as input_file:
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for line in input_file:
            output_file.write(line.replace(",", "\t"))

print("Conversion {} -> {} done".format(input_file_path, output_file_path))
