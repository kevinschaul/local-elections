import json

from utils import slugify

class Party(object):
    
    def __init__(self, name, abbreviation):
        self.name = name
        self.slug = slugify(name)
        self.abbreviation = abbreviation


#TODO test
class Candidate(object):

    def __init__(self, first_name, last_name, votes):
        self.first_name = first_name
        self.last_name = last_name
        self.slug = slugify(first_name + last_name)
        self.votes = votes

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        # TODO
        return self.__unicode__()


#TODO test
class Race(object):
    
    def __init__(self, title, jurisdiction, total_votes):
        self.title = title
        self.slug = slugify(title)
        self.jurisdiction = jurisdiction
        self.candidates = []
        self.total_votes = total_votes

    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    
    def __unicode__(self):
        return "%s" % self.title

    def __repr__(self):
        # TODO
        return self.__unicode__()


class DataSource(object):
    """
    Object to define what each data source will return.

    @args:
    source    A string representing the source type.
    """
    
    def __init__(self):
        self.source = ''
        self.races = {}

    def get_results(self):
        # This should be defined by the subclass
        raise NotImplementedError

    #TODO test
    def get_or_create_race(self, race):
        try:
            self.races[race.slug]
            created = False
        except KeyError:
            self.races[race.slug] = race
            created = True
        return self.races[race.slug], created 


class Results(object):
    """
    Object to hold all results from multiple DataSources
    """

    def __init__(self):
        self.races = {}

    #TODO test
    def add(self, races):
        """
        Adds races to the master results list
        """

        for race in races:
            try:
                self.races[races[race].slug]
            except KeyError:
                self.races[races[race].slug] = race

    def iter_races(self, *args, **kwargs):
        """
        Iterates through the races, based on passed in criteria
        """

        #raise NotImplementedError
        return self.races.iteritems()

