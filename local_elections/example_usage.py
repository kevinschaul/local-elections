import json

from local_elections.models import Results
from WA.data_sources import SOS as WA_SOS

wa_sos = WA_SOS()
wa_sos.get_results()

r = Results()

r.add(wa_sos.races)

races = []
for i in wa_sos.races.iteritems():
    race = i[1]
    candidates = []
    for c in race.candidates:
        candidates.append(
            {
                'first_name': c.first_name,
                'last_name': c.last_name,
                'votes': c.votes,
            }
        )
    races.append(
        {
            'name': race.title,
            'total_votes': race.total_votes,
            'candidates': candidates,
        }
    )

dump = {
    'races': races
}

print json.dumps(dump, indent=4)

