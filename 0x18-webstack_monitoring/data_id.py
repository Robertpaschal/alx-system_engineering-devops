import requests

# Datadog API base URL
base_url = "https://api.datadoghq.com/api/v1/dashboard"

# Datadog API key and application key
api_key = "ed7bbf5b8de0c21fdab6b13c0ba4b4a7"
app_key = "cff9501fdc157dbefa3ba61f398fc23d2af09733"

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": api_key,
    "DD-APPLICATION-KEY": app_key
}

# Make GET request to retrieve list of dashboards
response = requests.get(base_url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    # Loop through dashboards to find the desired one (you might want to adjust this part)
    for dashboard in data["dashboards"]:
        if dashboard["title"] == "Odinaka's Dashbord":
            # Get the ID of the dashboard
            dashboard_id = dashboard["id"]
            print("Dashboard ID:", dashboard_id)
            break
    else:
        print("Dashboard not found.")
else:
    print("Error:", response.status_code)
