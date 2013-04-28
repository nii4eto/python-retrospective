class Person:
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.child = []
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father

        for parent in [self.mother, self.father]:
            if parent:
                parent.child.append(self)

    def children(self, **kwargs):
        if kwargs:
            return [child for child in self.child
                    if child.gender == kwargs['gender']]
        else:
            return self.child

    def get_brothers(self):
        mother_sons = set()
        father_sons = set()

        if self.mother:
            mother_sons = {kid for kid in self.mother.child
                           if self.mother.gender != kid.gender
                           and kid is not self}
        if self.father:
            father_sons = {kid for kid in self.father.child
                           if self.father.gender == kid.gender
                           and kid is not self}

        brothers = list(mother_sons.union(father_sons))
        return brothers

    def get_sisters(self):
        mother_daughters = set()
        father_daughters = set()

        if self.mother:
            mother_daughters = {kid for kid in self.mother.child
                                if self.mother.gender == kid.gender
                                and kid is not self}
        if self.father:
            father_daughters = {kid for kid in self.father.child
                                if self.father.gender != kid.gender
                                and kid is not self}

        sisters = list(mother_daughters.union(father_daughters))
        return sisters

    def is_direct_successor(self, kid):
        if kid in self.child:
            return True
        else:
            return False
