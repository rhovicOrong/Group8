
import streamlit as st
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

            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if name not in self.formula_records:
                self.formula_records[name] = {}
            self.formula_records[name][date_str] = description

            return f"Formula '{name}' added to the list."
        except ValueError as e:
            return str(e)

    def view_formula(self):
        if not self.formula:
            return "No formulas added yet."
        formula_list = "\n".join([f"{name}: {description}" for name, description in self.formula.items()])
        return formula_list

    def view_recorded_formula_history(self, formula_name):
        if formula_name in self.formula_records:
            history = "\n".join(
                [f"{date}: {description}" for date, description in self.formula_records[formula_name].items()]
            )
            return f"Formula History for '{formula_name}':\n{history}"
        else:
            return f"No recorded history for the formula '{formula_name}'."

# Streamlit App
st.title("eCE lang sa DEs: Your Trusted Formula Compiler")

st.markdown("""
Welcome to **eCE lang sa DEs!**

eCE lang sa DEs is a sophisticated and user-centric equipment formula compiler designed to be your reliable partner in solving problems in **Differential Equations**.

---

### Objectives:
- User-friendly Interface
- Formula Compiling
- Reliability and Partnership

How can we help you today?
""")

manager = FormulaManager()

# Add Formula
st.header("1. Add Formula")
with st.form("add_formula_form"):
    name = st.text_input("Enter formula name")
    description = st.text_area("Enter formula description")
    add_button = st.form_submit_button("Add Formula")

    if add_button:
        message = manager.add_formula(name, description)
        st.success(message) if "added" in message else st.error(message)

# View Formula List
st.header("2. View Formula List")
if st.button("Show Formulas"):
    formulas = manager.view_formula()
    st.text_area("Formula List", formulas, height=200)

# View Recorded Formula History
st.header("3. View Recorded Formula History")
history_name = st.text_input("Enter formula name to view its history")
if st.button("View History"):
    history = manager.view_recorded_formula_history(history_name)
    st.text_area("Formula History", history, height=200)

# Footer
st.markdown("""
---
Still have questions?  
Our team is more than happy to help! Please send us an email at **eCElangsaDEs@batstate-u.edu.ph**.

---

**Copyright © 2024, eCElangsaDEs Inc.**  
Batangas State University-TNEU Alangilan
""")