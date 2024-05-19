https://github.com/BGSTA9/Linear_Regression/assets/99645827/5b1e5250-52ea-422b-9bd5-5995243ec460

Overview

Linear Regression is a fundamental statistical method used to model the relationship between a dependent variable and one or more independent variables. It is widely used for predictive analysis and finding the linear relationship between variables.

**This code sets up a linear regression model and animates the process of fitting this model incrementally with more data points. The animation shows the regression line updating in the first subplot and the slope’s rate of change in the second subplot.
**

Characteristics

Type: Regression Analysis\
Linear Model: Assumes a linear relationship between the dependent and independent variables.\
Equation: $y = \beta_0 + \beta_1x$  for simple linear.\
Assumptions:
1.	Linearity: The relationship between  x  and  y  is linear.
2.	Independence: Observations are independent of each other.
3.	Homoscedasticity: Constant variance of the errors.
4.	Normality: The residuals (errors) of the model are normally distributed.

How It Works

1.	Data Collection: Gather data for the dependent and independent variables.
2.	Model Specification: Define the linear regression model equation.
3.	Estimation of Parameters: Use the least squares method to estimate the parameters ( $\beta_0$  and  $\beta_1$ ).
4.	Prediction: Use the estimated model to make predictions.
5.	Evaluation: Evaluate the model using metrics like R-squared, Mean Squared Error (MSE), and residual plots.
5.1.	R-squared (R²)

	•	Unit: R-squared is a unitless measure.
	•	Explanation: R-squared, also known as the coefficient of determination, indicates how well the regression line fits the data. It ranges from 0 to 1, where:
	•	0 means the model explains none of the variability of the response data around its mean.
	•	1 means the model explains all the variability of the response data around its mean.
	•	Purpose: It tells us the proportion of the variance in the dependent variable (y) that is predictable from the independent variable (x). In simpler terms, it measures how well the model’s predictions match the actual data.
