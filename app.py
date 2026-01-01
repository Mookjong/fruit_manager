import streamlit as st
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
    
    
