class StudentRegistrationAgent:
    
    def register_student(self): 
        print("Student Registration System: Please enter your Name & Student ID.")
        student_input = input("\nStudent: ")
        if "," in student_input:
            name, st_id = map(str.strip, student_input.split(","))
            print(f"\nStudent Registration Agent: Welcome, {name} (ID: {st_id}). Proceeding to course selection.")
            return name, st_id
        else:
            print("\nStudent Registration Agent: Invalid input format. Please try again.")
            return self.register_student()
    
    def course_selection(self):
        courses = {"Data Structures": 300, "Algorithms": 350, "Machine Learning": 400}
        print("\nCourse Selection Agent: Available courses are:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course} - ${courses[course]}")
        
        print("\nPlease type the courses you want to register for, separated by commas.")
        selected_courses = input("Student: ").split(",")
        selected_courses = [course.strip() for course in selected_courses]
        total_cost = sum(courses[course] for course in selected_courses if course in courses)
        
        if total_cost > 0:
            print(f"\nCourse Selection Agent: You have selected {','.join(selected_courses)}. Total cost: ${total_cost}.")
            return total_cost
        else:
            print("\nCourse Selection Agent: No valid courses selected. Please try again.")
            return self.course_selection()
    
    def payment(self, total_cost):
        print(f"\nPayment Agent: The total cost is ${total_cost}.")
        payment_amount = float(input("\nPayment Agent: Please enter your payment amount: "))
        
        if payment_amount >= total_cost:
            print("\nPayment Agent: Payment successful! You are registered.")
            print(f"Your balance is ${payment_amount - total_cost:.2f}.")
        else:
            print("\nPayment Agent: Insufficient payment. Registration failed.")
    
def main():
    print("Student: I want to register for courses.\n")
    agent = StudentRegistrationAgent()    
    name, st_id = agent.register_student()
    total_cost = agent.course_selection()
    agent.payment(total_cost)

if __name__ == "__main__":
    main()
