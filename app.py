import streamlit as st # pyright: ignore[reportMissingImports]
from fruit_manager import *
import sys


inventory = load_inventory("./data/fruit_inventory.json")
pricies = load_price("./data/price.json")
try:
    treasury = load_treasury("./data/treasury.txt")
except FileNotFoundError:
    sys.exit("Exiting due to missing treasury file.")
else:
    display_treasury(treasury)


st.title("Fruit Manager")
st.header("Inventory")
st.table(inventory)


st.sidebar.header("Harvest Fruit")
harvest_fruit_name = st.sidebar.text_input("Fruit Name")
harvest_fruit_quantity = st.sidebar.number_input("Quantity", min_value=1, step=1)
if st.sidebar.button("Harvest"):
    harvest_fruit(inventory, harvest_fruit_name, harvest_fruit_quantity)
    save_inventory("./data/fruit_inventory.json", inventory)
    st.sidebar.success(
        f"Harvested {harvest_fruit_quantity} units of {harvest_fruit_name}."
    )
