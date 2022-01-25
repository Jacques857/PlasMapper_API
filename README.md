# **Endpoints**:
## **Get Features**:
#### Gets promoters, terminators, selectable markers, reporter genes, replication origins, regulatory sequences, affinity tags, and miscellaneous features.
### **Input JSON fields**:
* sequence : String
### **Output JSON fields**:
* promoters: Array of Feature Objects that represent promoters
* terminators: Array of Feature Objects that represent terminators
* regulatory sequences: Array of Feature Objects that represent regulatory sequences
* replication origins: Array of Feature Objects that represent replication origins
* selectable markers: Array of Feature Objects that represent selectable markers
* reporter genes: Array of Feature Objects that represent reporter genes
* affinity tags: Array of Feature Objects that represent affinity tags
* miscellaneous features: Array of Feature Objects that represent miscellaneous features
#### Feature has properties:
* name : String
* start : Integer
* stop : Integer
* legend : String
