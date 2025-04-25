
# navbar.py
import streamlit as st

def render_navbar():
    st.markdown("""
        <style>
            .top-nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #f0f2f6;
                padding: 10px 20px;
                border-bottom: 1px solid #ddd;
            }
            .top-nav .logo {
                font-size: 24px;
                font-weight: bold;
            }
            .top-nav .nav-links a {
                margin-left: 20px;
                text-decoration: none;
                font-size: 18px;
                color: black;
            }
            .top-nav .nav-links a:hover {
                text-decoration: underline;
            }
        </style>
        <div class="top-nav">
            <div class="logo" href="/">Micro Cortex</div>
            <div class="nav-links">
                <a href="/" target="_self">Home</a>
                <a href="/search" target="_self">Search</a>
                <a href="/about" target="_self">About</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

def setup_page(title="Micro Cortex"):
    # Set page configuration
    st.set_page_config(page_title=title, layout="wide")

    # Inject custom CSS for consistent styling
    st.markdown("""
        <style>
            /* Main header styling */
            .main-header {
                font-size: 4rem;
                font-weight: 700;
                text-align: center;
                margin-top: 2rem;
                color: #1f77b4;
            }

            /* Subheader styling */
            .sub-header {
                font-size: 1.5rem;
                text-align: center;
                color: #555;
                margin-bottom: 2rem;
            }

            /* Description text styling */
            .description {
                font-size: 1.2rem;
                text-align: center;
                max-width: 800px;
                margin: 0 auto 2rem auto;
                color: #333;
            }

            /* Action button styling */
            .action-btn {
                display: inline-block;
                padding: 0.75rem 1.5rem;
                background-color: #1f77b4;
                color: white;
                font-size: 1.2rem;
                border-radius: 5px;
                text-decoration: none;
                margin: 0 1rem;
                transition: background-color 0.3s ease;
            }

            .action-btn:hover {
                background-color: #105a8b;
            }

            /* Container for buttons */
            .button-container {
                text-align: center;
                margin-bottom: 2rem;
            }

            /* Responsive image styling */
            .hero-image {
                display: block;
                margin: 0 auto;
                max-width: 100%;
                height: auto;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
