import xlrd
import unicodecsv

headers = ['county', 'office', 'district', 'party', 'candidate', 'votes']
book = xlrd.open_workbook("/Users/dwillis/Downloads/mt_legis.xlsx")
total_sheets = book.nsheets
with open('state_legislative.csv', 'wb') as csvfile:
    w = unicodecsv.writer(csvfile, encoding='utf-8')
    w.writerow(headers)

    for sheet in range(1, total_sheets):
        sh = book.sheet_by_index(sheet)
        header = sh.row(6)
        district = header[0].value.split('DISTRICT ')[1]
        candidates = [x.value for x in header[2:]]
        for r in range(7, sh.nrows):
            row = sh.row(r)
            county = row[1].value
            cand_votes = zip(candidates, [x.value for x in row[2:]])
            for cand in cand_votes:
                name, party = cand[0].split(" - ")
                w.writerow([county, 'State House', district, party, name, int(cand[1])])
