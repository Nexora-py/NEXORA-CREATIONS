name = input("Enter your name: ")

print("Welcome", name)
print("🎉 Python Quiz Game 🎉")

score = 0

answer = input("What is the capital of INDIA? ")

if answer.lower() == "new delhi":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("Which is the electronic city of INDIA? ")

if answer.lower() == "bengaluru":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("Which language are we learning? ")

if answer.lower() == "python":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("What is the capital of Kerala? ")

if answer.lower() == "thiruvananthapuram":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

answer = input("What is 12 × 12? ")

if answer == "144":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

print("\n🏆 Quiz Finished!")
print("Your score is", score, "/ 5")

if score == 5:
    print("🌟 Excellent!")
elif score >= 3:
    print("👍 Good Job")
else:
    print("📚 Keep Learning")
