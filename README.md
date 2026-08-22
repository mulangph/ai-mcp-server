


# ERP MCP Server

A Python-based backend server demonstrating the deployment of custom business tools using the **Model Context Protocol (MCP)**. This project leverages Anthropic's **FastMCP** framework to effortlessly expose standard enterprise data sources (Orders, Inventory, and Vendors) as structured tools for LLM consumption.

For demonstration pursposes, It is designed to read localized mock databases and seamlessly host them over an MCP-compliant transport layer.

---

## 🚀 Key Features

* **FastMCP Integration:** Uses the high-level FastMCP wrapper to automatically generate schemas and expose functions as LLM-callable tools.
* **Granular ERP Modules:** Separate endpoints to pull distinct, isolated datasets for Orders, Inventory quantities, and Vendor metadata.
* **JSON-backed Persistence:** Simulates production database interactions using lightweight, predictable JSON flat files.
* **Robust Error Handling:** Returns well-formed JSON error schemas to gracefully inform LLMs when lookups fail.

---

## 🛠️ Exposed Tools

The server dynamically broadcasts four main developer tools to any connected client:

1. `get_sales_order(order_id: int)`: Fetches precise sales order data including statuses, pricing, and transactional lines.
2. `get_stock(product_id: int)`: Checks inventory tables for real-time stock levels and reorder parameters.
3. `get_vendor(vendor_id: int)`: Looks up explicit business credentials, risk profiles, and payment cycles for a single partner.
4. `get_vendors_information()`: Pulls the comprehensive registry of all active vendors for broad analytical overviews.


## Installation

Add the required dependencies individually using `uv` (this will automatically fetch the latest versions):

```bash
uv add gradio
uv add "mcp[cli]"
uv add openai
```

## To Run The server
uv run mcp run server.py --transport streamable-http