Healthcare Insurance Data Analysis

What This Project is About

For this project I worked on a healthcare insurance dataset with 1,337 patient records. The goal was to clean and analyze the data, find useful insights, and present everything in a clear way using Python and Power BI.
One of the most important things this project reveals is how smoking and high BMI are directly responsible for skyrocketing insurance charges. Patients who smoke or carry a high BMI end up paying dramatically more for their insurance because their lifestyle choices lead to serious and expensive medical conditions. This project not only analyzes the numbers but also highlights the real human and financial cost of these health risks.

1.	I used Python (pandas and NumPy) for data cleaning and exploratory data analysis
2.	Power BI for interactive dashboard visualization

ALL FILE SUMMARY

Python
healthcare_Dataset Project
1.	Data cleaning, Exploratory Data Analysis (EDA), and KPI Calculations
2.	Loads the raw insurance.csv, cleans it, runs all analysis, and exports insurance_cleaned.csv

![image alt](https://github.com/gautam-kumar-7590/Healthcare-Insurance-Analysis/blob/c7ff84d2849eb2699a9e6d9375191ffb54a38381/Screenshot%20(41).png)

POWER BI
Healthcare Insurance Analysis
1.	Interactive visuals dashboard with charts and KPI cards
2.	Bar charts, Donut charts, Line chart, Treemap, and KPI cards

![image alt](https://github.com/gautam-kumar-7590/Healthcare-Insurance-Analysis/blob/ad439ce80f470e3b5e327348c69c3e1bfdf70210/Screenshot%20(42).png)

Dataset Summary

The raw dataset consists of 1,338 rows of healthcare insurance records. After removing 1 duplicate, the final cleaned dataset has 1,337 rows with the following fields:

age, sex, bmi, children, smoker, region, charges

The two most powerful variables in this entire dataset are smoker and bmi. These two fields alone explain why some patients pay as little as $1,122 a year while others pay as much as $63,770. When a patient smokes, when their BMI is high, or when both are true at the same time, their insurance charges increase sharply -- and the data proves this without any doubt.

Key Performance Indicators
1.	Total Patients = 1,337
2.	Average Age = 39.22 years
3.	Average BMI = 30.66 -- This is in the clinically OBESE range (WHO: BMI 30 or above = Obese)
4.	Average Insurance Charges = $13,279 -- This average is heavily pulled up by smokers and high-BMI patients
5.	Maximum Single Charge = $63,770 -- The highest charges in this dataset all belong to smokers with high BMI
6.	Minimum Single Charge = $1,122 -- The lowest charges belong to young, non-smoking patients with healthy BMI
7.	Total Smokers = 274 (20.5% of patients) -- Only 1 in 5 patients smokes, yet they generate nearly half of all charges
8.	Total Non-Smokers = 1,063 (79.5% of patients) -- 4 in 5 patients do not smoke and pay far lower charges

Python Analysis Breakdown

Libraries Used
1.	Pandas -- Used for loading, cleaning, filtering, and analyzing the dataset using DataFrames
2.	NumPy -- Used for numerical operations like rounding values and converting data types

Methods and Functions Used
1.	pd.read_csv() -- Loads the insurance CSV file into a pandas DataFrame
2.	df.describe() -- Generates summary statistics: mean, min, max, std, and quartiles
3.	df.isnull().sum() -- Checks how many missing values exist in each column
4.	df.duplicated().sum() -- Counts the number of completely duplicate rows
5.	df.drop_duplicates() -- Removes all duplicate rows from the dataset (removed 1 row)
6.	df[df['smoker']=='yes']['charges'].mean() -- Average charges for smokers only
7.	df.groupby('region')['charges'].mean() -- Average charges broken down per region
8.	df.to_csv('insurance_cleaned.csv', index=False) -- Exports cleaned data to a new CSV file

Average Charges by Region

REGION      ||  AVERAGE CHARGES    ||  PATIENT COUNT
Southeast   ||  $14,735 (Highest)  ||  364
Northeast   ||  $13,406            ||  324
Northwest   || $12,418             ||  325
Southwest   || $12,347 (Lowest)    ||  324

The Southeast region has the highest average charges because it also has the highest number of smokers and the highest average BMI of all four regions. This is not a coincidence -- wherever smoking rates and BMI are higher, insurance charges follow and go up with them.

Power BI Dashboard Summary

The Power BI Dashboard titled 'Healthcare Insurance Analysis' provides interactive visual reporting across all key health and demographic dimensions. It is built on a single page with 9 visual components and 4 KPI cards. The dashboard makes it visually clear how smoking status and BMI are the two factors that push insurance charges the highest across all regions and age groups.


KPI CARDS
Total Patients, Average of Charges, Average BMI, Average Age

Visual Components
Average Charges by Region (Horizontal Bar Chart), Average of Charges by Age (Line Chart), Charges by Smoking Status by Region (Donut Chart)

Donut Charts
Charges by Gender, Charges by Smoker Status, Sum of Charges by Region (Treemap), BMI by Region (Waterfall Chart), Smokers Across Regions (Pie Chart)


Key Insights
HIGHEST RISK GROUP
1.	Highest Cost Region: Southeast (~$14,735 average charges) -- driven by the highest smoker count and highest BMI in the dataset
2.	Most Expensive Demographic: Smokers -- charges are nearly 4x higher than non-smokers, proving that smoking alone can multiply a person's insurance cost by 4 times
3.	Highest Patient Count Region: Southeast (364 patients)
4.	Most Critical Variable: Smoking status -- just 274 smokers (20.5% of patients) are responsible for nearly 50% of all total insurance charges in the entire dataset
LOWEST RISK GROUP 
1.	Lowest Cost Region: Southwest (~$12,347 average charges)
2.	Lowest Risk Demographic: Young non-smokers with healthy BMI -- these patients pay a fraction of what smokers and obese patients pay
3.	Lowest Charge Age Group: Patients aged 18-25 with non-smoker status and healthy BMI

Health Risk Awareness

This analysis highlights several critical health patterns that go beyond just numbers. The data tells a clear story about the real-world consequences of lifestyle choices and age on a person's health and the cost it carries. Here is what this dataset is really pointing to:

1.	Smoking is the single biggest reason insurance charges skyrocket -- smokers in this dataset pay nearly 4 times more in insurance charges than non-smokers. While smokers make up only 20.5% of patients, they are responsible for nearly 50% of all total insurance costs combined. The reason charges go this high is because smoking causes severe and chronic damage to the human body over time -- lung disease, heart disease, stroke, and multiple types of cancer. Treating these conditions means constant hospital visits, long-term medication, surgeries, and specialist care, all of which pile enormous costs onto the patient's insurance. The data in this project shows this pattern clearly -- every smoker in this dataset pays dramatically more than a non-smoker of the same age and region. People need to understand that when they choose to smoke, they are not just risking their health -- they are signing up for insurance bills that can be 4 times higher than what a non-smoker pays. Quitting smoking is the most powerful single action a person can take to protect both their body and their finances.
2.	High BMI directly causes insurance charges to rise sharply -- the average BMI across all 1,337 patients is 30.66, which puts the entire patient group in the clinically obese category according to WHO standards (BMI of 30 or above is classified as obese). A high BMI is not just a number -- it tells insurers that the body is under serious medical stress. Obesity leads directly to type 2 diabetes, cardiovascular disease, high blood pressure, sleep apnea, and joint deterioration, all of which are expensive and ongoing to treat. Because obese patients require more medical attention, more frequent hospital visits, and more long-term care, insurance companies charge them significantly higher premiums to cover those expected costs. In this dataset, patients with higher BMI values consistently show higher insurance charges -- the connection is direct and undeniable. What this means in real life is that a person who carries excess weight is paying more money every single year for their insurance, and those costs keep rising the longer the problem goes unaddressed. The awareness point here is powerful: losing weight and maintaining a healthy BMI is not just good for your health -- it can save you thousands of dollars in insurance charges every year.
3.	Aging comes with rising health costs and that needs early attention -- charges grow steadily from age 18 all the way to 64. This shows that health deteriorates progressively with age when lifestyle factors are not managed early. Starting healthy habits young -- regular exercise, balanced diet, not smoking -- can significantly reduce the medical costs and health complications seen in older age groups.
4.	The Southeast region shows the highest health risk concentration -- it has the most smokers, the highest average BMI, and the highest average charges of all four regions. This points to a geographic health inequality where certain populations face compounded risk factors. Targeted public health programmes, awareness campaigns, and community-level interventions are especially needed in high-risk regions like the Southeast.
5.	Prevention is far more powerful than treatment -- what this entire dataset ultimately shows is that the patients with the lowest charges are those who do not smoke, maintain a healthy BMI, and are younger. These are all preventable and controllable factors. Raising awareness about preventive healthcare -- regular check-ups, active lifestyles, and avoiding harmful habits -- could dramatically reduce the health and financial burden seen across this entire population.

Use of AI

I used AI Tools -- Claude and ChatGPT as assistants during the project, not to do the work for me. Here is how:

1.	I used AI to double check my Python analysis -- for example asking whether my KPI numbers looked correct given the dataset size and whether my groupby logic was right.
2.	I used AI to help me understand certain pandas methods and DAX formulas when I was unsure, and to verify the effectiveness of specific functions I was using.
3.	All analysis, data cleaning, dashboard building, and decision making was done by me. AI was used as a reference tool and writing assistant only.


Conclusion

This Healthcare Insurance Analysis project successfully processed 1,337 patient records to deliver meaningful insights through both Python and Power BI. The data reveals one dominant and unavoidable truth: smoking and high BMI are the two factors that cause insurance charges to skyrocket. Smokers pay nearly 4 times more than non-smokers. Patients with high BMI face significantly higher charges year after year. And when a patient smokes AND has a high BMI, their charges reach the very top of the dataset -- as high as $63,770 a year. These are not small differences. These are life-changing financial consequences that stem directly from lifestyle choices.

The goal of this project is not just to report numbers -- it is to make those numbers mean something. Every data point in this dataset represents a real person paying a real bill. The ones paying the most are the ones whose health is most at risk. That connection between lifestyle, health, and the cost people are forced to pay deserves to be understood clearly -- and that is what this analysis sets out to show.



Key action points based on this analysis:

1.	Invest in smoking-cessation awareness programmes -- smoking alone is responsible for nearly half of all insurance costs in this dataset
2.	Promote BMI and weight management education -- the average patient in this dataset is already in the obese range, and that is pushing average charges up for everyone
3.	Develop age-based preventive health programmes -- the earlier people adopt healthy habits, the lower their long-term insurance costs will be
4.	Focus public health resources on the Southeast region -- highest charges, most smokers, highest BMI, all concentrated in one region
5.	Educate patients on the direct financial link between their health choices and their insurance bills -- awareness of this connection can motivate real and lasting lifestyle change

