from rest_framework import status
from rest_framework.test import APITestCase
import json

# pTD103luxI_sfGFP -R
plasmid1 = {
    "sequence":"ctcgagagtctataccgatgacgacgacctattgtttgtcgcaagttttgcgtgttatatatcattaaaacggtaatggattgacatttgattctaataaattggatttttgtcacactattgtatcgctgggaatacaattacttaacataagcacctgtaggatcgtacaggtttacgcaagaaaatggtttgttatagtcgaatgaattcattaaagaggagaaaggtaccatgactataatgataaaaaaatcggattttttggcaattccatcggaggagtataaaggtattctaagtcttcgttatcaagtgtttaagcaaagacttgagtgggacttagttgtagaaaataaccttgaatcagatgagtatgataactcaaatgcagaatatatttatgcttgtgatgatactgaaaatgtaagtggatgctggcgtttattacctacaacaggtgattatatgctgaaaagtgtttttcctgaattgcttggtcaacagagtgctcccaaagatcctaatatagtcgaattaagtcgttttgctgtaggtaaaaatagctcaaagataaataactctgctagtgaaattacaatgaaactatttgaagctatatataaacacgctgttagtcaaggtattacagaatatgtaacagtaacatcaacagcaatagagcgatttttaaagcgtattaaagttccttgtcatcgtattggagacaaagaaattcatgtattaggtgatactaaatcggttgtattgtctatgcctattaatgaacagtttaaaaaagcagtcttaaatgcagcgaacgacgaaaattacgcccttgcagcgtaaacgcgtgctagaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctcctgagtaggacaaatccgccgccctagaagactgtcgctacagatagttcacacctattgtttgtcgcaagttttgcgtgttatatatcattaaaacggtaatggattgacatttgattctaataaattggatttttgtcacactattgtatcgctgggaatacaattacttaacataagcacctgtaggatcgtacaggtttacgcaagaaaatggtttgttatagtcgaatgaattcattaaagaggagaaaggtaccatgagcaaaggagaagaacttttcactggagttgtcccaattcttgttgaattagatggtgatgttaatgggcacaaattttctgtccgtggagagggtgaaggtgatgctacaaacggaaaactcacccttaaatttatttgcactactggaaaactacctgttccgtggccaacacttgtcactactctgacctatggtgttcaatgcttttcccgttatccggatcacatgaaacggcatgactttttcaagagtgccatgcccgaaggttatgtacaggaacgcactatatctttcaaagatgacgggacctacaagacgcgtgctgaagtcaagtttgaaggtgatacccttgttaatcgtatcgagttaaagggtattgattttaaagaagatggaaacattcttggacacaaactcgagtacaactttaactcacacaatgtatacatcacggcagacaaacaaaagaatggaatcaaagctaacttcaaaattcgccacaacgttgaagatggttccgttcaactagcagaccattatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtcgacacaatctgtcctttcgaaagatcccaacgaaaagcgtgaccacatggtccttcttgagtttgtaactgctgctgggattacacatggcatggatgagctctacaaagcagcgaacgacgaaaattacgcccttgcagcgtgaacgcgtgctagaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctcctgagtaggacaaatccgccgccctagacctagggcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggccaggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaagatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgactagtgcttggattctcaccaataaaaaacgcccggcggcaaccgagcgttctgaacaaatccagatggagttctgaggtcattactggatctatcaacaggagtccaagcgagctctcgaaccccagagtcccgctcagaagaactcgtcaagaaggcgatagaaggcgatgcgctgcgaatcgggagcggcgataccgtaaagcacgaggaagcggtcagcccattcgccgccaagctcttcagcaatatcacgggtagccaacgctatgtcctgatagcggtccgccacacccagccggccacagtcgatgaatccagaaaagcggccattttccaccatgatattcggcaagcaggcatcgccatgggtcacgacgagatcctcgccgtcgggcatgcgcgccttgagcctggcgaacagttcggctggcgcgagcccctgatgctcttcgtccagatcatcctgatcgacaagaccggcttccatccgagtacgtgctcgctcgatgcgatgtttcgcttggtggtcgaatgggcaggtagccggatcaagcgtatgcagccgccgcattgcatcagccatgatggatactttctcggcaggagcaaggtgagatgacaggagatcctgccccggcacttcgcccaatagcagccagtcccttcccgcttcagtgacaacgtcgagcacagctgcgcaaggaacgcccgtcgtggccagccacgatagccgcgctgcctcgtcctgcagttcattcagggcaccggacaggtcggtcttgacaaaaagaaccgggcgcccctgcgctgacagccggaacacggcggcatcagagcagccgattgtctgttgtgcccagtcatagccgaatagcctctccacccaagcggccggagaacctgcgtgcaatccatcttgttcaatcatgcgaaacgatcctcatcctgtctcttgatcagatcttgatcccctgcgccatcagatccttggcggcaagaaagccatccagtttactttgcagggcttcccaaccttaccagagggcgccccagctggcaattccgacgtctaagaaaccattattatcatgacattaacctataaaaataggcgtatcacgaggccctttcgtcttcac"
}

plasmid1Output = {
    "promoters": [],
    "terminators": [],
    "regulatorySequences": [],
    "replicationOrigins": [
        {
            "name": "pBR322_origin",
            "start": 2202,
            "stop": 2821,
            "legend": "pBR322_origin"
        }
    ],
    "selectableMarkers": [
        {
            "name": "NeoR/KanR_gene",
            "start": 3021,
            "stop": 3809,
            "legend": "NeoR/KanR"
        }
    ],
    "reporterGenes": [
        {
            "name": "green_fluorescent_protein_cycle_3_variant",
            "start": 1199,
            "stop": 1912,
            "legend": "GFP_cyc3"
        }
    ],
    "affinityTags": [],
    "localizationSequences": [],
    "twoHybridGenes": [],
    "genes": [],
    "primers": [
        {
            "name": "GFP_R_primer",
            "start": 1229,
            "stop": 1257,
            "legend": "GFP_R_primer"
        }
    ],
    "misc": []
}

# pTD103aiiA(Cm) -R
plasmid2 = {
    "sequence":"ctcgagacctattgtttgtcgcaagttttgcgtgttatatatcattaaaacggtaatggattgacatttgattctaataaattggatttttgtcacactattgtatcgctgggaatacaattacttaacataagcacctgtaggatcgtacaggtttacgcaagaaaatggtttgttatagtcgaatgaattcattaaagaggagaaaggtaccatgacagtaaagaaactttatttcatcccagcaggtcgttgcatgttggatcattcgtctgttaacagtgcgttaacaccggggaaactattaaacttgccggtgtggtgttatcttttggagacggaagaaggtcctattttagtagacacaggtatgccagaaagtgcagttaataatgaagggctttttaacggtacatttgttgaaggacagatcttaccgaaaatgactgaagaagatagaatcgtgaatatattaaagcgtgtagggtatgagccggacgaccttttatatattattagttctcacttacattttgatcatgcaggaggaaacggtgcttttacaaatacaccaattattgtgcagcgaacggaatatgaggcagcacttcatagagaagaatatatgaaagaatgtatattaccgcatttgaactacaaaattattgaaggggattatgaagtggtaccaggtgttcaattattgtatacgccaggtcattctccaggccatcagtcgctattcattgagacggagcaatccggttcagttttattaacgattgatgcatcgtacacgaaagagaattttgaagatgaagtgccgttcgcaggatttgatccagaattagctttatcttcaattaaacgtttaaaagaagttgtgaaaaaagagaaaccaattattttctttggtcatgatatagagcaggaaaagagttgtagagtgttcccggaatatatagcagcgaacgacgaaaattacgcccttgcagcgtaaacgcgtgctagaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctcctgagtaggacaaatccgccgccctagacctagggatatattccgcttcctcgctcactgactcgctacgctcggtcgttcgactgcggcgagcggaaatggcttacgaacggggcggagatttcctggaagatgccaggaagatacttaacagggaagtgagagggccgcggcaaagccgtttttccataggctccgcccccctgacaagcatcacgaaatctgacgctcaaatcagtggtggcgaaacccgacaggactataaagataccaggcgtttccccctggcggctccctcgtgcgctctcctgttcctgcctttcggtttaccggtgtcattccgctgttatggccgcgtttgtctcattccacgcctgacactcagttccgggtaggcagttcgctccaagctggactgtatgcacgaaccccccgttcagtccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggaaagacatgcaaaagcaccactggcagcagccactggtaattgatttagaggagttagtcttgaagtcatgcgccggttaaggctaaactgaaaggacaagttttggtgactgcgctcctccaagccagttacctcggttcaaagagttggtagctcagagaaccttcgaaaaaccgccctgcaaggcggttttttcgttttcagagcaagagattacgcgcagaccaaaacgatctcaagaagatcatcttattaatcagataaaatatttctagatttcagtgcaatttatctcttcaaatgtagcacctgaagtcagccccatacgatataagttgttactagtgcttggattctcaccaataaaaaacgcccggcggcaaccgagcgttctgaacaaatccagatggagttctgaggtcattactggatctatcaacaggagtccaagcgagctcgatatcaaattacgccccgccctgccactcatcgcagtactgttgtaattcattaagcattctgccgacatggaagccatcacagacggcatgatgaacctgaatcgccagcggcatcagcaccttgtcgccttgcgtataatatttgcccatggtgaaaacgggggcgaagaagttgtccatattggccacgtttaaatcaaaactggtgaaactcacccagggattggctgagacgaaaaacatattctcaataaaccctttagggaaataggccaggttttcaccgtaacacgccacatcttgcgaatatatgtgtagaaactgccggaaatcgtcgtggtattcactccagagcgatgaaaacgtttcagtttgctcatggaaaacggtgtaacaagggtgaacactatcccatatcaccagctcaccgtctttcattgccatacggaattccggatgagcattcatcaggcgggcaagaatgtgaataaaggccggataaaacttgtgcttatttttctttacggtctttaaaaaggccgtaatatccagctgaacggtctggttataggtacattgagcaactgactgaaatgcctcaaaatgttctttacgatgccattgggatatatcaacggtggtatatccagtgatttttttctccattttagcttccttagctcctgaaaatctcgataactcaaaaaatacgcccggtagtgatcttatttcattatggtgaaagttggaacctcttacgtgccgatcaacgtctcattttcgccagatatcgacgtctaagaaaccattattatcatgacattaacctataaaaataggcgtatcacgaggccctttcgtcttcac"
}

plasmid2Output = {
    "promoters": [],
    "terminators": [],
    "regulatorySequences": [],
    "replicationOrigins": [],
    "selectableMarkers": [
        {
            "name": "CAT/CamR",
            "start": 2047,
            "stop": 2706,
            "legend": "CAT/CamR"
        }
    ],
    "reporterGenes": [],
    "affinityTags": [],
    "localizationSequences": [],
    "twoHybridGenes": [],
    "genes": [],
    "primers": [],
    "misc": []
}

# pCru5-/CGA-mEGFP-IRES-mCherry
plasmid3 = {
    "sequence":"tcgagtaactaactaacgaatgggcgaattcagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagtccaagctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaagttcgaataagcatgcatctagggcggccaattccgcccctctccctcccccccccctaacgttactggccgaagccgcttggaataaggccggtgtgcgtttgtctatatgtgattttccaccatattgccgtcttttggcaatgtgagggcccggaaacctggccctgtcttcttgacgagcattcctaggggtctttcccctctcgccaaaggaatgcaaggtctgttgaatgtcgtgaaggaagcagttcctctggaagcttcttgaagacaaacaacgtctgtagcgaccctttgcaggcagcggaaccccccacctggcgacaggtgcctctgcggccaaaagccacgtgtataagatacacctgcaaaggcggcacaaccccagtgccacgttgtgagttggatagttgtggaaagagtcaaatggctctcctcaagcgtattcaacaaggggctgaaggatgcccagaaggtaccccattgtatgggatctgatctggggcctcggtgcacatgctttacatgtgtttagtcgaggttaaaaaaacgtctaggccccccgaaccacggggacgtggttttcctttgaaaaacacgatgataagcttgccacaacccgggatccgccaccatggtgagcaagggcgaggaggataacatggccatcatcaaggagttcatgcgcttcaaggtgcacatggagggctccgtgaacggccacgagttcgagatcgagggcgagggcgagggccgcccctacgagggcacccagaccgccaagctgaaggtgaccaagggtggccccctgcccttcgcctgggacatcctgtcccctcagttcatgtacggctccaaggcctacgtgaagcaccccgccgacatccccgactacttgaagctgtccttccccgagggcttcaagtgggagcgcgtgatgaacttcgaggacggcggcgtggtgaccgtgacccaggactcctccctgcaggacggcgagttcatctacaaggtgaagctgcgcggcaccaacttcccctccgacggccccgtaatgcagaagaagaccatgggctgggaggcctcctccgagcggatgtaccccgaggacggcgccctgaagggcgagatcaagcagaggctgaagctgaaggacggcggccactacgacgctgaggtcaagaccacctacaaggccaagaagcccgtgcagctgcccggcgcctacaacgtcaacatcaagttggacatcacctcccacaacgaggactacaccatcgtggaacagtacgaacgcgccgagggccgccactccaccggcggcatggacgagctgtacaagtaagcggccgctcgacgataaaataaaagattttatttagtctccagaaaaaggggggaatgaaagaccccacctgtaggtttggcaagctagcttaagtaacgccattttgcaaggcatggaaaaatacataactgagaatagagaagttcagatcaaggtcaggaacagatggaacagctgaatatgggccaaacaggatatctgtggtaagcagttcctgccccggctcagggccaagaacagatggaacagctgaatatgggccaaacaggatatctgtggtaagcagttcctgccccggctcagggccaagaacagatggtccccagatgcggtccagccctcagcagtttctagagaaccatcagatgtttccagggtgccccaaggacctgaaatgaccctgtgccttatttgaactaaccaatcagttcgcttctcgcttctgttcgcgcgcttctgctccccgagctcaataaaagagcccacaacccctcactcggggcgccagtcctccgattgactgagtcgcccgggtacccgtgtatccaataaaccctcttgcagttgcatccgacttgtggtctcgctgttccttgggagggtctcctctgagtgattgactacccgtcagcgggggtctttcatttccgacttgtggtctcgctgccttgggagggtctcctctgagtgattgactacccgtcagcgggggtcttcacatgcagcatgtatcaaaattaatttggttttttttcttaagtatttacattaaatggccatagttgcattaatgaatcggccaacgcgcggggagaggcggtttgcgtattggcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggccaggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaagatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgagattatcaaaaaggatcttcacctagatccttttaaattaaaaatgaagtttgcgcaaatcaatctaaagtatatatgagtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagggcttaccatctggccccagtgctgcaatgataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttgccattgctacaggcatcgtggtgtcacgctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaacacgggataataccgcgccacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccaccagctttgctcttaggagtttcctaatacatcccaaactcaaatatataaagcatttgacttgttctatgccctagttattaatagtaatcaattacggggtcattagttcatagcccatatatggagttccgcgttacataacttacggtaaatggcccgcctggctgaccgcccaacgacccccgcccattgacgtcaataatgacgtatgttcccatagtaacgccaatagggactttccattgacgtcaatgggtggagtatttacggtaaactgcccacttggcagtacatcaagtgtatcatatgccaagtacgccccctattgacgtcaatgacggtaaatggcccgcctggcattatgcccagtacatgaccttatgggactttcctacttggcagtacatctacgtattagtcatcgctattaccatggtgatgcggttttggcagtacatcaatgggcgtggatagcggtttgactcacggggatttccaagtctccaccccattgacgtcaatgggagtttgttttggcaccaaaatcaacgggactttccaaaatgtcgtaacaactccgccccattgacgcaaatgggcggtaggcatgtacggtgggaggtctatataagcagagctcaataaaagagcccacaacccctcactcggggcgccagtcctccgattgactgagtcgcccgggtacccgtgtatccaataaaccctcttgcagttgcatccgacttgtggtctcgctgttccttgggagggtctcctctgagtgattgactacccgtcagcgggggtctttcatttgggggctcgtccgggatcgggagacccctgcccagggaccaccgacccaccaccgggaggtaagctggccagcaacttatctgtgtctgtccgattgtctagtgtctatgactgattttatgcgcctgcgtcggtactagttagctaactagctctgtatctggcggacccgtggtggaactgacgagttcggaacacccggccgcaaccctgggagacgtcccagggacttcgggggccgtttttgtggcccgacctgagtccaaaaatcccgatcgttttggactctttggtgcaccccccttagaggagggatatgtggttctggtaggagacgagaacctaaaacagttcccgcctccgtctgaatttttgctttcggtttgggaccgaagccgcgccgcgcgtcttgtctgctgcagcatcgttctgtgttgtctctgtctgactgtgtttctgtatttgtctgaaaatatcggcccgggccagactgttaccactcccttaagtttgaccttaggtcactggaaagatgtcgagcggatcgctcacaaccagtcggtagatgtcaagaagagacgttgggttaccttctgctctgcagaatggccaacctttaacgtcggatggccgcgagacggcacctttaaccgagacctcatcacccaggttaagatcaaggtcttttcacctggcccgcatggacacccagaccaggtcccctacatcgtgacctgggaagccttggcttttgacccccctccctgggtcaagccctttgtacaccctaagcctccgcctcctcttcctccatccgccccgtctctcccccttgaacctcctcgttcgaccccgcctcgatcctccctttatccagccctcactccttctctaggcgcccccatatggccatatgagatcttatatggggcacccccgccccttgtaaacttccctgaccctgacatgacaagagttactaacagcccctctctccaagctcacttacaggctctctacttagtccagcacgaagtctggagacctctggcggcagcctaccaagaacaactggaccgaccggtggtacctcacccttaccgagtcggcgacacagtgtgggtccgccgacaccagactaagaacctagaacctcgctggaaaggaccttacacagtcctgctgaccacccccaccgccctcaaagtagacggcatcgcagcttggatacacgccgcccacgtgaaggctgccgaccccgggggtggaccatcctctagactgccggatc"
}

plasmid3Output = {
    "promoters": [
        {
            "name": "CMV_immearly_promoter",
            "start": 4934,
            "stop": 5501,
            "legend": "CMV_immearly_promoter"
        },
        {
            "name": "AmpR_promoter",
            "start": 4774,
            "stop": 4802,
            "legend": "AmpR_promoter"
        }
    ],
    "terminators": [],
    "regulatorySequences": [
        {
            "name": "3MoMuLV_long_terminal_repeat",
            "start": 2145,
            "stop": 2738,
            "legend": "3MoMuLV_LTR"
        },
        {
            "name": "internal_ribosome_entry_site",
            "start": 777,
            "stop": 1361,
            "legend": "IRES"
        },
        {
            "name": "ires_emcv",
            "start": 853,
            "stop": 1351,
            "legend": "ires_emcv"
        },
        {
            "name": "CAG_enhancer",
            "start": 4993,
            "stop": 5298,
            "legend": "CAG_enhancer"
        }
    ],
    "replicationOrigins": [
        {
            "name": "pBR322_origin",
            "start": 3095,
            "stop": 3714,
            "legend": "pBR322_origin"
        }
    ],
    "selectableMarkers": [
        {
            "name": "Ampicillin",
            "start": 3872,
            "stop": 4732,
            "legend": "Ampicillin"
        }
    ],
    "reporterGenes": [
        {
            "name": "mCherry",
            "start": 1382,
            "stop": 2086,
            "legend": "mCherry"
        },
        {
            "name": "enhanced_green_fluorescent_protein_(EGFP)_ORF",
            "start": 32,
            "stop": 742,
            "legend": "EGFP"
        },
        {
            "name": "enhanced_cyan_fluorescent_protein",
            "start": 32,
            "stop": 742,
            "legend": "ECFP"
        },
        {
            "name": "enhanced_yellow_fluorescent_protein_(EYFP)_gene",
            "start": 32,
            "stop": 743,
            "legend": "EYFP"
        },
        {
            "name": "destabilized_enhanced_yellow_fluorescent_protein_(d2EYFP)_ORF",
            "start": 32,
            "stop": 742,
            "legend": "d2EYFP"
        },
        {
            "name": "mStrawberry",
            "start": 1382,
            "stop": 2086,
            "legend": "mStrawberry"
        },
        {
            "name": "mOrange",
            "start": 1382,
            "stop": 2086,
            "legend": "mOrange"
        },
        {
            "name": "pAmCherry",
            "start": 1382,
            "stop": 2086,
            "legend": "pAmCherry"
        },
        {
            "name": "mOrange2",
            "start": 1382,
            "stop": 2086,
            "legend": "mOrange2"
        },
        {
            "name": "mTangerine",
            "start": 1413,
            "stop": 2086,
            "legend": "mTangerine"
        },
        {
            "name": "mRaspberry",
            "start": 1413,
            "stop": 2066,
            "legend": "mRaspberry"
        },
        {
            "name": "mHoneydew",
            "start": 1413,
            "stop": 2086,
            "legend": "mHoneydew"
        },
        {
            "name": "mRFP1",
            "start": 1413,
            "stop": 2066,
            "legend": "mRFP1"
        },
        {
            "name": "mPlum",
            "start": 1413,
            "stop": 2066,
            "legend": "mPlum"
        },
        {
            "name": "mBanana",
            "start": 1382,
            "stop": 2086,
            "legend": "mBanana"
        }
    ],
    "affinityTags": [],
    "localizationSequences": [],
    "twoHybridGenes": [],
    "genes": [
        {
            "name": "gag_gene",
            "start": 6153,
            "stop": 6647,
            "legend": "gag"
        }
    ],
    "primers": [],
    "misc": [
        {
            "name": "psi_plus_packaging_element2",
            "start": 5677,
            "stop": 6964,
            "legend": "psi_plus_pack2"
        },
        {
            "name": "5_long_terminal_repeat",
            "start": 4976,
            "stop": 5677,
            "legend": "5_LTR"
        },
        {
            "name": "5_prime_long_terminal_repeat2",
            "start": 2187,
            "stop": 2744,
            "legend": "5_LTR2"
        },
        {
            "name": "5_long_terminal_repeat2",
            "start": 2187,
            "stop": 2738,
            "legend": "5_LTR2"
        }
    ]
}

# pBbB6a-GFP
plasmid4 = {
    "sequence":"gacgtcggtgcctaatgagtgagctaacttacattaattgcgttgcgctcactgcccgctttccagtcgggaaacctgtcgtgccagctgcattaatgaatcggccaacgcgcggggagaggcggtttgcgtattgggcgccagggtggtttttcttttcaccagtgagacgggcaacagctgattgcccttcaccgcctggccctgagagagttgcagcaagcggtccacgctggtttgccccagcaggcgaaaatcctgtttgatggtggttaacggcgggatataacatgagctgtcttcggtatcgtcgtatcccactaccgagatgtccgcaccaacgcgcagcccggactcggtaatggcgcgcattgcgcccagcgccatctgatcgttggcaaccagcatcgcagtgggaacgatgccctcattcagcatttgcatggtttgttgaaaaccggacatggcactccagtcgccttcccgttccgctatcggctgaatttgattgcgagtgagatatttatgccagccagccagacgcagacgcgccgagacagaacttaatgggcccgctaacagcgcgatttgctggtgacccaatgcgaccagatgctccacgcccagtcgcgtaccgtcttcatgggagaaaataatactgttgatgggtgtctggtcagagacatcaagaaataacgccggaacattagtgcaggcagcttccacagcaatggcatcctggtcatccagcggatagttaatgatcagcccactgacgcgttgcgcgagaagattgtgcaccgccgctttacaggcttcgacgccgcttcgttctaccatcgacaccaccacgctggcacccagttgatcggcgcgagatttaatcgccgcgacaatttgcgacggcgcgtgcagggccagactggaggtggcaacgccaatcagcaacgactgtttgcccgccagttgttgtgccacgcggttgggaatgtaattcagctccgccatcgccgcttccactttttcccgcgttttcgcagaaacgtggctggcctggttcaccacgcgggaaacggtctgataagagacaccggcatactctgcgacatcgtataacgttactggtttcacattcaccaccctgaattgactctcttccgggcgctatcatgccataccgcgaaaggttttgcgccattcgatggtgtccgggatctcgacgctctcccttatgcgactcctgcattaggaagcagcccagtagtaggttgaggccgttgagcaccgccgccgcaaggaatggtgcatgcaaggagatggcgcccaacagtcccccggccacggggcctgccaccatacccacgccgaaacaagcgctcatgagcccgaagtggcgagcccgatcttccccatcggtgatgtcggcgatataggcgccagcaaccgcacctgtggcgccggtgatgccggccacgatgcgtccggcgtagaggatcgagaattgtgagcggataacaattgacattgtgagcggataacaagatactgagcacatcagcaggacgcactgaccgaattcaaaagatcttttaagaaggagatatacatatgagtaaaggagaagaacttttcactggagttgtcccaattcttgttgaattagatggtgatgttaatgggcacaaattttctgtcagtggagagggtgaaggtgatgcaacatacggaaaacttacccttaaatttatttgcactactggaaaactacctgttccgtggccaacacttgtcactactttctcttatggtgttcaatgcttttcccgttatccggatcacatgaaacggcatgactttttcaagagtgccatgcccgaaggttatgtacaggaacgcactatatctttcaaagatgacgggaactacaagacgcgtgctgaagtcaagtttgaaggtgatacccttgttaatcgtatcgagttaaaaggtattgattttaaagaagatggaaacattctcggacacaaactggagtacaactataactcacacaatgtatacatcacggcagacaaacaaaagaatggaatcaaagctaacttcaaaattcgccacaacattgaagatggctccgttcaactagcagaccattatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtccacacaatctgccctttcgaaagatcccaacgaaaagcgtgaccacatggtccttcttgagtttgtaactgctgctgggattacacatggcatggatgagctctacaaataaggatccaaactcgagtaaggatctccaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctctactagagtcacactggctcaccttcgggtgggcctttctgcgtttatacctaggctacagccgatagtctggaacagcgcacttacgggttgctgcgcaacccaagtgctaccggcgcggcagcgtgacccgtgtcggcggctccaacggctcgccatcgtccagaaaacacggctcatcgggcatcggcaggcgctgctgcccgcgccgttcccattcctccgtttcggtcaaggctggcaggtctggttccatgcccggaatgccgggctggctgggcggctcctcgccggggccggtcggtagttgctgctcgcccggatacagggtcgggatgcggcgcaggtcgccatgccccaacagcgattcgtcctggtcgtcgtgatcaaccaccacggcggcactgaacaccgacaggcgcaactggtcgcggggctggccccacgccacgcggtcattgaccacgtaggccaacacggtgccggggccgttgagcttcacgacggagatccagcgctcggccaccaagtccttgactgcgtattggaccgtccgcaaagaacgtccgatgagcttggaaagtgtcttctggctgaccaccacggcgttctggtggcccatctgcgccacgaggtgatgcagcagcattgccgccgtgggtttcctcgcaataagcccggcccacgcctcatgcgctttgcgttccgtttgcacccagtgaccgggcttgttcttggcttgaatgccgatttctctggactgcgtggccatgcttatctccatgcggtaggggtgccgcacggttgcggcaccatgcgcaatcagctgcaacttttcggcagcgcgacaacaattatgcgttgcgtaaaagtggcagtcaattacagattttctttaacctacgcaatgagctattgcggggggtgccgcaatgagctgttgcgtaccccccttttttaagttgttgatttttaagtctttcgcatttcgccctatatctagttctttggtgcccaaagaagggcacccctgcggggttcccccacgccttcggcgcggctccccctccggcaaaaagtggcccctccggggcttgttgatcgactgcgcggccttcggccttgcccaaggtggcgctgcccccttggaacccccgcactcgccgccgtgaggctcggggggcaggcgggcgggcttcgcccttcgactgcccccactcgcataggcttgggtcgttccaggcgcgtcaaggccaagccgctgcgcggtcgctgcgcgagccttgacccgccttccacttggtgtccaaccggcaagcgaagcgcgcaggccgcaggccggaggcactagtgcttggattctcaccaataaaaaacgcccggcggcaaccgagcgttctgaacaaatccagatggagttctgaggtcattactggatctatcaacaggagtccaagcgagctcgtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagggcttaccatctggccccagtgctgcaatgataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttgccattgctacaggcatcgtggtgtcacgctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaatacgggataataccgcgccacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccacct"
}

plasmid4Output = {
    "promoters": [
        {
            "name": "AmpR_promoter",
            "start": 4814,
            "stop": 4842,
            "legend": "AmpR_promoter"
        }
    ],
    "terminators": [],
    "regulatorySequences": [
        {
            "name": "lacI",
            "start": 49,
            "stop": 1140,
            "legend": "lacI"
        }
    ],
    "replicationOrigins": [],
    "selectableMarkers": [
        {
            "name": "Ampicillin",
            "start": 3912,
            "stop": 4772,
            "legend": "Ampicillin"
        }
    ],
    "reporterGenes": [
        {
            "name": "green_fluorescent_protein_cycle_3_variant",
            "start": 1609,
            "stop": 2325,
            "legend": "GFP_cyc3"
        }
    ],
    "affinityTags": [],
    "localizationSequences": [],
    "twoHybridGenes": [],
    "genes": [],
    "primers": [
        {
            "name": "GFP_R_primer",
            "start": 1639,
            "stop": 1667,
            "legend": "GFP_R_primer"
        }
    ],
    "misc": []
}

# pKB01_tagRFP
plasmid5 = {
    "sequence":"CTAGAGGAGGAAAATTAATGTCAGAACTTATCAAGGAAAATATGCACATGAAATTGTACATGGAAGGAACTGTCAATAATCACCACTTTAAATGTACCTCAGAAGGAGAAGGAAAACCATATGAAGGTACTCAAACCATGCGTATTAAGGTTGTCGAAGGTGGACCACTTCCTTTTGCTTTTGATATTCTTGCAACATCTTTTATGTACGGATCACGTACCTTTATCAATCATACACAAGGTATCCCAGATTTCTTTAAACAGTCTTTTCCTGAAGGATTTACATGGGAACGTGTTACAACTTATGAAGATGGTGGAGTCTTGACAGCTACTCAAGATACATCTTTGCAAGATGGTTGTTTGATCTACAATGTCAAGATCCGTGGAGTAAATTTTCCATCTAATGGTCCTGTTATGCAGAAAAAGACTCTTGGATGGGAAGCCAATACCGAAATGTTGTATCCTGCTGATGGTGGACTTGAAGGTCGTTCAGATATGGCATTGAAACTTGTTGGTGGAGGTCATTTGATCTGTAATTTTAAGACCACATACCGTAGTAAAAAGCCAGCAAAGAATCTTAAGATGCCTGGTGTATACTACGTCGATCATCGTTTGGAACGTATCAAAGAAGCCGATAAGGAAACTTATGTTGAACAACACGAAGTCGCCGTAGCACGTTACTGTGATTTGCCTAGTAAATTGGGACATAAATAATAATAAGGATCCTAACTCGAGAAAGAATTCATGACTAGTCAAGGTCGGCAATTCTGCAGTACTAGGACGCCGCCAAGCCAGCTTAAACCCAGCTCAATGAGCTGGGTTTTTTGTTTGTTAAAAATGAAGAAGAAACTGTGAAGCGTATTTATAGCAAAGCACTCAAAAGTTTACCTTATGGGTGCTTTTTTCGTGCTTTTTTGAAAAGACAAAAAAAAGAACCTTGCCAAGCAAGATTCTTTTGATAGCGCTATCGCTGAGCGCCGGTCGCTACCATTACCAGTTGGTCTGGTGTCAAAAATAATAATAACCGGGCAGGCCATGTCTGCCCGTATTTCGCGTAAGGAAATCCATTATGTACTATTTCTGGTGATGAAATCAACGTAACATTTAAAGCTGTCAAAGCCAAAGTCATGAGATGGCGTATGGAGCGTAAAGCTGACAAGAGCGGTGTTGCGATGATTGAGATGACCTTCCTTGCACCAAGTGAATTGCCTCAAGAAAGCACTCAATCAAAGATTCTTGTAGATGGAAAAGAACTTGCTGATTTCGCTGAAAATCGTCAAGACTATCAAATTACCTATAAAGGTCAACGGCCAAAAGTCTCAGTTGAAGAAAACAATCAAGTAGCTTCAACTGTGGTAGATAGTGGAGAAGATAGCCTTCCAGTACTTGTTCGCCTCGTTTCAGAAAGTGGAAAACAAGTCAAGGAATACCGTATCCAGTTGACTAAGGAAAAACCAGTTTCTGCTGTACAAGAAGATCTTCCAAAACTCGAATTTGTTGAAAAAGATTTGGCCTACAAGACAGTTGAGAAAAAAGATTCAACACTGTATCTAGGTGAAACTCGTGTAGAACAAGAAGGAAAAGTTGGAAAAGAACGTATCTTTACAGTGATTAATCCTGATGGAAGTAAGGAAGAAAAACTCCGTGAAGTGGTAGAAGTTCCGACAGACCGCATCGTCTTGGTTGGAACCAAACCAGTAGCTCAAGAAGCTAAAAAACCACAAGTGTCAGAAAAAGCAGATACAAAACCAATTGATTCAAGTGAAGCTGATCAAACTAATAAAGCCCAGTTACCAAATACAGGTAGTGCGGCAAGCCAAGCAGCAGTAGCAGCAGGTTTAGCCTGCCTCGCGCGTTTCGGTGATGACGGTGAAAACCTCTGACACATGCAGCTCCCGGAGACGGTCACAGCTTGTCTGTAAGCGGATGCCGGGAGCAGACAAGCCCGTCAGGGCGCGTCAGCGGGTGTTGGCGGGTGTCGGGGCGCAGCCATGACCCAGTCACGTAGCGATAGCGGAGTGTATACTGGCTTAACTATGCGGCATCAGAGCAGATTGTACTGAGAGTGCACCATATGCGGTGTGAAATACCGCACAGATGCGTAAGGAGAAAATACCGCATCAGGCGCTCTTCCGCTTCCTCGCTCACTGACTCGCTGCGCTCGGTCGTTCGGCTGCGGCGAGCGGTATCAGCTCACTCAAAGGCGGTAATACGGTTATCCACAGAATCAGGGGATAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCATAGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTGCACGAACCCCCCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCAACCCGGTAAGACACGACTTATCGCCACTGGCAGCAGCCACTGGTAACAGGATTAGCAGAGCGAGGTATGTAGGCGGTGCTACAGAGTTCTTGAAGTGGTGGCCTAACTACGGCTACACTAGAAGGACAGTATTTGGTATCTGCGCTCTGCTGAAGCCAGTTACCTTCGGAAAAAGAGTTGGTAGCTCTTGATCCGGCAAACAAACCACCGCTGGTAGCGGTGGTTTTTTTGTTTGCAAGCAGCAGATTACGCGCAGAAAAAAAGGATCTCAAGAAGATCCTTTGATCTTTTCTACGGGGTCTGACGCTCAGTGGAACGAAAACTCACGTTAAGGGATTTTGGTCATGAGATTATCAAAAAGGATCTTCACCTAGATCCTTTTAAATTAAAAATGAAGTTTTAAATCAATCTAAAGTATATATGAGTAAACTTGGTCTGACAGTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATACGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGAAGGGCCGAGCGCAGAAGTGGTCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTGCAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGTCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTAAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAACACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGAAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATACTCTTCCTTTTTCAATATTATTGAAGCATTTATCAGGGTTATTGTCTCATGAGCGGATACATATTTGAATGTATTTAGAAAAATAAACAAATAGGGGTTCCGCGCACATTTCCCCGAAAAGTGCCACCTGACGTCTAAGAAACCATTATTATCATGACATTAACCTATAAAAATAGGCGTATCACGAGGCCCTTTCGTCTTCAAGAATTAATTCCTTCTTAACGCCCCAAGTTCATCACCAATGACATCAACTCACATGAACTACATGATGAACCCAGTTATCATGGTTTTGGATAAGATTTTTGAAAAATTCTTCCCAGGCCTTGATAAATATGACTTTGATGCTGCTAAATTGAACAAGAAAATCGGTTTCTGGGGATCTAAATTCTTCATCGGTTTCATCCTTGGTATCGTTATCGGTATTATGGGAACTCCACATCCAATTGCAGGTGTTGCAGATGCAGATAAATGGCGTCTTGTTATCAAAGGATGGTTGTCTCTTGGTTTGACTGCCGGTGTATCTTTGGAACTCTTCTCACTTATCGGTTCATGGTTCATCGCAGCCGTAGAACCACTATCACAAGGTATTACAAACGTTGCTACTAAACGTCTTCAAGGACGTAAATTCAATATCGGTCTTGACTGGCCATTCATCGCTGGTCGTGCTGAAATCTGGGCTTGTGCCAACGTACTTGCACCAATCATGTTGATTGAAGCAGTGCTTCTTTCAAAAGTTGGAAATGGTATCTTGCCACTTGCAGGTATCATCGCTATGGGTGTTACTCCAGCTCTCTTGGTTGTAACTCGTGGTAAATTGCTCCGTATGATTATCTTCGGAACACTCTTGTTGCCACTCTTCCTTCTTTCAGGTACACTTATTGCACCATTTGCAACAGAACTTGCTAAAGGTGTAGGTGCCTTCCCAGAAGGTGTGAGCCAAACTCAATTGATTACTCACTCTACTCTTGAAGGACCAATCGAAAAACTTCTTGGTTGGACAATTGGTAACACTACAACTGGTGATATCAAAGCAATCCTTGGTGCAGTAGCCTTCCTTGTATTCTATATCGGTATCTTTGCTTGGTACAGAAAACAAATGATCAAACGTAACGAAGAGTACGCAGCAAAAGCAAAATAATGCGCTCCGCTAGCTTTACAGACAAAGAACTATCCTTAATGGAAGCACTAGCAAAAGGTATCAATGAAGCAAGAAATATTGAAGGCTAGTCAGTAAAATTCAGATAAACAAAAAGAGCCGATAAGATGAGAGTTTCATTTCTCAAATTATCGGCTCTGCGTCTTGGCGTCTGGCTCTTTGATTGTTATTATATTCATTTTTTGAACATTAATTAAAGTTTCGTTCTTACATTTGGGGCAGTATAAAGGGAAATTTTTAAGTATAGTATCCACTCGTATTCGTAGTCTTGTTTTATTTCCACAAATAGGACACAATATCCACTTGTAGTTTATAATAACAATCTCCTCCTTTCCACTTTAATTCAAATCTATATTAAAGAATATTTCATCTTATTTAATAAGAAACCATATTTATATAACAACATAAAACGCACTAAGTTATTTTATTGAACATATATCTTACTTTATCTATCTGACTATTTAGACGACGGGTCTGGCAAACAGGTTCGCCAGTGGTAACCTGATATCCTTTTAGCTCTGCTAAACAAACACTAAGCCCATTTGTAAAAAAAGTTAAATCATTGCGATAATCTTGAATACATCGAGCAGGAATTTCTCCAATAATAATGACCTCATTATTTTTCAGTTGAGTATTTACGATATTTGCACAATATTTGGGAGCATCGTTATATGCCCGTGAAAGATATTCCTGTGGTGCATAAACTTTAAAACTAAGATATGGCTCTAACAATTCTGTTCCAGCTTTTCTAAAGGCTTGCTCCAATACAATAGGAGCAAGCATCCGAAAATCTGCTGGGGTACTAACAGGGCTATAGTATAAGCCATACTTAAAACAGATTTTACAGTCCGTCACATTCCAACCATACAATCCTTGTTCACAACCATAGCGTATCCCTTCCATAACTGCATTTTGAAATGATTGATTTAAGTATCCAAGAGAAACCGAGCTCTCATACTGCATTCCACTTCCCAACGGAAGCGGTGATACAGATAAACCAATGGAAGCCCAGAAAGGATTTGGCGGCACTTCGATGTGAATGGTATATTCTGCATTTTTTAACGGTCTCTCCATATAAATGACTGTAGGCTCTTTTAGTTCTATCTCCACATGATACTTTTCTTGCAACAGTGCACTAATCACTTCCATTTGTACTTTCCCTAAGAAAGAAAGTATAATTTCATGTGTCGTAGAATCCACGTAATATCGTAGAAGCGGATCACTATCTGAGATTTCCAAAAGGGCATCAAGCAACATTTCTCTCTGTTCAGGTTTACTCGGTTCAACAGTTGTTTGTAGTAGAGGGTGCGGATTTTCAATCTTTTTTCTCTGTGGCAATAGTTTTGTATCTCCAAGAACACTATTTAACTTCAAAAACTCATTTTGCAAAATAACAATTTCTCCAGAATAAGCTCTATCAATCTTACATAATTCACCATTTATTGAAGTATACATTTCTGTAACTTTTATTTTTTCTTTTTCTGATACTCTAACCGAATCTCGTAAATGTAGTACTCCACTATAAAGGCGTATATATGCAAGACGTTGTCTTTTTTTTGTATATTCAATTTTGAAAACATTTCCGCAAAGTTCAGACGGACCTCGATGTGTTGATGAATAAAATTTATTAGTAATAACTTCTATAAGGTTATCAATCCCTATATTACTTTTTGCACTTCCATGATAAAGAGGGAACAGAGAACAATTCTGAAATCTTATGCTTTCCTCTTGTTCGAGTTCCAATGCTTCTAATGATTTACCGGACATATATTTCTCTAAAAGGTCATCGTTTCCCTCTATTACCGTATCCCATTGTTCAGATTCGGTAAAGTTCGTCACACACACATTAGGATACAGTTCTACCTTCTGTTTGATTACAATTTCGGCAGAAAGTTTCTCTTTAATATCCTGATAAACCGTTGATAAATCAATTCCATTTTGGTCAATCTTATTGATAAAAAAGATTGTGGGAATCCCCATTTTCCTAAGTGCATGAAATAATATACGAGTTTGTGCTTGTACGCCATCTTTTGCAGAAATCAGTAGAATTGCCCCATCTAAAACTGATAATGAACGATATACTTCTGCTAAGAAATCCATATGTCCTGGCGTGTCTATGATGTTCACCTTCGTATTTTCCCACTGAAAAGAGGTTATTCCTGTCTGAATTGTAATTCCTCTCTGACGTTCTAAAAGCGTATTATCCGTCCTCGTTGTACCTTTGTCCACGCTTCCTAATTCTGTAATCGCTCCACTGTTATATAATAAGCTTTCTGTTAAGGTAGTTTTTCCTGCATCAACATGAGCTAAAACTCCAATATTAATAATTTTCATGTGATTTTCCTCCATTCAAAAGCCCAAAAGGGCATAAAAATCCCAGTGATAAATACTCTTATCACTGGGATTTTTATGCATAACCATAGGCATACAAAGCATACAGATATTCTCCGGATACTTTAGAATCACATGATAAAGGTATTCTTAAACTGGGTACAAAAAACTAAGCCCTCCTAAAAAAGGACATCCAATTATTTGTTCCCGCTATCAAATTGACAGTTTATTTAAGAATACCTTGCCGCATATTTATTAACTCCTTTTAAATAGATACTTAAATTATAGCACGTAAGAGCATATTTGTAAAGGAATCTCCAATTTTTTATCAAAAAGAGTACATGATTACAAAGTATCTGTAATCATGTACCAATATTTGTTATTTTACAATCTTCCAATTATCTTGTTTTTCTAATATCAACTCAAATTGCGAGATTTGGGTTGCCTTTGTTTCTTGATCTAAATATTTCACAGCGACATTCACGATTACTTGGCTAGCGCTATATGCGTTGATGCAATTTCTATGCGCACCCGTTCTCGGAGCACTGTCCGACCGCTTTGGCCGCCGCCCAGTCCTGCTCGCTTCGCTACTTGGAGCCACTATCGACTACGCGATCATGGCGACCACACCCGTCCTGTGGATCTATCGATGCATGCAGCCGGTACCATCACAAGCACTTTGGGACGTTCTCCCTTAGTGCTTTTTTGATTTCTCATAGGCCGGCCTGTTAGTCATATGGACACTTAAGGCAAATTGTTCAGAACTGAATAAAGCTGACGTTTTGCTTCTATCCTTTCTTTGAGTTTTAGTGGATAATGATAATGAACAAGGTGTTCATAAATCTATTATAACAAGAATTCCAATCCCGGGTAAAGCTTCCAGCGGCCGCATAGGATCCATTGATATCATATT"
}

plasmid5Output = {
    "promoters": [
        {
            "name": "AmpR_promoter",
            "start": 3971,
            "stop": 3999,
            "legend": "AmpR_promoter"
        }
    ],
    "terminators": [],
    "regulatorySequences": [],
    "replicationOrigins": [
        {
            "name": "pBR322_origin",
            "start": 2295,
            "stop": 2914,
            "legend": "pBR322_origin"
        }
    ],
    "selectableMarkers": [
        {
            "name": "Ampicillin",
            "start": 3069,
            "stop": 3929,
            "legend": "Ampicillin"
        }
    ],
    "reporterGenes": [],
    "affinityTags": [],
    "localizationSequences": [],
    "twoHybridGenes": [],
    "genes": [],
    "primers": [],
    "misc": []
}

class FsdEndpointTestCase (APITestCase):
    def test_fsd_search(self):
        url = "/features"

        # Plasmid 1
        response = self.client.post(url, plasmid1, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), plasmid1Output)

        # Plasmid 2
        response = self.client.post(url, plasmid2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), plasmid2Output)

        # Plasmid 3
        response = self.client.post(url, plasmid3, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), plasmid3Output)

        # Plasmid 4
        response = self.client.post(url, plasmid4, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), plasmid4Output)

        # Plasmid 5
        response = self.client.post(url, plasmid5, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), plasmid5Output)
