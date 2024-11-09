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
  <br>
  ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/distribution_of_charges.PNG?raw=true)

- Scatter plot for Age vs Charges, differentiated by Smoker bs Non Smoker
  <br>
    ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/age_vs_charges.PNG?raw=true)
- Count the Number of Male and Female using countplot
    <br>
    ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/no_of_M_F.PNG?raw=true)
- Count the Number of Children
    <br>
    ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/no_children.PNG?raw=true)
- Count the Number of Smoker and Non Smoker
    <br>
    ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/smoker_non_smoker.PNG?raw=true)
- Create count plot of Number of Male and Female Base on Region (SouthWest,SouthEast,NorthWest,NorthEast)
    <br>
    ![Alt text](https://github.com/shakir1121/Medical_Insurance_Cost_Prediction/blob/main/EDA_Images/M_F_By_Region.PNG?raw=true)
- Number of Male and Female with their Age
# Model Development
- Split the dataset into training and testing sets.
- Implement a linear regression model.
- Evaluate model performance using appropriate metrics (e.g., R-squared, Mean Squared Error).
# Result
  Using Linear Regression Model result is 70%.improve result fine tuning.
# Conclusion
  Linear regression provides a baseline model for predicting medical charges based on demographic and health-related factors. Further analysis, including regularized linear models and sensitivity analysis, can help improve model robustness and generalization.
