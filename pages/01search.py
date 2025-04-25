"""
Search page for the Micro Cortex application.
"""
import random
import streamlit as st
from navbar import render_navbar, setup_page


# Create dummy product data
def get_dummy_products():
    products = []
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]

    product_names = [
        "Smart Watch Pro", "Wireless Earbuds", "Organic Cotton T-shirt",
        "Kitchen Mixer", "Bestselling Novel", "Air Fryer XL", "Bluetooth Speaker",
        "Yoga Mat", "Board Game Collection", "Coffee Maker"
    ]

    descriptions = [
        "Premium quality with extended battery life and health tracking features.",
        "Noise cancelling with superior sound quality and comfortable fit.",
        "Made from 100% organic cotton, breathable and eco-friendly.",
        "Professional grade with multiple attachments for various cooking needs.",
        "Award-winning story that will keep you engaged from start to finish.",
        "Cook healthier meals with less oil and more flavor.",
        "Waterproof design with deep bass and crystal clear audio.",
        "Extra thick for joint protection and superior grip.",
        "Perfect for family game nights with various difficulty levels.",
        "Programmable settings with thermal carafe to keep coffee hot for hours."
    ]

    for i in range(1, 11):
        price = round(random.uniform(9.99, 299.99), 2)
        rating = round(random.uniform(3.0, 5.0), 1)

        products.append({
            "id": i,
            "name": product_names[i - 1],
            "description": descriptions[i - 1],
            "price": price,
            "category": random.choice(categories),
            "rating": rating,
            "image": f"https://picsum.photos/id/{i + 50}/300/200"
        })

    return products


# Suggestions list
SEARCH_SUGGESTIONS = [
    "Smart Watch", "Wireless", "Organic", "Kitchen", "Book",
    "Electronics", "Clothing", "Home", "Toys", "Coffee"
]


def render():
    """Render the search page."""
    render_navbar()

    st.markdown("""
    <style>
    .product-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        background-color: white;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .product-card img {
        object-fit: cover;
        height: 180px;
    }
    .card-action-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 12px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
    }
    .fav-btn {
        background-color: white;
        border: 1px solid #ff4b4b;
        color: #ff4b4b;
        padding: 8px 12px;
        border-radius: 4px;
        cursor: pointer;
        margin-left: 8px;
    }
    .search-container {
        display: flex;
        margin-bottom: 20px;
    }
    .search-input {
        flex-grow: 1;
        margin-right: 10px !important;
    }
    .view-toggle {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 15px;
    }
    .list-view-product {
        display: flex;
        margin-bottom: 20px;
        background-color: white;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    .list-view-product img {
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    .list-view-details {
        padding: 15px;
        flex-grow: 1;
    }
    .list-view-actions {
        display: flex;
        justify-content: flex-start;
        margin-top: 15px;
    }
    .suggestion-tag {
        display: inline-block;
        background-color: #f0f0f0;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 15px;
        cursor: pointer;
        font-size: 0.8em;
    }
    .suggestion-tag:hover {
        background-color: #e0e0e0;
    }
    .suggestions-container {
        margin-bottom: 15px;
    }
    .rating-stars {
        color: #FFD700;
    }
    .price-tag {
        font-size: 1.2em;
        font-weight: bold;
        color: #2E7D32;
    }
    .category-badge {
        background-color: #f0f0f0;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 0.75em;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display header
    st.markdown('<h1>Search Products</h1>', unsafe_allow_html=True)

    # Search input with button in a container
    col1, col2 = st.columns([5, 1])

    with col1:
        search_query = st.text_input("", placeholder="Search for products...", key="search_box",
                                     label_visibility="collapsed")

    with col2:
        search_button = st.button("Search", use_container_width=True)

    # Suggestions based on search query
    if search_query:
        suggestions = [s for s in SEARCH_SUGGESTIONS if search_query.lower() in s.lower()]
        if suggestions:
            st.markdown('<div class="suggestions-container">', unsafe_allow_html=True)
            for suggestion in suggestions[:5]:  # Limit to 5 suggestions
                st.markdown(f'<span class="suggestion-tag">{suggestion}</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Get all products
    products = get_dummy_products()

    # Filter products if search query exists
    if search_query:
        products = [p for p in products if search_query.lower() in p["name"].lower() or
                    search_query.lower() in p["description"].lower() or
                    search_query.lower() in p["category"].lower()]

    # Display results
    st.markdown("<h2>Results</h2>", unsafe_allow_html=True)

    # View toggle (grid/list)
    view_col1, view_col2 = st.columns([6, 1])
    with view_col2:
        view_type = st.radio("View", ["Grid", "List"], horizontal=True, label_visibility="collapsed")

    if not products:
        st.info("No products found matching your search criteria.")
    else:
        if view_type == "Grid":
            # Display products in a grid
            cols = st.columns(3)

            for i, product in enumerate(products):
                with cols[i % 3]:
                    rating_stars = "★" * int(product['rating']) + "☆" * (5 - int(product['rating']))

                    st.markdown(f"""
                        <div class="product-card">
                            <img src="{product['image']}" style="width: 100%; border-radius: 8px;">
                            <span class="category-badge">{product['category']}</span>
                            <h3>{product['name']}</h3>
                            <p>{product['description'][:100]}{"..." if len(product['description']) > 100 else ""}</p>
                            <p class="price-tag">${product['price']:.2f}</p>
                            <p class="rating-stars">{rating_stars} <span style="color: #666;">({product['rating']})</span></p>
                            <div>
                                <button class="card-action-btn">Add to Cart</button>
                                <button class="fav-btn">❤️</button>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            # Display products in a list view
            for product in products:
                rating_stars = "★" * int(product['rating']) + "☆" * (5 - int(product['rating']))

                st.markdown(f"""
                    <div class="list-view-product">
                        <img src="{product['image']}">
                        <div class="list-view-details">
                            <span class="category-badge">{product['category']}</span>
                            <h3>{product['name']}</h3>
                            <p>{product['description']}</p>
                            <p class="price-tag">${product['price']:.2f}</p>
                            <p class="rating-stars">{rating_stars} <span style="color: #666;">({product['rating']})</span></p>
                            <div class="list-view-actions">
                                <button class="card-action-btn">Add to Cart</button>
                                <button class="fav-btn">❤️</button>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)


setup_page("Search with AI")
render()