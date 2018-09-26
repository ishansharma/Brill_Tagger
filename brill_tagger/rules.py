# Class to hold multiple rules
class Rules:
    def __init__(self):
        self.rules = []

    def __str__(self):
        """
        String representation is just a long string containing string representation of each string with new lines
        inserted after each rule

        Returns
        -------
        str
        """
        output_str = ""
        for rule in self.rules:
            output_str += str(rule) + "\n"

        return output_str

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.rules)

    def enqueue(self, rule):
        self.rules.append(rule)


# Class to hold a single rule
class Rule:
    def __init__(self, old_tag="", new_tag="", condition=""):
        """
        Constructor for new rules

        Parameters
        ----------
        old_tag str
        new_tag str
        condition str
        """
        self.old_tag = old_tag
        self.new_tag = new_tag
        self.condition = condition

    def __str__(self):
        """
        Output from, to and condition fields

        Returns
        -------
        str
        """
        return self.old_tag + " " + self.new_tag + " " + self.condition

    def __rpr__(self):
        return self.__str__()

    def __eq__(self, other):
        """
        Comparison needs to handle only the 3 fields
        Parameters
        ----------
        other Rule

        Returns
        -------

        """
        return self.old_tag == other.old_tag and self.new_tag == other.new_tag and self.condition == other.condition
