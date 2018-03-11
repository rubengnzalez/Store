The purpose of this document is to explain some choices along this solution's implementation.

Solutions has finally been implemented in Python 3.4 as it was the version I had previously installed, but it can be run with latest Python 3.6 version.
Since the requirements said "to develop a maintainable and extensible code", I decided to define the classes below:
  - Item -> Represents the item whose attributes are:
      1) code
      2) name
      3) price

  - Checkout -> Represents a checkout / purchase process. Its attributes are: 
      1) totalPrice: total price of the items in the checkout instance
      2) items: total number of items in checkout/ cart
      3) itemsDict: it is a dictionary (also known as hashmap in other languages like Java). The selected key is the item code and value is a tuple <Item, number_of_items>. This allows to not store the same item object too many times. If a product is scanned more than once, it will only increment the counter into tuple (for that type)
      4) pricing_rules: list PricingRule instances passed as parameter to the constructor so that they can be applied when total() function is called.
  
  - PricingRule -> This object is used to represent most pricing rules with the following attributes:
      1) description: it is the name of the rule
      2) itemCode: identifies the item / product that will be applied the discount
      3) minUnits: minimum number of items to be added to checkout (scanned) so that the discount can be applied
      4) divisor and 5) multiplier: these attributes allow to apply those discounts that give free products if you buy more than X product of that type. E.g. 2x1, 3x2, 5x3... offers can be defined with those attributes.
      5) discountPerc: discount percentage to be applied to all items' price. E.g. "If you buy 3 or more TShirts, their price will decrease to 19€"
      6)extraData: In JSON format, this attribute is not used currently but allows to represent any other pricing rule without modifying PricingRule structure. Some attributes may be defined such as: maxUnits (define a max number of items that will get the pricingRule), freeDifferentItem (may define other itemCode as gift),etc.


Regarding to the database architecture, two tables were defined for simplicity:
ITEM: same number of attributes than Item object.
PRICING_RULES: same number of attributes than PricingRules + itemCode

Note that a better (more formal) solution would be removing item code from PRICING_RULES table and creating a relation table "ActiveDiscounts" with <itemCode, id_pricingRule (or name)>

Database definition is provided in 'db' folder: storeDefinition.sql
It is assumed that products will be inserted into database through another interface, so creation/insertion of new products was not implemented in this solution.
If you try to scan an unkown product [ E.g. Checkout.scan("PET") ] it will not be included in the checkout total price.

Although SQLite does not require a separate server process, it is included a bash script that downloads, configures and intalls SQLite3 server. It could be helpful to read database status while the technicians check this solution.

StoreApp module is provided just to run the app in an easily mode, it allows to create database (deleting previous tables) and some checkout processes. Current implementation shows two checkout processes without pricing rules and the following ones will apply the pricing rules required: Vouchers 2x1 and T-Shirts to 19€ (by buying 3 or more). Two bill printers have been implemented: printBill (detailed) and printSimplifiedBill (simplified).

FEEL FREE TO MODIFY THE SCAN PROCESSES!!


 

