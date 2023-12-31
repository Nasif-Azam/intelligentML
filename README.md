# Iltelligent Machine Learning Task using Python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)    

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![image](https://img.shields.io/pypi/v/intelligentML.svg)](https://pypi.python.org/pypi/intelligentML) [![image](https://img.shields.io/conda/vn/conda-forge/intelligentML.svg)](https://anaconda.org/conda-forge/intelligentML) [![image](https://colab.research.google.com/assets/colab-badge.svg)]() [![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![image](https://github.com/gee-community/geemap/workflows/docs/badge.svg)](https://nasif-azam.github.io/intelligentML)

**An intelligent machine learning package. A Python library for handling duplicate data and performing data preprocessing on datasets. This library provides functions to identify and remove duplicate rows, handle missing values, and prepare data for analysis. All you have to do just provide the dataset url or path the library automatically do those tasks.**


-   Free software: MIT license
-   Documentation: https://Nasif-Azam.github.io/intelligentML

## Functionality of the Package

- hd_and_dp(dataPath) : Both handle duplication and data preprocessing by sending the dataset url or path link.
- handle_duplication(dataPath) : Handle duplication by sending the dataset url or path link.
- dataPreprocessing(dataPath) : Data preprocessing by sending the dataset url or path link.

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.
 ```
  pip install intelligentML
  ```
## Example-1

 ```
# test.py:

from intelligentML import hd_and_dp
url = "example.csv"
finalDataset = hd_and_dp(url)
print(f"Final Preprocessed Dataset: \n{finalDataset}")
  ```
## Example-2

 ```
# test.py:

from intelligentML import handle_duplication
url = "example.csv"
NoDupDataset = handle_duplication(url)
print(f"Dataset Without Duplications: \n{NoDupDataset}")
  ```
## Example-3

 ```
# test.py:

from intelligentML import dataPreprocessing
url = "example.csv"
PreproccessedDataset = dataPreprocessing(url)
print(f"Preprocessed Dataset: \n{PreproccessedDataset}")
  ```

## Run the following Script.
 ```
  python test.py
 ```

## Note 
- It is a very tiny package according to the large ML areas. I will update the package till to advance.
