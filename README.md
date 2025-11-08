# Parametric Curve Fitting – Research and Development / AI Assignment

## Objective
The goal of this work is to estimate the unknown parameters θ, M, and X for a given parametric curve using the provided dataset of (x, y) points.

The given equations are:

x = t*cos(θ) - e^(M|t|)*sin(0.3t)*sin(θ) + X  
y = 42 + t*sin(θ) + e^(M|t|)*sin(0.3t)*cos(θ)

The parameter t is defined in the range 6 < t < 60, and since t is always positive, |t| = t.

---

## Methodology
1. Loaded the dataset file `xy_data.csv` which contains the x and y coordinates.  
2. Since the time parameter t was not included, it was generated as uniformly spaced values between 6 and 60.  
3. Defined the equations for x(t) and y(t) based on the given expressions.  
4. Used the `scipy.optimize.least_squares` method to minimize the difference between the observed data and the model predictions.  
5. Applied parameter bounds:  
   - 0° < θ < 50°  
   - -0.05 < M < 0.05  
   - 0 < X < 100  
6. Computed the L1 distance (sum of absolute differences) as a measure of fit accuracy.  
7. Plotted the observed points and the fitted curve for visual comparison.

---

## Results

| Parameter | Value | Unit |
|------------|--------|------|
| θ | 0.516305 | radians (≈29.582°) |
| M | -0.05 | – |
| X | 55.013407 | – |
| L1 Distance | 38102.141459 | – |

---

## Final Equation
x(t) = t*cos(0.516305) - e^(-0.05*t)*sin(0.3*t)*sin(0.516305) + 55.013407  
y(t) = 42 + t*sin(0.516305) + e^(-0.05*t)*sin(0.3*t)*cos(0.516305)

---

## Desmos Visualization
To visualize the fitted curve, copy and paste the following expressions into the Desmos Parametric Graphing calculator:

x = t*cos(0.516305) - e^(-0.05*t)*sin(0.3*t)*sin(0.516305) + 55.013407  
y = 42 + t*sin(0.516305) + e^(-0.05*t)*sin(0.3*t)*cos(0.516305)  
6 <= t <= 60

---

## Files Included
- `fit_curve.py` – Python script used for parameter fitting  
- `xy_data.csv` – Input dataset  
- `fitted_params.csv` – Output file containing estimated parameters  
- `curve_fit.png` – Plot showing the observed and predicted curve  
- `README.md` – This project documentation

---

## Tools Used
Python 3, NumPy, Pandas, SciPy, Matplotlib, and Desmos.

---

## Conclusion
The parameters θ, M, and X were successfully estimated using nonlinear least squares optimization.  
The model closely fits the given data, and the results meet the required parameter constraints.  
This approach can be extended to other parametric models with unknown variables.

Author: Avinash A  
Institution: Amrita Vishwa Vidyapeetham, Chennai  
