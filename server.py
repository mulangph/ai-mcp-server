import json
from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("ERP MCP Server")


# ============================================================
# DATA DIRECTORY
# ============================================================

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename: str):
    """Load JSON data from the data directory."""

    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# ============================================================
# SALES ORDERS
# ============================================================

@mcp.tool()
def get_sales_order(order_id: int) -> str:
    """Get sales order details by order ID."""

    orders = load_json("orders.json")

    for order in orders:

        if order["order_id"] == order_id:
            return json.dumps(order, indent=2)

    return json.dumps({
        "error": "Sales order not found",
        "order_id": order_id
    })


# ============================================================
# STOCK
# ============================================================

@mcp.tool()
def get_stock(product_id: int) -> str:
    """Get inventory information for a product."""

    stock = load_json("stock_quant.json")

    for product in stock:

        if product["product_id"] == product_id:
            return json.dumps(product, indent=2)

    return json.dumps({
        "error": "Product not found",
        "product_id": product_id
    })


# ============================================================
# VENDOR BY ID
# ============================================================

@mcp.tool()
def get_vendor(vendor_id: int) -> str:
    """Get vendor information by vendor ID."""

    vendors = load_json("vendors.json")

    for vendor in vendors:

        if vendor["vendor_id"] == vendor_id:
            return json.dumps(vendor, indent=2)

    return json.dumps({
        "error": "Vendor not found",
        "vendor_id": vendor_id
    })

# ============================================================
# VENDORs
# ============================================================
@mcp.tool()
def get_vendors_information() -> str:
    """Get all vendors information."""

    vendors = load_json("vendors.json")

    return json.dumps(vendors, indent=2)

    

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    mcp.run()