"""
About page for the Micro Cortex application.
"""
import streamlit as st
import random

from navbar import render_navbar, setup_page


def render():
    """Render the about page."""
    # Page title with animation
    st.markdown(
        """
        <h1 style="text-align: center; margin-bottom: 3rem; color: #4F8BF9;">
            About "Team Micro Cortex"
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Introduction
    st.markdown(
        """
        <div style="max-width: 800px; margin: 0 auto; padding: 1.5rem; background-color: white; 
                border-radius: 12px; box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px; margin-bottom: 3rem;">
            <h2 style="margin-top: 0">Our Mission</h2>
            <p>
                Micro Cortex is a cutting-edge platform dedicated to advancing knowledge through 
                AI-driven search and analytics. Our mission is to make information accessible, 
                organized, and actionable for everyone.
            </p>
            <p>
                Founded in 2025, our team combines expertise in artificial intelligence, data science, 
                and user experience design to create intuitive tools that enhance human understanding 
                and productivity.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Team section title
    st.markdown(
        """
        <h2 style="text-align: center; margin-bottom: 2rem;">Meet Our Team</h2>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-bottom: 3rem;">
            """,
        unsafe_allow_html=True
    )

    # Team members
    col1, col2 = st.columns(2)

    # Team member 2
    with col1:
        st.markdown(
            """
            <div class="profile-card" style="height: 100%; transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-8px)';"
                 onmouseout="this.style.transform='none';">
                <div style="text-align: center;">
                    <div style="border-radius: 50%; overflow: hidden; width: 150px; height: 150px; margin: 0 auto;">
                        <img src="https://mahabubu-r.web.app/assets/photo-Duil5f5s.jpg" width="150" height="150" 
                             alt="Dr. Eliza Chen" style="object-fit: cover;">
                    </div>
                    <h3 style="margin-top: 1rem;">Mahabubur Rahman</h3>
                    <p style="color: #4F8BF9; font-weight: 500;">Lead Engineer @Micro Cortex</p>
                </div>
                <p style="margin-top: 1rem;">
                <h4>
                Software Engineer | Full Stack Developer | Competitive Programmer | Data Science Practitioner
                </h4>
                </P>
                <p style="margin-top: 1rem;">
                    👋 Hey there! I'm Mahabubur Rahman, a passionate Full Stack Developer who thrives on transforming ideas into reality. Here’s a glimpse of my expertise:
                    </p>
                <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;">
                    <a href="https://www.linkedin.com/in/mahabuburr/" style="color: #4F8BF9;"><i class="fab fa-linkedin"></i> LinkedIn</a>
                    <a href="https://mahabubu-r.web.app/" style="color: #4F8BF9;"><i class="fab fa-dribbble"></i> Portfolio</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    # Team member 2
    with col2:
        st.markdown(
            """
            <div class="profile-card" style="height: 100%; transition: all 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-8px)';"
                 onmouseout="this.style.transform='none';">
                <div style="text-align: center;">
                    <div style="border-radius: 50%; overflow: hidden; width: 150px; height: 150px; margin: 0 auto;">
                        <img src="https://avatars.githubusercontent.com/u/75668297?v=4" width="150" height="150" 
                             alt="Dr. Eliza Chen" style="object-fit: cover;">
                    </div>
                    <h3 style="margin-top: 1rem;">Abu Naser</h3>
                    <p style="color: #4F8BF9; font-weight: 500;">Kotlin Developer | Tech Enthusiast</p>
                </div>
                <h5 style="margin-top: 1rem;">
                Self-Taught Kotlin Multiplatform Developer Crafting Apps for Android, iOS, Web, and Beyond
                </p>
                <p style="margin-top: 1rem;">
                    My name is Abu Naser and I am a Kotlin Android Developer with a passion for creating beautiful, intuitive user interfaces. I specialize in using Jetpack Compose to create modern, responsive Android applications.                </p>
                <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;">
                    <a href="https://www.linkedin.com/in/abu-naser-bd" style="color: #4F8BF9;"><i class="fab fa-linkedin"></i> LinkedIn</a>
                    <a href="https://naser09.github.io" style="color: #4F8BF9;"><i class="fab fa-web"></i> Portfolio</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )



    # Close team section
    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )

    # Values section with animation
    with st.expander("Our Values", expanded=False):
        cols = st.columns(3)

        values = [
            {
                "icon": "🔍",
                "title": "Curiosity",
                "description": "We believe in asking questions and challenging assumptions to drive innovation."
            },
            {
                "icon": "🤝",
                "title": "Collaboration",
                "description": "We work together across disciplines to create holistic solutions."
            },
            {
                "icon": "🛡️",
                "title": "Integrity",
                "description": "We prioritize ethical AI development and transparent practices."
            }
        ]

        for i, value in enumerate(values):
            with cols[i]:
                st.markdown(
                    f"""
                        <div style="text-align: center; padding: 1rem; transition: all 0.3s ease;"
                             onmouseover="this.style.transform='scale(1.05)';"
                             onmouseout="this.style.transform='none';">
                            <div style="font-size: 3rem; margin-bottom: 0.5rem;">{value['icon']}</div>
                            <h3>{value['title']}</h3>
                            <p>{value['description']}</p>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

    # Contact section
    st.markdown(
        """
        <div style="max-width: 600px; margin: 3rem auto; padding: 1.5rem; background-color: white; 
                border-radius: 12px; box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px; text-align: center;">
            <h2>Get in Touch</h2>
            <p>Interested in learning more about Micro Cortex? We'd love to hear from you!</p>
            <p><strong>Email:</strong> md.naser09@gmail.com</p>
            <p><strong>Location:</strong> Dhaka, Bangladesh.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

setup_page("About us")
render_navbar()
render()