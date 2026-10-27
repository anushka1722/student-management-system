
def validate_student_email(email):
    return "@" in email and "." in email.split("@")[-1]


def main():
    email = "student@example.com"

    if validate_student_email(email):
        print("Valid student email")
    else:
        print("Invalid student email")


if __name__ == "__main__":
    main()
