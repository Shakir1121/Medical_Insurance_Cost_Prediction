# Medical Insurance Cost Prediction Using ML
The "Medical Insurance Cost Prediction" project leverages machine learning techniques to train model and predict the cost of medical insurance based on demographic and lifestyle features. This involves analyzing factors such as age, BMI, number of children, and smoking status to estimate how much an individual will pay for health insurance. By applying regression algorithms, the model will help insurance companies and customers alike to better understand the cost structure of insurance premiums and make data-driven decisions.
# Why this Project?
The medical insurance cost prediction project using machine learning helps in forecasting future healthcare costs, which can aid insurance companies in setting accurate premiums. By analyzing data patterns, ML models can predict individual healthcare expenses more efficiently than traditional methods. This helps reduce costs for both insurers and customers while improving service quality.
# Dataset
•	List the features of the dataset.
## Features
- **Age**: Age of the individual
- **Sex**: Gender of the individual
- **BMI**: Body Mass Index
- **Children**: Number of dependents
- **Smoker**: Whether the individual smokes
- **Region**: Residential area of the individual
- **Charges**: Medical insurance cost (target variable)
- # Data Preprocessing
- Handle Missing Data
- Convert categorical variables (sex, smoker, region) into numerical formats
- # Exploratory Data Analysis (EDA)
- Analyze the distribution of Target Variables (charges)
  ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/distribution_of_charges.PNG?raw=true)

- Scatter plot for Age vs Charges, differentiated by Smoker bs Non Smoker
- Count the Number of Male and Female using countplot
- Count the Number of Children
- Count the Number of Smoker and Non Smoker
- Create count plot of Number of Male and Female Base on Region (SouthWest,SouthEast,NorthWest,NorthEast)
- Number of Male and Female with their Age
