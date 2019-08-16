# CSV-pre-processor-for-GnuCash
Python 3 code to replace qifqif function to match GnuCash transactions with Transfer accounts based on transaction desccription. Wrote this because my bank took away the Qif file download so now have to download CSV files. Takes transaction CSV download from bank and adds Transfer Account column based on text in Description. 

You will need to install Python 3 and Pandas.

You can run it from the command line with: <b>csv_for_GnuCash</b> <i>transaction file name</i>

Transaction CSV columns from bank:

Date, Description, Amount, Balance

Ignore Balance, use characters from Description to id the Transfer Account from a lookup file. 

Lookup file columns:

Description string, String_start, String_length,	Transfer account

Default Lookup file name is "account_lookup_for_GnuCash.csv".

String_start is based on first letter being in position 0.  

So if wanted to pick up on MONZO from "HUGH WILLIAM WRIGHJOINT MONZO TOP UP" I would use 

Description String = "MONZO"

String start = 24

String length = 5 

Transfer account = "Expense:Variable"  (or whatever account you are assigning to the MONZO 
transactions

Note the Description string needs to be unique in the Lookup file, if not then only the first one found will be used. The Transfer account can of course be non-unique as multiple different payment types could assign to the same Transfer account. 

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
