# **Endpoints**:
## **Get Features** (GET request at /features):
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
* misc: Array of Feature Objects that represent miscellaneousFeatures
#### Feature has properties:
* name : String
* start : Integer
* stop : Integer
* legend : String

# **Deployment Details**:
## Steps to create a new db from updated features.fasta.nt file:
* Navigate to \plasmapperAPI\fsdSearch\featureDB\ and run:
* *path\to\blast\installation\blast-2.12.0+\bin\makeblastdb.exe -in 'features.fasta.nt' -dbtype 'nucl'*