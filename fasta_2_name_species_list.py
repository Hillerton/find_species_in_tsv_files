"""
script that aims to take a number of fasta files, get name and species (file name) from the fasta 
and then print this to a file in format "name \t species". 
Appends to the outfile to merge large number of fastas. 
Take a input directory and a output file
"""

import sys
import os
from os import listdir 
import argparse

#sub function that takes a table contaning species and file names allowing the outfile to contain actuall names instead of codes.
#file for this should be in tab format with code in first and name in last column 
def translation_table(table):
    return_dict = dict()

    with open(table, "r") as read:
        for line in read:
            line = line.rstrip()
            hold = line.split("\t")
            
            name = hold[0]
            name = name.split(" ")[0:2]
            name = "_".join(name)
            
            if " " in name:
                name = name.replace(" ", "_")

                return_dict[name] = hold[-1]+"\t"+hold[1]
            
    return (return_dict)

            
parser = argparse.ArgumentParser(
     description = "tool to get names and origin from fasta format. Can also be used to change codified file names to species with a table input"
)   
parser.add_argument("indir", action="store", help="Indir contaning all fasta files to be converted and merged. OBS fasta files will not be changed")
parser.add_argument("out", action="store", help="File to which the name,species data should be appended to")
parser.add_argument("-t", dest="trans", action="store", default=False, help="Give a table contaning wanted name and current name in tab list, current name must be col 0 and wanted must be col -1")

args = parser.parse_args()

indir = args.indir
outfile = args.out
translate = args.trans


if not os.path.isdir(indir):
    print (indir, "is not a directory")
    exit()

if translate:
    trans_table = translation_table(translate)

   
files=listdir(indir)

writer = open(outfile, "a+")


for f in files:

    filename = f.split("\/")[-1]
    sname = filename.split(".")[0]

    if translate:
        species = trans_table[sname]
    else:
        species = sname
    
    reader = open(indir+"/"+f, "r")
    for line in reader:
        if line[0] == ">":
            protid = line.split(" ")[0]

            if "|" in protid:
                protid = protid.split("|")[1]

            species=species.rstrip()
            protid = protid.rstrip()
            writer.write(protid+"\t"+species+"\n")

writer.close()
