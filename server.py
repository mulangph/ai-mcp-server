"""
ERP MCP Server

Exposes mock ERP data (sales orders, stock and vendors) as tools over the
Model Context Protocol, so any MCP client can discover and call them.

Run:
    uv run server.py
The server listens on http://127.0.0.1:8000/mcp by default.
"""

import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "ERP MCP Server",
    host=os.getenv("MCP_HOST", "127.0.0.1"),
    port=int(os.getenv("MCP_PORT", "8000")),
)

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename: str):
    """Load a JSON file from the data directory."""
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def not_found(message: str, **details) -> str:
    return json.dumps({"error": message, **details})


# ============================================================
# SALES ORDERS
# ============================================================

@mcp.tool()
def get_sales_order(order_id: int) -> str:
    """Get a sales order by its numeric ID (for example 12345).

    Returns customer, status, order date, currency, total amount and line items.
    """
    for order in load_json("orders.json"):
        if order["order_id"] == order_id:
            return json.dumps(order, indent=2)
    return not_found("Sales order not found", order_id=order_id)


# ============================================================
# STOCK
# ============================================================

@mcp.tool()
def get_stock(product_id: int) -> str:
    """Get inventory for a product by its numeric ID (for example 501).

    Returns on-hand, reserved and available quantities, the warehouse,
    and reorder settings including whether a reorder is needed.
    """
    for product in load_json("stock_quant.json"):
        if product["product_id"] == product_id:
            return json.dumps(product, indent=2)
    return not_found("Product not found", product_id=product_id)


# ============================================================
# VENDORS
# ============================================================

@mcp.tool()
def get_vendor(vendor_id: int) -> str:
    """Get one vendor by its numeric ID (for example 2001).

    Returns status, country, contact details, payment terms, rating
    and the products the vendor supplies.
    """
    for vendor in load_json("vendors.json"):
        if vendor["vendor_id"] == vendor_id:
            return json.dumps(vendor, indent=2)
    return not_found("Vendor not found", vendor_id=vendor_id)


@mcp.tool()
def get_vendors_information() -> str:
    """List every vendor. Use this to compare vendors or when no vendor ID is given."""
    return json.dumps(load_json("vendors.json"), indent=2)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
