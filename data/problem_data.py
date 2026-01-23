# data/tea_data.py

from models.problem import ProblemModel
from models.solution import SolutionModel

# Add a user_id to link each tea to a specific user
problems_list = [
    ProblemModel(
        title="Quadratic Equation", 
        equation_LaTeX="x^2 + 5x + 6 = 0", 
        ai_Solution="To solve x^2 + 5x + 6 = 0, we factor it into (x+2)(x+3) = 0. Therefore, x = -2 or x = -3.", 
        user_id=1
    ),
    ProblemModel(
        title="Basic Integration", 
        equation_LaTeX="\int x^2 dx", 
        ai_Solution="The integral of x^2 is (x^3 / 3) + C.", 
        user_id=2
    ),
    ProblemModel(
        title="Pythagorean Theorem", 
        equation_LaTeX="a^2 + b^2 = c^2", 
        ai_Solution="In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.", 
        user_id=4
    ),
    ProblemModel(
        title="Derivative of Sin", 
        equation_LaTeX="\frac{d}{dx} \sin(x)", 
        ai_Solution="The derivative of sin(x) with respect to x is cos(x).", 
        user_id=1
    ),
    ProblemModel(
        title="Linear Equation", 
        equation_LaTeX="2x + 10 = 20", 
        ai_Solution="Subtract 10 from both sides: 2x = 10. Divide by 2: x = 5.", 
        user_id=5
    )
]

solutions_list = [
    SolutionModel(content="You can also solve the quadratic equation using the general formula.", problem_id=1, user_id=2),
    SolutionModel(content="Don't forget to add the constant 'C' in integration!", problem_id=2, user_id=1),
    SolutionModel(content="This theorem only works for right-angled triangles.", problem_id=3, user_id=3),
    SolutionModel(content="Easy! The slope of the tangent line is cos(x).", problem_id=4, user_id=5),
    SolutionModel(content="Try to visualize it on a graph to understand it better.", problem_id=5, user_id=4)
]