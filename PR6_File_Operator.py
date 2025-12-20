# this code not run in online compiler because it requires user input and file operations

print("Welcome to Personal Journal Manager!")
print("Please select an option:")

from datetime import datetime

class JournalManager:
    def __init__(self, file_name="JournalEntry.txt"):
        self.file_name = file_name

    def add_new_entry(self):
        try:
            entry_text = input("Enter your journal entry:\n")
            current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            with open(self.file_name, "a") as journal_file:
                journal_file.write(f"{current_time}\n{entry_text}\n")

            print("\nEntry added successfully!")

        except Exception as error:
            print("Error while adding entry:", error)

    def view_all_entries(self):
        try:
            with open(self.file_name, "r") as journal_file:
                content = journal_file.read().strip()
                if content:
                    print("\nYour Journal Entries:")
                    print(content)
                else:
                    print("\nNo journal entries found. Start by adding a new entry!")
        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
        except Exception as error:
            print("Error:", error)

    def search_for_entry(self):
        try:
            search_term = input("Enter a keyword or date to search: ")
            with open(self.file_name, "r") as journal_file:
                lines = journal_file.read().strip().split('\n')
                entries = []
                for i in range(0, len(lines), 2):
                    if i + 1 < len(lines):
                        entry = f"[{lines[i]}]\n{lines[i+1]}"
                        entries.append(entry)
                
                matching_entries = []
                for entry in entries:
                    if search_term.lower() in entry.lower():
                        matching_entries.append(entry)
                
                if matching_entries:
                    print("\nMatching Entries:")
                    for match in matching_entries:
                        print(match)
                        print()
                else:
                    print(f"No entries were found for the keyword: {search_term}.")
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except Exception as error:
            print("Error:", error)

    def delete_all_entries(self):
        try:
            if not self._file_exists():
                print("No journal entries to delete.")
                return
            confirmation = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirmation.lower() == "yes":
                with open(self.file_name, "w") as journal_file:
                    pass
                print("All journal entries have been deleted.")
            else:
                print("Delete operation cancelled.")
        except Exception as error:
            print("Error:", error)

    def _file_exists(self):
        try:
            with open(self.file_name, "r"):
                return True
        except FileNotFoundError:
            return False


journal_mgr = JournalManager()

while True:
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        user_choice = int(input("User input:"))
    except ValueError:
        print("Invalid option. Please select a valid option from the menu.")
        continue

    if user_choice == 1:
        journal_mgr.add_new_entry()
    elif user_choice == 2:
        journal_mgr.view_all_entries()
    elif user_choice == 3:
        journal_mgr.search_for_entry()
    elif user_choice == 4:
        journal_mgr.delete_all_entries()
    elif user_choice == 5:
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.")