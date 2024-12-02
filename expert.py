class SimpleExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diseases = {
            "Flu": ["fever", "chills", "headache"],
            "Cold": ["cough", "sneezing", "sore throat"],
            "Covid-19": ["fever", "cough", "loss of taste"]
        }

    def ask_symptoms(self):
        print("Answer with yes or no:")
        questions = [
            ("fever", "Do you have a fever?"),
            ("cough", "Do you have a cough?"),
            ("chills", "Do you have chills?"),
            ("headache", "Do you have a headache?"),
            ("sneezing", "Do you have sneezing?"),
            ("sore throat", "Do you have a sore throat?"),
            ("loss of taste", "Have you lost your sense of taste or smell?")
        ]

        for symptom, question in questions:
            if input(question + " ").lower() == "yes":
                self.symptoms.append(symptom)

    def diagnose(self):
        print("\nPossible conditions:")
        matches = [
            disease for disease, symptoms in self.diseases.items()
            if all(symptom in self.symptoms for symptom in symptoms)
        ]

        if matches:
            print(", ".join(matches))
        else:
            print("No clear match found. Consider consulting a doctor.")

# Run the expert system
expert_system = SimpleExpertSystem()
expert_system.ask_symptoms()
expert_system.diagnose()
