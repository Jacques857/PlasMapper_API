# **Endpoints**:
## **Get Features** (GET request at /features):
#### Gets promoters, terminators, selectable markers, reporter genes, replication origins, regulatory sequences, affinity tags, and miscellaneous features.
### **Input JSON fields**:
* sequence : String
### **Output JSON fields**:
* promoters: Array of Feature Objects that represent promoters
* terminators: Array of Feature Objects that represent terminators
* regulatorySequences: Array of Feature Objects that represent regulatorySequences
* replicationOrigins: Array of Feature Objects that represent replicationOrigins
* selectableMarkers: Array of Feature Objects that represent selectableMarkers
* reporterGenes: Array of Feature Objects that represent reporterGenes
* affinityTags: Array of Feature Objects that represent affinityTags
* miscellaneousFeatures: Array of Feature Objects that represent miscellaneousFeatures
#### Feature has properties:
* name : String
* start : Integer
* stop : Integer
* legend : String
