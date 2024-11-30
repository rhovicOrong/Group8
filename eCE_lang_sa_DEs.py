import streamlit as st
import re
from datetime import datetime

# Initialize session state for formulas and formula records
if "formulas" not in st.session_state:
    st.session_state["formulas"] = {}
if "formula_records" not in st.session_state:
    st.session_state["formula_records"] = {}

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

class FormulaManager:
    @staticmethod
    def validate_alphanumeric_with_symbols(value, field_name):
        """Validates input to allow letters, numbers, spaces, and common mathematical symbols."""
        if not re.match(r"^[a-zA-Z0-9\s\+\-\*/\^().=]+$", value.strip()):
            raise ValueError(
                f"Error: {field_name} should contain only letters, numbers, spaces, and mathematical symbols (+, -, *, /, ^, (, ))."
            )

    @staticmethod
    def add_formula(name, description):
        """Adds a new formula and stores its history."""
        try:
            if not name.strip():
                raise ValueError("Error: Formula name is required.")
            FormulaManager.validate_alphanumeric_with_symbols(name, "Formula name")

            if not description.strip():
                raise ValueError("Error: Formula description cannot be empty.")
            FormulaManager.validate_alphanumeric_with_symbols(description, "Formula description")

            # Add formula to the main list
            st.session_state["formulas"][name] = description
            st.success(f"Formula '{name}' added successfully.")

            # Record history with a timestamp
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if name not in st.session_state["formula_records"]:
                st.session_state["formula_records"][name] = {}
            st.session_state["formula_records"][name][date_str] = description
        except ValueError as e:
            st.error(str(e))

    @staticmethod
    def view_formulas():
        """Displays the list of formulas."""
        st.subheader("Formula List")
        if st.session_state["formulas"]:
            st.write("-" * 60)
            st.write(f"{'Formula Name':<30}{'Description'}")
            st.write("-" * 60)

            for name, description in st.session_state["formulas"].items():
                st.write(f"{name:<30}| {description}")
        else:
            st.write("No formulas added yet.")

    @staticmethod
    def view_formula_history(formula_name):
        """Displays the history of a specific formula."""
        st.subheader(f"Formula History for '{formula_name}'")
        if formula_name in st.session_state["formula_records"]:
            st.write("-" * 60)
            for date, description in st.session_state["formula_records"][formula_name].items():
                st.write(f"{date:<20}| {description}")
        else:
            st.write("No recorded history for this formula.")


def main():
    option = st.radio(
        "Choose an option:",
        ["Add Formula", "View Formula List", "View Recorded Formula History"]
    )

    if option == "Add Formula":
        name = st.text_input("Enter formula name:", key="add_name")
        description = st.text_area("Enter formula description:", key="add_description")

        if st.button("Add Formula"):
            if name and description:
                FormulaManager.add_formula(name, description)
            else:
                st.error("Both name and description are required.")

    elif option == "View Formula List":
        FormulaManager.view_formulas()

    elif option == "View Recorded Formula History":
        formula_name = st.text_input("Enter formula name to view its history:", key="view_history")
        if st.button("View History"):
            if formula_name:
                FormulaManager.view_formula_history(formula_name)
            else:
                st.error("Please enter a formula name to view its history.")


if __name__ == "__main__":
    main()

# Footer
st.write("### Still have questions?")
st.write("Our team is more than happy to help! Please send us an email at eCElangsaDEs@batstate-u.edu.ph.")
st.write("© 2024, eCElangsaDEs Inc. | Batangas State University-TNEU Alangilan")
