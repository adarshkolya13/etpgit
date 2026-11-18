
import gradio as gr

gr.close_all()

def student_profile(name, age, branch, programming, hobbies, goals):
    return f"""
    🎓 STUDENT PROFILE

    Name: {name}
    Age: {age}
    Branch: {branch}
    Favourite Programming Language: {programming}
    Hobbies: {', '.join(hobbies) if hobbies else 'None selected'}
    Career Goal: {goals}

    Thank you for submitting your profile!
    """

demo = gr.Interface(
    fn=student_profile,

    inputs=[
        gr.Textbox(label="Enter Your Full Name", placeholder="Your name"),

        gr.Slider(
            minimum=17,
            maximum=30,
            step=1,
            label="Select Your Age"
        ),

        gr.Dropdown(
            choices=["CSE", "ISE", "ECE", "EEE", "Mechanical"],
            label="Select Your Branch"
        ),

        gr.Radio(
            choices=["Python", "Java", "C++", "JavaScript"],
            label="Favourite Programming Language"
        ),

        gr.CheckboxGroup(
            choices=["Dancing", "Singing", "Sports", "Reading", "Coding"],
            label="Select Your Hobbies"
        ),

        gr.Textbox(
            label="Future Career Goal",
            placeholder="e.g. Software Developer, Data Scientist..."
        )
    ],

    outputs=gr.Textbox(label="Your Submitted Profile"),

    title="Student Profile Generator 🎓",
    description="Fill in your details to generate your student profile."
)

demo.launch()
