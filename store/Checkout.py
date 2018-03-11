from Store.store.Item import Item

class Checkout:
    """Checkout allows to scan items, calculates their prices, applies pricing rules if possible and prints bill"""

    def __init__(self, pricing_rules=None):
        self.totalPrice = 0.0
        self.items = 0
        # this dictionary stores the items scanned. Item code is the key and value is a tuple, which includes <Item object, itemCount>
        self.itemsDict = dict()
        # list of PricingRule
        self.pricing_rules = pricing_rules

    def itemsCount(self):
        """Returns the current number of items in the cart"""
        return self.items

    def clear(self):
        """Clears the Checkout data"""
        self.itemsDict.clear()
        self.items = 0
        self.totalPrice = 0.0


    def scan(self, code):
        """Scans the item code and add it to the cart.
        If already exists, increments its counter, if not... adds it"""
        itemTuple = self.itemsDict.get(code)
        if itemTuple:
            auxList = list(itemTuple)
            auxList[1] += 1
            itemTuple = tuple(auxList)
            self.itemsDict[code] = itemTuple
            self.items += 1
        else:
            i = Item(code)
            if i.code != "":
                # add <item,counter> to the dict if code is not empty / unknown
                self.itemsDict[code] = (i, 1)
                self.items += 1


    def sameItemPrice(self, code):
        """Calculates the sub-total amount for a given item type"""
        tuple = self.itemsDict.get(code, None)
        if not tuple:
            return 0.0
        return tuple[0].price * float(tuple[1])


    def applyItemDiscount(self, code, items):
        """Calculates the sub-total amount for a given item type, applying discount if exists"""
        discount = None
        if self.pricing_rules:
            for rule in self.pricing_rules:
                if rule.itemCode == code:
                    tuple = self.itemsDict[code]
                    discount = float(rule.genericDiscountRate(items)) * float(tuple[0].price)
                    break
        if not discount:
            return self.sameItemPrice(code)
        return discount


    def rawTotal(self):
        """It calculates and returns the total amount without applying any discount rule"""
        total = 0.0
        if self.itemsDict:
            for code in self.itemsDict.keys():
                total += self.sameItemPrice(code)
                self.totalPrice = total
        self.printBill()
        return self.totalPrice


    def total(self):
        """It applies, if exists, discount rules to the given item collection and returns total amount to be paid"""
        if self.itemsDict:
            total = 0.0
            if not self.pricing_rules:
                return self.rawTotal()
            for code, tuple in self.itemsDict.items():
                total += self.applyItemDiscount(code,tuple[1])
            self.totalPrice = total
        self.printBill()
        return self.totalPrice


    def printSimplifiedBill(self):
        if self.itemsDict:
            sList = "ITEMS:\t"
            for tuple in self.itemsDict.values():
                sList += tuple[0].code + "(x" + str(tuple[1]) + "), "
            print(sList[:-2])
        print("TOTAL:\t" + str("{0:.2f}".format(self.totalPrice)) + " €")

    def printBill(self):
        """Prints a bill that specifies number of items, name of item total price"""
        if self.itemsDict:
            for tuple in self.itemsDict.values():
                print(str(tuple[1]) + "\tx\t" + tuple[0].name + "\t" + str("{0:.2f}".format(self.applyItemDiscount(tuple[0].code, tuple[1]))) + " €")
        print("****************************************")
        print("TOTAL: \t\t\t\t\t" + str("{0:.2f}".format(self.totalPrice)) + " €")

if __name__ == "__main__":

    print("Running Checkout as main class.")