# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt


# Define function to create admin dashboard
def create_admin_dashboard():
    # Load data from CSV file
    data = pd.read_csv("data.csv")

    # Calculate total number of users
    total_users = len(data)

    # Calculate percentage of active users
    active_users = data["status"].value_counts(normalize=True)["active"] * 100

    # Create bar chart to visualize user status
    plt.bar(["Active", "Inactive"], [active_users, 100 - active_users])
    plt.title("User Status")
    plt.xlabel("Status")
    plt.ylabel("Percentage")
    plt.show()

    # Calculate average session duration
    avg_session_duration = data["session_duration"].mean()

    # Calculate average number of logins per day
    avg_logins_per_day = data["logins"].sum() / len(data["date"].unique())

    # Print summary statistics
    print("Total number of users: {}".format(total_users))
    print("Percentage of active users: {:.2f}%".format(active_users))
    print("Average session duration: {:.2f} minutes".format(avg_session_duration))
    print("Average logins per day: {:.2f}".format(avg_logins_per_day))


# Call function to create admin dashboard
create_admin_dashboard()
