from datetime import date

class Badge:
    BADGE_FIRST_HABIT = "First Habit"
    BADGE_7_DAY_STREAK = "7 Day Streak"
    BADGE_30_DAY_STREAK = "30 Day Streak"
    BADGE_LEVEL_5 = "Level 5 Achiever"
    BADGE_PERFECT_WEEK = "Perfect Week"
    BADGE_CENTURY = "Century Club"  # 100 points



    def __init__(self, UserID,BadgeName,DateEarned=None,BadgeID=None):
        self.BadgeID = BadgeID
        self.UserID = UserID
        self.BadgeName = BadgeName
        self.DateEarned = DateEarned if DateEarned else date.today()

    
    def _validate_user_id(self, user_id):
        if user_id <= 0:
            return False, "User ID must be a positive integer."
        return True, ""
    
    def _validate_badge_name(self,badge_name):
        if not badge_name:
            return False, "Badge name cannot be empty."
        if len(badge_name) < 3:
            return False, "Badge name must be at least 3 characters long."
        return True, ""
    
    def _validate_date_earned(self, date_earned):
        if date_earned > date.today():
            return False, "Date earned cannot be in the future."
        return True, ""
    

    def __str__(self):
        return f"Badge(BadgeID={self.BadgeID}, UserID={self.UserID}, BadgeName={self.BadgeName}, DateEarned={self.DateEarned})" 
    
    def display_badge(self):
        print(f"Badge Name: {self.BadgeName}")
        print(f"Date Earned: {self.DateEarned}")    
    

    def is_earned_today(self):
        return self.DateEarned == date.today()
    
    def days_since_earned(self):
        return (date.today() - self.DateEarned).days
    
    def is_same_badge(self, other_badge):
        return self.BadgeName == other_badge.BadgeName and self.UserID == other_badge.UserID
    
    
    @classmethod
    def get_all_badges(cls):
        """Get list of all available badge types"""
        return [
            cls.BADGE_FIRST_HABIT,
            cls.BADGE_7_DAY_STREAK,
            cls.BADGE_30_DAY_STREAK,
            cls.BADGE_LEVEL_5,
            cls.BADGE_PERFECT_WEEK,
            cls.BADGE_CENTURY
        ]
        
    @classmethod
    def is_valid_badge_type(cls, badge_name):
        return badge_name in cls.get_all_badges()
    
from datetime import timedelta

# Test 1: Award a badge
print("Test 1: Award new badge")
badge1 = Badge(UserID=1, BadgeName=Badge.BADGE_FIRST_HABIT)
badge1.display_badge()

# Test 2: Badge with specific date
print("\nTest 2: Badge earned last week")
last_week = date.today() - timedelta(days=7)
badge2 = Badge(UserID=1, BadgeName=Badge.BADGE_7_DAY_STREAK, DateEarned=last_week)
badge2.display_badge()
print(f"Days since earned: {badge2.days_since_earned()}")

# Test 3: Check if earned today
print("\nTest 3: Check if earned today")
print(f"Badge1 earned today: {badge1.is_earned_today()}")
print(f"Badge2 earned today: {badge2.is_earned_today()}")

# Test 4: Compare badges
print("\nTest 4: Compare badges")
badge3 = Badge(UserID=2, BadgeName=Badge.BADGE_FIRST_HABIT)
print(f"Badge1 and Badge3 same type: {badge1.is_same_badge(badge3)}")
print(f"Badge1 and Badge2 same type: {badge1.is_same_badge(badge2)}")

# Test 5: Invalid user ID (should fail)
print("\nTest 5: Invalid user ID")
try:
    badge4 = Badge(UserID=-1, BadgeName=Badge.BADGE_FIRST_HABIT)
except ValueError as e:
    print(f"✓ Caught error: {e}")

# Test 6: Invalid badge name (should fail)
print("\nTest 6: Invalid badge name")
try:
    badge5 = Badge(UserID=1, BadgeName="Invalid Badge")
except ValueError as e:
    print(f"✓ Caught error: {e}")

# Test 7: Future date (should fail)
print("\nTest 7: Future date")
try:
    tomorrow = date.today() + timedelta(days=1)
    badge6 = Badge(UserID=1, BadgeName=Badge.BADGE_7_DAY_STREAK, DateEarned=tomorrow)
except ValueError as e:
    print(f"✓ Caught error: {e}")

# Test 8: Get all badge types
print("\nTest 8: All available badges")
all_badges = Badge.get_all_badges()
print("Available badges:")
for i, badge_name in enumerate(all_badges, 1):
    print(f"  {i}. {badge_name}")

# Test 9: Validate badge type
print("\nTest 9: Validate badge type")
print(f"Is 'First Habit' valid: {Badge.is_valid_badge_type('First Habit')}")
print(f"Is 'Fake Badge' valid: {Badge.is_valid_badge_type('Fake Badge')}")