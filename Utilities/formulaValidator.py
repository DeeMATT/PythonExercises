import re
from metrics.models import Metric

class FormulaValidator():
    """To parse and validate user formula upon creating a KPI"""

    def __init__(self):
        self.operator_set = ('+', '-', '*', '/', '^', '(', ')', '%')

    def _format(self, formula):
        """To format the given formula to an arithmetic standard"""

        if " " in formula:
            # replace all whitespaces in the expression
            expression = formula.replace(" ", '')
            formula = expression
        if formula.startswith('('):
            expression = formula.replace("(", '')
            formula = expression
        if formula.endswith(')'):
            expression = formula.replace(")", '')
            formula = expression
        return formula

    def parse(self, formula):
        """To parse and extract variables in an formula"""

        for operator in self.operator_set:
            if operator in formula:
                # replace all operator in the formula
                formula = formula.replace(operator, ',')

        variables = [var for var in formula.split(',')]
        return variables

    def validate(self, formula):
        """To validate the specified formula"""

        expression = self._format(formula)
        for op in self.operator_set:
            # check if there are 2 consecutive operators used after each other
            validator = re.search('\\'+op+'{2,}', expression)
            if type(validator) != re.Match:
                pass
            else:
                raise ArithmeticError("Formula contains consecutive operators")

            # check if the formula ends with an operator
            validator = re.search('\\'+op+'$', expression)
            if type(validator) != re.Match:
                pass
            else:
                raise ArithmeticError("Formula ends with an operator")

        # check if variables are valid metric codes
        variables = self.parse(formula)

        for variable in variables:
            metric = Metric.objects.filter(name__icontains=variable).values()
            if variable == metric.name:
                pass
            else:
                return "The variable you specified isn't a valid metric"
        return "valid"


# ================================ To evaluate KPI formula ====================================
def evaluator(formula, variables_dict):
    """To calculate the formula by substituting the variables with their respective values."""
    extracted_variables = FormulaValidator().parse(formula)
    for variable, value in variables_dict:
        if variable in extracted_variables:
            # substitute variables into the formula
            sub_formula = formula.replace(variable, value, 1)

    # evaluate the formula to generate an answer
    evaluated_answer = eval(sub_formula)
    return evaluated_answer