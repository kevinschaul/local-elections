import csv
import re

import requests

from models import Candidate, DataSource, Party, Race

class SOS(DataSource):
    
    def __init__(self):
        self.source = 'SOS'
        self.href = 'http://vote.wa.gov/results/current/export/MediaResults.txt'
        self.races = {}

    #TODO test
    def get_results(self):
        #r = requests.get(self.href)
        #data = r.text
        #reader = csv.DictReader(data.splitlines(), delimiter='\t')

        data = open('local_elections/WA/test_data/MediaResults.txt', 'r')
        reader = csv.DictReader(data, delimiter='\t')

        reader.next() # Skip header now
        for row in reader:
            raw_candidate_name = row['BallotName']
            candidate_name_split = raw_candidate_name.split()
            candidate_first_name = candidate_name_split[0]
            candidate_last_name = ' '.join(candidate_name_split[1:])

            raw_candidate_party = row['PartyName']
            party_regex = re.compile("Prefers (\w+) Party")
            party_result = party_regex.findall(raw_candidate_party)
            party_name = ''
            party_abbreviation = ''
            if party_result:
                party_name = party_result[0]
                party_abbreviation = party_name[0].upper()

            p = Party(party_name, party_abbreviation)

            c = Candidate(
                candidate_first_name,
                candidate_last_name,
                row['Votes']
            )

            r = Race(
                row['RaceName'],
                row['RaceJurisdictionTypeName'],
                row['TotalBallotsCastByRace']
            )

            race, created = self.get_or_create_race(r)
            race.add_candidate(c)

