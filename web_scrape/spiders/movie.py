
class Movie:
    """
    Movie object. attend_actor will direct to a list of actor objects for it forms a graph
    """
    name = ""
    year = ""
    grossing = 0
    attend_actor = []

    def __init__(self, name, year, grossing, attend_actor):
        """
        initialize movie object
        :param name:
        :param year:
        :param grossing:
        :param attend_actor:
        """
        self.name = name
        self.grossing = grossing
        self.attend_actor = attend_actor
        self.year = year

    def get_name(self):
        """
        return name of movie
        :return:
        """
        return self.name

    def get_grossing(self):
        """
        return grossing of movie
        :return:
        """
        return self.grossing

    def get_attend_actor(self):
        """
        return attend actor object list of movie
        :return:
        """
        return self.attend_actor

    def get_year(self):
        """
        return year of movie made
        :return:
        """
        return self.year
