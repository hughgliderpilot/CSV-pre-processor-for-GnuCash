# CSV-pre-processor-for-GnuCash
Takes transaction CSV download from bank and adds Transfer Account column based on text in 
Description. 

Transaction CSV columns from bank:
Date, Description, Amount, Balance

Ignore Balance, use characters from Description to id the Transfer Account from a lookup file. 

Lookup file columns:
Description string, String start, String length,	Transfer account
Default Lookup file name is "account_lookup_for_GnuCash.csv".

String start is based on first letter being in position 0.  

So if wanted to pick up on MONZO from "HUGH WILLIAM WRIGHJOINT MONZO TOP UP" I would use 
Description String = "MONZO"
String start = 24
String length = 5 
Transfer account = "Expense:Variable"  (or whatever account you are assigning to the MONZO 
transactions

Output file:
Date, Description, Amount, Balance, Transfer Account
If no Transfer Account found then just return null in the Transfer Account column.

Will also output to the screen the Description for non-matching transactions, and also output
these to a file non-matching.csv to facilitate adding them to the Lookup file for future use if required. 

There will be no Lookup file editing facility, if you want to edit it just use Excel or similar. 

Then can use GnuuCash Import Transactions from CSV. Need to set up the various settings and 
save so that can re-use and do future imports easily. 

Overall this should save time on transaction import and account matching by assigning regular 
payments to accounts. 
