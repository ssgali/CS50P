import matplotlib.pyplot as plt
import numpy as np

# Display Software House and Team Information
def display_info():
    print("\n=== Solar Farm Layout Optimization Software ===")
    print("Software House: BrightEnergy Solutions")
    print("Programming Team:")
    print("1. Student A - ID: 123456")
    print("2. Student B - ID: 7891011")
    print("3. Student C - ID: 12131415")
    print("=============================================")
    print("\n")

# Ask user for year and predict global temperature (Example values, to be expanded)
def get_year_and_predict_temp():
    year = int(input("Enter a year for global temperature prediction (e.g., 2025, 2050, 2100): "))
    predicted_temp = predict_global_temp(year)
    print(f"\nPredicted Average Global Temperature for {year}: {predicted_temp:.2f} °C")
    input("\nPress any key to continue...")
    return year

# Dummy temperature prediction function (Replace with a real model)
def predict_global_temp(year):
    base_temp = 15.0  # Base global temperature in 2020
    year_diff = year - 2020
    increase_rate = 0.02  # Increase rate per year
    return base_temp + year_diff * increase_rate

display_info()
year = get_year_and_predict_temp()
from datetime import datetime, timedelta

# Constants for solar position calculation
DEG_TO_RAD = np.pi / 180
RAD_TO_DEG = 180 / np.pi

# Solar declination calculation
def solar_declination(day_of_year):
    return 23.45 * np.sin(DEG_TO_RAD * (360 / 365 * (day_of_year - 81)))

# Hour angle calculation
def hour_angle(hour, solar_noon=12):
    return 15 * (hour - solar_noon)

# Solar altitude and azimuth calculation
def solar_position(latitude, day_of_year, hour):
    declination = solar_declination(day_of_year)
    h_angle = hour_angle(hour)

    sin_altitude = (np.sin(DEG_TO_RAD * latitude) * np.sin(DEG_TO_RAD * declination) +
                    np.cos(DEG_TO_RAD * latitude) * np.cos(DEG_TO_RAD * declination) *
                    np.cos(DEG_TO_RAD * h_angle))
    altitude = np.arcsin(sin_altitude) * RAD_TO_DEG

    cos_azimuth = ((np.sin(DEG_TO_RAD * declination) - np.sin(DEG_TO_RAD * latitude) * np.sin(DEG_TO_RAD * altitude)) /
                   (np.cos(DEG_TO_RAD * latitude) * np.cos(DEG_TO_RAD * altitude)))
    azimuth = np.arccos(cos_azimuth) * RAD_TO_DEG

    if h_angle > 0:
        azimuth = 360 - azimuth

    return altitude, azimuth

# Solar irradiance model
def solar_irradiance(altitude, azimuth, tilt=0, panel_azimuth=0):
    I_0 = 1367  # Solar constant in W/m^2
    AM = 1 / np.sin(DEG_TO_RAD * altitude)  # Air mass coefficient

    if altitude > 0:
        tilt_factor = (np.cos(DEG_TO_RAD * (tilt - altitude)) *
                       np.cos(DEG_TO_RAD * (azimuth - panel_azimuth)))
        I_tilted = I_0 * tilt_factor / (AM ** 1.5)
    else:
        I_tilted = 0

    return max(I_tilted, 0)

# Energy production model
def energy_production(day_of_year, latitude, tilt, panel_azimuth, efficiency=0.15, area=1):
    energy = 0
    for hour in range(0, 24):
        altitude, azimuth = solar_position(latitude, day_of_year, hour)
        irradiance = solar_irradiance(altitude, azimuth, tilt, panel_azimuth)
        energy += irradiance * efficiency * area
    return energy

# Example energy calculation
latitude = 35.0
day_of_year = 172  # June 21 (Summer Solstice)
tilt = 30
panel_azimuth = 180

daily_energy = energy_production(day_of_year, latitude, tilt, panel_azimuth)
print(f"\nEstimated Daily Energy Output: {daily_energy:.2f} Wh")
from scipy.optimize import minimize

# Cost function (land usage + cost + energy production)
def objective(params, day_of_year, latitude):
    tilt, panel_azimuth, spacing = params
    daily_energy = energy_production(day_of_year, latitude, tilt, panel_azimuth)
    land_usage = spacing * 10  # Example land usage cost model
    cost = land_usage + 1000 / daily_energy  # Simplified cost model
    return -daily_energy + cost

# Constraints
def spacing_constraint(params):
    return params[2] - 0.5  # Minimum spacing of 0.5 units

# Optimization setup
initial_guess = [30, 180, 1.0]  # Initial guess for tilt, azimuth, spacing
constraints = {'type': 'ineq', 'fun': spacing_constraint}
bounds = [(0, 90), (0, 360), (0.5, 5.0)]  # Tilt, azimuth, spacing bounds

# Run optimization
opt_result = minimize(objective, initial_guess, args=(day_of_year, latitude), constraints=constraints, bounds=bounds)

optimal_tilt, optimal_azimuth, optimal_spacing = opt_result.x
optimal_energy = -opt_result.fun

print(f"\nOptimal Tilt: {optimal_tilt:.2f} degrees")
print(f"Optimal Azimuth: {optimal_azimuth:.2f} degrees")
print(f"Optimal Spacing: {optimal_spacing:.2f} units")
print(f"Optimal Daily Energy Output: {optimal_energy:.2f} Wh")
# Graph Solar Irradiance Throughout the Day
def graph_irradiance(day_of_year, latitude, tilt, azimuth):
    hours = range(0, 24)
    irradiances = [solar_irradiance(*solar_position(latitude, day_of_year, hour), tilt, azimuth) for hour in hours]

    plt.figure(figsize=(10, 5))
    plt.plot(hours, irradiances, marker='o')
    plt.title('Solar Irradiance Throughout the Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Irradiance (W/m^2)')
    plt.grid(True)
    plt.show()

graph_irradiance(day_of_year, latitude, optimal_tilt, optimal_azimuth)
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from scipy.optimize import minimize

# Constants
DEG_TO_RAD = np.pi / 180
RAD_TO_DEG = 180 / np.pi

# Display Software House and Team Information
def display_info():
    print("\n=== Solar Farm Layout Optimization Software ===")
    print("Software House: BrightEnergy Solutions")
    print("Programming Team:")
    print("1. Student A - ID: 123456")
    print("2. Student B - ID: 7891011")
    print("3. Student C - ID: 12131415")
    print("=============================================")
    print("\n")

# Ask user for year and predict global temperature
def get_year_and_predict_temp():
    year = int(input("Enter a year for global temperature prediction (e.g., 2025, 2050, 2100): "))
    predicted_temp = predict_global_temp(year)
    print(f"\nPredicted Average Global Temperature for {year}: {predicted_temp:.2f} °C")
    input("\nPress any key to continue...")
    return