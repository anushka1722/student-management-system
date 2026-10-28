
def register_student(name, email, roll_number):
    if not name.strip():
        return "Invalid: Name is required"

    if not email or "@" not in email or "." not in email.split("@")[-1]:
        return "Invalid: Email address"

    if not str(roll_number).strip():
        return "Invalid: Roll number is required"

    return "Student registered successfully"


if __name__ == "__main__":
    print(register_student("Anu Mali", "anu@example.com", "24"))
