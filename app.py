import streamlit as st  # pyright: ignore[reportMissingImports]
from fruit_manager import *
import sys
import plotly.graph_objects as go
import json


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



st.divider()

# Affichage de l'évolution de la trésorerie
st.header("Évolution de la trésorerie")
try:
    with open("./data/treasury_history.json", "r") as f:
        treasury_history = json.load(f)
except Exception as e:
    st.error(f"Erreur lors du chargement de l'historique de trésorerie : {e}")
    treasury_history = []

if treasury_history:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y=treasury_history,
            x=list(range(1, len(treasury_history) + 1)),
            mode="lines+markers",
            name="Trésorerie",
            line=dict(color="royalblue", width=2),
            marker=dict(size=8),
        )
    )
    fig.update_layout(
        xaxis_title="Période",
        yaxis_title="Montant (€)",
        title="Évolution de la trésorerie",
        template="plotly_white",
    )
    st.plotly_chart(fig, use_container_width=False)
else:
    st.info("Aucune donnée de trésorerie à afficher.")
