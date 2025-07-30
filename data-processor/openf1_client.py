import requests

def get_race_data():
    response = requests.get("https://api.openf1.org/v1/sessions?year=2023&session_name=Race")
    return response.json()

if __name__ == "__main__":
    data = get_race_data()
    print(f"Found {len(data)} races")
    print(data[0])  # Print first race to see structure