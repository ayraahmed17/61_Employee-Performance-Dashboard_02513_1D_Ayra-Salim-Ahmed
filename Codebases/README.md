#  Employee Performance Dashboard

##  Project Overview

The **Employee Performance Dashboard** is a Python-based project that analyzes employee performance using data stored in a CSV file.

It uses Python libraries like **Pandas** and **Matplotlib** to process employee information, calculate department-wise performance, identify top performers, and display results through graphs and charts.

The project provides a simple menu-driven interface that allows users to explore employee performance data.

##  Project Objectives

- Analyze employee performance ratings.
- Calculate average ratings for each department.
- Identify the top-performing employee.
- Categorize employees based on their ratings.
- Calculate total projects completed by each department.
- Display data using bar charts and pie charts.
- Handle invalid or missing employee records.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data handling and analysis |
| Matplotlib | Data visualization |
| CSV | Storing employee information |

##  Project Structure

```text
Employee-Performance-Dashboard/
│
├── employee_dashboard.py
├── employees.csv
├── README.md
└── requirements.txt
```

##  CSV File Format

The project requires an `employees.csv` file containing the following columns:

| Name | Department | Rating | Projects |
|---|---|---:|---:|
| Rahul | IT | 4.8 | 5 |
| Aman | HR | 3.9 | 3 |
| Priya | Finance | 4.5 | 6 |
| Neha | IT | 2.8 | 2 |
| Karan | HR | 3.2 | 4 |

**Note:** Rating must be between 1 and 5, and the number of projects must be zero or greater.

##  Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Install Required Libraries

Open the VS Code terminal and execute:

```bash
pip install pandas matplotlib
```

### Step 3: Prepare Project Files

Create the following files:

- `employee_dashboard.py` – Store the Python project code.
- `employees.csv` – Store employee records.
- `README.md` – Project documentation.

### Step 4: Run the Project

Execute the following command in the terminal:

```bash
python employee_dashboard.py
```

##  Project Features

### 1. Department Average

Calculates the average performance rating of employees in each department and displays a bar chart.

### 2. Top Performer

Identifies the employee with the highest performance rating and displays their name, department, rating, and performance category.

### 3. Performance Categories

Classifies employees into four performance categories:

| Rating | Category |
|---|---|
| 4.5 – 5.0 | Outstanding |
| 3.5 – 4.49 | Good |
| 2.5 – 3.49 | Average |
| 1.0 – 2.49 | Needs Improvement |

Displays the distribution using a pie chart.

### 4. Projects per Department

Calculates the total number of projects completed by employees in each department and displays a bar chart.

### 5. Exit

Allows users to safely exit the dashboard.

##  Python Concepts Used

- **Pandas:** Used for reading, cleaning, and analyzing employee data.
- **Matplotlib:** Used to create graphs and charts.
- **CSV Handling:** Used to read employee information from a CSV file.
- **Conditional Statements:** Used to classify employee performance.
- **Functions:** Used to categorize employee ratings.
- **Loops:** Used to repeatedly display the menu until the user exits.
- **Data Validation:** Used to identify and skip invalid records.
- **GroupBy:** Used to calculate department-wise statistics.
- **Aggregation:** Used to calculate average ratings and total projects.

##  Expected Output

When the program runs, the following menu appears:

```text
===== EMPLOYEE PERFORMANCE DASHBOARD =====

1. Department Average
2. Top Performer
3. Performance Categories
4. Projects per Department
5. Exit

Enter your choice:
```

The user can select any option from 1 to 5 to explore employee performance information.

##  Future Improvements

- Add an interactive graphical user interface (GUI).
- Store employee information in a database.
- Generate downloadable performance reports.
- Add employee search functionality.
- Include more performance metrics.
- Allow users to add and update employee records.

##  Conclusion

The Employee Performance Dashboard is a simple data analysis project developed using Python. It demonstrates how employee data can be cleaned, analyzed, categorized, and visualized.

This project helps understand the practical applications of Python programming, data analysis, and data visualization.

---

**Project Name:** Employee Performance Dashboard  
**Language:** Python  
**Libraries:** Pandas, Matplotlib  
**Project Type:** Data Analysis and Visualization