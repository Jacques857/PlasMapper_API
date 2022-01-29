from multiprocessing import parent_process
import os
from Utility import Utility
from Bio.Blast.Applications import NcbiblastnCommandline

class FSDSearch:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.program = Utility.getEnvValue("BLAST_PATH")
        self.database = Utility.getEnvValue("FEATURE_DB")

        self.doBlast()

    # Perform a BLAST search against self.database. Output to self.outputFile
    def doBlast(self):
        try:
            # outfmt = 6 -> tabular alignment view
            # dust = no -> no query sequence filtering with DUST
            # soft_masking = False -> no filtering location applied
            command = NcbiblastnCommandline(cmd = self.program, db = self.database, query = self.inputFile, out = self.outputFile, outfmt = 6, dust = "no", soft_masking = False)
            print(command)
            command()
        except Exception as e:
            print(e)

    def getHitFeatures(self):
        pass

#Testing Script
#f = FSDSearch(os.getcwd() + "\\temp\\input1_1642245434580.txt", os.getcwd() + "\\temp\\output1_1642245434580.txt")