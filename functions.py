from csv import writer
from csv import *
from datetime import *
import datetime as dt
import pandas as pd
from pandas import *
import os
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'bold red'})
console = Console(theme=custom_theme)


# De juiste werkmap instellen
working_directory = '\\Users\\Gebruiker\\Documents\\Wincacademy\\Superpy'


# Functie om de huidige datum in te stellen in naar het bestand "current_date.txt" schrijven
def set_date():
    current_date = str(datetime.now().date())
    file_path = os.path.join(working_directory, 'current_date.txt')
    with open("current_date.txt", "w") as file:
        file.write(current_date)
        print(current_date)
        return 
set_date()


def set_specific_date(specific_date):
    with open('specific_date.txt', "w") as f:
        f.write(str(specific_date))

    print(f'Date set to: {specific_date}')

    return 

# Functie die de koop van een product beschrijft
def buy(id, product_name, buy_price, expiration_date, amount):
    file_exists = os.path.isfile('buy_overview.tsv')
    current_date = str(datetime.now().date())

    data = {
        'ID': id,
        'Product_name': product_name,
        'Buy_date': current_date,
        'Price': buy_price,
        'Expiration_date': expiration_date,
        'Amount': amount
    }

    with open('buy_overview.tsv', 'a', newline='') as file:
        writer_object = writer(file, delimiter='\t')
        if not file_exists:
            headers = data.keys()
            writer_object.writerow(headers)        
        
        writer_object.writerow(data.values())

    print(f'{product_name} bought')
    return 

# Functie die de verkoop van een product beschrijft
def sell(id, product_name, sell_price, amount):
    file_exists = os.path.isfile('sell_overview.tsv')
    current_date = str(datetime.now().date())
    total_profit = (sell_price - get_price(id)) * amount
    revenue = sell_price * amount

    data = {
        'ID': id,
        'Product_name': product_name,
        'Sell_date': current_date,
        'Price': sell_price,
        'Amount': amount,
        'Revenue': revenue,
        'Profit': total_profit    
    }

    with open('sell_overview.tsv', 'a', newline='') as file:
        writer_object = writer(file, delimiter='\t')
        if not file_exists:
            headers = data.keys()
            writer_object.writerow(headers)

        writer_object.writerow(data.values())
        file.close()
        return print('Product Sold')



# Current date > expiration date
# Itereren over de hele voorraad, kijken welke 'expiration_date(s)' in het verleden liggen t.o.v. 'current_date'
# Deze producten verwijderen
def expired_product():
    current_date = str(datetime.now().date())
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('buy_overview.tsv', sep='\t')
    df = df[(df['Expiration_date'] <= current_date)]
    return print(df)

# Functie waarmee de huidige datum met een specifiek aantal dagen gemanipuleerd kan worden
def advance_time(days):
    if days >= 0:
        current_date = datetime.now().date()
        time_delta = dt.timedelta(days)
        new_date = current_date + time_delta
        with open('advance_date.txt', 'w') as f:
            f.write(str(new_date))
        return print(f'Date advanced with {days} days, the new date is set to: {new_date}')
    else:
        print("Enter a number equal or greater than 0")
        return

def set_specific_date(date_string):
    specific_date = datetime.strptime(date_string, '%Y-%m-%d')
    return specific_date


# In deze functie wordt de hoeveelheid voorraad opgehaald op basis van het identificatienummer van een product
def report_inventory(id):
    df = pd.read_csv('buy_overview.tsv', sep='\t')
    df = df[df.ID.eq(id)]
    amount = df["Amount"].sum() 
    print(f'The amount of product with ID: {id} is: {amount}')
    return 

# In deze functie wordt de hoeveelheid verkochte producten opgehaald op basis van het identificatienummer van een product
def report_sales(id):
    df = pd.read_csv('sell_overview.tsv', sep='\t')
    df = df[df.ID.eq(id)]
    amount = df["Amount"].sum() 
    print(f'The amount of product with ID: {id} is: {amount}')
    return 

def revenue_today():
    current_date = str(datetime.now().date())
    df = pd.read_csv('sell_overview.tsv', sep='\t')
    df = df[df.Sell_date.eq(current_date)]
    revenue = df["Revenue"].sum() 
    print(f'The total revenue on {current_date} is: ${revenue}')
    return

def revenue_period(date1, date2):
    df = pd.read_csv('sell_overview.tsv', sep='\t')
    if date1 != None and date2 != None:
        df = df[(df['Sell_date'] >= date1) & (df['Sell_date'] <= date2)] 
        revenue = df["Revenue"].sum()
        print(f'The total profit between {date1} and {date2} is: ${revenue}')

    elif date1 != None and date2 == None:
        df = df[df.Sell_date.eq(date1)]
        revenue = df["Revenue"].sum()
        print(f'The total profit on {date1} is: ${revenue}')
    
    elif date1 == None and date2 != None:
        df = df[df.Sell_date.eq(date2)]
        revenue = df["Revenue"].sum()
        print(f'The total profit on {date2} is: ${revenue}')

    else:
        print("Please enter the required arguments")

    return


def profit_today():
    current_date = str(datetime.now().date())
    df = pd.read_csv('sell_overview.tsv', sep='\t')
    df = df[df.Sell_date.eq(current_date)]
    profit = df["Profit"].sum() 
    print(f'The total profit on {current_date} is: ${profit}')
    return

def profit_period(date1, date2):
    df = pd.read_csv('sell_overview.tsv', sep='\t')
    if date1 != None and date2 != None:
        df = df[(df['Sell_date'] >= date1) & (df['Sell_date'] <= date2)] 
        profit = df["Profit"].sum()
        print(f'The total profit between {date1} and {date2} is: ${profit}')

    elif date1 != None and date2 == None:
        df = df[df.Sell_date.eq(date1)]
        profit = df["Profit"].sum()
        print(f'The total profit on {date1} is: ${profit}')
    
    elif date1 == None and date2 != None:
        df = df[df.Sell_date.eq(date2)]
        profit = df["Profit"].sum()
        print(f'The total profit on {date2} is: ${profit}')

    else:
        print("Please enter the required arguments")

    return


def get_price(id):
    df = pd.read_csv('buy_overview.tsv', sep='\t')
    df = df[df.ID.eq(id)]
    product_price = df["Price"].sum()
    return(product_price)








