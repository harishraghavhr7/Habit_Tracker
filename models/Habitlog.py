from datetime import date

class HabitLog:
    """Tracks completion of a habit on a specific date"""
    
    def __init__(self, habit_id, logdate=None, completed=False, log_id=None):
        """
        Initialize habit log
        
        Args:
            habit_id (int): ID of habit being logged
            logdate (date, optional): Date of log (defaults to today)
            completed (bool): Whether completed (default False)
            log_id (int, optional): ID for existing logs
        """
        self.log_id = log_id
        self.habit_id = habit_id
        self.date = logdate if logdate else date.today()
        self.completed = completed
        
        # Validate after setting attributes
        valid, error = self._validate_habit_id(habit_id)
        if not valid:
            raise ValueError(error)
        
        valid, error = self._validate_date(self.date)
        if not valid:
            raise ValueError(error)
        
        valid, error = self._validate_completed(completed)
        if not valid:
            raise ValueError(error)

    def _validate_habit_id(self, habit_id):
        """Validate habit ID is positive"""
        if habit_id <= 0:
            return False, "Habit ID must be a positive integer."
        return True, ""
    
    def _validate_date(self, log_date):  # ✅ Renamed parameter
        """Validate date is not in future"""
        if log_date > date.today():
            return False, "Log date cannot be in the future."
        return True, ""
    
    def _validate_completed(self, completed):
        """Validate completed is boolean"""
        if not isinstance(completed, bool):  # ✅ Check type, not value
            return False, "Completed must be a boolean value."
        return True, ""
    
    def __str__(self):
        """String representation"""
        status = "✓" if self.completed else "✗"
        return f"HabitLog(ID={self.log_id}, HabitID={self.habit_id}, Date={self.date}, Status={status})"
    
    def display_log(self):
        """Display log information"""
        status = "Completed ✓" if self.completed else "Incomplete ✗"
        print(f"{'='*40}")
        print(f"Log ID: {self.log_id}")
        print(f"Habit ID: {self.habit_id}")
        print(f"Date: {self.date}")
        print(f"Status: {status}")
        print(f"{'='*40}")
    
    def mark_completed(self):
        """Mark as completed"""
        self.completed = True
        print(f"✓ Habit log for HabitID {self.habit_id} marked as completed on {self.date}.")
    
    def mark_incomplete(self):
        """Mark as incomplete"""
        self.completed = False
        print(f"✗ Habit log for HabitID {self.habit_id} marked as incomplete on {self.date}.")
    
    def toggle_completion(self):
        """Toggle completion status"""
        self.completed = not self.completed
        status = "completed ✓" if self.completed else "incomplete ✗"
        print(f"Habit log for HabitID {self.habit_id} toggled to {status} on {self.date}.")
    
    def is_today(self):
        """Check if log is for today"""
        return self.date == date.today()
    
    def is_completed_on_date(self, check_date):
        """Check if completed on specific date"""
        return self.date == check_date and self.completed


# ============= TESTS =============
if __name__ == "__main__":
    from datetime import timedelta
    
    print("="*50)
    print("Test 1: Create log for today")
    print("="*50)
    log1 = HabitLog(habit_id=1)
    log1.display_log()
    
    print("\n" + "="*50)
    print("Test 2: Create log for specific date")
    print("="*50)
    yesterday = date.today() - timedelta(days=1)
    log2 = HabitLog(habit_id=1, logdate=yesterday, completed=False)
    log2.display_log()
    
    print("\n" + "="*50)
    print("Test 3: Toggle completion")
    print("="*50)
    log1.toggle_completion()
    log1.display_log()
    
    print("\n" + "="*50)
    print("Test 4: Check if today")
    print("="*50)
    print(f"Log1 is today: {log1.is_today()}")
    print(f"Log2 is today: {log2.is_today()}")
    
    print("\n" + "="*50)
    print("Test 5: Invalid habit ID (should fail)")
    print("="*50)
    try:
        log3 = HabitLog(habit_id=-1)
    except ValueError as e:
        print(f"✓ Caught error: {e}")
    
    print("\n" + "="*50)
    print("Test 6: Future date (should fail)")
    print("="*50)
    try:
        tomorrow = date.today() + timedelta(days=1)
        log4 = HabitLog(habit_id=1, logdate=tomorrow)  # ✅ Fixed typo
    except ValueError as e:
        print(f"✓ Caught error: {e}")
    
    print("\n" + "="*50)
    print("Test 7: Mark completed/incomplete")
    print("="*50)
    log2.mark_completed()
    log2.display_log()
    log2.mark_incomplete()
    log2.display_log()