class DailyTemplate(gym, reading, socializing, coding, chores, sleep, diet):
    def __init__(self, gym, reading, socializing, coding, chores, sleep, diet):
        self.gym = gym
        self.reading = reading
        self.socializing = socializing
        self.coding = coding
        self.chores = chores
        self.sleep = sleep
        self.diet = diet

    def run(self):
        print(f"Today's yield: {self.gym + self.reading + self.socializing + self.coding + self.chores + self.sleep + self.diet}")