
questions = [
    "1. When it comes to running, I am:",
    "2. My preferred skill is:",
    "3. I enjoy playing:",
    "4. When I don't have the ball, I am good at:",
    "5. My favorite part of the game is:",
    "6. In a tight game, I prefer to:",
    "7. When my team is behind, I:",
    "8. My role model in football is:",
]

options = [
    ["A. Exceptionally fast", "B. Average in speed", "C. Not very fast"],
    ["A. Dribbling past opponents", "B. Accurate passing", "C. Shooting on goal"],
    ["A. In the front, close to the opponent's goal", "B. In the midfield, controlling the game",
     "C. In the defense, stopping the opponent's attacks"],
    ["A. Pressuring the opponent and stealing the ball", "B. Finding open spaces and creating passing lanes",
     "C. Marking the opponent and protecting my goal"],
    ["A. Scoring goals and celebrating", "B. Orchestrating plays and assists", "C. Making crucial tackles and blocks"],
    ["A. Take the last-minute shot", "B. Maintain possession and control", "C. Secure the defence and prevent goals"],
    ["A. Push forward and take more risks", "B. Work on creating opportunities", "C. Ensure we don't concede more goals"],
    ["A. Timo Werner", "B. Zinedine Zidane", "C. Paolo Maldini"],
]

# Track user's preferences
positions = {
    "Striker": 0,
    "Midfielder": 0,
    "Defender": 0,
}


# Function to ask questions and update position dict
def ask_question(question, options):
    print(question)
    for option in options:
        print(option)

    while True:
        response = input("Choose your answer (A/B/C): ").strip().upper()

        # Check if the response is a valid choice (A, B, or C)
        if response in ['A', 'B', 'C']:
            break
        else:
            print("Please type 'A' for the first option, 'B' for the second option, or 'C' for the third option.")

    # Map responses directly to positions
    if response == 'A':
        positions["Striker"] += 1
    elif response == 'B':
        positions["Midfielder"] += 1
    elif response == 'C':
        positions["Defender"] += 1


print("Welcome to the Football Position Quiz!")
print("For each question, choose the answer that best describes you.")
print("Please type 'A' for the first option, 'B' for the second option, and 'C' for the third option.")

# Iterate through questions and options
for i in range(len(questions)):
    ask_question(questions[i], options[i])

# Determine the user's recommended position
recommended_position = max(positions, key=positions.get)

print(f"Based on your answers, your recommended football position is: {recommended_position}")

if recommended_position == "Striker":
    print("You have a knack for scoring goals and being in attacking positions.")
elif recommended_position == "Midfielder":
    print("You excel in controlling the game and distributing passes.")
elif recommended_position == "Defender":
    print("You are strong in defensive skills and protecting your team's goal.")

print("Thanks for taking the Football Position Quiz!")
