import csv

pad = '/Users/Quintijn/Desktop/School/Jaar 3/DSC3a/Dataset/'

with open(pad+'Renesse - Pension de Herberg/2012 tot 2013-ANO.csv', 'r') as original: data = original.read()
with open(pad+'Renesse - Pension de Herberg/2012 tot 2013-ANO.csv', 'w+') as modified: modified.write("sep=;\n" + data)

