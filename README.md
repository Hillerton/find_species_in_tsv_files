# find_species_in_tsv_files
Small project with code used to look at what species are present in a tsv tree file made from trees

The project consists of 2 execuable files (and a file with proteins and coresponding species for QFO18) 

To run the tool first get all of the fasta files that where used in whatever step was done to generate the tsv. 
An optional translation file can also be created (manually or with a seperate script) if you wish to change the species names in the fasta file
to something new. See the species_decoded.table for an example. 

Once this is done run the fasta_2_name_species_list.py tool with or without the -t option. 

python fasta_2_name_species_list.py -i dir_with_all_fasta -o file_for_all_names (-t translation file)

When this is done using the find_species.py script to generate a list of species who have proteins in the tsv file.

python find_species.py tsv_of_intrest.tsv file_for_all_names outputfile.txt

The outputfile includes a simple newline seperated list with one entery for each sepcies found as well as any species seen in the fasta files that was not found in the tsv. 
