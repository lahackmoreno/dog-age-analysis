import pandas as pd
import matplotlib.pyplot as plt

# Set the dog's current age
dog_age = 2

# Create a range of ages to compare (1 to dog_age + 2)
ages = list(range(1, dog_age + 3))

# Simple method: 1 dog year = 7 human years
human_years_simple = [age * 7 for age in ages]

# Realistic method based on veterinary science
human_years_realistic = []
for age in ages:
    if age == 1:
        human_years_realistic.append(15)
    elif age == 2:
        human_years_realistic.append(24)
    else:
        human_years_realistic.append(24 + (age - 2) * 5)

# Create a DataFrame to organize the data
df = pd.DataFrame({
    "Dog Age": ages,
    "Simple Method": human_years_simple,
    "Realistic Method": human_years_realistic
})

# Display the data table
print("Dog Age to Human Age Comparison")
print("=" * 45)
print(df)
print()

# Create visualization
plt.figure(figsize=(10, 6))

# Plot both methods
plt.plot(df["Dog Age"], df["Simple Method"], 
         marker='o', label="Simple Method (x7)", 
         linewidth=2, markersize=8, color='blue')

plt.plot(df["Dog Age"], df["Realistic Method"], 
         marker='s', label="Realistic Method", 
         linewidth=2, markersize=8, color='green')

# Customize the plot
plt.title("Dog Age vs Human Age Comparison", fontsize=14, fontweight='bold')
plt.xlabel("Dog Age (years)", fontsize=12)
plt.ylabel("Human Age (years)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()

# Show the plot
plt.show()

# Print specific information for the current dog age
print(f"For a {dog_age}-year-old dog:")
print(f"  Simple method: {dog_age * 7} human years")
if dog_age == 1:
    realistic = 15
elif dog_age == 2:
    realistic = 24
else:
    realistic = 24 + (dog_age - 2) * 5
print(f"  Realistic method: {realistic} human years")