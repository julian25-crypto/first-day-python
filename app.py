import streamlit as st

st.set_page_config(page_title="Mini Amazon Demo", layout="wide")

st.title("🛒 Mini Amazon Demo")

# Fake product data
products = [
    {
        "name": "Wireless Headphones",
        "price": 39.99,
        "desc": "Lightweight Bluetooth headphones with 10-hour battery life.",
        "img": "https://via.placeholder.com/150"
    },
    {
        "name": "Smartwatch",
        "price": 59.99,
        "desc": "Tracks fitness, heart rate, and sleep.",
        "img": "https://via.placeholder.com/150"
    },
    {
        "name": "Portable Speaker",
        "price": 24.99,
        "desc": "Water-resistant speaker with deep bass.",
        "img": "https://via.placeholder.com/150"
    },
]

# Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Product grid
cols = st.columns(3)

for i, product in enumerate(products):
    with cols[i]:
        st.image(product["img"])
        st.subheader(product["name"])
        st.write(product["desc"])
        st.write(f"**Price: ${product['price']}**")

        if st.button(f"Add to Cart #{i}"):
            st.session_state.cart.append(product)
            st.success("Added to cart!")

st.write("---")

st.subheader("🛍️ Your Cart")

if len(st.session_state.cart) == 0:
    st.info("Your cart is empty.")
else:
    total = 0
    for item in st.session_state.cart:
        st.write(f"- **{item['name']}** — ${item['price']}")
        total += item["price"]

    st.write(f"### 💰 Total: ${total:.2f}")

    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.experimental_rerun()
