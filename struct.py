class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

def main():
    s1 = Student("Rahul", 101, 87.5)
    print(f"Name: {s1.name}")
    print(f"Roll: {s1.roll}")
    print(f"Marks: {s1.marks:.1f}")

if __name__ == "__main__":
    main()
