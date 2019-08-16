## Installation and Run Instructions

There is no automatic installation. 

I tried to make it run from right-clicking the transaction file and then have csv_for_GnuCash as an option, this can be done if you compile the code with something like Pyinstaller and then associate the Python module csv_pre_processor_for GnuCash.exe with .CSV files so it opens the programmer when you right click on your CSV file downloaded from the bank with the transactions.  (See detailed instructions on how to do this below. )

Otherwise just run from a Python 3 command line.

You will need:

1. Python 3 and Pandas installing.

2. A config file, the easiest way to set this up is to download the .csv_GnuCash.csv file from this repo to your home directory (typically <b>C:\\Users\\</b><i>USERNAME</i>) and edit if required. This file specifies
- Lookup_file path and file name. 
- Output_folder path indicating the directories to be used for the output files. 

If not found or invalid entries then the following defaults will be used. 
- Lookup file: {home_directory}\Documents\account_lookup_for_GnuCash.csv
- Output_folder: {home_directory}\Downloads

The output files are called 
- xac_ac_for_GnuCash_<date_time> eg typically on Windows: <b>C:\\Users\\</b><i>USERNAME</i><b>\\Downloads\\xac_ac_for_GnuCash_yymmddHHMM.csv</b>
- account_lookup_no_match_<date_time> eg typically on Windows: <b>C:\\Users\\</b><i>USERNAME</i><b>\\Downloads\\account_lookup_no_match_yymmddHHMM.csv</b>

3. To Create a lookup file using Excel or similar called "account_lookup_for_GnuCash.csv" or whatever you specify in .csv_GnuCash.csv. 

The first row needs to have the following column headings:
Description	
String_start	
String_length	
Transfer_account
See the example file uploaded to this repo "sample_account_lookup_for_GnuCash.csv"


## To Run

Download csv files from bank containing transactions. 

Start Python 3 and then use <b>csv_for_GnuCash</b> <i>transaction_file_name.csv</i>.

Or if you have compiled using pyinter and associated csv files with csv_for_GnuCash this should work:

Double click on the transaction file and then and then csv_for GnuCash.exe should start.  

THE DOWNLOAD FILES MUST INCLUDE A FIRST ROW WITH THE FOLLOWING COLUMN HEADERS:

Date	
Description	
Amount
See example uploaded to this repo userhome "sample_x_action_file.csv"


## Detailed instructions below regarding Associating Python module with csv file:
(Note this will set csv_for_GnuCash.exe as the default program to open .csv files
which may not be what you want!)

- Right click on the csv file.
- Click on "Open with"
- Select "Choose another app"
- Tick the "Always use this app to open .csv files" box
- Scroll down and click on "More apps"
- Scroll down to the bottom of the list and select "Look for another app on this PC"
- This will open a file explorer window, you need to find where the csv_for_GnuCash.exe file is, select it and click "Open" 
This will run the program against the selected file. Next time you can just double click on the transactions csv file. 
