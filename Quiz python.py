print('welcome to play quiz game')

player = input('do you want to play?(y/n)')

if player.lower() != "y":
    quit()

print('ok lets play')

correctscore=0
incorrectscore=0

#question no:01

print("1.How many days do we have in a week?")
print("a) Five")
print("b) Six")
print("c) Seven")
print("d) Eight")
answer=input("Your answer: ").lower()
if answer.lower() == "seven" or answer.lower() == "c":
    print('correct')
    correctscore+=1
else:
    print('incorrect')
    incorrectscore+=1
print("your correctscore"+ str(correctscore))
print("your incorrectscore"+ str(incorrectscore))

#question no:02

print("2.King of cricket?")
print("(a) Sachin Tendulkar")
print("(b) MS Dhoni")
print("(c) Virat Kohli")
print("(d) Rohit Sharma")
answer=input("Your answer: ").lower()
if answer.lower() == "viratkohli" or answer.lower() == "virat kohli" or answer.lower() == "c":
    print('correct')
    correctscore+=1
else:
    print('incorrect')
    incorrectscore+=1

print("your correctscore"+ str(correctscore))
print("your incorrectscore"+ str(incorrectscore))

#question no:03

print("3.which is strongest country?")
print("(a) China")
print("(b) Russia")
print("(c) America")
print("(d) India")
answer=input("Your answer: ").lower()
if answer.lower() == "america" or answer.lower() == "c":
    print('correct')
    correctscore+=1
else:
    print('incorrect')
    incorrectscore+=1

print("your correctscore"+ str(correctscore))
print("your incorrectscore"+ str(incorrectscore))

#question no:04

print("4.What is the capital city of France?")
print("(a) London")
print("(b) Paris")
print("(c) India")
print("(d) Madrid")
answer=input("Your answer: ").lower()
if answer.lower() == "paris" or answer.lower() == "b":
    print('correct')
    correctscore+=1
else:
    print('incorrect')
    incorrectscore+=1

print("your correctscore"+ str(correctscore))
print("your incorrectscore"+ str(incorrectscore))

#question no:05

print("5.What is the largest planet in our solar system?")
print("(a) Earth")
print("(b) Mars")
print("(c) venus")
print("(d) Jupiter")
answer=input("Your answer: ").lower()
if answer.lower() == "jupiter" or answer.lower() == "d":
    print('correct')
    correctscore+=1
else:
    print('incorrect')
    incorrectscore+=1

print("Your Total Correct answer is: "+ str(correctscore))
print("Your Total Incorrect answer is: "+ str(incorrectscore))

total_questions = 5 #no of question
percentage_correct = (correctscore / total_questions) * 100

print(f"Percentage Correct: {percentage_correct:.2f}%")

pass_threshold=50

if percentage_correct>=pass_threshold:
    print("Result: pass")
else:
    print("Result: fail")
