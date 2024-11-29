import streamlit as st

st.write("Hello Group 8")

# Page Title
print("eCE lang sa DEs: Your Trusted Formula Compiler")
print()
# Introduction
print("Welcome to eCE lang sa DEs!")
my_string = """eCE lang sa DEs is a sophisticated and user-centric equipment
 formula compiler designed to be your reliable 
 partner in solving problems in Differential Equations."""
print()
print(my_string)
print()
# Objectives
print("Objectives:")
print("This tool is aiming for the following:")
print("* User-friendly Interface")
print("* Formula Compiling")
print("* Reliability and Partnership")
print()

print("How can we help you?")
print()
print("Please Select an Option:")

import re
from datetime import datetime


class FormulaManager:
    def __init__(self):
        self.formula = {}
        self.formula_records = {}

    def validate_alphanumeric_with_spaces(self, value, field_name):
        if field_name == "Formula description":
            return
        if not re.match("^[a-zA-Z0-9\s-]+$", value.strip()):
            raise ValueError(f"Error: {field_name} should contain only letters, numbers, spaces, and dashes.")

    def validate_input(self, name, description, date_str=None):
        self.validate_alphanumeric_with_spaces(name, "Formula name")
        self.validate_alphanumeric_with_spaces(description, "Formula description")

    def add_formula(self, name, description):
        try:
            if not name.strip():
                raise ValueError("Error: Formula name is required.")
            if not re.match("^[a-zA-Z0-9\s-]+$", name):
                raise ValueError("Error: Invalid Formula name.")
            if not description.strip():
                raise ValueError("Error: Formula description cannot be empty.")

            self.formula[name] = description
            print(f"Formula '{name}' added to the list.")

            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if name not in self.formula_records:
                self.formula_records[name] = {}
            self.formula_records[name][date_str] = description
        except ValueError as e:
            print(str(e))

    def view_formula(self):
        print("-" * 60)
        print("\n\t\tFormula Lists\n")
        print("-" * 60)
        print(f"{'Formula Name':<40}{'Description'}")
        print("-" * 60)

        for name, description in self.formula.items():
            print(f"{name:<25}| {description}")

    def view_recorded_formula_history(self, formula_name):
        print(f"\nFormula History for '{formula_name}':")
        print("-" * 60)
        print("\n\t\t", formula_name, "\n")
        print("-" * 60)
        if formula_name in self.formula_records:
            for date, description in self.formula_records[formula_name].items():
                print(f"{date:<20}| {description}")
        else:
            print("No recorded history for this formula.")


def main():
    manager = FormulaManager()

    while True:
        print("\nOptions:")
        print("1. Add Formula")
        print("2. View Formula List")
        print("3. View Recorded Formula History")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            while True:
                name = input("Enter formula name: ")
                if not name.strip():
                    print("Error: Formula name is required.")
                elif not re.match("^[a-zA-Z0-9\s-]+$", name):
                    print("Error: Invalid formula name. Only letters, numbers, spaces, and dashes are allowed.")
                else:
                    description = input("Enter formula description: ")
                    manager.add_formula(name, description)
                    break

        elif choice == "2":
            manager.view_formula()

        elif choice == "3":
            while True:
                formula_name = input("Enter formula name to view its history: ")
                if not formula_name.strip():
                    print("Error: Formula name cannot be empty.")
                else:
                    manager.view_recorded_formula_history(formula_name)
                    break

        elif choice == "4":
            print("Thank you for using eCE lang sa DEs. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if _name_ == "_main_":
    main()

print("Still have questions?")
print('Our team is more than happy to help!. Please send us an email at eCElangsaDEs@batstate-u.edu.ph.')
print()
print()
print('Copyright © 2024, eCElangsaDEs Inc.')
print('Batangas State University-TNEU Alangilan')