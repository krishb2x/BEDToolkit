import os
import sys
import statistics

def print_help():
    print("Usage:                 python3.9 Dragencovstats.py <function_name> </path/to/the/BED_file>")
    print("bed_overlap_remover:   It removes lines that have overlapping ranges within the same chromosome and exome.")
    print(":        ")
    print("")
    print("Script by Krishna Vaibhav Tiwari")

def bed_overlap_remover(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        bed_data = {}
        line_number = 0
        for line in f_in:
            line_number += 1
            fields = line.strip().split('\t')
            line_chromosome = fields[0]
            line_exome = fields[3]
            line_start = int(fields[1])
            line_end = int(fields[2])
            if line_chromosome in bed_data and line_exome in bed_data[line_chromosome]:
                overlaps = False
                for start, end in bed_data[line_chromosome][line_exome]:
                    if start <= line_end and line_start <= end:
                        overlaps = True
                        break
                if not overlaps:
                    bed_data[line_chromosome][line_exome].append((line_start, line_end))
                    f_out.write(line)
                else:
                    print(f"Line {line_number} removed: Overlapping range found: {line.strip()}")
            else:
                bed_data.setdefault(line_chromosome, {})
                bed_data[line_chromosome].setdefault(line_exome, [(line_start, line_end)])
                f_out.write(line)
    print("BED file processing complete")
def BedStats(input_file):
    exomes_by_chromosome = {}
    total_exomes = set()
    total_lines = 0
    total_interval_length = 0
    max_interval_length = 0
    min_interval_length = float('inf')
    total_chromosomes = 0
    total_exome_coverage = 0

    with open(input_file, 'r') as f:
        for line in f:
            total_lines += 1
            fields = line.strip().split('\t')
            chromosome = fields[0]
            exome = fields[3]
            start = int(fields[1])
            end = int(fields[2])

            if chromosome not in exomes_by_chromosome:
                exomes_by_chromosome[chromosome] = []
                total_chromosomes += 1

            if exome not in exomes_by_chromosome[chromosome]:
                exomes_by_chromosome[chromosome].append(exome)
                total_exomes.add(exome)

            interval_length = end - start
            total_interval_length += interval_length
            max_interval_length = max(max_interval_length, interval_length)
            min_interval_length = min(min_interval_length, interval_length)
            total_exome_coverage += interval_length

    print("Statistics for BED file:")
    print("========================")
    print(f"Total lines in the BED file: {total_lines}")
    print(f"Total unique exome entries overall: {len(total_exomes)}")
    print(f"Total number of chromosomes: {total_chromosomes}")
    print(f"Average interval length in the BED file: {total_interval_length / total_lines:.2f}")
    print(f"Maximum interval length in the BED file: {max_interval_length}")
    print(f"Minimum interval length in the BED file: {min_interval_length}")
    print(f"Total exome coverage: {total_exome_coverage} bp")
    print("")

    for chromosome, exomes in exomes_by_chromosome.items():
        percentage = (len(exomes) / len(total_exomes)) * 100
        unique_exomes_per_chromosome = len(exomes)
        average_exome_coverage_per_chromosome = sum(len(exome) for exome in exomes) / len(exomes)
        
        print(f"Chromosome {chromosome}:")
        print(f"Total unique exome entries: {unique_exomes_per_chromosome}")
        print(f"Percentage of unique exomes: {percentage:.2f}%")
        print(f"Average exome coverage: {average_exome_coverage_per_chromosome:.2f} bp")
        print("")

    print("========================")
    print("Statistics calculation complete")


def function_name3(input_file):
    # Implementation of function_name3 function
    pass

def main():
    if len(sys.argv) != 3 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        sys.exit()

    function_name = sys.argv[1]
    input_file = sys.argv[2]
    
    output_file = function_name + "_results.txt"
    output_file_path = os.path.join(os.getcwd(), output_file)
    sys.stdout = open(output_file_path, 'w')
    
    if function_name == 'bed_overlap_remover':
        input_dir = os.path.dirname(input_file)
        output_file = os.path.join(input_dir, "output_file.bed")
        bed_overlap_remover(input_file, output_file)
    elif function_name == 'BedStats':
        BedStats(input_file)
    elif function_name == 'function_name3':
        function_name3(input_file)
    else:
        print(f"Unknown function: {function_name}")

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    # Close the output file
    #stdout.close()
    sys.stdout.close()

if __name__ == "__main__":
    main()
