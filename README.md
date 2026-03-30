# 📊 Data Analysis & Visualization Program

A powerful **Python CLI application** for ***loading, exploring, cleaning, analyzing, and visualizing*** CSV datasets — all from the terminal using **Pandas** and **Matplotlib**.

---

## 📌 Project Overview

**Data Analysis & Visualization Program** is a terminal-based Python application that gives users a ***complete data analysis pipeline*** through a clean, menu-driven interface. Users can load any ***CSV dataset***, explore its structure, perform ***DataFrame operations***, handle ***missing values***, generate ***descriptive statistics***, create ***6 types of visualizations***, and ***save plots*** — all without writing a single line of code manually.

Built using **Pandas** for data manipulation and **Matplotlib** for visualization, this project demonstrates how ***real-world data analysis workflows*** can be packaged into an interactive CLI tool.

---

## ✨ Features

- 📂 **Load Dataset** — Load any ***CSV file*** into a Pandas DataFrame by entering its file path
- 🔍 **Explore Data** — View *first/last 5 rows*, *column names*, *data types*, and *basic info*
- 🔧 **DataFrame Operations** — Perform *filtering*, *sorting*, *grouping*, and *column selection*
- 🩹 **Handle Missing Data** — *Display*, *fill*, *drop*, or *replace* missing values with ease
- 📈 **Descriptive Statistics** — Generate ***mean, median, std, min, max*** and more via `describe()`
- 🎨 **Data Visualization** — Create ***Bar Plot***, ***Line Plot***, ***Scatter Plot***, ***Pie Chart***, ***Histogram***, and ***Stack Plot***
- 💾 **Save Visualization** — Export any generated plot as a ***PNG file*** with a custom filename
- 🚪 **Exit** — *Cleanly exit* the program with a farewell message

---

## 🖥️ Program Walkthrough

### Step 1 — Main Menu & Load Dataset (Screenshot 1)

When the program launches, the ***main menu*** displays all **8 available options**. Selecting **`1`** prompts the user to enter a ***CSV file path***. The dataset is loaded into a **Pandas DataFrame** and a *success message* is shown.

> Example: Path **`data/sales_data.csv`** → *"Dataset loaded successfully!"*

![Main Menu and Load Dataset](Features/Screenshort_1.PNG)

---

### Step 2 — Explore Data & Handle Missing Data (Screenshot 2)

**Explore Data (Case 2):** Selecting **`2`** opens a sub-menu with **5 options** — display *first 5 rows*, *last 5 rows*, *column names*, *data types*, or *basic info*. The dataset is displayed in a ***clean tabular format***.

> Example: First 5 rows show **SalesID**, **Product**, **Region**, **Sales**, **Year** columns.

**Handle Missing Data (Case 4):** Selecting **`4`** opens a sub-menu to *display*, *fill*, *drop*, or *replace* missing values. If the dataset is clean, ***"No missing values found!"*** is displayed.

![Explore Data and Handle Missing](Features/Screenshort_2.PNG)

---

### Step 3 — Data Visualization & Save Visualization (Screenshot 3)

**Data Visualization (Case 6):** Selecting **`6`** opens a sub-menu with **6 chart types** — *Bar Plot*, *Line Plot*, ***Scatter Plot***, *Pie Chart*, *Histogram*, *Stack Plot*. Each chart prompts for relevant *axis column names*.

> Example: Scatter Plot with **x-axis: Sales**, **y-axis: Year** → *"Scatter plot displayed successfully!"*

**Save Visualization (Case 7):** Selecting **`7`** prompts for a ***filename*** and saves the current plot as a *PNG image*.

> Example: Saved as **`scatter_plot.png`** → *"Visualization saved successfully!"*

![Visualization and Save](Features/Screenshort_3.PNG)

---

### Step 4 — Exit (Screenshot 4)

Selecting **`8`** ***gracefully exits*** the program with the message — *"Exiting the program. Goodbye!"*

![Exit](Features/Screenshort_4.PNG)

---

## 🧠 Concepts Used

- 🐼 **Pandas Library** — Core DataFrame operations: `read_csv()`, `head()`, `tail()`, `describe()`, `info()`, `dtypes`, `isnull()`, `fillna()`, `dropna()`
- 📊 **Matplotlib Library** — All 6 chart types rendered using `plt.bar()`, `plt.plot()`, `plt.scatter()`, `plt.pie()`, `plt.hist()`, `plt.stackplot()` and `plt.savefig()`
- 🔀 **`match-case` Control Flow** — *Clean, structured* branching for the ***main menu*** and all ***nested sub-menus***
- 🗂️ **CSV File Handling** — Dataset loaded directly from a *file path* using `pd.read_csv()`
- 🩹 **Missing Data Handling** — Four strategies: *display*, *fill with mean*, *drop rows*, *replace with value*
- 📐 **Descriptive Statistics** — `df.describe()` generates *count, mean, std, min, max, quartiles* in one call
- 🔁 **`while True` Loop** — Keeps the program *running continuously* until the user exits
- 💻 **CLI Programming** — Interactive terminal interface using `input()` and `print()` with *formatted separators*

---

## ▶️ How to Run (Windows Friendly)

**Requirements:**
- ***Python 3.10 or higher*** (required for `match-case` support)
- ***Pandas*** and ***Matplotlib*** libraries installed

**Install dependencies:**
```bash
pip install pandas matplotlib
```

**Run the program:**
```bash
python SalesDataAnalyzer.py
```

**Prepare your dataset:**
```bash
# Place your CSV file in a data/ folder or provide the full path
# Example: data/sales_data.csv
```

> 💡 Make sure to **Load Dataset first** (option `1`) before using any other menu options — otherwise operations will fail on an *empty DataFrame*.

---

## 📂 Program Flow

> *The diagram below illustrates the complete program logic — menu choices, sub-menus, DataFrame operations, and loop flow.*
>
> **Flow Summary:**
> - 🟢 Program starts → **Main Menu** with **8 options**
> - 📂 **Case 1** → Prompts for CSV path → loads into ***Pandas DataFrame***
> - 🔍 **Case 2** → Sub-menu → *head / tail / columns / dtypes / info*
> - 🔧 **Case 3** → Sub-menu → *filter / sort / group / select columns*
> - 🩹 **Case 4** → Sub-menu → *display / fill / drop / replace* missing values
> - 📈 **Case 5** → Calls `df.describe()` → ***descriptive statistics***
> - 🎨 **Case 6** → Sub-menu → *6 chart types* → rendered via **Matplotlib**
> - 💾 **Case 7** → Prompts filename → saves plot as ***PNG***
> - 🔁 **while True** → All valid cases return to main menu automatically
> - ⏹ **Case 8** → Program exits gracefully

---

## 👨‍💻 Developer Notes & Code Highlights

### 📂 Loading a CSV Dataset with Pandas
```python
import pandas as pd

df = pd.read_csv("data/sales_data.csv")
print("Dataset loaded successfully!")
```
> `pd.read_csv()` loads any ***comma-separated file*** directly into a DataFrame — the foundation of every subsequent operation in the program.

---

### 🩹 Handling Missing Values — 4 Strategies
```python
# Display missing rows
print(df[df.isnull().any(axis=1)])

# Fill with mean
df.fillna(df.mean(), inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Replace with specific value
df.fillna(value, inplace=True)
```
> ***`inplace=True`*** modifies the DataFrame *directly* without needing to reassign — a key Pandas pattern for *in-place data cleaning*.

---

### 🎨 Generating a Scatter Plot with Matplotlib
```python
import matplotlib.pyplot as plt

plt.scatter(df[x_col], df[y_col])
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title("Scatter Plot")
plt.show()
```
> Column names are passed ***dynamically*** from user input — making the visualization engine flexible enough to work with *any dataset*, not just `sales_data.csv`.

---

### 💾 Saving a Visualization
```python
filename = input("Enter file name to save the plot: ")
plt.savefig(filename)
print(f"Visualization saved as {filename} successfully!")
```
> `plt.savefig()` exports the ***currently active Matplotlib figure*** — so the plot must be *generated first* before saving. The filename is fully *user-defined*.

---

## 📜 License

This project is licensed under the **MIT License** — *free to use, modify, and distribute.*

---

> Built with 🐍 **Python**, 🐼 **Pandas** & 📊 **Matplotlib**
