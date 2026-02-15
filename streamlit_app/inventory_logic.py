def load_inventory_decisions(inventory_df):
    """
    Extract inventory decision metrics from the inventory_decisions.csv file.
    This keeps business logic separate from UI logic.
    """
    return {
        "EOQ": inventory_df["EOQ"].iloc[0],
        "Safety_Stock": inventory_df["Safety_Stock"].iloc[0],
        "Reorder_Point": inventory_df["Reorder_Point"].iloc[0]
    }
