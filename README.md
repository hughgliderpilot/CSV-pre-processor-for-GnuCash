# CSV-pre-processor-for-GnuCash
Takes transaction CSV download from bank and adds Transfer Account column based on Description. 

Transaction CSV columns from bank:
Date, Description, Amount, Balance

Ignore Balance, use characters from Description to id the Transfer Account from a lookup file. 

Lookup file columns:
Description String, String match position,	Transfer Account

Output file:
Date, Description, Amount, Balance, Transfer Account
If no Transfer Account found then just return null in the Transfer Account column.

Will also output Non-matching transactions, to facilitate adding the to the Lookup file for 
future use if required. 
There will be no Lookup file editing facility, if you want to edit it just use Excel or similar. 

Then can use GnuuCash Import Transactions from CSV. Need to set up the various settings and 
save so that can re-use and do future imports easily. 

Overall this should save time on transaction import and account matching by assigning regular 
payments to accounts. 
