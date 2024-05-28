# Laptop Price Predictor

#### Site:
https://mlpricepredictor.streamlit.app/

```
git clone https://github.com/Shoaib1990/LaptopPricePredictor
```

#### Presentation: 
https://docs.google.com/presentation/d/1gxzJclaC72h6s_zwFfFvJqAM0Xfp9fo53Nr_HA7whrk/edit?usp=sharing

#### Proposal: 
https://docs.google.com/document/d/16UX3HekPxmAR-Psw4p2OZGtZnUEampIysP-rewSwC3I/edit?usp=sharing


## Project Overview:
The proposed project aims to develop a machine learning-based web application that predicts the price of a laptop based on its specifications. This application will assist users in making informed purchasing decisions by providing accurate price estimates based on the inputted specifications.

## Packages/Tools Used:
Python
Streamlit
Pickle
Plotly
Numpy
Matplotlib
Seaborn
Scikit-Learn

## Data:

- web-scraper-start-url	
- single	
- single-href	
- title	
- price	
- manufacturer	
- model_name	
- screen_size	
- display_resolution	
- cpu_model	
- processor	
- graphics_copressor	
- ram	
- storage	
- operating_system	
- weight	
- num_processors	
- processor_brand

## Model Building:
- The 'web-scraper-start-url', 'single', 'single-href', 'title','model_name', 'screen_size' and 'processor_brand' columns were dropped because some of theym were irrelevant and some of them of were used to create new features such 'touchable', 'ips', etc.
- The categorical features (manufacturer, cpu_name, os and graphics_copressor) were transformed into numerical data.
- Linear Regression, Ridge Regression, Lasso Regression, Random Forest Regressor, Decision Tree, and Support Vector Regressor models were all built.
- Root mean squared error (RMSE) which is the square root of the sum of the difference between the true value and the predicted value was the metric used to evaluate the performance of the model.
- The Randomforest model has the best performance.
- The model was tested on new data and it predicted a good price.