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
    "misc": [],
    "restriction": [
        {
            "name": "HpaII",
            "locations": [
                [
                    1420,
                    1424
                ],
                [
                    2362,
                    2366
                ],
                [
                    2509,
                    2513
                ],
                [
                    2535,
                    2539
                ],
                [
                    2725,
                    2729
                ],
                [
                    2913,
                    2917
                ],
                [
                    3179,
                    3183
                ],
                [
                    3360,
                    3364
                ],
                [
                    3427,
                    3431
                ],
                [
                    3517,
                    3521
                ],
                [
                    3648,
                    3652
                ],
                [
                    3676,
                    3680
                ],
                [
                    3698,
                    3702
                ],
                [
                    3775,
                    3779
                ]
            ],
            "count": 14
        },
        {
            "name": "ApoI",
            "locations": [
                [
                    207,
                    213
                ],
                [
                    733,
                    739
                ],
                [
                    1171,
                    1177
                ],
                [
                    1273,
                    1279
                ],
                [
                    1330,
                    1336
                ],
                [
                    1694,
                    1700
                ]
            ],
            "count": 6
        },
        {
            "name": "SacI",
            "locations": [
                [
                    1900,
                    1906
                ],
                [
                    2992,
                    2998
                ]
            ],
            "count": 2
        },
        {
            "name": "EcoRI",
            "locations": [
                [
                    207,
                    213
                ],
                [
                    1171,
                    1177
                ]
            ],
            "count": 2
        },
        {
            "name": "AlwNI",
            "locations": [
                [
                    2566,
                    2575
                ]
            ],
            "count": 1
        },
        {
            "name": "AluI",
            "locations": [
                [
                    564,
                    568
                ],
                [
                    614,
                    618
                ],
                [
                    1683,
                    1687
                ],
                [
                    1901,
                    1905
                ],
                [
                    2096,
                    2100
                ],
                [
                    2322,
                    2326
                ],
                [
                    2412,
                    2416
                ],
                [
                    2458,
                    2462
                ],
                [
                    2715,
                    2719
                ],
                [
                    2993,
                    2997
                ],
                [
                    3117,
                    3121
                ],
                [
                    3575,
                    3579
                ],
                [
                    3935,
                    3939
                ]
            ],
            "count": 13
        },
        {
            "name": "AccI",
            "locations": [
                [
                    1645,
                    1651
                ],
                [
                    1800,
                    1806
                ]
            ],
            "count": 2
        },
        {
            "name": "MboI",
            "locations": [
                [
                    163,
                    167
                ],
                [
                    519,
                    523
                ],
                [
                    1127,
                    1131
                ],
                [
                    1423,
                    1427
                ],
                [
                    1825,
                    1829
                ],
                [
                    2722,
                    2726
                ],
                [
                    2797,
                    2801
                ],
                [
                    2808,
                    2812
                ],
                [
                    2816,
                    2820
                ],
                [
                    2969,
                    2973
                ],
                [
                    3262,
                    3266
                ],
                [
                    3340,
                    3344
                ],
                [
                    3349,
                    3353
                ],
                [
                    3430,
                    3434
                ],
                [
                    3508,
                    3512
                ],
                [
                    3819,
                    3823
                ],
                [
                    3838,
                    3842
                ],
                [
                    3843,
                    3847
                ],
                [
                    3849,
                    3853
                ],
                [
                    3866,
                    3870
                ]
            ],
            "count": 20
        },
        {
            "name": "Sau3AI",
            "locations": [
                [
                    163,
                    167
                ],
                [
                    519,
                    523
                ],
                [
                    1127,
                    1131
                ],
                [
                    1423,
                    1427
                ],
                [
                    1825,
                    1829
                ],
                [
                    2722,
                    2726
                ],
                [
                    2797,
                    2801
                ],
                [
                    2808,
                    2812
                ],
                [
                    2816,
                    2820
                ],
                [
                    2969,
                    2973
                ],
                [
                    3262,
                    3266
                ],
                [
                    3340,
                    3344
                ],
                [
                    3349,
                    3353
                ],
                [
                    3430,
                    3434
                ],
                [
                    3508,
                    3512
                ],
                [
                    3819,
                    3823
                ],
                [
                    3838,
                    3842
                ],
                [
                    3843,
                    3847
                ],
                [
                    3849,
                    3853
                ],
                [
                    3866,
                    3870
                ]
            ],
            "count": 20
        },
        {
            "name": "HincII",
            "locations": [
                [
                    499,
                    505
                ],
                [
                    1800,
                    1806
                ]
            ],
            "count": 2
        },
        {
            "name": "AvrI",
            "locations": [
                [
                    0,
                    6
                ],
                [
                    1618,
                    1624
                ]
            ],
            "count": 2
        },
        {
            "name": "DraI",
            "locations": [
                [
                    689,
                    695
                ],
                [
                    792,
                    798
                ],
                [
                    1585,
                    1591
                ]
            ],
            "count": 3
        },
        {
            "name": "PvuII",
            "locations": [
                [
                    3574,
                    3580
                ],
                [
                    3934,
                    3940
                ]
            ],
            "count": 2
        },
        {
            "name": "KpnI",
            "locations": [
                [
                    228,
                    234
                ],
                [
                    1192,
                    1198
                ]
            ],
            "count": 2
        },
        {
            "name": "NarI",
            "locations": [
                [
                    3679,
                    3685
                ],
                [
                    3927,
                    3933
                ]
            ],
            "count": 2
        },
        {
            "name": "BglII",
            "locations": [
                [
                    3842,
                    3848
                ]
            ],
            "count": 1
        },
        {
            "name": "NcoI",
            "locations": [
                [
                    3246,
                    3252
                ]
            ],
            "count": 1
        },
        {
            "name": "Bsp24I",
            "locations": [
                [
                    2657,
                    2669
                ],
                [
                    2835,
                    2847
                ]
            ],
            "count": 2
        },
        {
            "name": "BclI",
            "locations": [
                [
                    3837,
                    3843
                ]
            ],
            "count": 1
        },
        {
            "name": "AvaI",
            "locations": [
                [
                    0,
                    6
                ],
                [
                    1618,
                    1624
                ]
            ],
            "count": 2
        },
        {
            "name": "AvaII",
            "locations": [
                [
                    1508,
                    1513
                ],
                [
                    1851,
                    1856
                ],
                [
                    3163,
                    3168
                ]
            ],
            "count": 3
        },
        {
            "name": "PstI",
            "locations": [
                [
                    3629,
                    3635
                ]
            ],
            "count": 1
        },
        {
            "name": "SphI",
            "locations": [
                [
                    3277,
                    3283
                ]
            ],
            "count": 1
        },
        {
            "name": "HaeIII",
            "locations": [
                [
                    898,
                    902
                ],
                [
                    1367,
                    1371
                ],
                [
                    1768,
                    1772
                ],
                [
                    1997,
                    2001
                ],
                [
                    2169,
                    2173
                ],
                [
                    2180,
                    2184
                ],
                [
                    2198,
                    2202
                ],
                [
                    2632,
                    2636
                ],
                [
                    3181,
                    3185
                ],
                [
                    3208,
                    3212
                ],
                [
                    3599,
                    3603
                ],
                [
                    3773,
                    3777
                ],
                [
                    4006,
                    4010
                ]
            ],
            "count": 13
        },
        {
            "name": "XhoI",
            "locations": [
                [
                    0,
                    6
                ],
                [
                    1618,
                    1624
                ]
            ],
            "count": 2
        }
    ]
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
    "misc": [],
    "restriction": [
        {
            "name": "HpaII",
            "locations": [
                [
                    292,
                    296
                ],
                [
                    313,
                    317
                ],
                [
                    493,
                    497
                ],
                [
                    761,
                    765
                ],
                [
                    952,
                    956
                ],
                [
                    1418,
                    1422
                ],
                [
                    1476,
                    1480
                ],
                [
                    1548,
                    1552
                ],
                [
                    1574,
                    1578
                ],
                [
                    1651,
                    1655
                ],
                [
                    1952,
                    1956
                ],
                [
                    2364,
                    2368
                ],
                [
                    2492,
                    2496
                ],
                [
                    2534,
                    2538
                ],
                [
                    2753,
                    2757
                ]
            ],
            "count": 15
        },
        {
            "name": "ApoI",
            "locations": [
                [
                    187,
                    193
                ],
                [
                    804,
                    810
                ],
                [
                    2487,
                    2493
                ]
            ],
            "count": 3
        },
        {
            "name": "SacI",
            "locations": [
                [
                    2031,
                    2037
                ]
            ],
            "count": 1
        },
        {
            "name": "EcoRI",
            "locations": [
                [
                    187,
                    193
                ],
                [
                    2487,
                    2493
                ]
            ],
            "count": 2
        },
        {
            "name": "AlwNI",
            "locations": [
                [
                    1605,
                    1614
                ]
            ],
            "count": 1
        },
        {
            "name": "AluI",
            "locations": [
                [
                    849,
                    853
                ],
                [
                    1497,
                    1501
                ],
                [
                    1730,
                    1734
                ],
                [
                    2032,
                    2036
                ],
                [
                    2461,
                    2465
                ],
                [
                    2590,
                    2594
                ],
                [
                    2709,
                    2713
                ],
                [
                    2718,
                    2722
                ]
            ],
            "count": 8
        },
        {
            "name": "AccI",
            "locations": [
                [
                    358,
                    364
                ],
                [
                    705,
                    711
                ]
            ],
            "count": 2
        },
        {
            "name": "MboI",
            "locations": [
                [
                    143,
                    147
                ],
                [
                    262,
                    266
                ],
                [
                    429,
                    433
                ],
                [
                    535,
                    539
                ],
                [
                    838,
                    842
                ],
                [
                    1810,
                    1814
                ],
                [
                    1821,
                    1825
                ],
                [
                    2008,
                    2012
                ],
                [
                    2761,
                    2765
                ],
                [
                    2804,
                    2808
                ]
            ],
            "count": 10
        },
        {
            "name": "Sau3AI",
            "locations": [
                [
                    143,
                    147
                ],
                [
                    262,
                    266
                ],
                [
                    429,
                    433
                ],
                [
                    535,
                    539
                ],
                [
                    838,
                    842
                ],
                [
                    1810,
                    1814
                ],
                [
                    1821,
                    1825
                ],
                [
                    2008,
                    2012
                ],
                [
                    2761,
                    2765
                ],
                [
                    2804,
                    2808
                ]
            ],
            "count": 10
        },
        {
            "name": "HincII",
            "locations": [
                [
                    274,
                    280
                ],
                [
                    285,
                    291
                ]
            ],
            "count": 2
        },
        {
            "name": "AvrI",
            "locations": [
                [
                    0,
                    6
                ]
            ],
            "count": 1
        },
        {
            "name": "DraI",
            "locations": [
                [
                    870,
                    876
                ],
                [
                    2230,
                    2236
                ],
                [
                    2569,
                    2575
                ]
            ],
            "count": 3
        },
        {
            "name": "PvuII",
            "locations": [
                [
                    2589,
                    2595
                ]
            ],
            "count": 1
        },
        {
            "name": "KpnI",
            "locations": [
                [
                    208,
                    214
                ],
                [
                    684,
                    690
                ]
            ],
            "count": 2
        },
        {
            "name": "BglII",
            "locations": [
                [
                    428,
                    434
                ]
            ],
            "count": 1
        },
        {
            "name": "HpaI",
            "locations": [
                [
                    274,
                    280
                ],
                [
                    285,
                    291
                ]
            ],
            "count": 2
        },
        {
            "name": "NcoI",
            "locations": [
                [
                    2186,
                    2192
                ]
            ],
            "count": 1
        },
        {
            "name": "Bsp24I",
            "locations": [
                [
                    1673,
                    1685
                ]
            ],
            "count": 1
        },
        {
            "name": "BclI",
            "locations": [
                [
                    534,
                    540
                ]
            ],
            "count": 1
        },
        {
            "name": "AvaI",
            "locations": [
                [
                    0,
                    6
                ]
            ],
            "count": 1
        },
        {
            "name": "AvaII",
            "locations": [
                [
                    346,
                    351
                ]
            ],
            "count": 1
        },
        {
            "name": "EcoRV",
            "locations": [
                [
                    2037,
                    2043
                ],
                [
                    2826,
                    2832
                ]
            ],
            "count": 2
        },
        {
            "name": "HaeIII",
            "locations": [
                [
                    727,
                    731
                ],
                [
                    1049,
                    1053
                ],
                [
                    1254,
                    1258
                ],
                [
                    1439,
                    1443
                ],
                [
                    2223,
                    2227
                ],
                [
                    2310,
                    2314
                ],
                [
                    2532,
                    2536
                ],
                [
                    2577,
                    2581
                ],
                [
                    2890,
                    2894
                ]
            ],
            "count": 9
        },
        {
            "name": "XhoI",
            "locations": [
                [
                    0,
                    6
                ]
            ],
            "count": 1
        },
        {
            "name": "XbaI",
            "locations": [
                [
                    1849,
                    1855
                ]
            ],
            "count": 1
        }
    ]
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
    ],
    "restriction": [
        {
            "name": "HpaII",
            "locations": [
                [
                    53,
                    57
                ],
                [
                    116,
                    120
                ],
                [
                    176,
                    180
                ],
                [
                    707,
                    711
                ],
                [
                    831,
                    835
                ],
                [
                    894,
                    898
                ],
                [
                    1363,
                    1367
                ],
                [
                    1961,
                    1965
                ],
                [
                    2060,
                    2064
                ],
                [
                    2311,
                    2315
                ],
                [
                    2386,
                    2390
                ],
                [
                    2621,
                    2625
                ],
                [
                    3255,
                    3259
                ],
                [
                    3402,
                    3406
                ],
                [
                    3428,
                    3432
                ],
                [
                    3618,
                    3622
                ],
                [
                    4025,
                    4029
                ],
                [
                    4059,
                    4063
                ],
                [
                    4126,
                    4130
                ],
                [
                    4236,
                    4240
                ],
                [
                    4478,
                    4482
                ],
                [
                    5560,
                    5564
                ],
                [
                    5688,
                    5692
                ],
                [
                    5730,
                    5734
                ],
                [
                    5876,
                    5880
                ],
                [
                    6158,
                    6162
                ],
                [
                    6758,
                    6762
                ],
                [
                    6936,
                    6940
                ],
                [
                    6962,
                    6966
                ]
            ],
            "count": 29
        },
        {
            "name": "ApoI",
            "locations": [
                [
                    25,
                    31
                ],
                [
                    6044,
                    6050
                ]
            ],
            "count": 2
        },
        {
            "name": "SacI",
            "locations": [
                [
                    2557,
                    2563
                ],
                [
                    5496,
                    5502
                ]
            ],
            "count": 2
        },
        {
            "name": "EcoRI",
            "locations": [
                [
                    25,
                    31
                ]
            ],
            "count": 1
        },
        {
            "name": "AlwNI",
            "locations": [
                [
                    1879,
                    1888
                ],
                [
                    2300,
                    2309
                ],
                [
                    2375,
                    2384
                ],
                [
                    3459,
                    3468
                ]
            ],
            "count": 4
        },
        {
            "name": "AluI",
            "locations": [
                [
                    44,
                    48
                ],
                [
                    77,
                    81
                ],
                [
                    149,
                    153
                ],
                [
                    182,
                    186
                ],
                [
                    398,
                    402
                ],
                [
                    446,
                    450
                ],
                [
                    557,
                    561
                ],
                [
                    644,
                    648
                ],
                [
                    731,
                    735
                ],
                [
                    1002,
                    1006
                ],
                [
                    1350,
                    1354
                ],
                [
                    1526,
                    1530
                ],
                [
                    1643,
                    1647
                ],
                [
                    1760,
                    1764
                ],
                [
                    1889,
                    1893
                ],
                [
                    1955,
                    1959
                ],
                [
                    2075,
                    2079
                ],
                [
                    2173,
                    2177
                ],
                [
                    2177,
                    2181
                ],
                [
                    2264,
                    2268
                ],
                [
                    2339,
                    2343
                ],
                [
                    2558,
                    2562
                ],
                [
                    2989,
                    2993
                ],
                [
                    3215,
                    3219
                ],
                [
                    3305,
                    3309
                ],
                [
                    3351,
                    3355
                ],
                [
                    3608,
                    3612
                ],
                [
                    4132,
                    4136
                ],
                [
                    4232,
                    4236
                ],
                [
                    4295,
                    4299
                ],
                [
                    4861,
                    4865
                ],
                [
                    5497,
                    5501
                ],
                [
                    5740,
                    5744
                ],
                [
                    5820,
                    5824
                ],
                [
                    5828,
                    5832
                ],
                [
                    6676,
                    6680
                ],
                [
                    6898,
                    6902
                ]
            ],
            "count": 37
        },
        {
            "name": "AccI",
            "locations": [
                [
                    6884,
                    6890
                ]
            ],
            "count": 1
        },
        {
            "name": "MboI",
            "locations": [
                [
                    525,
                    529
                ],
                [
                    673,
                    677
                ],
                [
                    711,
                    715
                ],
                [
                    1235,
                    1239
                ],
                [
                    1240,
                    1244
                ],
                [
                    1367,
                    1371
                ],
                [
                    1476,
                    1480
                ],
                [
                    1872,
                    1876
                ],
                [
                    2239,
                    2243
                ],
                [
                    3615,
                    3619
                ],
                [
                    3690,
                    3694
                ],
                [
                    3701,
                    3705
                ],
                [
                    3709,
                    3713
                ],
                [
                    3787,
                    3791
                ],
                [
                    3799,
                    3803
                ],
                [
                    3907,
                    3911
                ],
                [
                    4248,
                    4252
                ],
                [
                    4266,
                    4270
                ],
                [
                    4312,
                    4316
                ],
                [
                    4570,
                    4574
                ],
                [
                    4587,
                    4591
                ],
                [
                    4623,
                    4627
                ],
                [
                    5692,
                    5696
                ],
                [
                    5951,
                    5955
                ],
                [
                    6220,
                    6224
                ],
                [
                    6352,
                    6356
                ],
                [
                    6537,
                    6541
                ],
                [
                    6595,
                    6599
                ],
                [
                    6965,
                    6969
                ]
            ],
            "count": 29
        },
        {
            "name": "Sau3AI",
            "locations": [
                [
                    525,
                    529
                ],
                [
                    673,
                    677
                ],
                [
                    711,
                    715
                ],
                [
                    1235,
                    1239
                ],
                [
                    1240,
                    1244
                ],
                [
                    1367,
                    1371
                ],
                [
                    1476,
                    1480
                ],
                [
                    1872,
                    1876
                ],
                [
                    2239,
                    2243
                ],
                [
                    3615,
                    3619
                ],
                [
                    3690,
                    3694
                ],
                [
                    3701,
                    3705
                ],
                [
                    3709,
                    3713
                ],
                [
                    3787,
                    3791
                ],
                [
                    3799,
                    3803
                ],
                [
                    3907,
                    3911
                ],
                [
                    4248,
                    4252
                ],
                [
                    4266,
                    4270
                ],
                [
                    4312,
                    4316
                ],
                [
                    4570,
                    4574
                ],
                [
                    4587,
                    4591
                ],
                [
                    4623,
                    4627
                ],
                [
                    5692,
                    5696
                ],
                [
                    5951,
                    5955
                ],
                [
                    6220,
                    6224
                ],
                [
                    6352,
                    6356
                ],
                [
                    6537,
                    6541
                ],
                [
                    6595,
                    6599
                ],
                [
                    6965,
                    6969
                ]
            ],
            "count": 29
        },
        {
            "name": "HincII",
            "locations": [
                [
                    1975,
                    1981
                ],
                [
                    4483,
                    4489
                ]
            ],
            "count": 2
        },
        {
            "name": "BglI",
            "locations": [
                [
                    1073,
                    1084
                ],
                [
                    4058,
                    4069
                ],
                [
                    5016,
                    5027
                ],
                [
                    5138,
                    5149
                ],
                [
                    5209,
                    5220
                ]
            ],
            "count": 5
        },
        {
            "name": "AvrI",
            "locations": [
                [
                    1362,
                    1368
                ],
                [
                    1654,
                    1660
                ],
                [
                    1846,
                    1852
                ],
                [
                    2554,
                    2560
                ],
                [
                    2587,
                    2593
                ],
                [
                    2620,
                    2626
                ],
                [
                    5526,
                    5532
                ],
                [
                    5559,
                    5565
                ],
                [
                    6157,
                    6163
                ],
                [
                    6935,
                    6941
                ]
            ],
            "count": 10
        },
        {
            "name": "XmaI",
            "locations": [
                [
                    1362,
                    1368
                ],
                [
                    2620,
                    2626
                ],
                [
                    5559,
                    5565
                ],
                [
                    6157,
                    6163
                ],
                [
                    6935,
                    6941
                ]
            ],
            "count": 5
        },
        {
            "name": "DraI",
            "locations": [
                [
                    3805,
                    3811
                ],
                [
                    4519,
                    4525
                ]
            ],
            "count": 2
        },
        {
            "name": "PvuII",
            "locations": [
                [
                    1954,
                    1960
                ],
                [
                    2263,
                    2269
                ],
                [
                    2338,
                    2344
                ]
            ],
            "count": 3
        },
        {
            "name": "HindIII",
            "locations": [
                [
                    1001,
                    1007
                ],
                [
                    1349,
                    1355
                ]
            ],
            "count": 2
        },
        {
            "name": "KpnI",
            "locations": [
                [
                    1218,
                    1224
                ],
                [
                    2624,
                    2630
                ],
                [
                    5563,
                    5569
                ],
                [
                    6763,
                    6769
                ]
            ],
            "count": 4
        },
        {
            "name": "NarI",
            "locations": [
                [
                    1855,
                    1861
                ],
                [
                    1963,
                    1969
                ],
                [
                    2592,
                    2598
                ],
                [
                    5531,
                    5537
                ],
                [
                    6572,
                    6578
                ]
            ],
            "count": 5
        },
        {
            "name": "BglII",
            "locations": [
                [
                    6594,
                    6600
                ]
            ],
            "count": 1
        },
        {
            "name": "StuI",
            "locations": [
                [
                    1601,
                    1607
                ],
                [
                    1823,
                    1829
                ]
            ],
            "count": 2
        },
        {
            "name": "NcoI",
            "locations": [
                [
                    1376,
                    1382
                ],
                [
                    1811,
                    1817
                ],
                [
                    5292,
                    5298
                ]
            ],
            "count": 3
        },
        {
            "name": "NdeI",
            "locations": [
                [
                    5165,
                    5171
                ],
                [
                    6580,
                    6586
                ],
                [
                    6588,
                    6594
                ]
            ],
            "count": 3
        },
        {
            "name": "Bsp24I",
            "locations": [
                [
                    1536,
                    1548
                ],
                [
                    3550,
                    3562
                ],
                [
                    3728,
                    3740
                ],
                [
                    5198,
                    5210
                ],
                [
                    5844,
                    5856
                ],
                [
                    6788,
                    6800
                ]
            ],
            "count": 6
        },
        {
            "name": "SmaI",
            "locations": [
                [
                    1362,
                    1368
                ],
                [
                    2620,
                    2626
                ],
                [
                    5559,
                    5565
                ],
                [
                    6157,
                    6163
                ],
                [
                    6935,
                    6941
                ]
            ],
            "count": 5
        },
        {
            "name": "AvaI",
            "locations": [
                [
                    1362,
                    1368
                ],
                [
                    1654,
                    1660
                ],
                [
                    1846,
                    1852
                ],
                [
                    2554,
                    2560
                ],
                [
                    2587,
                    2593
                ],
                [
                    2620,
                    2626
                ],
                [
                    5526,
                    5532
                ],
                [
                    5559,
                    5565
                ],
                [
                    6157,
                    6163
                ],
                [
                    6935,
                    6941
                ]
            ],
            "count": 10
        },
        {
            "name": "AvaII",
            "locations": [
                [
                    681,
                    686
                ],
                [
                    2409,
                    2414
                ],
                [
                    2422,
                    2427
                ],
                [
                    2477,
                    2482
                ],
                [
                    4082,
                    4087
                ],
                [
                    4304,
                    4309
                ],
                [
                    5713,
                    5718
                ],
                [
                    5843,
                    5848
                ],
                [
                    6064,
                    6069
                ],
                [
                    6394,
                    6399
                ],
                [
                    6751,
                    6756
                ],
                [
                    6799,
                    6804
                ],
                [
                    6842,
                    6847
                ],
                [
                    6944,
                    6949
                ]
            ],
            "count": 14
        },
        {
            "name": "PstI",
            "locations": [
                [
                    1729,
                    1735
                ],
                [
                    6094,
                    6100
                ],
                [
                    6276,
                    6282
                ]
            ],
            "count": 3
        },
        {
            "name": "SphI",
            "locations": [
                [
                    751,
                    757
                ]
            ],
            "count": 1
        },
        {
            "name": "ApaI",
            "locations": [
                [
                    890,
                    896
                ]
            ],
            "count": 1
        },
        {
            "name": "EcoRV",
            "locations": [
                [
                    2285,
                    2291
                ],
                [
                    2360,
                    2366
                ]
            ],
            "count": 2
        },
        {
            "name": "BamHI",
            "locations": [
                [
                    1366,
                    1372
                ]
            ],
            "count": 1
        },
        {
            "name": "HaeIII",
            "locations": [
                [
                    97,
                    101
                ],
                [
                    197,
                    201
                ],
                [
                    486,
                    490
                ],
                [
                    598,
                    602
                ],
                [
                    766,
                    770
                ],
                [
                    808,
                    812
                ],
                [
                    829,
                    833
                ],
                [
                    891,
                    895
                ],
                [
                    904,
                    908
                ],
                [
                    1081,
                    1085
                ],
                [
                    1247,
                    1251
                ],
                [
                    1300,
                    1304
                ],
                [
                    1407,
                    1411
                ],
                [
                    1462,
                    1466
                ],
                [
                    1495,
                    1499
                ],
                [
                    1546,
                    1550
                ],
                [
                    1602,
                    1606
                ],
                [
                    1789,
                    1793
                ],
                [
                    1824,
                    1828
                ],
                [
                    1903,
                    1907
                ],
                [
                    1938,
                    1942
                ],
                [
                    2047,
                    2051
                ],
                [
                    2091,
                    2095
                ],
                [
                    2275,
                    2279
                ],
                [
                    2320,
                    2324
                ],
                [
                    2350,
                    2354
                ],
                [
                    2395,
                    2399
                ],
                [
                    2866,
                    2870
                ],
                [
                    2889,
                    2893
                ],
                [
                    3062,
                    3066
                ],
                [
                    3073,
                    3077
                ],
                [
                    3091,
                    3095
                ],
                [
                    3525,
                    3529
                ],
                [
                    3986,
                    3990
                ],
                [
                    4066,
                    4070
                ],
                [
                    4333,
                    4337
                ],
                [
                    5015,
                    5019
                ],
                [
                    5208,
                    5212
                ],
                [
                    5744,
                    5748
                ],
                [
                    5878,
                    5882
                ],
                [
                    5914,
                    5918
                ],
                [
                    5926,
                    5930
                ],
                [
                    6155,
                    6159
                ],
                [
                    6161,
                    6165
                ],
                [
                    6285,
                    6289
                ],
                [
                    6306,
                    6310
                ],
                [
                    6371,
                    6375
                ],
                [
                    6585,
                    6589
                ]
            ],
            "count": 48
        },
        {
            "name": "NotI",
            "locations": [
                [
                    2089,
                    2097
                ]
            ],
            "count": 1
        },
        {
            "name": "XbaI",
            "locations": [
                [
                    2441,
                    2447
                ],
                [
                    6953,
                    6959
                ]
            ],
            "count": 2
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
    "misc": [],
    "restriction": [
        {
            "name": "HpaII",
            "locations": [
                [
                    349,
                    353
                ],
                [
                    457,
                    461
                ],
                [
                    698,
                    702
                ],
                [
                    1090,
                    1094
                ],
                [
                    1157,
                    1161
                ],
                [
                    1208,
                    1212
                ],
                [
                    1334,
                    1338
                ],
                [
                    1457,
                    1461
                ],
                [
                    1466,
                    1470
                ],
                [
                    1481,
                    1485
                ],
                [
                    1830,
                    1834
                ],
                [
                    2541,
                    2545
                ],
                [
                    2687,
                    2691
                ],
                [
                    2695,
                    2699
                ],
                [
                    2719,
                    2723
                ],
                [
                    2725,
                    2729
                ],
                [
                    2747,
                    2751
                ],
                [
                    2911,
                    2915
                ],
                [
                    3106,
                    3110
                ],
                [
                    3151,
                    3155
                ],
                [
                    3497,
                    3501
                ],
                [
                    3516,
                    3520
                ],
                [
                    3739,
                    3743
                ],
                [
                    3767,
                    3771
                ],
                [
                    3808,
                    3812
                ],
                [
                    4065,
                    4069
                ],
                [
                    4099,
                    4103
                ],
                [
                    4166,
                    4170
                ],
                [
                    4276,
                    4280
                ],
                [
                    4518,
                    4522
                ]
            ],
            "count": 30
        },
        {
            "name": "ApoI",
            "locations": [
                [
                    500,
                    506
                ],
                [
                    1573,
                    1579
                ],
                [
                    1683,
                    1689
                ],
                [
                    1740,
                    1746
                ],
                [
                    2104,
                    2110
                ]
            ],
            "count": 5
        },
        {
            "name": "SacI",
            "locations": [
                [
                    2310,
                    2316
                ],
                [
                    3887,
                    3893
                ]
            ],
            "count": 2
        },
        {
            "name": "EcoRI",
            "locations": [
                [
                    1573,
                    1579
                ]
            ],
            "count": 1
        },
        {
            "name": "AlwNI",
            "locations": [
                [
                    2619,
                    2628
                ]
            ],
            "count": 1
        },
        {
            "name": "AluI",
            "locations": [
                [
                    21,
                    25
                ],
                [
                    85,
                    89
                ],
                [
                    178,
                    182
                ],
                [
                    293,
                    297
                ],
                [
                    717,
                    721
                ],
                [
                    997,
                    1001
                ],
                [
                    2093,
                    2097
                ],
                [
                    2311,
                    2315
                ],
                [
                    2923,
                    2927
                ],
                [
                    3001,
                    3005
                ],
                [
                    3253,
                    3257
                ],
                [
                    3339,
                    3343
                ],
                [
                    3364,
                    3368
                ],
                [
                    3888,
                    3892
                ],
                [
                    4172,
                    4176
                ],
                [
                    4272,
                    4276
                ],
                [
                    4335,
                    4339
                ]
            ],
            "count": 17
        },
        {
            "name": "AccI",
            "locations": [
                [
                    2055,
                    2061
                ]
            ],
            "count": 1
        },
        {
            "name": "MboI",
            "locations": [
                [
                    389,
                    393
                ],
                [
                    762,
                    766
                ],
                [
                    866,
                    870
                ],
                [
                    1212,
                    1216
                ],
                [
                    1401,
                    1405
                ],
                [
                    1492,
                    1496
                ],
                [
                    1583,
                    1587
                ],
                [
                    1833,
                    1837
                ],
                [
                    2235,
                    2239
                ],
                [
                    2326,
                    2330
                ],
                [
                    2344,
                    2348
                ],
                [
                    2813,
                    2817
                ],
                [
                    2937,
                    2941
                ],
                [
                    3528,
                    3532
                ],
                [
                    3864,
                    3868
                ],
                [
                    3947,
                    3951
                ],
                [
                    4288,
                    4292
                ],
                [
                    4306,
                    4310
                ],
                [
                    4352,
                    4356
                ],
                [
                    4610,
                    4614
                ],
                [
                    4627,
                    4631
                ],
                [
                    4663,
                    4667
                ]
            ],
            "count": 22
        },
        {
            "name": "Sau3AI",
            "locations": [
                [
                    389,
                    393
                ],
                [
                    762,
                    766
                ],
                [
                    866,
                    870
                ],
                [
                    1212,
                    1216
                ],
                [
                    1401,
                    1405
                ],
                [
                    1492,
                    1496
                ],
                [
                    1583,
                    1587
                ],
                [
                    1833,
                    1837
                ],
                [
                    2235,
                    2239
                ],
                [
                    2326,
                    2330
                ],
                [
                    2344,
                    2348
                ],
                [
                    2813,
                    2817
                ],
                [
                    2937,
                    2941
                ],
                [
                    3528,
                    3532
                ],
                [
                    3864,
                    3868
                ],
                [
                    3947,
                    3951
                ],
                [
                    4288,
                    4292
                ],
                [
                    4306,
                    4310
                ],
                [
                    4352,
                    4356
                ],
                [
                    4610,
                    4614
                ],
                [
                    4627,
                    4631
                ],
                [
                    4663,
                    4667
                ]
            ],
            "count": 22
        },
        {
            "name": "HincII",
            "locations": [
                [
                    271,
                    277
                ]
            ],
            "count": 1
        },
        {
            "name": "BglI",
            "locations": [
                [
                    2694,
                    2705
                ],
                [
                    4098,
                    4109
                ]
            ],
            "count": 2
        },
        {
            "name": "AvrI",
            "locations": [
                [
                    2334,
                    2340
                ],
                [
                    3603,
                    3609
                ]
            ],
            "count": 2
        },
        {
            "name": "DraI",
            "locations": [
                [
                    1995,
                    2001
                ],
                [
                    4559,
                    4565
                ]
            ],
            "count": 2
        },
        {
            "name": "PvuII",
            "locations": [
                [
                    84,
                    90
                ],
                [
                    177,
                    183
                ],
                [
                    3252,
                    3258
                ]
            ],
            "count": 3
        },
        {
            "name": "NarI",
            "locations": [
                [
                    136,
                    142
                ],
                [
                    1318,
                    1324
                ],
                [
                    1432,
                    1438
                ],
                [
                    1453,
                    1459
                ]
            ],
            "count": 4
        },
        {
            "name": "BglII",
            "locations": [
                [
                    1582,
                    1588
                ]
            ],
            "count": 1
        },
        {
            "name": "HpaI",
            "locations": [
                [
                    271,
                    277
                ]
            ],
            "count": 1
        },
        {
            "name": "NdeI",
            "locations": [
                [
                    1605,
                    1611
                ]
            ],
            "count": 1
        },
        {
            "name": "Bsp24I",
            "locations": [
                [
                    920,
                    932
                ],
                [
                    2020,
                    2032
                ]
            ],
            "count": 2
        },
        {
            "name": "BclI",
            "locations": [
                [
                    761,
                    767
                ],
                [
                    2812,
                    2818
                ]
            ],
            "count": 2
        },
        {
            "name": "AvaI",
            "locations": [
                [
                    2334,
                    2340
                ],
                [
                    3603,
                    3609
                ]
            ],
            "count": 2
        },
        {
            "name": "AvaII",
            "locations": [
                [
                    224,
                    229
                ],
                [
                    2261,
                    2266
                ],
                [
                    2975,
                    2980
                ],
                [
                    4122,
                    4127
                ],
                [
                    4344,
                    4349
                ]
            ],
            "count": 5
        },
        {
            "name": "SphI",
            "locations": [
                [
                    1304,
                    1310
                ]
            ],
            "count": 1
        },
        {
            "name": "ApaI",
            "locations": [
                [
                    568,
                    574
                ]
            ],
            "count": 1
        },
        {
            "name": "BamHI",
            "locations": [
                [
                    2325,
                    2331
                ]
            ],
            "count": 1
        },
        {
            "name": "HaeIII",
            "locations": [
                [
                    102,
                    106
                ],
                [
                    200,
                    204
                ],
                [
                    569,
                    573
                ],
                [
                    915,
                    919
                ],
                [
                    1050,
                    1054
                ],
                [
                    1272,
                    1276
                ],
                [
                    1336,
                    1340
                ],
                [
                    1344,
                    1348
                ],
                [
                    1468,
                    1472
                ],
                [
                    1777,
                    1781
                ],
                [
                    2178,
                    2182
                ],
                [
                    2389,
                    2393
                ],
                [
                    2460,
                    2464
                ],
                [
                    2723,
                    2727
                ],
                [
                    2867,
                    2871
                ],
                [
                    2898,
                    2902
                ],
                [
                    2915,
                    2919
                ],
                [
                    2949,
                    2953
                ],
                [
                    3044,
                    3048
                ],
                [
                    3108,
                    3112
                ],
                [
                    3195,
                    3199
                ],
                [
                    3509,
                    3513
                ],
                [
                    3540,
                    3544
                ],
                [
                    3547,
                    3551
                ],
                [
                    3680,
                    3684
                ],
                [
                    3758,
                    3762
                ],
                [
                    3765,
                    3769
                ],
                [
                    4026,
                    4030
                ],
                [
                    4106,
                    4110
                ],
                [
                    4373,
                    4377
                ]
            ],
            "count": 30
        },
        {
            "name": "XhoI",
            "locations": [
                [
                    2334,
                    2340
                ]
            ],
            "count": 1
        }
    ]
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
    "misc": [],
    "restriction": [
        {
            "name": "HpaII",
            "locations": [
                [
                    976,
                    980
                ],
                [
                    1023,
                    1027
                ],
                [
                    1894,
                    1898
                ],
                [
                    1928,
                    1932
                ],
                [
                    2455,
                    2459
                ],
                [
                    2602,
                    2606
                ],
                [
                    2628,
                    2632
                ],
                [
                    2818,
                    2822
                ],
                [
                    3222,
                    3226
                ],
                [
                    3256,
                    3260
                ],
                [
                    3323,
                    3327
                ],
                [
                    3433,
                    3437
                ],
                [
                    3675,
                    3679
                ],
                [
                    4442,
                    4446
                ],
                [
                    6845,
                    6849
                ],
                [
                    7533,
                    7537
                ],
                [
                    8076,
                    8080
                ],
                [
                    8137,
                    8141
                ],
                [
                    8283,
                    8287
                ]
            ],
            "count": 19
        },
        {
            "name": "ApoI",
            "locations": [
                [
                    388,
                    394
                ],
                [
                    737,
                    743
                ],
                [
                    1489,
                    1495
                ],
                [
                    4237,
                    4243
                ],
                [
                    4312,
                    4318
                ],
                [
                    4552,
                    4558
                ],
                [
                    5163,
                    5169
                ],
                [
                    5317,
                    5323
                ],
                [
                    5676,
                    5682
                ],
                [
                    6706,
                    6712
                ],
                [
                    8272,
                    8278
                ]
            ],
            "count": 11
        },
        {
            "name": "SacI",
            "locations": [
                [
                    6032,
                    6038
                ]
            ],
            "count": 1
        },
        {
            "name": "EcoRI",
            "locations": [
                [
                    737,
                    743
                ],
                [
                    8272,
                    8278
                ]
            ],
            "count": 2
        },
        {
            "name": "AlwNI",
            "locations": [
                [
                    1454,
                    1463
                ],
                [
                    2659,
                    2668
                ]
            ],
            "count": 2
        },
        {
            "name": "AluI",
            "locations": [
                [
                    325,
                    329
                ],
                [
                    792,
                    796
                ],
                [
                    803,
                    807
                ],
                [
                    812,
                    816
                ],
                [
                    1107,
                    1111
                ],
                [
                    1149,
                    1153
                ],
                [
                    1341,
                    1345
                ],
                [
                    1698,
                    1702
                ],
                [
                    1707,
                    1711
                ],
                [
                    1764,
                    1768
                ],
                [
                    1889,
                    1893
                ],
                [
                    1908,
                    1912
                ],
                [
                    2189,
                    2193
                ],
                [
                    2415,
                    2419
                ],
                [
                    2505,
                    2509
                ],
                [
                    2551,
                    2555
                ],
                [
                    2808,
                    2812
                ],
                [
                    3329,
                    3333
                ],
                [
                    3429,
                    3433
                ],
                [
                    3492,
                    3496
                ],
                [
                    4716,
                    4720
                ],
                [
                    5079,
                    5083
                ],
                [
                    5600,
                    5604
                ],
                [
                    5827,
                    5831
                ],
                [
                    6033,
                    6037
                ],
                [
                    6496,
                    6500
                ],
                [
                    7353,
                    7357
                ],
                [
                    7390,
                    7394
                ],
                [
                    8189,
                    8193
                ],
                [
                    8291,
                    8295
                ]
            ],
            "count": 30
        },
        {
            "name": "AccI",
            "locations": [
                [
                    590,
                    596
                ],
                [
                    2019,
                    2025
                ],
                [
                    6533,
                    6539
                ]
            ],
            "count": 3
        },
        {
            "name": "MboI",
            "locations": [
                [
                    210,
                    214
                ],
                [
                    361,
                    365
                ],
                [
                    376,
                    380
                ],
                [
                    526,
                    530
                ],
                [
                    602,
                    606
                ],
                [
                    720,
                    724
                ],
                [
                    1474,
                    1478
                ],
                [
                    1768,
                    1772
                ],
                [
                    2815,
                    2819
                ],
                [
                    2890,
                    2894
                ],
                [
                    2901,
                    2905
                ],
                [
                    2909,
                    2913
                ],
                [
                    2987,
                    2991
                ],
                [
                    2999,
                    3003
                ],
                [
                    3104,
                    3108
                ],
                [
                    3445,
                    3449
                ],
                [
                    3463,
                    3467
                ],
                [
                    3509,
                    3513
                ],
                [
                    3767,
                    3771
                ],
                [
                    3784,
                    3788
                ],
                [
                    3820,
                    3824
                ],
                [
                    4307,
                    4311
                ],
                [
                    5028,
                    5032
                ],
                [
                    6303,
                    6307
                ],
                [
                    7873,
                    7877
                ],
                [
                    8030,
                    8034
                ],
                [
                    8057,
                    8061
                ],
                [
                    8311,
                    8315
                ]
            ],
            "count": 28
        },
        {
            "name": "Sau3AI",
            "locations": [
                [
                    210,
                    214
                ],
                [
                    361,
                    365
                ],
                [
                    376,
                    380
                ],
                [
                    526,
                    530
                ],
                [
                    602,
                    606
                ],
                [
                    720,
                    724
                ],
                [
                    1474,
                    1478
                ],
                [
                    1768,
                    1772
                ],
                [
                    2815,
                    2819
                ],
                [
                    2890,
                    2894
                ],
                [
                    2901,
                    2905
                ],
                [
                    2909,
                    2913
                ],
                [
                    2987,
                    2991
                ],
                [
                    2999,
                    3003
                ],
                [
                    3104,
                    3108
                ],
                [
                    3445,
                    3449
                ],
                [
                    3463,
                    3467
                ],
                [
                    3509,
                    3513
                ],
                [
                    3767,
                    3771
                ],
                [
                    3784,
                    3788
                ],
                [
                    3820,
                    3824
                ],
                [
                    4307,
                    4311
                ],
                [
                    5028,
                    5032
                ],
                [
                    6303,
                    6307
                ],
                [
                    7873,
                    7877
                ],
                [
                    8030,
                    8034
                ],
                [
                    8057,
                    8061
                ],
                [
                    8311,
                    8315
                ]
            ],
            "count": 28
        },
        {
            "name": "HincII",
            "locations": [
                [
                    1301,
                    1307
                ],
                [
                    1437,
                    1443
                ],
                [
                    3680,
                    3686
                ]
            ],
            "count": 3
        },
        {
            "name": "BglI",
            "locations": [
                [
                    3255,
                    3266
                ]
            ],
            "count": 1
        },
        {
            "name": "AvrI",
            "locations": [
                [
                    728,
                    734
                ],
                [
                    8282,
                    8288
                ]
            ],
            "count": 2
        },
        {
            "name": "XmaI",
            "locations": [
                [
                    8282,
                    8288
                ]
            ],
            "count": 1
        },
        {
            "name": "DraI",
            "locations": [
                [
                    86,
                    92
                ],
                [
                    254,
                    260
                ],
                [
                    1102,
                    1108
                ],
                [
                    3005,
                    3011
                ],
                [
                    3024,
                    3030
                ],
                [
                    3716,
                    3722
                ],
                [
                    5791,
                    5797
                ],
                [
                    7681,
                    7687
                ]
            ],
            "count": 8
        },
        {
            "name": "HindIII",
            "locations": [
                [
                    7352,
                    7358
                ],
                [
                    8290,
                    8296
                ]
            ],
            "count": 2
        },
        {
            "name": "KpnI",
            "locations": [
                [
                    8078,
                    8084
                ]
            ],
            "count": 1
        },
        {
            "name": "BglII",
            "locations": [
                [
                    1473,
                    1479
                ]
            ],
            "count": 1
        },
        {
            "name": "StuI",
            "locations": [
                [
                    4248,
                    4254
                ]
            ],
            "count": 1
        },
        {
            "name": "NdeI",
            "locations": [
                [
                    117,
                    123
                ],
                [
                    2070,
                    2076
                ],
                [
                    7183,
                    7189
                ],
                [
                    8150,
                    8156
                ]
            ],
            "count": 4
        },
        {
            "name": "Bsp24I",
            "locations": [
                [
                    2750,
                    2762
                ],
                [
                    2928,
                    2940
                ]
            ],
            "count": 2
        },
        {
            "name": "BclI",
            "locations": [
                [
                    1767,
                    1773
                ],
                [
                    5027,
                    5033
                ]
            ],
            "count": 2
        },
        {
            "name": "SmaI",
            "locations": [
                [
                    8282,
                    8288
                ]
            ],
            "count": 1
        },
        {
            "name": "AvaI",
            "locations": [
                [
                    728,
                    734
                ],
                [
                    8282,
                    8288
                ]
            ],
            "count": 2
        },
        {
            "name": "AvaII",
            "locations": [
                [
                    161,
                    166
                ],
                [
                    404,
                    409
                ],
                [
                    3279,
                    3284
                ],
                [
                    3501,
                    3506
                ],
                [
                    4900,
                    4905
                ],
                [
                    6683,
                    6688
                ]
            ],
            "count": 6
        },
        {
            "name": "PstI",
            "locations": [
                [
                    766,
                    772
                ],
                [
                    3382,
                    3388
                ]
            ],
            "count": 2
        },
        {
            "name": "SphI",
            "locations": [
                [
                    8068,
                    8074
                ]
            ],
            "count": 1
        },
        {
            "name": "EcoRV",
            "locations": [
                [
                    4951,
                    4957
                ],
                [
                    5589,
                    5595
                ],
                [
                    8319,
                    8325
                ]
            ],
            "count": 3
        },
        {
            "name": "BamHI",
            "locations": [
                [
                    719,
                    725
                ],
                [
                    8310,
                    8316
                ]
            ],
            "count": 2
        },
        {
            "name": "HaeIII",
            "locations": [
                [
                    1030,
                    1034
                ],
                [
                    1307,
                    1311
                ],
                [
                    1509,
                    1513
                ],
                [
                    2262,
                    2266
                ],
                [
                    2273,
                    2277
                ],
                [
                    2291,
                    2295
                ],
                [
                    2725,
                    2729
                ],
                [
                    3183,
                    3187
                ],
                [
                    3263,
                    3267
                ],
                [
                    3530,
                    3534
                ],
                [
                    4117,
                    4121
                ],
                [
                    4249,
                    4253
                ],
                [
                    4574,
                    4578
                ],
                [
                    7977,
                    7981
                ],
                [
                    8135,
                    8139
                ],
                [
                    8139,
                    8143
                ],
                [
                    8301,
                    8305
                ]
            ],
            "count": 17
        },
        {
            "name": "NotI",
            "locations": [
                [
                    8299,
                    8307
                ]
            ],
            "count": 1
        },
        {
            "name": "XhoI",
            "locations": [
                [
                    728,
                    734
                ]
            ],
            "count": 1
        },
        {
            "name": "ClaI",
            "locations": [
                [
                    8062,
                    8068
                ]
            ],
            "count": 1
        }
    ]
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
