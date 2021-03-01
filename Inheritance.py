"""
Problem
Objective 
Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.
Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png
Input Format
The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.
The first line contains , , and , separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes .
Constraints

Output Format
Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if average < 40:
            grade = "T"
        elif average >= 40 and average < 55:
            grade = "D"
        elif average >= 55 and average < 70:
            grade = "P"
        elif average >= 70 and average < 80:
            grade = "A"  
        elif average >= 80 and average < 90:
            grade = "E"
        else:
            grade = "O" 
        return grade
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
