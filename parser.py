import unicodecsv

headers = ['county', 'office', 'district', 'party', 'candidate', 'votes']

with open('state_legislative.csv', 'wb') as csvfile:
    w = unicodecsv.writer(csvfile, encoding='utf-8')
    w.writerow(headers)

    lines = open('/Users/DW-Admin/Downloads/2006_Legislative_Primary.txt').readlines()
    for line in lines:
        if line.strip() == '':
            continue
        if 'Election Results' in line:
            continue
        if 'Affiliation' in line:
            continue
        if 'Incumbent' in line:
            continue
        print line
#        if any(x in line for x in ['Democrat', 'Republican', 'Libertarian']):
#            parties = [x.strip() for x in line.strip().split('  ') if x != '']
#            continue
#        if all(word.isupper() for word in [x.strip() for x in line.split('  ') if x != '']):
#            candidates = [x.strip() for x in line.split('  ') if x != '']
#            continue
        if line[0:2] == 'HD':
            bits = [x.strip() for x in line.split('  ') if x != '']
            office = 'State House'
            district = bits[0].split(' ')[1]
            candidates = [c.split('(') for c in bits[1:]]
        elif line[0:2] == 'SD':
            bits = [x.strip() for x in line.split('  ') if x != '']
            office = 'State Senate'
            district = bits[0].split(' ')[1]
            candidates = [c.split('(') for c in bits[1:]]
        else:
            bits = [x.strip() for x in line.split('  ') if x != '']
            county = bits[0]
            results = [x.replace(',','') for x in bits[1:]]
            county_results = zip(candidates, results)
            for (candidate, party), result in county_results:
                w.writerow([county, office, district, party.split(')')[0], candidate, result])
