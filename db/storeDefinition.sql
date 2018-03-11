/********************
Drop tables
*********************/
DROP TABLE IF EXISTS [Items];
DROP TABLE IF EXISTS [Pricing_Rules];

/********************
Create tables
*********************/
CREATE TABLE [Items]
(
  [code] TEXT NOT NULL,
  [name] TEXT NOT NULL,
  [price] REAL NOT NULL,
  CONSTRAINT [PK_Code] PRIMARY KEY ([code])
);

CREATE TABLE [Pricing_Rules]
(
  [name] TEXT NOT NULL,
  [item_code] TEXT NOT NULL,
  [min_units] INTEGER NOT NULL,
  [divisor] INTEGER,
  [multiplier] INTEGER,
  [discount] REAL,
  [extra_data] TEXT,
  CONSTRAINT [PK_RuleName_Item] PRIMARY KEY ([name], [item_code])
);



/*************************
Insert values
**************************/
INSERT INTO [Items] VALUES ('VOUCHER','Voucher',5.0);
INSERT INTO [Items] VALUES ('TSHIRT','T-Shirt',20.0);
INSERT INTO [Items] VALUES ('MUG','Coffee Mug',7.5);
