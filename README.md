## Metabolic Flux Distributions Across Eight Microbial Organisms
Maastricht University - Maastricht Science Programme
Course: MAT2007 - Introduction to Programming
Name: Asya Özzeybek


## Project Description
This project compares metabolic flux distributions across eight microbial organisms for glycolysis, the TCA cycle, and the phosphate pathway (PPP) using descriptive statistics and boxplots. Python is used to clean the data, assign the KEGG reaction IDs to pathways, calculate descriptive statistics and visualize the data using boxplots.

## Installation
Install Python 3.14.7 from https://www.python.org/downloads/release/python-3147/. Using Visual Studio Code is recommended, install Microsoft Python extension and select your Pyhton interpreter. 

Open a terminal in the MAT2007Project.py folder and install the required packages: 

```bash
python -m pip install pandas numpy matplotlib seaborn openpyxl
```
## Dependencies
- NumPy: for the statistical analysis
- pandas: for data cleaning and analysis
- Matplotlib: data visualization in the form of boxplots
- seaborn: #for making several panels at once for the boxplot
- openpyxl: to read the excel file

## Execution:
To organize code execution the program is separated into functions that are called following user input. The user presses Enter to initiate each step and display its results.

## Conditions
The actions required for the successful execution of the project are listed bellow:
- The dataset (MAT2007RawData.xlsx) must be in the same folder as the code (MAT2007Project.py). 
- Press Enter when prompted in the terminal with "to .... press enter"
- Close the first plot window so the program can produce the second plot.

## Files:
- MAT2007Project.py: Python analysis with comments
- MAT2007RawData.xlsx: Input dataset
- MAT2007_Project_Report.pdf: Project report
- README.md: Pproject description and instructions 

## Outputs: 
- flux_data_including_pathways.csv:
  data set after KEGG reaction IDs are matched with the pathways
- data_analysis.csv:
  Descriptive statistics for each species–pathway group
- pathway_boxplot.png:
  Separate boxplots for glycolysis, TCA, and PPP
- species_boxplot.png:
  Boxplots pooling observations from the three pathways for each species

## Data Cleaning 
The data cleaning is initiated as a part of the code, additional data cleaning is not required. 

## Dataset 
The data set is taken from the website of CeCaFDB (http://www.cecafdb.org/) by selecting "Browse Flux Distributions" under the "Browse" option in the main menu. All of the cases of the following articles are chosen in the database:
- Metab Eng. 2007 Mar;9(2):177-92. Determining Actinobacillus succinogenes metabolic pathways and fluxes by NMR and GC-MS analyses of 13C-labeled metabolic product isotopomers. McKinlay JB, Shachar-Hill Y, Zeikus JG, et al
- Biotechnol. 2013 Dec;168(4):355-61. Metabolic flux analysis of Arthrobacter sp. CGMCC 3584 for cAMP production based on 13C tracer experiments and gas chromatography-mass spectrometry. Niu H, Chen Y, Yao S,et al.
- J Biosci Bioeng. 2014 Aug 13. pii: S1389-1723(14)00230-8. Comparative metabolic flux analysis of an Ashbya gossypii wild type strain and a high riboflavin-producing mutant strain. Jeong BY, Wittmann C, Kato T, et al.
- PLoS One. 2008 3(12):e3847. Systems analysis unfolds the relationship between the phosphoketolase pathway and growth in Aspergillus nidulans. Panagiotou G, Andersen MR, Grotkjaer T, et al.
- Metab Eng. 2012 Jan;14(1):47-58. Integration of in vivo and in silico metabolic fluxes for improvement of recombinant protein production. Driouch H, Melzer G, Wittmann C.
- Bioprocess Biosyst Eng. 2007 Jan;30(1):47-59. Comparative study on central metabolic fluxes of Bacillus megaterium strains in continuous culture using 13C labelled substrates. Furch T, Hollmann R, Wittmann C, et al.
- BMC Syst Biol. 2008 Mar;2:29. Hybrid optimization for 13C metabolic flux analysis using systems parametrized by compactification. Yang TH, Frick O, Heinzle E.
- J Biol Chem. 2010 Dec;285(50):39544-50. Metabolic flux analysis of the mixotrophic metabolisms in the green sulfur bacterium Chlorobaculum tepidum. Feng X, Tang KH, Blankenship RE, et al.
Because the database does not allow downloading the data, it was manually copy and pasted to the Excel file MAT2007RawData.xlsx. Please use this excel file for running the code.
