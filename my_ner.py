class Sentence:
    ents: list
    
    def __init__(self, conll_sent: list):
        self.ents = [NamedEntity(ner) for ner in conll_sent]
    
    
    def __str__(self):
        return ' '.join([ent.text for ent in self.ents])
    
    
    def __repr__(self):
        return str([ent.__repr__() for ent in self.ents])


class NamedEntity:
    text: str
    pos: str
    chunk_iob: str
    ent_iob: str
    
    def __init__(self, conll_row):
        elems = conll_row[0].split()
        self.text = elems[0]
        self.pos = elems[1]
        self.chunk_iob = elems[2]
        self.ent_iob = elems[3]
    
    
    def __str__(self):
        return self.text
    
    
    def __repr__(self):
        return str([self.text, self.pos, self.chunk_iob, self.ent_iob])