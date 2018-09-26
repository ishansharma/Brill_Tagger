class BrillTagger:
    def __init__(self, corpus):
        self.corpus = corpus

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
