# Example fixed exchange rates for demonstration purposes
exchange_rates = {
    'USD': {'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'JPY': 129.53, 'GBP': 0.88},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 151.16}
}

def convert_currency(amount, from_currency, to_currency):
    """Converts currency from one form to another using the exchange rates."""
    if from_currency == to_currency:
        return amount
    try:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        return "Error: Conversion rate not available."

def currency_converter():
    print("Welcome to the Currency Converter!")
    print("Available currencies: USD, EUR, JPY, GBP")

    while True:
        from_currency = input("Enter the currency you have (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        result = convert_currency(amount, from_currency, to_currency)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

        next_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if next_conversion != 'yes':
            break

# Call the currency converter function
currency_converter()
import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = 'YOUR_API_KEY'  # Replace with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    if to_currency in data['rates']:
        return data['rates'][to_currency]
    else:
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return amount * rate
    else:
        return "Error: Conversion rate not available."

# Replace the currency_converter function with one using the new convert_currency
def currency_converter():
    print("Welcome to the Currency Converter!")
    print("Available currencies: Check your API for supported currencies")

    while True:
        from_currency = input("Enter the currency you have (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        result = convert_currency(amount, from_currency, to_currency)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

        next_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if next_conversion != 'yes':
            break
        #call the currency converter function
        currency_converter()