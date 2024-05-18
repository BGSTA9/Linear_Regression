import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

# Random Sample Data
np.random.seed(0)
x = np.random.rand(100, 1) * 10
y = 2.5 * x.flatten() + np.random.rand(100) * 5

# Creating the linear regression model
model = LinearRegression()

# Creating a figure and two axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Initializing a list to store slopes
slopes = []

def animate(i):
    # Training the model using the first i+1 data points
    model.fit(x[:i+1], y[:i+1])
    
    # Making predictions using the trained model
    y_pred = model.predict(x)
    
    # Clearing previous plots, otherwise previous lines will be visible on the plot
    ax1.cla()
    ax2.cla()
    
    # Plotting the data points and the linear regression line
    ax1.scatter(x, y, color='blue', alpha=0.5)
    ax1.plot(x, y_pred, color='red')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title("Linear Regression")
    
    # Calculating the slope and intercept
    slope = model.coef_[0]
    intercept = model.intercept_
    slopes.append(slope)
    
    # Display of the linear equation
    equation_text = f'y = {slope:.2f}x + {intercept:.2f}'
    ax1.text(0.05, 0.95, equation_text, transform=ax1.transAxes, fontsize=12,verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='white'))
    
    # Plotting the rate of change (slope) over time, with respect to the model
    ax2.plot(range(1, len(slopes) + 1), slopes, color='green')
    ax2.set_xlabel('Number of Data Points')
    ax2.set_ylabel('Slope')
    ax2.set_title("Rate of Change of Slope")

# Creating the animation
ani = FuncAnimation(fig, animate, frames=len(x), repeat=False)

# Saving the animation as a video file
ani.save('Linear_Regression_Opt.mp4', writer='ffmpeg')

plt.show()