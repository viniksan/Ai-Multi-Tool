import streamlit as st
import random


def show_content_generator():

    st.title("✍️ AI Content Generator")

    topic = st.text_input(
        "Enter Topic"
    )

    content_type = st.selectbox(
        "Select Content Type",
        [
            "LinkedIn Post",
            "Project Description",
            "Resume Objective",
            "Blog Introduction"
        ]
    )

    if st.button("Generate Content"):

        if topic:

            linkedin_posts = [
                f"""
🚀 Excited to share my latest work on {topic}!

This project helped me strengthen my problem-solving abilities and gain hands-on experience with modern technologies.

Key Highlights:
• Practical implementation
• Real-world applications
• Enhanced technical skills

Looking forward to exploring more innovative solutions.

#Python #AI #Technology #Learning
""",
                f"""
💡 Recently completed a project focused on {topic}.

Through this experience, I improved my analytical thinking, development skills, and understanding of industry best practices.

Every project is an opportunity to learn, grow, and innovate.

#Programming #Development #AI
"""
            ]

            project_descriptions = [
                f"""
{topic} is a professional application designed to improve efficiency, automate processes, and provide meaningful insights through technology.

The system incorporates modern development practices, user-friendly interfaces, and scalable architecture to deliver reliable performance.
""",
                f"""
The {topic} project was developed to address practical challenges through intelligent automation and data-driven decision-making.

It demonstrates strong technical implementation, clean design principles, and real-world applicability.
"""
            ]

            resume_objectives = [
                f"""
Motivated and detail-oriented professional seeking opportunities to apply knowledge of {topic} while contributing to organizational growth and continuous innovation.
""",
                f"""
Enthusiastic learner with strong interest in {topic}, aiming to leverage technical expertise, problem-solving abilities, and teamwork skills in a challenging environment.
"""
            ]

            blog_intro = [
                f"""
In today's rapidly evolving technological landscape, {topic} has become an important area of innovation and development.

This article explores its significance, applications, and future potential.
""",
                f"""
Understanding {topic} is essential for professionals and students looking to stay competitive in the modern digital world.

Let's explore the key concepts and benefits.
"""
            ]

            if content_type == "LinkedIn Post":
                output = random.choice(linkedin_posts)

            elif content_type == "Project Description":
                output = random.choice(project_descriptions)

            elif content_type == "Resume Objective":
                output = random.choice(resume_objectives)

            else:
                output = random.choice(blog_intro)

            st.subheader("Generated Content")

            st.text_area(
                "",
                output,
                height=300
            )

        else:

            st.warning(
                "Please enter a topic."
            )