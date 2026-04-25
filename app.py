
#DATA STORAGE

tasks = []
expenses = []
incomes = []
goals = []


#HELPER FUNCTIONS

def divider():
    print("─" * 45)

def header(title):
    print("\n" + "=" * 45)
    print("   " + title)
    print("=" * 45)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter an integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")


#TASK MANAGER


def add_task():
    task_name = input("Enter task: ").strip()
    if task_name == "":
        print("Task cannot be empty.")
        return
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    pending = []
    done = []
    for t in tasks:
        if t["done"] == False:
            pending.append(t)
        else:
            done.append(t)

    print("\nPending Tasks (" + str(len(pending)) + "):")
    divider()
    if len(pending) == 0:
        print("  All tasks completed!")
    else:
        for i in range(len(pending)):
            print("  " + str(i+1) + ". " + pending[i]["task"])

    print("\nCompleted Tasks (" + str(len(done)) + "):")
    divider()
    if len(done) == 0:
        print("  None completed yet.")
    else:
        for i in range(len(done)):
            print("  " + str(i+1) + ". " + done[i]["task"])


def complete_task():
    pending = []
    for t in tasks:
        if t["done"] == False:
            pending.append(t)

    if len(pending) == 0:
        print("No pending tasks!")
        return

    print("\nPending Tasks:")
    for i in range(len(pending)):
        print("  " + str(i+1) + ". " + pending[i]["task"])

    choice = get_int("Enter task number to mark complete: ")
    if choice >= 1 and choice <= len(pending):
        pending[choice - 1]["done"] = True
        print("'" + pending[choice - 1]["task"] + "' marked as complete!")
    else:
        print("Invalid number.")


def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    for i in range(len(tasks)):
        if tasks[i]["done"]:
            status = "Done"
        else:
            status = "Pending"
        print("  " + str(i+1) + ". " + tasks[i]["task"] + " [" + status + "]")

    choice = get_int("Enter task number to delete: ")
    if choice >= 1 and choice <= len(tasks):
        removed = tasks[choice - 1]
        tasks.pop(choice - 1)
        print("'" + removed["task"] + "' deleted.")
    else:
        print("Invalid number.")


def task_menu():
    while True:
        header("TASK MANAGER")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Back to Main Menu")

        choice = input("\nChoice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



#EXPENSE & SAVINGS TRACKER


def add_income():
    amount = input("Enter income amount (BDT): ")
    if amount.replace(".", "", 1).isdigit() == False: 
        print("Invalid input. Enter a number.")
        return
    amount = float(amount)  
    source = input("Source (e.g. Allowance, Freelance): ")
    incomes.append({"amount": amount, "source": source})
    print("Income of " + str(amount) + " BDT added!")


def add_expense():
    amount = input("Enter expense amount (BDT): ")
    if amount.replace(".", "", 1).isdigit() == False:
        print("Invalid input. Enter a number.")
        return
    amount = float(amount)
    print("Categories:")
    print("  1. Food  2. Transport  3. Study  4. Entertainment  5. Other")
    cat = input("Choose category (1-5): ")
    if cat == "1":
        category = "Food"
    elif cat == "2":
        category = "Transport"
    elif cat == "3":
        category = "Study"
    elif cat == "4":
        category = "Entertainment"
    else:
        category = "Other"
    note = input("Note (optional, press Enter to skip): ")
    expenses.append({"amount": amount, "category": category, "note": note})
    print("Expense of " + str(amount) + " BDT added under '" + category + "'!")


def view_finances():
    if len(expenses) == 0 and len(incomes) == 0:
        print("No financial records yet.")
        return

    total_income = 0
    for i in incomes:
        total_income = total_income + i["amount"]

    total_expense = 0
    for e in expenses:
        total_expense = total_expense + e["amount"]

    savings = total_income - total_expense

    print("\nIncome Records:")
    divider()
    if len(incomes) == 0:
        print("  No income added.")
    else:
        for i in incomes:
            print("  + " + str(i["amount"]) + " BDT - " + i["source"])

    print("\nExpense Records:")
    divider()
    if len(expenses) == 0:
        print("  No expenses added.")
    else:
        for e in expenses:
            print("  - " + str(e["amount"]) + " BDT - " + e["category"] + " " + e["note"])

    print("\nSummary:")
    divider()
    print("  Total Income  : " + str(total_income) + " BDT")
    print("  Total Expense : " + str(total_expense) + " BDT")
    if savings >= 0:
        print("  Savings       : " + str(savings) + " BDT")
    else:
        print("  Deficit       : " + str(abs(savings)) + " BDT (Overspent!)")


def view_by_category():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    categories = ["Food", "Transport", "Study", "Entertainment", "Other"]
    print("\nExpenses by Category:")
    divider()
    for cat in categories:
        total = 0
        for e in expenses:
            if e["category"] == cat:
                total = total + e["amount"]
        if total > 0:
            print("  " + cat + " : " + str(total) + " BDT")


def expense_menu():
    while True:
        header("EXPENSE & SAVINGS TRACKER")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Records and Summary")
        print("4. View Expenses by Category")
        print("5. Back to Main Menu")

        choice = input("\nChoice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_finances()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



#GOAL TRACKER

def add_goal():
    name = input("Enter goal (e.g. Save 5000 BDT, Read 10 books): ").strip()
    if name == "":
        print("Goal cannot be empty.")
        return
    target = get_float("Enter target number (e.g. 5000 or 10): ")
    if target == 0:
        print("Target cannot be zero.")
        return
    unit = input("Unit (e.g. BDT, books, km, hours): ")
    goals.append({"name": name, "target": target, "progress": 0, "unit": unit, "done": False})
    print("Goal '" + name + "' added! Target: " + str(target) + " " + unit)

def update_goal():
    active = []
    for g in goals:
        if g["done"] == False:
            active.append(g)

    if len(active) == 0:
        print("No active goals.")
        return

    print("\nActive Goals:")
    for i in range(len(active)):
        percent = (active[i]["progress"] / active[i]["target"]) * 100
        print("  " + str(i+1) + ". " + active[i]["name"] + " - " + str(active[i]["progress"]) + "/" + str(active[i]["target"]) + " " + active[i]["unit"] + " (" + str(round(percent, 1)) + "%)")

    choice_input = input("Enter goal number to update: ")
    if choice_input.isdigit() == False:
        print("Invalid input. Please enter a number.")
        return

    choice = int(choice_input)
    if choice >= 1 and choice <= len(active):
        amount_input = input("Enter progress to add: ")
        if amount_input.replace(".", "", 1).isdigit() == False:
            print("Invalid amount. Please enter a number.")
            return

        amount = float(amount_input)
        active[choice - 1]["progress"] = active[choice - 1]["progress"] + amount
        g = active[choice - 1]
        percent = (g["progress"] / g["target"]) * 100
        if percent > 100:
            percent = 100
        print("Progress: " + str(g["progress"]) + "/" + str(g["target"]) + " " + g["unit"] + " (" + str(round(percent, 1)) + "%)")
        if g["progress"] >= g["target"]:
            g["done"] = True
            print("GOAL '" + g["name"] + "' COMPLETED!")
    else:
        print("Invalid number.")



def view_goals():
    if len(goals) == 0:
        print("No goals set.")
        return

    active = []
    completed = []
    for g in goals:
        if g["done"]:
            completed.append(g)
        else:
            active.append(g)

    print("\nActive Goals (" + str(len(active)) + "):")
    divider()
    if len(active) == 0:
        print("  No active goals.")
    else:
        for g in active:
            if g["target"] == 0:
                percent = 0
            
            else:
                percent = (g["progress"] / g["target"]) * 100
            
            filled = int(percent / 10)
            bar = "█" * filled + "░" * (10 - filled)
            print("  " + g["name"])
            print("  [" + bar + "] " + str(round(percent, 1)) + "% - " + str(g["progress"]) + "/" + str(g["target"]) + " " + g["unit"])

    print("\nCompleted Goals (" + str(len(completed)) + "):")
    divider()
    if len(completed) == 0:
        print("  None yet.")
    else:
        for g in completed:
            print("  Done: " + g["name"])


def goal_menu():
    while True:
        header("GOAL TRACKER")
        print("1. Add New Goal")
        print("2. Update Goal Progress")
        print("3. View All Goals")
        print("4. Back to Main Menu")

        choice = input("\nChoice: ")
        if choice == "1":
            add_goal()
        elif choice == "2":
            update_goal()
        elif choice == "3":
            view_goals()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


#DAILY SUMMARY


def daily_summary():
    header("YOUR DAILY SUMMARY")

    total_tasks = len(tasks)
    done_tasks = 0
    for t in tasks:
        if t["done"]:
            done_tasks = done_tasks + 1
    pending_tasks = total_tasks - done_tasks

    if total_tasks > 0:
        task_percent = (done_tasks / total_tasks) * 100
    else:
        task_percent = 0

    print("\nTasks:")
    divider()
    print("  Total   : " + str(total_tasks))
    print("  Done    : " + str(done_tasks) + " (" + str(round(task_percent)) + "%)")
    print("  Pending : " + str(pending_tasks))

    total_income = 0
    for i in incomes:
        total_income = total_income + i["amount"]

    total_expense = 0
    for e in expenses:
        total_expense = total_expense + e["amount"]

    savings = total_income - total_expense

    print("\nFinances:")
    divider()
    print("  Income   : " + str(total_income) + " BDT")
    print("  Expenses : " + str(total_expense) + " BDT")
    if savings >= 0:
        print("  Savings  : " + str(savings) + " BDT")
    else:
        print("  Deficit  : " + str(abs(savings)) + " BDT (Overspent!)")

    active_count = 0
    done_count = 0
    for g in goals:
        if g["done"]:
            done_count = done_count + 1
        else:
            active_count = active_count + 1

    print("\nGoals:")
    divider()
    print("  Active    : " + str(active_count))
    print("  Completed : " + str(done_count))

    score = 0
    if total_tasks > 0:
        score = score + (task_percent * 0.5)
    if savings > 0:
        score = score + 30
    elif total_income > 0:
        score = score + 10
    if done_count > 0:
        score = score + 20
    if score > 100:
        score = 100

    score = round(score)
    filled = int(score / 10)
    bar = "█" * filled + "░" * (10 - filled)

    print("\nProductivity Score:")
    divider()
    print("  [" + bar + "] " + str(score) + "/100")

    if score >= 80:
        print("  Excellent day! Keep it up!")
    elif score >= 50:
        print("  Good progress. Push a little more!")
    else:
        print("  Room to grow. You got this!")


#MAIN MENU


def main():
    print("\n" + "=" * 45)
    print("   Daily Life and Productivity Tracker")
    print("=" * 45)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Task Manager")
        print("2. Expense and Savings Tracker")
        print("3. Goal Tracker")
        print("4. Daily Summary")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            task_menu()
        elif choice == "2":
            expense_menu()
        elif choice == "3":
            goal_menu()
        elif choice == "4":
            daily_summary()
        elif choice == "5":
            print("Stay productive! Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 to 5.")

if __name__ == "__main__":
    main()

