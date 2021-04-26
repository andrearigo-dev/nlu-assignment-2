class Sentence:
    ents: list
    
    def __init__(self, conll_sent: list, from_slice=False):
        if not from_slice:
            self.tokens = [NamedEntity(ner) for ner in conll_sent]
        else:
            self.tokens = conll_sent
    
    
    def __repr__(self):
        return ' '.join([ent.text for ent in self.tokens])
    
    
    def __getitem__(self, slice_):
        sliced = self.tokens[slice_]
        
        if not isinstance(sliced, list):
            sliced = [sliced]
        
        return Sentence(sliced, from_slice=True)
    
    
    def __len__(self):
        return len(self.tokens)


class NamedEntity:
    text: str
    pos: str
    chunk_tag: str
    ent_tag: str
    
    def __init__(self, conll_row):
        elems = conll_row[0].split()
        self.text = elems[0]
        self.pos = elems[1]
        self.chunk_tag = elems[2]
        self.ent_tag = elems[3]
    
    
    def __repr__(self):
        return self.text
    
    
    def to_list(self):
        return [self.text, self.pos, self.chunk_tag, self.ent_tag]