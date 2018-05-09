<p align="center">
  <img width="460" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Senza%20titolo4.jpg">
</p>

# PitE-AnalisysCreditApproval

[![M&M](https://img.shields.io/badge/m%26m-projects-blue.svg)](https://img.shields.io/badge/m%26m-projects-blue.svg)


This is the fifth homework of the course "Python in the Enterprise", as requested has been analyze Credit Approval Data Set. The dataset analysed in this report is the Credit Approval dataset taken from the archives of the machine learning repository
of University of California, Irvine (UCI). It contains data from credit card applications. In its initial, unaltered form, the datasetmade available by UCI contains 690 cases, representing 690 individuals, and 16 variables named A1 – A16. The first 15
variables represent various attributes of the individuals submitting the application and the 16 th variable contains the outcome of the application, either positive (represented by “+”) meaning granted or negative (represented by "-") meaning rejected.

## Variable name

From the source of the dataset, it was observed that the names and values of the attributes have been changed to some generic and meaningless symbols to ensure the confidentiality and privacy of the applicants. So as to avoid confusion and for simplicity, the labels of some variables in our analysis have been assumed to be some working names according to the values in
the attributes like:

- A1 changed to Sex
- A2 changed to Age
- A8 changed to Years of work
- A15 changed to Income
- A16 changed to Approved. 

This assumption is common to find in any credit approval dataset and somewhat fit our data. 


## Data Transformations

As mentioned, the data in this analysis contains categorical values that are transformed to binary values or factors 1s and 0s.
Approved variable have values '+' and '-' in original dataset and with our assumption '+' means granted changed to 1 and '-' changedto 0. Similarly, with attributes Sex having values 'a' changed to 0 representing male and 'b' changed to 1.


## Missing data Treatment

On investigating the dataset, the missing values are labelled as '?'; so in case that we consider attribute with continous values, we replace this label with the mean of all values of the attribute, in case that we consider binary attribute we replace tha label of missing values with a random choice between 0 and 1. 

## Getting Started

**Prerequisites**
* In order to run this project is important to use python version 3 or upper.                                                    
  Install it with:
  
  ```shell
  $ sudo apt-get install python3
  ```
  now check your version: 
  ```shell
  $ python --version
  ```
 * In order to run this project is also important use numpy, pandas and matplotlib
                                                   
  Install it with:
  
  ```shell
  $ pip install --user numpy 
  
  $ pip install --user pandas
  
  $ pip install --user matplotlib
  
  ```
  
## Analysis
In order to make our analysis, we have been concentrating this whole time on the main attributes that are common in any credit approval dataset, like Age, Years of york, sex or income of the applicant. We choose to study first all this attributes individually and afther we've been trying to figure out the correlation that each of these have with the positive or negative approval.

**Differnt type of Attributes**

* Distribution of Attribute Age
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/age.png">
</p>

* Label attribute Sex
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/sex.png">
</p>

* Distribution of Income Attribute
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/income.png">
</p>

* Distribution of Years of Work Attribute
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/y_o_y.png">
</p>

**Correlation between Attribute and Approval state**

* Correlation between Sex and Approval
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/sex1_approval.png">
</p>


<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/sex_0_Approval.png">
</p>


* * Correlation between Income and Approval
<p align="center">
  <img width="660" height="300" src="https://raw.githubusercontent.com/Mario181091/Mario_content/master/Income_Approval.png">
</p>


  
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - [other projects](https://github.com/mario181091)
* **Marco Amato** - *Erasmus student AGH* - [other projects](https://github.com/mark91m12)
