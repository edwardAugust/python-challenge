#  this is for the bank challenge
import os
import pandas as pd
import csv

#reference the csv file
bankFile = "Resources/budget_data.csv"
bankFileDf = pd.read_csv(bankFile)
print(bankFileDf.head())