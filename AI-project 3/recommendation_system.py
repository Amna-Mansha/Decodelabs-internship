# AI Recommendation Logic System

items = {
    "Python for Beginners": ["python", "programming"],
    "Machine Learning Basics": ["machine learning", "ai"],
    "Deep Learning Guide": ["deep learning", "ai"],
    "Web Development": ["html", "css", "javascript"],
    "Data Science with Python": ["python", "data science"],
    "Artificial Intelligence Mastery": ["ai", "machine learning"]
}

print("=== AI Recommendation System ===")

user_input = input("Enter your interests separated by commas: ")

user_preferences = [x.strip().lower() for x in user_input.split(",")]

recommendations = []

for item, tags in items.items():
    score = len(set(user_preferences) & set(tags))

    if score > 0:
        recommendations.append((item, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Items:")

if recommendations:
    for item, score in recommendations:
        print(f"{item} (Match Score: {score})")
else:
    print("No recommendations found.")