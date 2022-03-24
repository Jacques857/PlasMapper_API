import os
import re
from .Utility import Utility
from .Feature import Feature
from Bio.Blast.Applications import NcbiblastnCommandline

class FSDSearch:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.program = Utility.getEnvValue("BLAST_PATH")
        self.database = Utility.getEnvValue("FEATURE_DB")
        self.promoters = []
        self.terminators = []
        self.regulatorySequences = []
        self.replicationOrigins = []
        self.selectableMarkers = []
        self.reporterGenes = []
        self.affinityTags = []
        self.localizationSequences = []
        self.twoHybridGenes = []
        self.genes = []
        self.primers = []
        self.misc = []

        self.doBlast()
        self.curateFeatures()

    # Perform a BLAST search against self.database. Output to self.outputFile
    def doBlast(self):
        try:
            # outfmt = 6 -> tabular alignment view
            # dust = no -> no query sequence filtering with DUST
            # soft_masking = False -> no filtering location applied
            command = NcbiblastnCommandline(cmd = self.program, db = self.database, query = self.inputFile, out = self.outputFile, outfmt = 6, dust = "no", soft_masking = False, word_size = 12)
            command()
        except Exception as e:
            print(e)

    # Parse the outputFile to fill feature lists with curated features (self.promoters, self.terminators, etc.)
    def curateFeatures(self):
        file = open(self.outputFile, 'r')
        hits = file.readlines() # this represents the hits from BLAST
        lengthCutoff1 = 100 # defines the upper limit of the first length bracket
        lengthCutoff2 = 500 # defines the upper limit of the second length bracket
        alignCutoff1 = 1 # defines the minimum proportion of alignLength/length necessary in the first length bracket
        alignCutoff2 = 0.95 # defines the minimum proportion of alignLength/length necessary in the second length bracket
        alignCutoff3 = 0.90 # defines the minimum proportion of alignLength/length necessary in the third length bracket
        identityCutoff1 = 95 # defines the identity cutoff for the first bracket
        identityCutoff2 = 95 # defines the identity cutoff for the second bracket
        identityCutoff3 = 95 # defines the identity cutoff for the third bracket

        # parse the outputFile
        for hit in hits:
            # parse the outputFile
            # tokenList is formatted as follows:
            # [queryId, subjectId, featureType, featureLegend, length, identity, alignLength, mismatches, gapOpenings, qAlignStart, qAlignStop, sAlignStart, sAlignStop, eValue, bitScore]
            tokenList = re.split('\t|\r|\f|\[|\]\{|\},', hit.strip())
            name = tokenList[1]
            featureType = tokenList[2]
            featureLegend = tokenList[3]
            length = tokenList[4]
            identity = tokenList[5]
            alignLength = tokenList[6]
            qAlignStart = tokenList[9]
            qAlignStop = tokenList[10]

            # convert numbers to int
            length = int(length)
            identity = float(identity)
            alignLength = int(alignLength)
            qAlignStart = int(qAlignStart)
            qAlignStop = int(qAlignStop)

            # only add curated features
            if length <= lengthCutoff1:
                if alignLength == (alignCutoff1 * length) and identity >= identityCutoff1:
                    self.addFeature(name, qAlignStart, qAlignStop, featureType, featureLegend)
            elif length > lengthCutoff1 and length <= lengthCutoff2:
                if alignLength > (alignCutoff2 * length) and identity >= identityCutoff2:
                    self.addFeature(name, qAlignStart, qAlignStop, featureType, featureLegend)
            else:
                if alignLength > (alignCutoff3 * length) and identity >= identityCutoff3:
                    self.addFeature(name, qAlignStart, qAlignStop, featureType, featureLegend)

    # Create a new Feature object and add it to the appropriate feature list
    def addFeature(self, name, start, stop, featureType, featureLegend):
        # sort the feature into the appropriate feature list
        if featureType == "PRO":
            self.promoters.append(Feature(name, start, stop, featureLegend))
        elif featureType == "TER":
            self.terminators.append(Feature(name, start, stop, featureLegend))
        elif featureType == "REG":
            self.regulatorySequences.append(Feature(name, start, stop, featureLegend))
        elif featureType == "ORI":
            self.replicationOrigins.append(Feature(name, start, stop, featureLegend))
        elif featureType == "SEL":
            self.selectableMarkers.append(Feature(name, start, stop, featureLegend))
        elif featureType == "REP":
            self.reporterGenes.append(Feature(name, start, stop, featureLegend))
        elif featureType == "TAG":
            self.affinityTags.append(Feature(name, start, stop, featureLegend))
        elif featureType == "LOC":
            self.localizationSequences.append(Feature(name, start, stop, featureLegend))
        elif featureType == "HYB":
            self.twoHybridGenes.append(Feature(name, start, stop, featureLegend))
        elif featureType == "GEN":
            self.genes.append(Feature(name, start, stop, featureLegend))
        elif featureType == "PRI":
            self.primers.append(Feature(name, start, stop, featureLegend))
        elif featureType == "OTH":
            self.misc.append(Feature(name, start, stop, featureLegend))

#Testing Script
"""f = FSDSearch(os.getcwd() + "\\temp\\input.txt", os.getcwd() + "\\temp\\output.txt")
print("promoters:", f.promoters)
print("terminators:", f.terminators)
print("regulatorySequences:", f.regulatorySequences)
print("replicationOrigins:", f.replicationOrigins)
print("selectableMarkers:", f.selectableMarkers)
print("reporterGenes:", f.reporterGenes)
print("affinityTags:", f.affinityTags)
print("localizationSequences:", f.localizationSequences)
print("twoHybridGenes:", f.twoHybridGenes)
print("genes:", f.genes)
print("primers:", f.primers)
print("misc:", f.misc)"""
