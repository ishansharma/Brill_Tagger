class BrillTagger:
    def __init__(self, corpus):
        self.corpus = corpus
        self.frequencies = self.calculate_word_pos_frequency()
        self.probabilities = self.calculate_word_pos_probabilities()

    def calculate_word_pos_frequency(self):
        """
        Calculate the number of times each word is seen tagged with a specific POS
        Also stores a total count which is useful
        Returns
        -------
        dict
        """
        frequencies = {}

        for token in self.corpus:
            if token.word in frequencies:
                if token.pos in frequencies[token.word]:
                    frequencies[token.word][token.pos] += 1
                else:
                    frequencies[token.word][token.pos] = 1
                frequencies[token.word]['total'] += 1
            else:
                frequencies[token.word] = {
                    token.pos: 1,
                    'total': 1
                }
        return frequencies

    def calculate_word_pos_probabilities(self):
        """
        Calculate probability of each word being a particular pos
        Returns
        -------
        dict
            Dictionary containing probabilities for words and POS
        """
        probabilities = {}
        for word in self.frequencies:
            if word not in probabilities:
                probabilities[word] = {}

            for pos in self.frequencies[word]:
                if pos != 'total':
                    probabilities[word][pos] = self.frequencies[word][pos] / self.frequencies[word]['total']

        return probabilities

    def apply_transform(self, rule):
        """
        Apply a transformation to entire corpus

        Parameters
        ----------
        rule : Rule
        """
        for index, token in enumerate(self.corpus[1:]):  # first token has no predecessor
            # print(self.corpus[index - 1].pos)
            if token.pos == rule.old_tag and self.corpus[index].pos == rule.condition:
                token.pos = rule.new_tag
