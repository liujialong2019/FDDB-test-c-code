# FDDB-test-c++-code
Official C++ code used to generate tempDiscROC.txt and tempContROC.txt
## Requirements
Opencv 2.x is ok, for example, opencv2.4.11 on Windows 11, Visual Studio 2019 Community Edition
## DataSets
The following four variables need to be modified in evaluate.cpp:
```
  string baseDir = "F:/scratch/Data/facesInTheWild/";
  string listFile = "F:/scratch/Data/detectionResults/FDDB/imList.txt";
  string detFile = "F:/scratch/Data/detectionResults/FDDB/MikolajczykDets.txt";
  string annotFile = "F:/scratch/Data/detectionResults/FDDB/ellipseList.txt";
```
