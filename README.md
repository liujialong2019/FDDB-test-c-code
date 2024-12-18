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
baseDir represents the directory after decompressing the test image package downloaded from https://vis-www.cs.umass.edu/fddb/ <br />
listFile is like image.txt above <br />
detFile needs to correspond to the path in image.txt one by one, and evaluate.cpp supports two annotation types: ellipse and rectangle. The ellipse annotation type is <major_axis_radius minor_axis_radius angle center_x center_y 1>, and the rectangle annotation type is <left_x top_y width height detection_score> <br />
annotFile has been merged into one file, such as label.txt above
## Attention
1、Some possible errors may be caused by C++ syntax errors, environment variables, or missing .dll files. <br />
2、This is not a complete FDDB test process, it is limited to generating two discrete and continuous score txt files
## Citations
```
@TechReport{fddbTech,
  author = {Vidit Jain and Erik Learned-Miller},
  title =  {FDDB: A Benchmark for Face Detection in Unconstrained Settings},
  institution =  {University of Massachusetts, Amherst},
  year = {2010},
  number = {UM-CS-2010-009}
  }
```
