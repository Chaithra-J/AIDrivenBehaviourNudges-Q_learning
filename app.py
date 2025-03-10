<<<<<<< HEAD
import random
import os
import numpy as np
import pandas as pd
import nltk
from transformers import pipeline
from collections import defaultdict
from database import save_user_response
import sys

sys.stdout.reconfigure(encoding='utf-8')


nltk.download("stopwords")

SUSTAINABILITY_AREAS = {
    "transport": [
        "Walk or cycle for short trips ",
        "Use public transport instead of a personal car ",
        "Carpool to save fuel and reduce emissions ",
    ],
    "energy": [
        "Switch off unused appliances to save energy",
        "Use LED bulbs instead of incandescent ones ",
        "Lower your thermostat by 1°C to save electricity ",
    ],
    "shopping": [
        "Buy locally sourced products to reduce your carbon footprint ",
        "Bring reusable bags instead of plastic ones ",
        "Support brands that prioritize sustainability ",
    ],
    "food": [
        "Reduce meat consumption and opt for plant-based meals ",
        "Avoid food waste by planning your meals carefully ",
        "Choose seasonal and locally grown produce ",
    ],
    "waste": [
        "Recycle paper, plastic, and glass responsibly ",
        "Compost organic waste to reduce landfill pollution ",
        "Avoid single-use plastics and switch to reusable alternatives ",
    ],
}

class SustainabilityAdvisor:
    def __init__(self):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.2  # Exploration vs exploitation

    def assess_user(self):
        """Ask the user sustainability-related questions and assign a score."""
        scores = {}
        print(" Sustainability Self-Assessment ")
        
        for area, questions in {
            "transport": "How often do you use public transport instead of a car? (never/sometimes/always)",
            "energy": "Do you switch off appliances when not in use? (never/sometimes/always)",
            "shopping": "Do you prioritize eco-friendly products? (never/sometimes/always)",
            "food": "Do you try to reduce meat consumption? (never/sometimes/always)",
            "waste": "Do you recycle and minimize waste? (never/sometimes/always)"
        }.items():
            response = input(f"{questions} ").strip().lower()
            scores[area] = {"never": 0, "sometimes": 1, "always": 2}.get(response, 1)

        return scores

    def select_nudge(self, area):
        """Select the best nudge using an ε-greedy policy."""
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(SUSTAINABILITY_AREAS[area]) 
        else:
            return max(SUSTAINABILITY_AREAS[area], key=lambda x: self.q_table[area][x])  # Exploitation

    def update_q_value(self, area, nudge, reward):
        """Update Q-values based on user feedback."""
        self.q_table[area][nudge] += self.learning_rate * (
            reward + self.discount_factor * max(self.q_table[area].values(), default=0) - self.q_table[area][nudge]
        )

# sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyze sentiment of user-provided climate thoughts."""
    result = sentiment_analyzer(text)[0]
    return f"Sentiment: {result['label']} (Score: {result['score']:.2f})"

#Assessment & Recommendations
def run_sustainability_assessment():
    advisor = SustainabilityAdvisor()
    
    # User assessment
    user_scores = advisor.assess_user()
    print("\nSustainability Score Summary:")
    for area, score in user_scores.items():
        print(f"🔹 {area.capitalize()}: {score}/2")

    # Provide AI-powered nudges
    print("\nPersonalized Climate Action Recommendations:")
    recommendations = {}
    for area, score in user_scores.items():
        if score < 2:  # Recommend nudges only for areas needing improvement
            suggested_nudge = advisor.select_nudge(area)
            print(f"{area.capitalize()}: {suggested_nudge}")

    # User feedback on recommendations
    for area, score in user_scores.items():
        if score < 2:
            nudge = advisor.select_nudge(area)
            feedback = input(f"Did you follow this suggestion? (yes/no): ").strip().lower()
            reward = 1 if feedback == "yes" else -1
            # reward += 1 & print("You've earned a reward point") if feedback == "yes" else (reward - 1) & print("You have lost 1 of your saved rewards")
            advisor.update_q_value(area, nudge, reward)

            # Save user response & AI recommendation to database
            save_user_response(area, nudge, feedback)
        print("\n Your responses and AI recommendations have been saved to the database!")
        # exit()

    # Sentiment Analysis
    user_text = input("\nShare a climate-related thought or experience: ")
    print(analyze_sentiment(user_text))

# Run the assessment
if __name__ == "__main__":
    run_sustainability_assessment()
=======
import random
import os
import numpy as np
import pandas as pd
import nltk
from transformers import pipeline
from collections import defaultdict
from database import save_user_response
import sys

sys.stdout.reconfigure(encoding='utf-8')


nltk.download("stopwords")

SUSTAINABILITY_AREAS = {
    "transport": [
        "Walk or cycle for short trips ",
        "Use public transport instead of a personal car ",
        "Carpool to save fuel and reduce emissions ",
    ],
    "energy": [
        "Switch off unused appliances to save energy",
        "Use LED bulbs instead of incandescent ones ",
        "Lower your thermostat by 1°C to save electricity ",
    ],
    "shopping": [
        "Buy locally sourced products to reduce your carbon footprint ",
        "Bring reusable bags instead of plastic ones ",
        "Support brands that prioritize sustainability ",
    ],
    "food": [
        "Reduce meat consumption and opt for plant-based meals ",
        "Avoid food waste by planning your meals carefully ",
        "Choose seasonal and locally grown produce ",
    ],
    "waste": [
        "Recycle paper, plastic, and glass responsibly ",
        "Compost organic waste to reduce landfill pollution ",
        "Avoid single-use plastics and switch to reusable alternatives ",
    ],
}

class SustainabilityAdvisor:
    def __init__(self):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.2  # Exploration vs exploitation

    def assess_user(self):
        """Ask the user sustainability-related questions and assign a score."""
        scores = {}
        print(" Sustainability Self-Assessment ")
        
        for area, questions in {
            "transport": "How often do you use public transport instead of a car? (never/sometimes/always)",
            "energy": "Do you switch off appliances when not in use? (never/sometimes/always)",
            "shopping": "Do you prioritize eco-friendly products? (never/sometimes/always)",
            "food": "Do you try to reduce meat consumption? (never/sometimes/always)",
            "waste": "Do you recycle and minimize waste? (never/sometimes/always)"
        }.items():
            response = input(f"{questions} ").strip().lower()
            scores[area] = {"never": 0, "sometimes": 1, "always": 2}.get(response, 1)

        return scores

    def select_nudge(self, area):
        """Select the best nudge using an ε-greedy policy."""
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(SUSTAINABILITY_AREAS[area]) 
        else:
            return max(SUSTAINABILITY_AREAS[area], key=lambda x: self.q_table[area][x])  # Exploitation

    def update_q_value(self, area, nudge, reward):
        """Update Q-values based on user feedback."""
        self.q_table[area][nudge] += self.learning_rate * (
            reward + self.discount_factor * max(self.q_table[area].values(), default=0) - self.q_table[area][nudge]
        )

# sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyze sentiment of user-provided climate thoughts."""
    result = sentiment_analyzer(text)[0]
    return f"Sentiment: {result['label']} (Score: {result['score']:.2f})"

#Assessment & Recommendations
def run_sustainability_assessment():
    advisor = SustainabilityAdvisor()
    
    # User assessment
    user_scores = advisor.assess_user()
    print("\nSustainability Score Summary:")
    for area, score in user_scores.items():
        print(f"🔹 {area.capitalize()}: {score}/2")

    # Provide AI-powered nudges
    print("\nPersonalized Climate Action Recommendations:")
    recommendations = {}
    for area, score in user_scores.items():
        if score < 2:  # Recommend nudges only for areas needing improvement
            suggested_nudge = advisor.select_nudge(area)
            print(f"{area.capitalize()}: {suggested_nudge}")

    # User feedback on recommendations
    for area, score in user_scores.items():
        if score < 2:
            nudge = advisor.select_nudge(area)
            feedback = input(f"Did you follow this suggestion? (yes/no): ").strip().lower()
            reward = 1 if feedback == "yes" else -1
            # reward += 1 & print("You've earned a reward point") if feedback == "yes" else (reward - 1) & print("You have lost 1 of your saved rewards")
            advisor.update_q_value(area, nudge, reward)

            # Save user response & AI recommendation to database
            save_user_response(area, nudge, feedback)
        print("\n Your responses and AI recommendations have been saved to the database!")
        # exit()

    # Sentiment Analysis
    user_text = input("\nShare a climate-related thought or experience: ")
    print(analyze_sentiment(user_text))

# Run the assessment
if __name__ == "__main__":
    run_sustainability_assessment()
>>>>>>> master
