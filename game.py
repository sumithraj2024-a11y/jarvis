score = 0

print("🎉 Welcome to the Python Quiz Game!")
print("----------------------------------")

# Question 1
answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer: New Delhi\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer: Mars\n")

# Question 3
answer = input("3. How many days are there in a leap year? ")
if answer == "366":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer: 366\n")

# Question 4
answer = input("4. Who developed Python? ")
if answer.lower() == "guido van rossum":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer: Guido van Rossum\n")

# Question 5
answer = input("5. What is 12 × 8? ")
if answer == "96":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer: 96\n")

print("----------------------------------")
print("🏆 Your Final Score:", score, "/ 5")

if score == 5:
    print("🌟 Excellent! Perfect Score!")
elif score >= 3:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")