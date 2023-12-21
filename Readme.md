# Diabetes Prediction Capstone project.

<img src="./media/diabetes_day.png" alt="drawing" width="1000"/>

## Table of Contents
- [Project Overview](#project-overview)
- [Getting started](#getting-started)
- [Datasets](#datasets)
- [Model](#model)
- [Dependencies](#dependencies)
- [Workflow](#workflow)
- [Directory structure](#dirctory-structure)
- [Follow-up Work](#follow-up-work)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contributions and Feedback](#contributions-and-feedback)
- [Key Concepts](#key-concepts)

---

## [Project Overview](#project-overview)

In a transition to a preventive health system, being able to identify risk of diabetes to implement an early warning system and also a campaign preventive health measures from your healht providers is paramount. There is a classical approach using clinical exams, but being able to implement it from non-intrusive measures based on behavioral risk factors based on a surveillance system based on remote surveys might lead to reduce post-sickness attentional demand and those cost associated. The objective is to be able to predict the probability and an early-warning risk alert based on the available dataset.

## [Getting started](#getting-started)




## [Datasets](#datasets)

The Behavioral Risk Factor Surveillance System (BRFSS) is an ongoing, state-based telephone survey that collects data about health-related risk behaviors, chronic health conditions, and the use of preventive services among adults aged 18 years and older residing in the United States. Conducted annually by the Centers for Disease Control and Prevention (CDC), the BRFSS has been providing valuable insights into the health status and behaviors of U.S. adults since its inception in 1984.

The most relevant fields in the dataset and whose descriptors are in the data dictionary are:

- DIABETE4: Diabetes Awareness
_RFHYPE6: High Blood Pressure Awareness ("yes" or "no")
TOLDHI3: Cholesterol Awareness ("yes" or "no")
_CHOLCH3: Cholesterol check within past five years ("yes" or "no")
_BMI5: Body mass index (scale)
SMOKE100: Smoked at Least 100 Cigarettes ("yes" or "no")
CVDSTRK3: Chronic Health Conditions ("yes" or "no")
_MICHD: Ever had CHD or MI (Coronary Heart Disease (CHD) and Myocardial Infarction (MI)) ("yes" or "no")
_TOTINDA: Leisure Time Physical Activity
_FRTLT1A: Consume Fruit 1 or more per day ("yes" or "no")
_VEGLT1A: Consume Vegetables 1 or more per day ("yes" or "no")
_RFDRHV7: Heavy Alcohol Consumption ("yes" or "no")
_HLTHPLN: Have any health insurance ("yes" or "no")
MEDCOST1: Could Not Afford To See Doctor ("yes" or "no")
GENHLTH: General health status ("excellent", "very good", "good", "fair", "poor")
MENTHLTH: Number of Days Mental Health is Not Good (scale based on the amount of days)
PHYSHLTH: Number of Days Physical Health is Not Good (scale based on the amount of days)
DIFFWALK: Difficulty walking or climbing stairs ("yes" or "no")
_SEX: Gender ("male", "female")
_AGEG5YR: Age group (5-year intervals)
EDUCA: Highest level of education attained
INCOME3: Family income (11 categories)

The CDC BRFSS Survey 2021, can be found on Kaggle Datsets [CDC BRFSS Survey 2021](https://www.kaggle.com/datasets/dariushbahrami/cdc-brfss-survey-2021). All the dataset files can be downloaded and decompressed from there and stored in the ./data folder for reproducibility of this project.

The CDC BRFSS Survey 2021 codebook with a detailed dictionary of its variables, description and codification, can be found on Kaggle Datsets [CDC BRFSS Survey CODEBOOK](https://www.cdc.gov/brfss/annual_data/2021/pdf/codebook21_llcp-v2-508.pdf). To learn more about the data, you can go to the official page [Centers for Disease Control and Prevention, 2021 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)
