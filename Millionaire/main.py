#Ask a series of questions and based on that user will win or loose

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i=0
# Iterate over questions and their options

for ques in questions:
    print(ques[0])
    print(f"a. {ques[1]}")
    print(f"a. {ques[2]}")
    print(f"a. {ques[3]}")
    print(f"a. {ques[4]}")


# Check whether answer is correct or not  
    # Taking user input
    userAnswer = int(input("Enter your answer: 1 for a, 2 for b, 3 for c, 4 for d\n"))

    if(ques[5]==userAnswer):
        print("Correct Answers")
    else:
        print(f"Oops! Incorrect, the correct answer is: {ques[5]}")
        break 
    print(f"You won :{prizes[i]}")
    i+=1   
