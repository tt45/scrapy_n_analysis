
class Actor:
    """
    actor object. act_movie is a list of movie objects that will form a graph with movie objects
    """
    name = ""
    age = 0
    act_movie = []
    total_grossing = 0

    def __init__(self, name, age, act_movie, total_grossing):
        """
        initialize actor object
        :param name:
        :param age:
        :param act_movie:
        :param total_grossing:
        """
        self.name = name
        self.age = age
        self.act_movie = act_movie
        self.total_grossing = total_grossing

    def get_name(self):
        """
        return name of actor
        :return:
        """
        return self.name

    def get_age(self):
        """
        return age of actor
        :return:
        """
        return self.age

    def get_act_movie(self):
        """
        return movie of actor
        :return:
        """
        return self.act_movie

    def get_total_grossing(self):
        """
        return total grossing of actor
        :return:
        """
        return self.total_grossing
