def student_details(**kwargs):
    print(kwargs['age'])
student_details(name="John", age=20, grade="A")

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_details(name="Amit", role="Developer")