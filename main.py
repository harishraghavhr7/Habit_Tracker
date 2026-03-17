
from datetime import dategit
from users import users
from goal import create_goal, goal
from journal import create_journal, journal
from reminder import reminder
from community import community
from communitymembers import communitymembers
from communitypost import communitypost
from badge import badge
from userbadge import userbadge


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def read_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def read_optional_date(prompt):
    raw = input(prompt).strip()
    if raw == "":
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD. Using today.")
        return None


def read_frequency():
    while True:
        freq = input("Frequency (daily/weekly/monthly): ").strip().lower()
        if freq in ("daily", "weekly", "monthly"):
            return freq
        print("Invalid frequency. Choose daily, weekly, or monthly.")


def menu_main():
    print("\n=== Habit Tracker ===")
    print("1. User")
    print("2. Goals")
    print("3. Journal")
    print("4. Reminder")
    print("5. Community")
    print("6. Badge")
    print("0. Exit")
    return input("Choose: ").strip()


def menu_user():
    print("\n--- User Menu ---")
    print("1. Create User")
    print("2. Set Admin")
    print("3. Update User")
    print("4. Get User by ID")
    print("5. Create Habit for User")
    print("0. Back")
    return input("Choose: ").strip()


def menu_goal():
    print("\n--- Goal Menu ---")
    print("1. Create Goal")
    print("2. Mark Done")
    print("3. Unmark Done")
    print("4. Show Progress")
    print("5. List Goals by User")
    print("6. Evaluate and Award Badge")
    print("0. Back")
    return input("Choose: ").strip()


def menu_journal():
    print("\n--- Journal Menu ---")
    print("1. Create Journal Entry")
    print("2. List Journals by User")
    print("0. Back")
    return input("Choose: ").strip()


def menu_reminder():
    print("\n--- Reminder Menu ---")
    print("1. Create Reminder")
    print("2. List Reminders by Goal")
    print("3. Delete Reminder")
    print("0. Back")
    return input("Choose: ").strip()


def menu_community():
    print("\n--- Community Menu ---")
    print("1. Create Community")
    print("2. Update Community")
    print("3. Add Member")
    print("4. Remove Member")
    print("5. List Members")
    print("6. Create Post")
    print("7. List Posts")
    print("0. Back")
    return input("Choose: ").strip()


def menu_badge():
    print("\n--- Badge Menu ---")
    print("1. Create Badge by Admin")
    print("2. List Badges")
    print("3. List User Badges")
    print("0. Back")
    return input("Choose: ").strip()


def handle_user():
    while True:
        c = menu_user()
        try:
            if c == "1":
                userid = read_int("User ID: ")
                username = read_text("Username: ")
                email = read_text("Email: ")
                password = read_text("Password: ")
                u = users.create_user(userid, username, email, password)
                print("Created user:", u.userid, u.username)

            elif c == "2":
                userid = read_int("User ID to set admin: ")
                users.set_admin(userid)
                print("User set as admin.")

            elif c == "3":
                userid = read_int("User ID: ")
                username = input("New username (blank to skip): ").strip() or None
                email = input("New email (blank to skip): ").strip() or None
                password = input("New password (blank to skip): ").strip() or None
                u = users.update_user(userid, username=username, email=email, password=password)
                print("Updated user:", u.userid, u.username, u.email)

            elif c == "4":
                userid = read_int("User ID: ")
                u = users.get_by_id(userid)
                if not u:
                    print("User not found.")
                else:
                    print("User:", u.userid, u.username, u.email, "admin=", u.is_admin)

            elif c == "5":
                userid = read_int("User ID: ")
                habitid = read_int("Habit ID: ")
                habitname = read_text("Habit Name: ")
                u = users.get_by_id(userid)
                if not u:
                    print("User not found.")
                else:
                    h = u.create_habit(habitid, habitname)
                    print("Habit created:", h.habitid, h.habitname)

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def handle_goal():
    while True:
        c = menu_goal()
        try:
            if c == "1":
                name = read_text("Goal Name: ")
                userid = read_int("User ID: ")
                goalid = read_int("Goal ID: ")
                habitid = read_int("Habit ID: ")
                description = read_text("Description: ")
                frequency = read_frequency()
                g = create_goal(name, userid, goalid, habitid, description, frequency)
                print("Goal created:", g.goalid, g.name)

            elif c == "2":
                goalid = read_int("Goal ID: ")
                d = read_optional_date("Done date YYYY-MM-DD (blank=today): ")
                g = goal.get_by_id(goalid)
                if not g:
                    print("Goal not found.")
                else:
                    g.mark_done(d)
                    print("Marked done.")

            elif c == "3":
                goalid = read_int("Goal ID: ")
                d = read_optional_date("Done date YYYY-MM-DD (blank=today): ")
                g = goal.get_by_id(goalid)
                if not g:
                    print("Goal not found.")
                else:
                    g.unmark_done(d)
                    print("Unmarked done.")

            elif c == "4":
                goalid = read_int("Goal ID: ")
                g = goal.get_by_id(goalid)
                if not g:
                    print("Goal not found.")
                else:
                    print("Progress:", g.get_progress())

            elif c == "5":
                userid = read_int("User ID: ")
                items = goal.list_goals_by_userid(userid)
                if not items:
                    print("No goals found.")
                else:
                    for g in items:
                        print("Goal:", g.goalid, g.name, g.frequency)

            elif c == "6":
                goalid = read_int("Goal ID: ")
                g = goal.get_by_id(goalid)
                if not g:
                    print("Goal not found.")
                else:
                    awarded = g.evaluate_and_award_badge()
                    print("Awarded badges:", awarded)

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def handle_journal():
    while True:
        c = menu_journal()
        try:
            if c == "1":
                entryid = read_int("Entry ID: ")
                userid = read_int("User ID: ")
                habitid = read_int("Habit ID: ")
                goalid = read_int("Goal ID: ")
                entry_date = input("Entry date (text or YYYY-MM-DD): ").strip()
                entry = read_text("Entry text: ")
                j = create_journal(entryid, userid, habitid, goalid, entry_date, entry)
                print("Journal created:", j.entryid)

            elif c == "2":
                userid = read_int("User ID: ")
                items = journal.list_journals_by_userid(userid)
                if not items:
                    print("No journals found.")
                else:
                    for j in items:
                        print("Entry:", j.entryid, "| Date:", j.date, "| Text:", j.entry)

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def handle_reminder():
    while True:
        c = menu_reminder()
        try:
            if c == "1":
                reminderid = read_int("Reminder ID: ")
                goalid = read_int("Goal ID: ")
                remindertime = read_text("Reminder time (text): ")
                r = reminder.create_reminder(reminderid, goalid, remindertime)
                print("Reminder created:", r.reminderid)

            elif c == "2":
                goalid = read_int("Goal ID: ")
                items = reminder.list_reminders_by_goalid(goalid)
                if not items:
                    print("No reminders found.")
                else:
                    for r in items:
                        print("Reminder:", r.reminderid, r.remindertime)

            elif c == "3":
                reminderid = read_int("Reminder ID: ")
                reminder.delete_reminder(reminderid)
                print("Reminder deleted.")

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def handle_community():
    while True:
        c = menu_community()
        try:
            if c == "1":
                communityid = read_int("Community ID: ")
                name = read_text("Name: ")
                description = read_text("Description: ")
                createdby = read_int("Created by user ID: ")
                cm = community.create_community(communityid, name, description, createdby)
                print("Community created:", cm.communityid, cm.name)

            elif c == "2":
                communityid = read_int("Community ID: ")
                name = input("New name (blank to skip): ").strip() or None
                description = input("New description (blank to skip): ").strip() or None
                cm = community.update_community(communityid, name=name, description=description)
                print("Community updated:", cm.communityid, cm.name)

            elif c == "3":
                communityid = read_int("Community ID: ")
                userid = read_int("User ID: ")
                role = read_text("Role: ")
                joined_id = read_text("Joined ID/value: ")
                m = communitymembers.create_communitymembers(communityid, userid, role, joined_id)
                print("Member added:", m.userid, "to community", m.communityid)

            elif c == "4":
                communityid = read_int("Community ID: ")
                userid = read_int("User ID: ")
                communitymembers.remove_communitymembers(communityid, userid)
                print("Member removed.")

            elif c == "5":
                communityid = read_int("Community ID: ")
                items = communitymembers.list_communitymembers_by_communityid(communityid)
                if not items:
                    print("No members found.")
                else:
                    for m in items:
                        print("Member:", m.userid, "| Role:", m.role)

            elif c == "6":
                postid = read_int("Post ID: ")
                communityid = read_int("Community ID: ")
                userid = read_int("User ID: ")
                content = read_text("Post content: ")
                p = communitypost.create_communitypost(postid, communityid, userid, content)
                print("Post created:", p.postid)

            elif c == "7":
                communityid = read_int("Community ID: ")
                posts = communitypost.list_communityposts_by_communityid(communityid)
                if not posts:
                    print("No posts found.")
                else:
                    for p in posts:
                        print("Post:", p.postid, "| User:", p.userid, "|", p.content)

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def handle_badge():
    while True:
        c = menu_badge()
        try:
            if c == "1":
                admin_userid = read_int("Admin User ID: ")
                badgeid = read_int("Badge ID: ")
                name = read_text("Badge Name: ")
                description = read_text("Badge Description: ")
                criteria_type = input("Criteria type (progress_percentage/completed_count): ").strip()
                if criteria_type not in ("progress_percentage", "completed_count"):
                    print("Invalid criteria type.")
                    continue
                criteria_value = read_float("Criteria value: ")
                b = badge.create_badge_by_admin(
                    admin_userid, badgeid, name, description, criteria_type, criteria_value
                )
                print("Badge created:", b.badgeid, b.name)

            elif c == "2":
                items = badge.list_badges()
                if not items:
                    print("No badges available.")
                else:
                    for b in items:
                        print(
                            "Badge:", b.badgeid, b.name,
                            "| type:", b.criteria_type,
                            "| value:", b.criteria_value
                        )

            elif c == "3":
                userid = read_int("User ID: ")
                print("User badges:", userbadge.list_userbadges_by_userid(userid))

            elif c == "0":
                return
            else:
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)


def run():
    while True:
        c = menu_main()
        if c == "1":
            handle_user()
        elif c == "2":
            handle_goal()
        elif c == "3":
            handle_journal()
        elif c == "4":
            handle_reminder()
        elif c == "5":
            handle_community()
        elif c == "6":
            handle_badge()
        elif c == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()