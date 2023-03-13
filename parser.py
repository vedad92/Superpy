import argparse
import sys
from functions import *
from report import *
from tabulate import tabulate
import argparse
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'bold red'})
console = Console(theme=custom_theme)


func_dict = {
    'buy': buy,
    'sell': sell,
    'advance_time': advance_time,
    'set_specific_date': set_specific_date,
    'expired_product': expired_product,
    'report_inventory': report_inventory,
    'report_sales': report_sales,
    'report_revenue_today': revenue_today,
    'report_revenue_period': revenue_period,
    'report_profit_today': profit_today,
    'report_profit_period': profit_period,
}

my_parser = argparse.ArgumentParser(prog='PROG')
my_parser.add_argument('function', choices=list(func_dict.keys()), type=str, help='function to call')
my_parser.add_argument('-id', help='Fill in ID') #my_parser.add_argument('-id', type=int and str, help='Fill in ID')
my_parser.add_argument('-prn', '--product_name', help='product name', metavar='')
my_parser.add_argument('-exp', '--exp_date', help='expiration date yyyy-mm-dd', metavar='')
my_parser.add_argument('-am', '--amount', type=int, help='amount', metavar='')
my_parser.add_argument('-bp', '--buy_price', type=float, help='buy price', metavar='')
my_parser.add_argument('-slp', '--sell_price', type=float, help='sell price', metavar='')
my_parser.add_argument('-days', '--days', type=int, help='advance time in days', metavar='')
my_parser.add_argument('-dt1', '--date1', type=str, help='date format yyyy-mm-dd', metavar='')
my_parser.add_argument('-dt2', '--date2', type=str, help='date format yyyy-mm-dd', metavar='')
my_parser.add_argument('-spd', '--specific_date', type=str, help='date format yyyy-mm-dd', metavar='')



args = my_parser.parse_args()

if args.function == 'buy':
    if args.id is None:
        print("required product name")
        exit()
    elif args.product_name is None:
        print("required product name")
        exit()
    elif args.buy_price is None:
        print("required product price")
        exit()
    elif args.exp_date is None:
        print("required expiration date")
        exit()
    elif args.amount is None:
        print("required expiration date")
        exit()
    else:
        buy(args.id, args.product_name, args.buy_price, args.exp_date, args.amount)


#Verbeteringen:
# - scannen op expiration date om te kijken of het product wat verkocht wordt niet over datum is
# - 
if args.function == 'sell':
    if args.id is None:
        print("required product name")
        exit()
    elif args.product_name is None:
        print("required product name")
        exit()
    elif args.sell_price is None:
        print("required product price")
        exit()
    # elif args.exp_date is None:
    #     print("required expiration date")
    #     exit()
    elif args.amount is None:
        print("required expiration date")
        exit()
    else:
        sell(args.id, args.product_name, args.sell_price, args.amount)

if args.function == 'expired_product':
    expired_product()

if args.function == 'advance_time':
    if args.days is None:
        print("Required amount of days to advance time with")
        exit()
    else:
        advance_time(args.days)

if args.function == 'set_specific_date':
    if args.specific_date is None:
        print("Please enter the date you want to set")
        exit()
    else:
        set_specific_date(args.specific_date)



if args.function == 'report_inventory':
    if args.id is None:
        print("Required id to find products")
        exit()
    else:
        report_inventory(args.id)

if args.function == 'report_sales':
    if args.id is None:
        print("Required id to find products")
        exit()
    else:
        report_inventory(args.id)

if args.function == 'report_revenue_today':
    revenue_today()

if args.function == 'report_revenue_period':
    revenue_period(args.date1, args.date2)

if args.function == 'report_profit_today':
    profit_today()

if args.function == 'report_profit_period':
    profit_period(args.date1, args.date2)





    



# sell_parser = subparsers.add_parser('sell')
# sell_parser.add_argument('-product')
# sell_parser.add_argument('-price')
# sell_parser.add_argument('-amount')
# sell_parser.add_argument('-amount')

# report_parser = subparsers.add_parser('report')
# report_parser.add_argument()
# report_parser.add_argument()
# report_parser.add_argument()
# report_parser.add_argument()

# args = buy_parser.parse_args()

# print(add_bought_product(args.id, args.product_name,args.price, args.expiration_date, args.amount))