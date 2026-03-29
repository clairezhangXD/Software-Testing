Would you prefer to indent your code using tabs or spaces? Why?
Tabs, its much more convenient

Look up the coding conventions of your favourite programming language. Discuss.
Anything surprising?
have to put semi colon after every line for Java and Javascript, but code will still run for Javascript

Anything you disagree with?
Seems redundant to add a semicolon for Javascript

How do the conventions differ between the languages people at your table chose?
Naming Conventions for python:
Use snake_case for function and variable names.
Use CapWords (PascalCase) for class names.
Constants should be written in ALL_CAPS.

Naming conventions for Java:
Use camelCase for method and variable names.
Use PascalCase (CapWords) for class and interface names.
Constants should be written in ALL_CAPS with words separated by underscores.

You are designing the coding conventions for a company. What rules would you insist on? Feel free to look at the conventions of popular open source projects for inspiration.

Consider the complexity metrics discussed in the workshop (lines of code, cyclomatic complexity, Halstead complexity). What are the pros and cons of each? Would you use any?
1.	Lines of Code (LOC)
	•	Pros: Simple to measure; easy to understand.
	•	Cons: Doesn’t account for code quality, logic, or complexity; large codebases may not be complex and vice versa.
	•	Would I use it?: Useful for a high-level estimate, but insufficient for assessing complexity.
2.	Cyclomatic Complexity
	•	Pros: Measures the number of independent paths through the code, indicating complexity in logic and control flow.
	•	Cons: Can penalize code with lots of conditional logic, even if it’s well-structured.
	•	Would I use it?: Yes, especially for identifying overly complex functions.
3.	Halstead Complexity
	•	Pros: Measures complexity based on the number of operators and operands, giving insight into effort, difficulty, and bugs.
	•	Cons: Difficult to compute manually; may be hard to interpret without practice.
	•	Would I use it?: Occasionally, to get a deeper understanding of code complexity in terms of mental effort required to maintain.


Consider the code quality metrics discussed in the workshop (test coverage, test efficiency, defect density, mutation score). What are the pros and cons of each?
1.	Test Coverage
	* Pros: Measures how much of the code is tested; higher coverage often means fewer untested paths.
	* Cons: Doesn’t guarantee that tests are thorough or meaningful; 100% coverage doesn’t mean all edge cases are handled.
	•	Would I use it?: Yes, as a baseline indicator of how well-tested the code is.
2.	Test Efficiency
	* Pros: Evaluates the effectiveness of tests (e.g., how many bugs they catch); can help prioritize high-value tests.
	* Cons: Difficult to measure directly; might not capture latent bugs.
	* Would I use it?: Useful for optimizing test suites, but harder to measure consistently.
3.	Defect Density
	* Pros: Measures the number of defects per line of code, which can indicate quality over time.
	* Cons: Requires detailed defect tracking; high-density doesn’t always correlate with severity.
	* Would I use it?: Only for long-term projects to measure improvement in code quality.
4.	Mutation Score
	* Pros: Measures test suite robustness by introducing small code changes (“mutants”) and seeing if the tests fail.
	* Cons: Time-consuming to run; requires advanced tools.
	* Would I use it?: Yes, for critical systems where test suite strength is crucial.

In pairs or small groups, find a software quality metric that wasn't covered in the workshop. Write a short description, and a list of pros and cons.
code churn --> indicates how often changes are made to a specific piece of code
pros
* Indicates Change: Shows how actively the code is being updated or improved.
* Identifies Issues: Helps detect areas with frequent changes, which may need attention.
* Enhances Understanding: Provides insight into code evolution over time.

cons
* Potential Red Flag: High churn may signal instability or poor design choices.
* Not Always Meaningful: High churn doesn’t necessarily mean better quality; it can be misleading.
* Focus on Quantity: Might lead to an emphasis on the amount of change rather than the quality of changes.

If you were reviewing someone else's code, what quality metric(s) would you use? How would it be measured, and how would you use the result?
I would use Cyclomatic Complexity to measure the complexity of the code, aiming to keep it low for better maintainability and readability. I would also prioritise Test Coverage to ensure that critical parts of the code are well-tested, aiming for at least 80% coverage for reliability.


Identify as many code smells as you can in the following code, and explain what makes it a code smell:

def discount(cart, sr):
    if sr == True:
        if cart > 100:
            dis = 0.1
            if cart > 200:
                dis = 0.2
            return cart * (1 - dis)
        else:
            return cart * 0.95
    else:
        if cart > 100:
            if cart > 200:
                return cart * 0.8
            else:
                return cart * 0.9
        else:
            return cart * 0.98

def main():
    c = 250
    s = True
    d = discount(c, s)
    print("Discounted price: ", d)
    c = 50
    s = False
    d = discount(c, s)
    print("Discounted price: ", d)
    c = 150
    s = False
    d = discount(c, s)
    print("Discounted price: ", d)
    c = 300
    s = True
    d = discount(c, s)
    print("Discounted price: ", d)

main()

- magic numbers (what does 100,200 or 0.95 mean?)
- repetitive code, where c and s are being redefined each time, instead could have these passed into the discount function