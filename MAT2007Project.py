#Project: Data Analysis and Visualization of the Metabolic Flux Distributions Across Different Species

#Maastricht University - Maastricht Science Programme
#Course: MAT2007 - Introduction to Programming
#Name: Asya Özzeybek
#Student ID: i6423633
#Student email: a.ozzeybek@student.maastrichtuniversity.nl

#Importing the libraries that are required for this project:
import pandas as pd #used for data cleaning and analysis
import matplotlib.pyplot as plt #for plotting
import seaborn as sns #for making statistical graphics
import numpy as np #SciPy could not be used because one of its compiled components was blocked by Windows Security, so the required statistical measures are calculated using NumPy.

#The data is in an excel file named MAT2007RawData.xlsx which includes the reaction IDs as KEGG codes, we need to assign the reaction names to the 3 main pathways we will focus on.
#These pathways are: Glycolysis, TCA Cycle (Krebs Cycle) and Pentose Phosphate Pathway (PPP).

#Using the KEGG modules M00001, M00009, M00004, M00006, and M00007 in the KEGG website, the reaction IDs for each pathway was determined.
#We need to match the pathways to the data in the excel file.

#First we need to show which reactions are included in the 3 pathways. Doing this manually would take time, a more efficient way is to use dictionaries and ".map()" function.
#Dictionaries are used to store data values in value pairs - uses curly brackets { } (Python Dictionaries, n.d.).

pathways = {"R01786": "Glycolysis", "R02740": "Glycolysis", "R04779": "Glycolysis", "R01070": "Glycolysis", "R01015": "Glycolysis", "R01061": "Glycolysis", "R01512": "Glycolysis", "R01518": "Glycolysis", "R00658": "Glycolysis", "R00200": "Glycolysis",
"R00351": "TCA", "R01324": "TCA", "R00267": "TCA", "R08549": "TCA", "R00405": "TCA", "R00402": "TCA", "R01082": "TCA", "R00342": "TCA", "R00214": "TCA", "R00217": "TCA",
"R02736": "PPP", "R02035": "PPP", "R01528": "PPP", "R01641": "PPP", "R01827": "PPP", "R01830": "PPP", "R01056": "PPP", "R01529": "PPP"}

#Loading the data:
print("Data is Loading...")

#pd.read_excel() function reads an Excel file into a DataFrame (Pandas.Read_Excel — Pandas 3.0.6 Documentation, n.d.).
flux_data = pd.read_excel("MAT2007RawData.xlsx") 

flux_data["Species"] = flux_data["Species"].str.strip()
flux_data["Reaction"] = flux_data["Reaction"].str.strip()
flux_data["Condition"] = flux_data["Condition"].str.strip()

#Creating a new column called "Pathway" and using the .map() function to match the reactions under the "Reaction" column to one of the three pathways in the dictionary. If the reaction is not a part of these pathways, it is left blank (they will be excluded from the research).
flux_data["Pathway"] = flux_data["Reaction"].map(pathways) #map() looks up each Reaction ID in the dictionary and returns the corresponding pathway (GeeksforGeeks, 2026).

#Then we need to determine the number of data points after matching the reactions to the pathways.
def pathway_match_results (flux_data):
    print("Pathway Matching Results:")
    counts = flux_data['Pathway'].value_counts(dropna=False) #This line of code counts how mant reactions fall into each pathway, there are three possible pathways; Glycolysis, TCA and PPP so it counts how many reactions are under each (and how many are not assigned - NaN)
    print(counts) #Printing the results

input("To see the number of data points assigned to Glycolysis, TCA and PPP Pathways click enter.") #I decided not to print all the information at once, so that the output is more clear to follow by the user.
pathway_match_results(flux_data)

flux_data.to_csv("flux_data_including_pathways.csv", index=False) #Naming and saving the new flux data file as a CSV file, index = False means the row numbers will not be written.
print("See the flux_data_including_pathways.csv")

#The file flux_data_including_pathways.csv still has some blanks in flux values for some reaction IDs.
#We need to remove empty flux values and convert the column to numbers (not string).

#Data Cleaning:
print("Cleaning the data...")
def data_cleaning(flux_data):
    #To remove the rows where Flux_Value is empty we use dropna() function.
    #dropna() method removes the rows that contains NULL values (W3Schools.com, n.d.-a). 
    #If we wrote "flux_data = flux_data.dropna()" is would delete the row if any column had a missing value. That is not our purpose, we want the row to be deleted if the value in the Flux_Value column is missing - we use "subset =["Flux_Value"]" for this purpose.
    flux_data = flux_data.dropna(subset=["Flux_Value"]) 
    
    #For the analysis, we need to ensure all the data are numeric, taking into account the chance that any of them were stored in text, we use pd.to_numeric() which converts the argument to a numeric type (Pandas.to_Numeric — Pandas 3.0.6 Documentation, n.d.). 
    flux_data['Flux_Value'] = pd.to_numeric(flux_data['Flux_Value'], errors='coerce')
    
    #After the conversion if any values became NaN, they will be deleted using:
    flux_data = flux_data.dropna(subset=['Flux_Value'])

    return flux_data

input("To initiate data cleaning process press enter.")
flux_data = data_cleaning(flux_data)

pathway_data = flux_data.dropna(subset=['Pathway']).copy()

def summary_data(pathway_data):
    print(f"Total usable data points are {len(pathway_data)}") #The total usable data points in our analysis can be determined through len(pathway_data).
    #The f inside the print() statement is the f-string, which enables the elements inside curly brackets to be evaluated and the result to be printed.

    print(f"Number of species in the analysis are {pathway_data['Species'].nunique()}") #nunique() method returns the number of unique elements for the column "Species" (W3Schools.com, n.d.-b).

    print("\nNumber of data points for each species:")
    species_count = pathway_data['Species'].value_counts() #Returns a Series containing the counts of unique values (elements), with the resulting object in descending order (pandas.Series.value_counts — Pandas 3.0.6 Documentation, n.d.).
    print(species_count)

    print("\nNumber of data points for each species and pathway:")
    pathway_counts = pathway_data.groupby(['Species', 'Pathway']).size() #groupby() groups the data by species and pathway, and size() counts the rows in each group.
    pathway_counts = pathway_counts.unstack(fill_value=0) #unstack() displays the pathways as separate columns, using 0 where a species has no observations for a pathway.
    pathway_counts = pathway_counts.reindex(columns=['Glycolysis', 'TCA', 'PPP']) #Sets the order of the pathway columns.
    print(pathway_counts)
    
input("To print the summary of the cleaned data press enter.")
summary_data(pathway_data)

#For the analysis we will calculate the mean, median, standard deviation, inter quartile range, skewness and kurtosis for each species and pathway. This would enable a comphrensive comparison.

print("\nStatistical Analysis:")
#Because the Windows Smart App Controls block scpiy and I couldn't resolve the issue, the statistical functions must be done manually.

#The skesness() and kurtosis() functions I created in Week4Tutorial.py was adapted to the project:
def skewness(sample): #We define a function for the skewness of a sample (Lecture 4 MAT2007). 
    
    sample = np.asarray(sample, dtype=float) #Converting the "sample" into a NumPy array as float as the data type.
    mean = np.mean(sample) #Calculating sample mean: x̄ = Σx/n.  
    
    standard_deviation = np.std(sample, ddof=0)

    if standard_deviation == 0:
        return 0.0

    skewness_value = np.mean(((sample - mean) / standard_deviation)**3)

    return skewness_value

def kurtosis(sample): #We define a function to calculate the formula for calculating kurtosis (Lecture 4 MAT2007).
    sample = np.asarray(sample, dtype=float) #Converting the "sample" into a NumPy array as float as the data type.
    mean = np.mean(sample)

    standard_deviation = np.std(sample, ddof=0)

    if standard_deviation == 0:
        return 0.0

    kurtosis_value = np.mean(((sample - mean) / standard_deviation)**4) - 3

    return kurtosis_value

def std_dev(x):
    return np.std(x, ddof=0)

def q1(x):
    return x.quantile(0.25)

def q3(x):
    return x.quantile(0.75)

def data_analysis(pathway_data):
    #groupby() groups rows that have the same value in one of the columns: Species or Pathway, so that we can calculate statistics seperately for each group (Pandas.DataFrame.Groupby — Pandas 3.0.6 Documentation, n.d.). For each of the groups the calculations are made using the Flux_value column.
    #This is useful for this analysis as we want to compare the flux distributions of each organism seperately within Glycolysis, TCA, and PPP.
    analysis = pathway_data.groupby(['Species', 'Pathway'])['Flux_Value'].agg( #agg() which is short for aggregate means for each group of data calculate the summary values.
        Count="count", #for each species-pathway group counting the number of Flux_Value observations
        Mean="mean", #mean of the flux values in each group
        Median="median", #calculating median which is the middle value after the data is sorted.
        Std_Dev=std_dev, #Calculating standard deviation, ddof=0 meaning it is divided by N.
        Min="min", #minimum value in each group
        Max="max", #maximum value in each group
        #For calculating the first and third quartiles which will be used to calculate the interquartile range:
        Q1=q1, 
        Q3=q3,
        Skewness=skewness,
        Kurtosis=kurtosis
    )

    analysis["IQR"] = analysis["Q3"] - analysis["Q1"] #The Interquartile Range
    analysis = analysis.round(3) #Rounding the answer to 3 decimal places.
    
    print(analysis)
    analysis.to_csv("data_analysis.csv")
    print("Saved to data_analysis.csv")
    
    print("\nKey Quantitative Results:") #To obtain some important values from the data_analysis.csv produced.
    highest_mean = analysis['Mean'].idxmax() #Return index of first occurence of maximum over requested axis (pandas.DataFrame.idxmax — Pandas 3.0.6 Documentation, n.d.).
    highest_mean_value = analysis['Mean'].max() #

    lowest_mean = analysis['Mean'].idxmin()
    lowest_mean_value = analysis['Mean'].min()

    highest_iqr = analysis['IQR'].idxmax()
    highest_iqr_value = analysis['IQR'].max()
    
    print(f"Highest mean flux: {highest_mean[0]} - {highest_mean[1]} = {highest_mean_value}")
    print(f"Lowest mean flux: {lowest_mean[0]} - {lowest_mean[1]} = {lowest_mean_value}")
    print(f"Largest IQR: {highest_iqr[0]} - {highest_iqr[1]} = {highest_iqr_value}")

    highest_median = analysis['Median'].idxmax()
    highest_median_value = analysis['Median'].max()

    highest_std = analysis['Std_Dev'].idxmax()
    highest_std_value = analysis['Std_Dev'].max()
    
    print(f"Highest median flux: {highest_median[0]} - {highest_median[1]} = {highest_median_value}")
    print(f"Largest standard deviation: {highest_std[0]} - {highest_std[1]} = {highest_std_value}")
    
    most_skewed = analysis['Skewness'].abs().idxmax()
    most_skewed_value = analysis.loc[most_skewed, 'Skewness']
    
    highest_kurtosis = analysis['Kurtosis'].idxmax()
    highest_kurtosis_value = analysis['Kurtosis'].max()

    print(f"Most skewed distribution: {most_skewed[0]} - {most_skewed[1]} = {most_skewed_value}")
    print(f"Highest kurtosis: {highest_kurtosis[0]} - {highest_kurtosis[1]} = {highest_kurtosis_value}")

input("To see the data analysis including mean, median, standard deviation, minimum, maximum, interquartile range, skewness and kurtosis for each pathway and species press enter.")
data_analysis(pathway_data)

#Data Visualization: Boxplots
print("\nData Visualization:")

def data_visualization():
    if len(pathway_data) > 0: #len(pathway_data) represents the number of rows, the plot is created is the number of rows are bigger than 0.
        #First boxplot: Showing the flux distributions for each species separetely for each pathway
        
        #Both catplot() and boxplot() are Seaborn plotting functions, boxplot() creates a single boxplot figure while catplot() can create several panels at once - the three panels enable the comparison between different pathways.

        plot = sns.catplot( #Seaborn (which is imported as sns) is a library used for statistical data visualization. It makes it easier to create a boxplot for many groups at once (Seaborn.Catplot — Seaborn 0.13.2 Documentation, n.d.).
            data=pathway_data, #Using the dataframe called pathway_data.
            x="Species", y="Flux_Value", #Species is on the x axis and Flux_Value on the y-axis.
            col="Pathway", #Creating a separete plot panel for each unique element in the Pathway column. 
            kind="box", #Specifies which kind of plot we want, it is a boxplot which shows Q1, Q3, IQR and possible outliers.
            col_wrap=3, #The number of plot panels that can appear in a row - because we focus on three pathways.
            height=5, #Height of the panels
            aspect=1.2, #Width relative to height
            hue="Species", #hue means using different colors for different categories.
            palette="colorblind", #The color palette - Seaborn has numerous built-in palettes. Should be something that can be interpreted by color_palette().
            legend=False, #We don't need a legend because the species names are already on the x-axis.
            sharey=True, #Ensures that all three pathway panels use the same y-axis scale.
            col_order=['Glycolysis', 'TCA', 'PPP'] #The order that the panels will appear.
        )

        #Note: for palette= I tried "dark" which had some colors that were hard to distinguish. My other option was the color palette "colorblind" to make the results also accessible for color blind people.

        plot.set_xticklabels(rotation=45, ha="right") #rotation=45 rotates the labels 45 degrees because species names are long, ha="right" horizontal alignment is set to the right.
        plot.set_titles("{col_name}", size=14) #col is set as "Pathway" for this reason it sets the title of each separate pathway panel.
        plot.set_axis_labels("Species", "Relative Flux Value (Substrate Uptake = 100)") #Species is the x-axis and Flux Value is the y axis
        plt.tight_layout() #Prevent species names overlapping or any label being cut off.
        plt.savefig("pathway_boxplot.png", dpi=300) #Figure name and dpi means dots per inch (it controls the resolution of the image) - it is set as 300 for high resolution (the default is 100)
        plt.show()
        print("See the file pathway_boxplot.png")

        #2nd box plot: shows for the pathways combined how do the flux distributions differ between species.
        plt.figure(figsize=(12, 6))
        sns.boxplot( #(Seaborn.Boxplot — Seaborn 0.13.2 Documentation, n.d.)
            data=pathway_data,
            x="Species",
            y="Flux_Value",
            hue="Species",
            palette="colorblind",
            legend=False 
        )

        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Species")
        plt.ylabel("Relative Flux Value (Substrate Uptake = 100)")
        plt.tight_layout()
        plt.savefig("species_boxplot.png", dpi=300)
        plt.show()

        print("See the file species_boxplot.png")
    
    else: 
        print("No pathway assigned data found.")
    
    print(" The following files have been created in your folder:")
    print("   - flux_data_including_pathways.csv")
    print("   - data_analysis.csv")
    print("   - pathway_boxplot.png")
    print("   - species_boxplot.png")

input("To create the boxplots for each pathway press enter.")
data_visualization()

#Sources:
#GeeksforGeeks. (2026, June 26). Python map() function. https://www.geeksforgeeks.org/python/python-map-function/  
#pandas.DataFrame.groupby — pandas 3.0.6 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
#pandas.DataFrame.idxmax — pandas 3.0.6 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html
#pandas.read_excel — pandas 3.0.6 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
#pandas.Series.value_counts — pandas 3.0.6 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html 
#pandas.to_numeric — pandas 3.0.6 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
#Python Dictionaries. (n.d.). W3Schools. https://www.w3schools.com/python/python_dictionaries.asp
#seaborn.boxplot — seaborn 0.13.2 documentation. (n.d.). https://seaborn.pydata.org/generated/seaborn.boxplot.html
#seaborn.catplot — seaborn 0.13.2 documentation. (n.d.). https://seaborn.pydata.org/generated/seaborn.catplot.html
#W3Schools.com. (n.d.-a). W3Schools. https://www.w3schools.com/python/pandas/ref_df_dropna.asp
#W3Schools.com. (n.d.-b). W3Schools. https://www.w3schools.com/python/pandas/ref_df_nunique.asp