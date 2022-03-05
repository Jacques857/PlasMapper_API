import re

# Common restriction enzymes as specified in PlasMapper 2
COMMON_ENZYMES = [ 
  { "name": 'HpaII', "reg": 'ccgg'},
  { "name": 'ApoI', "reg": '[ag]aatt[ct]'},
  { "name": 'SacI', "reg": 'gagctc'},
  { "name": 'EcoRI', "reg": 'gaattc'},
  { "name": 'AlwNI', "reg": 'cag[actg][actg][actg]ctg'},
  { "name": 'AluI', "reg": 'agct'},
  { "name": 'AccI', "reg": 'gt[ac][gt]ac'},
  { "name": 'MboI', "reg": 'gatc'},
  { "name": 'Sau3AI', "reg": 'gatc'},
  { "name": 'SfiI', "reg": 'ggcc[actg][actg][actg][actg][actg]ggcc'},
  { "name": 'HincII', "reg": 'gt[ct][ag]ac'},
  { "name": 'NruI', "reg": 'tcgcga'},
  { "name": 'BglI', "reg": 'gcc[actg][actg][actg][actg][actg]ggc'},
  { "name": 'AvrI', "reg": 'c[ct]cg[ag]g'},
  { "name": 'XmaI', "reg": 'cccggg'},
  { "name": 'DraI', "reg": 'tttaaa'},
  { "name": 'PvuII', "reg": 'cagctg'},
  { "name": 'HindIII', "reg": 'aagctt'},
  { "name": 'KpnI', "reg": 'ggtacc'},
  { "name": 'NarI', "reg": 'ggcgcc'},
  { "name": 'BglII', "reg": 'agatct'},
  { "name": 'HpaI', "reg": 'gttaac'},
  { "name": 'StuI', "reg": 'aggcct'},
  { "name": 'NcoI', "reg": 'ccatgg'},
  { "name": 'NdeI', "reg": 'catatg'},
  { "name": 'Bsp24I', "reg": 'gac[actg][actg][actg][actg][actg][actg]tgg'},
  { "name": 'BclI', "reg": 'tgatca'},
  { "name": 'SmaI', "reg": 'cccggg'},
  { "name": 'AvaI', "reg": 'c[ct]cg[ag]g'},
  { "name": 'AvaII', "reg": 'gg[at]cc'},
  { "name": 'PstI', "reg": 'ctgcag'},
  { "name": 'SphI', "reg": 'gcatgc'},
  { "name": 'ApaI', "reg": 'gggccc'},
  { "name": 'EcoRV', "reg": 'gatatc'},
  { "name": 'BamHI', "reg": 'ggatcc'},
  { "name": 'HaeIII', "reg": 'ggcc'},
  { "name": 'NotI', "reg": 'gcggccgc'},
  { "name": 'XhoI', "reg": 'ctcgag'},
  { "name": 'ClaI', "reg": 'atcgat'},
  { "name": 'XbaI', "reg": 'tctaga'} 
  ]

def checkRestrictionSites(sequence):
    """
    Gets the restriction sites for a given DNA sequence

    Input
    ----------
    sequence : str

    Output
    -------
    A list of dictionaries. One for each restriction site that appears at least once.
    name : str 
        Name of the restriction enzyme
    locations : list of tuples
        Locations of occurences (start, stop)
    count : int 
        Number of occurences
    """
    features = []
    for enzyme in COMMON_ENZYMES:
        findEnzyme = [*re.finditer(enzyme["reg"], sequence)]  # Run the RegEx for the enzyme on the sequence
        if findEnzyme:
            features.append({"name": enzyme["name"], 
                             "locations": [match.span() for match in findEnzyme],
                             "count": len(findEnzyme)})
    return features