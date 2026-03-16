class Habit:
    def __init__(self, HabitID, UserID, HabitName, Frequency):
        self.HabitName = HabitName
        self.Frequency = Frequency
        self.HabitID= HabitID
        self.UserID = UserID

        valid,error = self._validate_habit_name(HabitName)
        if not valid:
            raise ValueError(error)
        valid,error = self._validate_frequency(Frequency)
        if not valid:
            raise ValueError(error)

    
    def _validate_frequency(self,habit_frequency):
        valid_frequencies = ["daily", "weekly", "monthly"]
        if habit_frequency not in valid_frequencies:
            return False,f"Frequency must be one of {valid_frequencies}."
        return True,""
    
    def __str__(self):
        return f"Habit(HabitID={self.HabitID}, UserID={self.UserID}, HabitName={self.HabitName}, Frequency={self.Frequency})"
    
    def display_habit(self):
        print(f"Habit Name: {self.HabitName}")
        print(f"Frequency: {self.Frequency}")

    def update_habit(self,new_name=None,new_frequency=None):
        updated = False
        if new_name:
            valid,error = self._validate_habit_name(new_name)
            if not valid:
                print(f"Error updating habit name: {error}")
            else:
                self.HabitName = new_name
                updated = True
        if new_frequency:
            valid,error = self._validate_frequency(new_frequency)
            if not valid:
                print(f"Error updating habit frequency: {error}")
            else:
                self.Frequency = new_frequency
                updated = True 
        if updated:
            print("Habit updated successfully!")    
        else:
            print("No updates made to the habit.")


habit1=Habit(1,1,"Exercise","daily")

habit1.display_habit()
habit1.update_habit(new_name="Morning Exercise",new_frequency="weekly")
habit1.display_habit()
