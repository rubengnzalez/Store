import os
import sqlite3


class Item:
    """Defines an item. It can be initialized by providing its code. Remaining information <name, price>
    is retrieved from a database (in this case, SQLite3)"""

    def __init__(self, code):
        data = self.getItemByCode(code)
        if data:
            # Data tupleis filled
            self.code = data[0]
            self.name = data[1]
            self.price = data[2]
        else:
            #Unknown item, return default values
            self.code = ''
            self.name = ''
            self.price = 0.0

    def getItemByCode(self, code):
        """Tries to connect to database and get ITEM tuple for the code given as parameter"""
        try:
            PATH = os.path.dirname(os.path.realpath(__file__))
            DATABASE = os.path.join(PATH, '..', 'db', 'store.db')
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('SELECT * FROM ITEMS WHERE CODE=?', (code,))
            row = c.fetchone()
            while True:
                if row == None:
                    return None
                else:
                    return row
        except sqlite3.Error as e:
            print("An error occurred while retrieving Item: ", e.args[0])
            return None
        finally:
            c.close()
            conn.close()

    def toString(self):
        """Returns a printable string of the ITEM object"""
        return '[ code: ' + self.code + ',\tname: ' + self.name + ',\tprice: ' + str(self.price) + ' € ]'

if __name__ == "__main__":

    print("Running Item as main class.")