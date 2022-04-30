class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for val in self.order_domain_values(var, assignment):
            if self.is_consistent(var, val, assignment):
                assignment[var] = val

                result = self.recursive_backtracking(assignment)
                if result:
                    return result

                del assignment[var]

        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    cri, pan, col, ven, guy, sur, guf, ecu, per, bra, bol, pry, chl, arg, ury = 'cri', 'pan', 'col', 'ven', 'guy', 'sur', 'guf', 'ecu', 'per', 'bra', 'bol', 'pry', 'chl', 'arg', 'ury'
    values = ['Yellow', 'Blue', 'Red', 'Green']
    variables = [cri, pan, col, ven, guy, sur, guf, ecu, per, bra, bol, pry, chl, arg, ury]
    domains = {
        cri: values[:],
        pan: values[:],
        col: values[:],
        ven: values[:],
        guy: values[:],
        sur: values[:],
        guf: values[:],
        ecu: values[:],
        per: values[:],
        bra: values[:],
        bol: values[:],
        pry: values[:],
        chl: values[:],
        arg: values[:],
        ury: values[:]
    }
    neighbours = {
        cri: [pan],
        pan: [cri, col],
        col: [pan, ven, ecu, bra],
        ven: [col, ecu, bra],
        guy: [ven, sur, bra],
        sur: [guy, guf, bra],
        guf: [sur, guf, bra],
        ecu: [col, per],
        per: [ecu, col, bra, chl, bol],
        bra: [col, ven, guy, sur, guf, per, bol, pry, ury],
        bol: [per, bra, chl, arg, pry],
        pry: [bol, bra, arg],
        chl: [per, bol, arg],
        arg: [chl, bol, pry, bra, ury],
        ury: [arg, bra]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cri: constraint_function,
        pan: constraint_function,
        col: constraint_function,
        ven: constraint_function,
        guy: constraint_function,
        sur: constraint_function,
        guf: constraint_function,
        ecu: constraint_function,
        per: constraint_function,
        bra: constraint_function,
        bol: constraint_function,
        pry: constraint_function,
        chl: constraint_function,
        arg: constraint_function,
        ury: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
