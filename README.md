# Mission Pizza 🍕🤖  
Making OpenAPI Services AI-Agent Ready using MCP

---

## Overview
Mission Pizza is a multi-phase project that transforms traditional OpenAPI pizza APIs into fully functional Model Context Protocol (MCP) servers.  
It demonstrates how AI agents can autonomously interact with these APIs to place orders and coordinate delivery using agent-to-agent communication.

The project showcases:
- Automatic OpenAPI → MCP server generation
- AI agent-driven pizza ordering
- Agent-to-agent coordination with a mock scheduling MCP server

---

## Project Phases

### Phase 1: OpenAPI to MCP Automation
- Parses the OpenAPI specification (`pizza.yaml`)
- Generates MCP-compatible tools for menu retrieval, order placement, and order tracking
- Binds tools to backend logic (mocked for simplicity)

### Phase 2: Pizza Ordering Agent
- Rule-based AI agent that interprets natural language commands
- Decides which MCP tool to invoke
- Places and tracks pizza orders autonomously
- Returns `order_id` and estimated preparation time

### Phase 3: Scheduling / Coordination Agent
- A second agent receives order details from the Ordering Agent
- Coordinates delivery using an external MCP-style scheduling service
- Demonstrates Agent-to-Agent (A2A) communication
- Schedules delivery and returns confirmation

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/Harshvi25/Mission-Pizza.git
cd MissionPizza

**### 2. Install Dependencies**
pip install -r requirements.txt

### 3. Run Phase 1 (MCP Server)
python mcpserver/server.py

### 4. Run Phase 2 & 3 Demo
python mcpserver/ordering_agent.py

## Example Flow

### 1. View Menu
User: "Show me the pizza menu"

### 2. Place Order
User: "Order 2 large Margherita pizzas"

## Technologies Used
Python
OpenAPI 3.0
Model Context Protocol (MCP)
Agent-to-Agent (A2A) communication
Rule-based AI agent logic

## Notes
Backend logic is intentionally lightweight and mocked
Focus is on MCP translation, agent orchestration, and multi-agent workflows
Flow demonstrates end-to-end real-world scenario from menu selection to delivery scheduling

## Author
Harshvi Patel




