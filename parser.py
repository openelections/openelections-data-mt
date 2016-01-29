import unicodecsv

headers = ['county', 'office', 'district', 'party', 'candidate', 'votes']

with open('state_legislative.csv', 'wb') as csvfile:
    w = unicodecsv.writer(csvfile, encoding='utf-8')
    w.writerow(headers)

    lines = open('/Users/derekwillis/Downloads/2014-Primary-Official-Legislative-Canvass.txt').readlines()
    for line in lines:
        if line.strip() == '':
            continue
        if 'MONTANA SECRETARY OF STATE LINDA McCULLOCH' in line:
            continue
        if 'Affiliation' in line:
            continue
        print line
        if any(x in line for x in ['Democrat', 'Republican', 'Libertarian']):
            parties = [x.strip() for x in line.strip().split('  ') if x != '']
            continue
        if all(word.isupper() for word in [x.strip() for x in line.split('  ') if x != '']):
            candidates = [x.strip() for x in line.split('  ') if x != '']
            continue
        if line[0:2] == 'HD':
            bits = [x.strip() for x in line.split('  ') if x != '']
            office = 'State House'
            district = bits[0].split(' ')[1]
            county = bits[1]
            results = [x.replace(',','') for x in bits[2:]]
            candidates_with_party = zip(candidates, parties)
            county_results = zip(candidates_with_party, results)
            for (candidate, party), result in county_results:
                w.writerow([county, office, district, party, candidate, result])
        elif line[0:2] == 'SD':
            bits = [x.strip() for x in line.split('  ') if x != '']
            office = 'State Senate'
            district = bits[0].split(' ')[1]
            county = bits[1]
            results = [x.replace(',','') for x in bits[2:]]
            candidates_with_party = zip(candidates, parties)
            county_results = zip(candidates_with_party, results)
            for (candidate, party), result in county_results:
                w.writerow([county, office, district, party, candidate, result])
        else:
            bits = [x.strip() for x in line.split('  ') if x != '']
            county = bits[0]
            results = [x.replace(',','') for x in bits[1:]]
            candidates_with_party = zip(candidates, parties)
            county_results = zip(candidates_with_party, results)
            for (candidate, party), result in county_results:
                w.writerow([county, office, district, party, candidate, result])
