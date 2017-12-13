import csv

pad = '/Users/Quintijn/Desktop/School/Jaar 3/DSC3a/Opschonen/Oostkapelle - Villa Magnolia/'

with open(pad+'Landenstatistieken_-_maandelijks_2017-3.csv') as csvfile:
    filereader = csv.reader(csvfile)

    for idx,row in enumerate(filereader):
        if idx == 30:
            filtered = filter(lambda x: x !='', row)
            print('\n'.join(list(filtered)))
