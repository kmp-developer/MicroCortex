import streamlit as st

from navbar import render_navbar


# Home Page
def home_page():
    # Set page configuration
    st.set_page_config(page_title="Micro Cortex", layout="wide")

    # Render the navigation bar
    render_navbar()

    # Inject custom CSS for styling
    st.markdown("""
        <style>
            /* Main header styling with enhanced highlighting */
            .main-header {
                font-size: 4.5rem;
                font-weight: 800;
                text-align: center;
                margin-top: 2rem;
                background: linear-gradient(90deg, #1f77b4 0%, #3a97d4 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
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
                line-height: 1.6;
            }

            /* Enhanced action button styling */
            .action-btn {
                display: inline-block;
                padding: 0.85rem 2rem;
                background: linear-gradient(90deg, #1f77b4 0%, #3a97d4 100%);
                color: red;
                font-size: 1.2rem;
                font-weight: 600;
                border-radius: 8px;
                text-decoration: none;
                margin: 0 1rem;
                transition: all 0.3s ease;
                box-shadow: 0 4px 12px rgba(31, 119, 180, 0.3);
            }

            .action-btn:hover {
                background: linear-gradient(90deg, #176399 0%, #2d8bc7 100%);
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(31, 119, 180, 0.4);
            }

            /* Secondary button styling */
            .secondary-btn {
                display: inline-block;
                padding: 0.85rem 2rem;
                background-color: transparent;
                color: #1f77b4;
                font-size: 1.2rem;
                font-weight: 600;
                border: 2px solid #1f77b4;
                border-radius: 8px;
                text-decoration: none;
                margin: 0 1rem;
                transition: all 0.3s ease;
            }

            .secondary-btn:hover {
                background-color: rgba(31, 119, 180, 0.1);
                transform: translateY(-2px);
            }

            /* Container for buttons */
            .button-container {
                text-align: center;
                margin: 2rem 0 3rem 0;
            }

            /* Responsive image styling */
            .hero-image {
                display: block;
                margin: 0 auto;
                max-width: 100%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            }

            /* Full-width container */
            .stApp > header {
                background-color: transparent;
            }

            .main .block-container {
                max-width: 100%;
                padding-top: 1rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 class="main-header">Micro Cortex</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Smart shopping for smart people</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="description">Welcome to Micro Cortex - your intelligent shopping assistant. We help you find the best products with the power of AI and machine learning. Start your smart shopping journey today!</p>',
        unsafe_allow_html=True)

    # Action buttons
    st.markdown("""
        <div class="button-container">
            <a href="/search" class="action-btn" style="color:white" target="_self">Search with AI</a>
            <a href="/about" class="secondary-btn">About Us</a>
        </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    home_page()