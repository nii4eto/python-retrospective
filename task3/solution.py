class Person:
    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.child = []
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        if mother:
            self.mother = mother
            self.mother.child.append(self)
        else:
            self.mother = None

        if father:
            self.father = father
            self.father.child.append(self)
        else:
            self.father = None

    def children(self, **kwargs):
        if kwargs:
            return [child for child in self.child
                    if child.gender == kwargs['gender']]
        else:
            return self.child

    def get_brothers(self):
        brothers = set()
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

        brothers = mother_sons.union(father_sons)
        return list(brothers)

    def get_sisters(self):
        sisters = set()
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

        sisters = mother_daughters.union(father_daughters)
        return list(sisters)

    def is_direct_successor(self, child):
        if self == child.mother:
            return True
        elif self == child.father:
            return True
        else:
            return False
