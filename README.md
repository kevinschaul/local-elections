# Local elections

A python module to simplify election results for local races.


## Current usage

An example script `example_usage.py` can be run from the root of the project and is an example of a script to run repeatedly on election night.

    python local_elections/example_usage.py

## Idea usage (when complete)

    import local_elections

    >>> wa = local_elections.WA()
    >>> wa.races
    ['U.S. Senator', 'Congressional District 1 - U.S. Representative']
    >>> sen = wa.races[0]
    >>> sen.candidates
    ['Michael Baumgartner', 'Will Baker', 'Chuck Jackson']
    >>> for candidate in sen.candidates:
    >>>     print "%s -- %d" % (candidate, candidate.votes)
    >>> 
    Michael Baumgartner -- 109225
    Will Baker -- 387252
    Chuck Jackson -- 109225
    >>> sen.winner
    ['Will Baker']
    >>> sen.winner.party
    GOP
    >>> sen.winner.votes
    387252
    >>> sen.winner.percent_won
    78.00
    >>> sen.statewide
    True
    >>> sen.district.statewide
    True
    >>> c1_rep = wa.races[1]
    >>> dist = c1_rep.district
    >>> dist.number
    1
    >>> dist.jurisdiction
    Congressional
    >>> dist.statewide
    False

