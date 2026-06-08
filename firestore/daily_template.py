class DailyTemplate(gym, reading, socializing, coding, chores, sleep, diet_sugar, diet_protein):
    def __init__(self, gym, reading, socializing, coding, chores, sleep, diet_sugar, diet_protein):
        self.gym = gym # Bool | Did you go to the gym today?
        self.reading = reading # Bool | Did you read today?
        self.socializing = socializing # Bool | Did you socialize today?
        self.coding = coding # Bool | Did you code today?
        self.chores = chores # Bool | Did you do chores today?
        self.sleep = sleep # Int | How many hours did you sleep tonight?
        self.diet_sugar = diet_sugar # Bool | Did you consume too much sugar today?
        self.diet_protein = diet_protein # Bool | Did you consume enough protein today?

    def run(self):
        print(f"Today's yield: {self.gym + self.reading + self.socializing + self.coding + self.chores + self.sleep + self.diet_sugar + self.diet_protein}")