from urllib import response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from .FSDSearch import FSDSearch
from .serializers import FeatureSerializer, SequenceSerializer
import time, os, json

# Returns the metadata of all plasmids in the database
@api_view(['GET'])
def getPlasmidMeta(request):

    # load in the json file
    file = open(os.path.join(os.path.dirname(__file__), "metadata.json"), 'r')
    data = json.load(file)
    
    responseDict = {"plasmids" : data}
    return JsonResponse(responseDict)

# Returns a sequence given the name of a plasmid as a query parameter
@api_view(['GET'])
def getPlasmidSequence(request):
    name = request.GET.get("name")

    # load in the json file
    file = open(os.path.join(os.path.dirname(__file__), "sequences.json"), 'r')
    data = json.load(file)

    # check if the given name matches any plasmid in the database
    match = False
    sequence = None
    for dict in data:
        if dict["name"] == name:
            match = True
            sequence = dict["sequence"]
            break
    
    # if no plasmid with the given name was found return 404
    if not match:
        return getResponse(404, "Plasmid with name '" + name + "' was not found")
    
    serializedData = SequenceSerializer({"sequence" : sequence}).data
    return JsonResponse(serializedData)

# Performs a feature site database search given "sequence" in the request body. Outputs to outputFileName
@api_view(['POST'])
@parser_classes([JSONParser])
def doFsdSearch(request):
    # get and validate the sequence from the request body
    try:
        sequence = request.data["sequence"]
        if type(sequence) != type(""):
            return getResponse(400, "'sequence' must be of type String")
    except KeyError:
        return getResponse(400, "Missing 'sequence' from the JSON body.")
    
    # set path at which to store files
    currentTime = str(time.time()).replace(".", "") # the number of seconds since epoch
    path = os.path.dirname(__file__) + '\\temp\\'
    inputFileName = path + "input" + currentTime + ".txt"
    outputFileName = path + "output" + currentTime + ".txt"

    # fill input file with sequence in FASTA format
    writeToFile(sequence.replace("\n", ""), inputFileName)

    # perform FSDSearch
    search = FSDSearch(inputFileName, outputFileName)

    # extract fields into a dict
    responseDict = {
        "promoters" : search.promoters,
        "terminators" : search.terminators,
        "regulatorySequences" : search.regulatorySequences,
        "replicationOrigins" : search.replicationOrigins,
        "selectableMarkers" : search.selectableMarkers,
        "reporterGenes" : search.reporterGenes,
        "affinityTags" : search.affinityTags,
        "localizationSequences" : search.localizationSequences,
        "twoHybridGenes" : search.twoHybridGenes,
        "genes" : search.genes,
        "primers" : search.primers,
        "misc" : search.misc,
    }

    # serialize data
    for key in responseDict:
        serializer = FeatureSerializer(responseDict[key], many = True)
        responseDict[key] = serializer.data

    return JsonResponse(responseDict)

# Write a raw sequence "seq" to a file at path "fileName" in FASTA format
def writeToFileFasta(seq, fileName):
    f = open(fileName, 'w')

    # write 60 characters from seq on each line
    length = len(seq)
    index = 0
    while length > 60:
        f.write(seq[index : index + 60] + '\n')
        index += 60
        length -= 60

    # write the remaining <60 characters from seq on the last line
    if length > 0:
        f.write(seq[index :])

# Write a String "seq" to a file at path "fileName"
def writeToFile(seq, fileName):
    f = open(fileName, 'w')
    f.write(seq)

# Return an HttpResponse object given status_code and reason_phrase
def getResponse(status_code, reason_phrase):
    response = HttpResponse()
    response.status_code = status_code
    response.reason_phrase = reason_phrase
    return response