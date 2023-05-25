# split_bam_by_chromosomes
The BAM File Splitter is a bash script that splits a BAM (Binary Alignment/Map) file into separate BAM files based on the chromosomes present in the input file. This can be useful when you want to analyze or process reads from a specific chromosome separately.

Prerequisites
Before running the script, ensure that you have the following dependencies installed:

samtools: A suite of programs for interacting with high-throughput sequencing data in SAM/BAM format.

Usage:----

bash split_bam_by_chromosomes.sh <input_bam>
Replace <input_bam> with the path to the BAM file you want to split. The script will generate separate BAM files for each chromosome present in the input file.

Output

The script creates one BAM file per chromosome, named <chromosome>.bam, where <chromosome> represents the name of the chromosome in the input file. Each output BAM file contains reads that align to the corresponding chromosome.


Example

Suppose you have a BAM file named sample.bam containing reads from multiple chromosomes. To split the file, run the following command:


bash bam_file_splitter.sh sample.bam


The script will generate separate BAM files for each chromosome, such as chr1.bam, chr2.bam, etc.
