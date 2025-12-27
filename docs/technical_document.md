# Technical Design Document – Mission Pizza 🍕🤖

## 1. Architectural Overview
Mission Pizza is designed as a **three-phase, agent-driven system** that transforms traditional OpenAPI APIs into MCP-compatible tools and demonstrates multi-agent workflows.

**High-level flow:**


Phases are modular and build upon each other, enabling clear separation of responsibilities.

---

## 2. Phase 1: OpenAPI to MCP Automation

### Architectural Choices
- **OpenAPI 3.0 specification** (`pizza.yaml`) serves as the single source of truth.
- All endpoints are automatically converted into **MCP tools** with:
  - Tool name
  - Description
  - Input schema
  - Output schema
- Tools are bound to **backend functions** (mocked).

### Design Assumptions
- Backend uses **in-memory storage** (`ORDERS` dictionary) for simplicity.
- Focus is on **MCP translation and tool accessibility**, not backend complexity.

### Ambiguities Addressed
- API response selection: first defined response in OpenAPI is used.
- Path parameter handling: dynamic paths are normalized for tool names.

---

## 3. Phase 2: Pizza Ordering Agent

### Architectural Choices
- Rule-based AI agent interprets **natural language input**.
- Intents are prioritized:
  1. Track order
  2. Place order
  3. View menu
- Agent calls MCP tools (`get_menu`, `post_order`, `get_order_order_id`) based on intent.

### Design Assumptions
- Natural language inputs are simple, command-like.
- Pizza types and sizes are predefined.
- Quantity is extracted by searching for numeric values in the input.

### Ambiguities Addressed
- Intent conflicts (e.g., “order pizzas”) resolved by **prioritizing ordering over menu retrieval**.
- Order lifecycle management uses **unique UUIDs** for `order_id`.
- Estimated preparation time is fixed (mocked) for simplicity.

---

## 4. Phase 3: Scheduling / Coordination Agent

### Architectural Choices
- A second agent (Scheduling Agent) demonstrates **Agent-to-Agent (A2A) communication**.
- Scheduling Agent receives `order_id` and ETA from Ordering Agent.
- Uses a **mock external MCP server** to schedule delivery.
- Returns delivery confirmation (`delivery_id`, delivery time, status).

### Design Assumptions
- Delivery scheduling is mocked to demonstrate coordination, not real-world time calculation.
- Agents communicate using **structured data exchange**, ensuring extensibility.

### Ambiguities Addressed
- Multi-agent workflow is simplified to a single-step handoff.
- External MCP server behavior is deterministic and predictable for evaluation.

---

## 5. Key Takeaways
- OpenAPI specifications can be automatically transformed into agent-ready MCP servers.
- Multi-agent workflows demonstrate autonomous coordination and task delegation.
- Modular design ensures each phase is testable and reusable.
- The project adheres strictly to PDF requirements and shows end-to-end workflow:
  1. Menu retrieval
  2. Order placement
  3. Delivery scheduling via external MCP

