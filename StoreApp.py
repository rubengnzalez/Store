import os
import sqlite3

from Store.store.Checkout import Checkout
from Store.store.Item import Item
from Store.store.PricingRule import PricingRule


###################################################################################################
# PREPARE ENVIRONMENT - CREATE DATABASE and INSERT ITEMS
###################################################################################################


def createDB():
    res = True
    try:
        # read database definition script
        PATH = os.path.dirname(os.path.realpath(__file__))
        scriptPATH = os.path.join(PATH, 'db', 'storeDefinition.sql')
        qry = open(sqlScriptPath, 'r').read()
        DATABASE = os.path.join(PATH, 'db', 'store.db')
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # execute previously read script
        c.executescript(qry)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred while creating DB: ", e.args[0])
        res = False
    finally:
        c.close()
        conn.close()
        return res


if __name__ == "__main__":
    sqlScriptPath = './db/storeDefinition.sql'
    dbPath = './db/store.db'
    # database creation
    successDB = createDB()
    if not successDB:
        print("An error occurred while creating database. Aborting...")
        exit()

    voucher = Item('VOUCHER')
    # Create pricing rules
    voucher_2x1 = PricingRule('Voucher_2x1','VOUCHER', 2, 2, 1, 0.0, None)
    tshirt_decreasePrice = PricingRule('TShirt_19€','TSHIRT', 3, 1, 1, 0.05, None)
    pricing_rules = [voucher_2x1, tshirt_decreasePrice]
    # Initialize a Checkout 1 without pricing rules.
    co1 = Checkout()
    co1.scan("VOUCHER")
    co1.scan("VOUCHER")
    # scan an unknown item <PET>, so it will not be included in the bill
    co1.scan("PET")
    co1.total()
    co1.clear()
    print("****************************************")

    co1.scan("VOUCHER")
    co1.scan("MUG")
    co1.scan("TSHIRT")
    co1.scan("TSHIRT")
    co1.scan("TSHIRT")
    co1.scan("VOUCHER")
    co1.total()
    co1.clear()
    print("****************************************")

    # Initialize Checkout WITH Pricing Rules
    print("New Discounts: VOUCHERS 2x1!! Take 3 or more T-Shirts and pay 19€ each!!")
    print("****************************************")
    co2 = Checkout(pricing_rules)
    co2.scan("VOUCHER")
    co2.scan("TSHIRT")
    co2.scan("MUG")
    co2.total()
    co2.clear()
    print("****************************************")

    co2.scan("VOUCHER")
    co2.scan("TSHIRT")
    co2.scan("VOUCHER")
    co2.total()
    co2.clear()
    print("****************************************")

    co2.scan("TSHIRT")
    co2.scan("TSHIRT")
    co2.scan("TSHIRT")
    co2.scan("VOUCHER")
    co2.scan("TSHIRT")
    co2.total()
    co2.clear()
    print("****************************************")

    co2.scan("VOUCHER")
    co2.scan("TSHIRT")
    co2.scan("VOUCHER")
    co2.scan("VOUCHER")
    co2.scan("MUG")
    co2.scan("TSHIRT")
    co2.scan("TSHIRT")
    co2.total()
    print("****************************************")
    print("Example of Simplied bill for the same Checkout:")
    co2.printSimplifiedBill()
    co1.clear()
