
# Employee Performance Dashboard

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read employee data from CSV file
df = pd.read_csv("employees.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check required columns
required = ["Name", "Department", "Rating", "Projects"]

if not all(col in df.columns for col in required):
    print("CSV file has missing columns.")
    exit()

# Remove extra spaces from text
df["Name"] = df["Name"].astype(str).str.strip()
df["Department"] = df["Department"].astype(str).str.strip()

# Convert Rating and Projects into numbers
ratings = pd.to_numeric(df["Rating"], errors="coerce")
projects = pd.to_numeric(df["Projects"], errors="coerce")

# Step 2: Validate employee data
valid = (
    ratings.between(1, 5)
    & projects.notna()
    & (projects >= 0)
    & (df["Name"] != "")
    & (df["Department"] != "")
)

# Show invalid rows
for i in df.index:
    if not valid.loc[i]:
        if not ratings.notna().loc[i] or not ratings.between(1, 5).loc[i]:
            print(
                f"Invalid rating {df.loc[i, 'Rating']} "
                f"for {df.loc[i, 'Name']}. "
                "Rating must be between 1 and 5. Row skipped."
            )
        else:
            print("Invalid employee data. Row skipped.")

# Keep only valid rows
df = df.loc[valid].copy()

# Store converted numbers
df["Rating"] = ratings.loc[valid]
df["Projects"] = projects.loc[valid]

if df.empty:
    print("No valid employee records found.")
    exit()

# Step 3: Assign performance categories
def get_category(rating):

    if rating >= 4.5:
        return "Outstanding"

    elif rating >= 3.5:
        return "Good"

    elif rating >= 2.5:
        return "Average"

    else:
        return "Needs Improvement"


df["Category"] = df["Rating"].apply(get_category)

# Step 4: Calculate department average and projects
department_data = df.groupby("Department").agg(
    Average_Rating=("Rating", "mean"),
    Total_Projects=("Projects", "sum")
)

# Step 5: Display menu
while True:

    print("\n===== EMPLOYEE PERFORMANCE DASHBOARD =====")
    print("1. Department Average")
    print("2. Top Performer")
    print("3. Performance Categories")
    print("4. Projects per Department")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Department Average
    if choice == "1":

        print("\nDepartment Average Ratings")

        print(department_data["Average_Rating"].round(2))

        department_data["Average_Rating"].plot(
            kind="bar",
            title="Average Rating by Department",
            xlabel="Department",
            ylabel="Average Rating"
        )

        plt.tight_layout()
        plt.show()

    # Option 2: Top Performer
    elif choice == "2":

        top_index = df["Rating"].idxmax()
        top = df.loc[top_index]

        print("\nTop Performer:", top["Name"])
        print("Department:", top["Department"])
        print("Rating:", top["Rating"])
        print("Category:", top["Category"])

    # Option 3: Performance Categories
    elif choice == "3":

        categories = [
            "Outstanding",
            "Good",
            "Average",
            "Needs Improvement"
        ]

        counts = df["Category"].value_counts().reindex(
            categories, fill_value=0
        )

        print("\nPerformance Categories")

        for category in categories:
            print(category + ":", counts[category])

        # Pie chart
        counts = counts[counts > 0]

        counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            title="Employee Performance Categories"
        )

        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    # Option 4: Projects per Department
    elif choice == "4":

        print("\nTotal Projects per Department")

        print(department_data["Total_Projects"])

        department_data["Total_Projects"].plot(
            kind="bar",
            title="Projects per Department",
            xlabel="Department",
            ylabel="Total Projects"
        )

        plt.tight_layout()
        plt.show()

    # Option 5: Exit
    elif choice == "5":

        print("Thank you for using Employee Dashboard!")
        break

    else:

        print("Invalid choice. Please select 1 to 5.")
