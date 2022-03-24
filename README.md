# **Endpoints**:
## **Get Features** (POST request at /features):
#### Gets promoters, terminators, selectable markers, reporter genes, replication origins, regulatory sequences, affinity tags, and miscellaneous features.
### **Input JSON fields**:
* sequence : String of raw sequence with no headers
### **Output JSON fields**:
* promoters: Array of Feature Objects that represent promoters
* terminators: Array of Feature Objects that represent terminators
* regulatorySequences: Array of Feature Objects that represent regulatorySequences
* replicationOrigins: Array of Feature Objects that represent replicationOrigins
* selectableMarkers: Array of Feature Objects that represent selectableMarkers
* reporterGenes: Array of Feature Objects that represent reporterGenes
* affinityTags: Array of Feature Objects that represent affinityTags
* localizationSequences: Array of Feature Objects that represent localization sequences
* twoHybridGenes: Array of Feature Objects that represent two hybrid genes
* genes: Array of Feature Objects that represent genes
* primers: Array of Feature Objects that represent primers
* misc: Array of Feature Objects that represent miscellaneousFeatures
#### Feature has properties:
* name : String
* start : Integer
* stop : Integer
* legend : String

## **Get Sequence** (GET request at /plasmids):
#### Gets the sequence given the plasmid name.
### **Input query parameters**:
* ?name=theNameOfThePlasmid
### **Output JSON fields**:
* sequence: String of raw sequence with no headers

## **Get Metadata** (GET request at /plasmids/meta):
#### Gets all metadata except sequence for all plasmids in the database.
### **Output JSON fields**:
* plasmids: List of Plasmid objects
#### Plasmid has properties:
* name : String
* sequenceLength : Integer
* backbone : String
* supplier : String
* expression : String
* features : String of comma separated feature names

## **Increment Plasmid Popularity** (POST request at /plasmids/popularity):
#### Takes in a plasmid name and increments that plasmid's popularity if it exists in the database.
### **Input JSON fields**:
* name: String

# **Deployment Details**:
## Steps to create a new db from updated features.fasta.nt file:
* Navigate to \plasmapperAPI\fsdSearch\featureDB\ and run:
* *path\to\blast\installation\blast-2.12.0+\bin\makeblastdb.exe -in 'features.fasta.nt' -dbtype 'nucl'*
