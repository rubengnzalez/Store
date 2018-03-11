import os
import sqlite3


class PricingRule:
    """Defines PricingRule concept."""

    def __init__(self, description, itemCode, minUnits, divisor, multiplier, discountPerc, extraData):
        """Initializes PricingRule with some fixed attributes and another, in JSON format, named extra_data
        which is a dynamic field (JSON format) that may contain more parameters
        for calculating discounts, such as maximumum number of items, free item of different type, etc."""
        self.description = description
        self.itemCode = itemCode
        self.minUnits = minUnits
        self.divisor = divisor
        self.multiplier = multiplier
        self.discountPerc = discountPerc
        self.extraData = extraData
        self.createRule();

    def createRule(self):
        """Insert a PricingRule into Database if does not exist"""
        res = True

        try:
            PATH = os.path.dirname(os.path.realpath(__file__))
            DATABASE = os.path.join(PATH, '..', 'db', 'store.db')
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('INSERT OR IGNORE INTO PRICING_RULES VALUES (?, ?, ?, ?, ?, ?, ?)',
                      (self.description, self.itemCode, self.minUnits, self.divisor, self.multiplier, self.discountPerc, self.extraData))
            conn.commit()
        except sqlite3.Error as e:
            print("An error occurred while creating rule <" + self.description + "> for <" + self.itemCode + ">: ", e.args[0])
            res = False
        finally:
            c.close()
            conn.close()
            return res

    def genericDiscountRate(self, items):
        """Applies a generic algorithm / formula based on main fields of PricingRules
        except extra_data and returns a rate to be applied to base price of the item"""
        rate = float(items)
        if items >= self.minUnits:
            rate = (float(int(items / self.divisor)) * self.multiplier * (1.0 - self.discountPerc)) + (float(int(items % self.divisor)) * self.multiplier * (1.0 - self.discountPerc))
        return rate


if __name__ == "__main__":

    print("Running PricingRule as main class.")