class DietExpertSystem: 
    def __init__(self):
        self.knowledge_base = {
            "Vegetarian": "You should focus on plant-based foods and avoid meat and animal products.",
            "Vegan": "You should follow a strict plant-based diet, avoiding all animal products.",
            "Omnivore": "You have a wide range of food options, including both plant-based and animal-based foods.",
        }
        
    def get_diet_recommendation(self, dietary_preference):
        recommendation = self.knowledge_base.get(dietary_preference) 
        if recommendation:
            return recommendation 
        else:
            return "I don't have a specific recommendation for that dietary preference."
        

diet_system = DietExpertSystem()
dietary_preference = "Vegetarian"
recommendation = diet_system.get_diet_recommendation(dietary_preference)
print(f"If you are a {dietary_preference}, {recommendation}")