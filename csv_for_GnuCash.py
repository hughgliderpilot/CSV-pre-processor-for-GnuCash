# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:53:08 2019

@author: hughg
"""

import pandas as pd
import sys
import datetime
from pathlib import Path

# Sort out files and folders
userhome = Path.home()

transaction_file = sys.argv[1]  # needed for live
transaction_file = Path(transaction_file)

# below lines to make testing easier
# transaction_file = userhome / "Downloads" / "16062019_2432.csv"
# end of testing lines

# config file processing, exists? valid format? has right data?
config_file_exists = True
file_config_name = userhome / ".csv_GnuCash.csv"
try:
    df_file_config = pd.read_csv(file_config_name, index_col="File")
    lookup_file_str = df_file_config.loc["Lookup_file", "File_path"]
except FileNotFoundError:
    print("Config file {} not found, using defaults".format(file_config_name))
    lookup_file_str = userhome / "Documents" / "account_lookup_for_GnuCash.csv"
    config_file_exists = False
except TypeError:
    print("File {} is not a valid config file, "
          "using defaults".format(file_config_name))
    lookup_file_str = userhome / "Documents" / "account_lookup_for_GnuCash.csv"
    config_file_exists = False
except KeyError:
    lookup_file_str = userhome / "Documents" / "account_lookup_for_GnuCash.csv"
if config_file_exists:
    try:
        output_folder_str = df_file_config.loc["Output_folder", "File_path"]
    except KeyError:
        output_folder_str = userhome / "Downloads"
else:
    output_folder_str = userhome / "Downloads"
# end of config file processing

# lookup file processing
try:
    lookup_file = Path(lookup_file_str)
    df_lookup = pd.read_csv(lookup_file)
except FileNotFoundError:
    print("Lookup file not found, ending run")
    input("Press Enter to continue...")
    raise
except TypeError:
    print("File {} is not a valid lookup file, "
          "ending run".format(lookup_file))
    input("Press Enter to continue...")
    raise
# Check the Lookup file has the correct column names
lookup_cols = list(df_lookup)
for x in ['String_length', 'String_length', 'Transfer_account', 'Description']:
    if x not in lookup_cols:
        print('Problem with Column Headings in lookup file, '
              '\"{}\" not found'.format(x))
        input("Press Enter to continue...")
        sys.exit(1)
# end of lookup file processing

# transaction file processing
try:
    df_transactions = pd.read_csv(transaction_file)
except FileNotFoundError:
    print("Transaction file {} not found, ending run".format(transaction_file))
    input("Press Enter to continue...")
    raise
except TypeError:
    print("File {} is not a valid transaction file, "
          "ending run".format(transaction_file))
    input("Press Enter to continue...")
# Check the transaction file has the correct column names
transaction_cols = list(df_transactions)
for x in ['Date', 'Amount', 'Description']:
    if x not in transaction_cols:
        print('Problem with Column Headings in transaction file, '
              '\"{}\" not found'.format(x))
        input("Press Enter to continue...")
        sys.exit(1)
# end of transaction file processing

# transaction matching
df_lookup['String_end'] = df_lookup[
        'String_start'] + df_lookup['String_length']
df_output = pd.DataFrame()
for row in df_lookup.itertuples():
    df_transactions['Sub_string'] = df_transactions[
            'Description'].str[row.String_start:row.String_end]
    df_match = df_transactions[
            df_transactions['Sub_string'] == row.Description].copy()
    df_match['Transfer_account'] = row.Transfer_account
    df_match.drop('Sub_string', axis=1, inplace=True)
    df_output = pd.concat([df_output, df_match])
    df_transactions = df_transactions[
            df_transactions['Sub_string'] != row.Description]
df_transactions.drop('Sub_string', axis=1, inplace=True)
df_transactions['Transfer_account'] = ''
df_output = pd.concat([df_output, df_transactions])
print('Transactions with no match, shown below '
      'and stored in account_lookup_no_match.csv...')
pd.set_option('display.max_columns', 500)
print(df_transactions[["Date", "Description", "Amount"]])
# end of transaction matching

# output file processing
date_time_now = datetime.datetime.now()
fmt_date_time_now = date_time_now.strftime("%y%m%d%H%M%S")
No_match_file_name = "account_lookup_no_match_" + fmt_date_time_now + ".csv"
No_match_file = userhome / output_folder_str / No_match_file_name
output_file_name = "xac_ac_for_GnuCash_" + fmt_date_time_now + ".csv"
output_file = userhome / output_folder_str / output_file_name
df_transactions.to_csv(No_match_file, index=False)
df_output.to_csv(output_file, index=False)
# end of output file processing
input("Press Enter to continue...")

