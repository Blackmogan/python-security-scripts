import requests

url = input("Enter URL (http/https): ")

try:
    response = requests.get(url, timeout=5)

    print("\nStatus Code:", response.status_code)
    print("\nHeaders:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print("Error:", e)
