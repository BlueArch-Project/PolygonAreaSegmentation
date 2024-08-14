# PolygonAreaSegmentation


## Overview
The meaPolygon function calculates the area of polygons based on coordinates provided in a text file and corresponding image dimensions. This function is useful for tasks where polygonal regions of an image need to be analyzed, such as in image segmentation or object detection.

Additionally, this function is designed to work with text files formatted for semantic segmentation in the YOLO format. This means that it can accurately process polygon coordinates that are normalized relative to image dimensions, as commonly used in YOLO-based object detection and segmentation tasks.

[![PyPI version](https://badge.fury.io/py/meaPolygon.svg)](https://badge.fury.io/py/meaPolygon)
[![GitHub stars](https://img.shields.io/github/stars/BlueArch-Project/PolygonAreaSegmentation.svg)](https://github.com/BlueArch-Project/PolygonAreaSegmentation/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/BlueArch-Project/PolygonAreaSegmentation.svg)](https://github.com/BlueArch-Project/PolygonAreaSegmentation/issues)
[![GitHub license](https://img.shields.io/github/license/BlueArch-Project/PolygonAreaSegmentation.svg)](https://github.com/BlueArch-Project/PolygonAreaSegmentation/blob/main/LICENSE)
[![Main Project](https://img.shields.io/badge/GitHub-Main_Project-brightgreen)](https://github.com/BlueArch-Project)



<p align="center">
  <img src="https://github.com/BlueArch-Project/PolygonAreaSegmentation/raw/main/examples/data/readme1.png" width="300" alt="Original" />
  <img src="https://github.com/BlueArch-Project/PolygonAreaSegmentation/raw/main/examples/data/readme2.png" width="300" alt="Yolo format Semantic Segmentation" />
</p>
<p align="center">
  <b>Original</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Yolo format Semantic Segmentation</b>
</p>



## Installation

First, install the necessary dependencies. After cloning or downloading this project, run the following command to install the package:

```bash
pip3 install .
pip install meaPolygon
```

This will install the module containing the meaPolygon function, making it available for use in your Python environment.



## Usage

1. Prepare the YOLO Format Text File
Prepare a text file formatted for YOLO semantic segmentation. Each line should contain a label and normalized polygon coordinates.

Example:
```
0 0.1 0.2 0.3 0.4 0.5 0.6
1 0.2 0.3 0.4 0.5 0.6 0.7
```

2. Create a Python Script

```python
from my_module.polygon_area import meaPolygon

# Specify the paths to the image file and the text file
img_path = "examples/data/example.png"
txt_path = "examples/data/example.txt"

# Calculate the polygon areas
areas = meaPolygon(img_path, txt_path)

# Display the results
print("Calculated Polygon Areas:", areas)

```

3. Run the Script

```bash
python3 your_script.py
```

4. Expected Output
When you run the script, you should see output similar to the following, depending on the content of your text file and image dimensions:

```
Calculated Polygon Areas: [15.34, 28.92, 35.76]
```

Each value in the list corresponds to the area of a polygon defined in the text file. The values are in square units based on the dimensions of the input image.



## Contact & Support
f you have any questions, issues, or suggestions, please feel free to contact us:

- BlueArch : https://bluearch.or.jp/
- Main Project : https://github.com/BlueArch-Project
- Email: aki2262hiro103kawano@gmail.com
- GitHub Issues: https://github.com/BlueArch-Project/PolygonAreaSegmentation/issues


For more detailed discussions, bug reports, or feature requests, please open an issue on the GitHub repository. We appreciate your feedback and contributions!