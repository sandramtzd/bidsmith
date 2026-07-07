# BidSmith: Secure Multi-Agent Orchestration for Technical Engineering Tenders

## Bridging the gap between specialised engineering data and agentic workflows using ADK, Model Context Protocol (MCP), and Zero-Trust anti-hallucination guardrails.

* **Track:** Agents for Business
* **Project Repository:** [Insert Your GitHub Link Here]
* **Video Demonstration:** [Insert Your YouTube Link Here]

---

## 1. Executive Summary & Core Value Proposition
In highly specialised engineering sectors—such as oil, gas, and structural modelling—the traditional process of responding to Requests for Proposals (RFPs) and compiling tenders is slow, labor-intensive, and prone to risk. Engineering firms must evaluate client requests against mountains of internal compliance rules, historic bidding datasets, and exact safety tolerances. 

While generic Large Language Models (LLMs) promise to accelerate text drafting, they present two fatal flaws for enterprise engineering environments:
1. **Data Exfiltration Risks:** Uploading proprietary engineering tolerances or client project specs to public cloud LLMs breaches strict data governance and corporate cybersecurity policies.
2. **The Hallucination Liability:** Standard AI models confidently speculate when missing factual data. In engineering, a hallucinated pressure threshold or a wrong material recommendation can lead to catastrophic hardware failure, structural damage, or severe legal penalties.

**BidSmith** is an intelligent, multi-agent AI system designed to automate tender analysis and bid compilation safely. Built during the *5-Day AI Agents: Intensive Vibe Coding Course with Google*, BidSmith utilises a secure, local **Model Context Protocol (MCP)** framework coupled with intent-driven **Agent Skills** to ensure that an AI system never hallucinates outside its designated boundary. It offers corporate teams a scalable "company-specific knowledge environment" that cuts administrative bidding times from days to seconds while enforcing zero-trust data safety.

---

## 2. Problem Statement & Deep Dive
Specialised engineering operations (like those at oil & gas companies) receive highly detailed technical bids daily. A typical proposal requires verifying whether the company's existing methodologies and materials can safely fulfill the client's environmental parameters (e.g., fluid dynamics, pressure limits, chemical exposures).

**Traditional Workflow Pain Points:**

> **Path A:** [Client RFP] ──> [Manual Search Across Internal Manuals] ──> [Human Compliance Drift Risk] ──> **[Delayed Bid]**
>
> *OR*
>
> **Path B:** [Client RFP] ──> [Public AI Tool (Data Leakage)] ──> [Hallucinated Specifications] ──> **[Catastrophic Liability]**

When engineers turn to generic chatbots to assist in bid drafting, they encounter severe limitations. A generic model does not natively possess a firm's unique historical parameters. If forced to answer, it creates plausible-sounding but technically incorrect data.

To bridge this gap securely, an engineering firm needs an environment where:
* **Data Isolation:** Internal guidelines remain isolated from global AI training sets.
* **Anti-Hallucination Gating:** The system actively refuses to generate a proposal if the baseline safety parameters are completely missing from internal records.
* **Multi-Step Routing:** Autonomous execution handles multi-step routing (e.g., verifying technical feasibility separately from looking up senior consultant hourly rates).

---

## 3. Agentic Architecture & Solution Design
BidSmith moves beyond static prompts by implementing a modular, multi-agent architecture built upon the **Agent Development Kit (ADK)** pattern taught throughout the course.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21894605%2Fcd53856d5db4b94103fa1f356bab096a%2Fmermaid-diagram-2026-07-06-193658.png?generation=1783363233587119&alt=media)

The system splits cognitive workloads into discrete components:

### A. Lead Orchestrator Agent (ADK Framework)
The master controller accepts raw text inputs from an engineering RFP. Rather than processing the entire text monolithically, it acts as a router. It extracts technical engineering thresholds and separate commercial dependencies, passing them downstream to specialised agents.

### B. Secure Model Context Protocol (MCP) Server Link
To maintain zero-trust principles, BidSmith connects the open LLM logic to machine-readable local knowledge structures using the core principles of an MCP Server. The data resides entirely inside a protected corporate directory (`internal_knowledge/`), functioning as an isolated grounding boundary. The model queries this engine strictly as an external utility tool, ensuring company data is never hardcoded or leaked into external weights.

### C. Technical Compliance Agent
This specialised agent ingests the specific engineering tolerances from the Orchestrator, utilizes the MCP data link to scan historical safety metrics (such as the `SKILL.md` context parameters), and identifies dependencies (e.g., mapping required operating pressures against mandatory metallurgical steel grades).

### D. Hardened Security Guardrails
The final layer before response generation is a strict programmatic safety gate. If an input query relates to an asset or environment completely unmapped within the secure internal knowledge base, the guardrail intercepts execution, suppresses the LLM's natural inclination to invent data, and triggers a structured warning state.

---

## 4. Technical Implementation & Course Concept Mapping
The implementation of BidSmith explicitly demonstrates the application of the key architectural concepts learned over the 5-day intensive curriculum:

| Course Concept | Practical Demonstration in BidSmith | Target Code/Video Asset |
| :--- | :--- | :--- |
| **Agent / Multi-Agent System (ADK)** | Orchestrator architecture handling decoupled processing pipelines via clear structural code routing. | `app/agent.py` |
| **MCP Server Concepts** | Connecting localised text datasets securely to the agent context without public exposures. | `internal_knowledge/` directory queries |
| **Security Features** | Zero-trust token/credential policy design and automated execution blocks for missing domain knowledge. | Code Execution Pipeline & Hardened System Prompts |
| **Agent Skills Context** | Dynamic utilisation of markdown-driven target profiles (`SKILL.md`) to prevent context rot. | Grounding Pipeline execution |
| **Google Antigravity IDE** | Rapid design optimisation utilising test-driven development hooks and terminal output tracing. | Featured heavily throughout the Video Demo |

### Sample Code Traceability (No-Leak Policy)
As mandated by enterprise coding best practices and hackathon criteria, the system relies on absolute structural hygiene. No production API keys, master passwords, or hardcoded sensitive environments exist inside the public-facing codebase:

```python
# Extract from app/agent.py illustrating the security-gated verification loop
def verify_compliance(mcp_context, client_parameter):
    # Security Guardrail: Anti-Hallucination trigger
    if mcp_context == "NOT_FOUND" or not mcp_context:
        return "🛑 CRITICAL COMPLIANCE FAILURE: Target parameter missing from local registry. Speculation blocked."
    
    # Context-driven safe translation
    return f"✅ Verified Context: {mcp_context}"
```
---

## 5. Repository Structure

```text
bidsmith/
├── internal_knowledge/
│   └── SKILL.md             # Secure grounding context for pipeline specs
├── app/
│   └── agent.py             # Multi-agent routing core and compliance logic
├── pyproject.toml           # Project dependencies & configurations
└── README.md                # System documentation
```

---

## 6. Installation & Execution Guide

Follow these steps to run and verify the BidSmith workspace environment locally from your terminal.

### Step 1: Clone the Repository

```
git clone [Insert Your GitHub Link Here]
cd bidsmith
```

### Step 2: Execute Verification Scenarios

Run the main script wrapper to evaluate both compliance execution flows:

```
python app/agent.py

```
This runs Scenario A (Valid parameters) to output a verified proposal, followed immediately by Scenario B (Undocumented parameters) to trigger the deterministic safety intercept gates.

---

## 7. The Project Journey: From Managing Teams to Orchestrating Agents

The inspiration for BidSmith began during an interview conversation with a Commercial Director at an oil and gas firm. They articulated a critical operational necessity: the team needed to connect internal engineering systems with AI to streamline documentation workflows, yet copying proprietary data into standard cloud applications meant exposing high-value corporate assets to Silicon Valley companies.

Determined to solve this enterprise privacy dilemma, I have been looking for options since then. However, at the time, I couldn't figure a real-world solution. I joined Kaggle’s Intensive Course to explore how agentic design could bridge the gap. Coming from a background of managing human teams, the shift to the modular Agent Development Kit (ADK) felt intuitive. The core principles are identical: instead of assigning tasks to human specialists, I am now routing objectives to specialised digital agents.

Utilising the Google Antigravity IDE during this intensive window allowed me to translate my leadership experience into technical design. The journey proved that the next generation of leadership isn't just about managing people; it is about acting as an AI Systems Architect, structuring secure context parameters, setting operational guardrails, and managing networks of autonomous agents to safely optimise complex industry workflows.

---

## 8. Business Value & User Experience Impact

BidSmith turns AI from a dangerous corporate liability into a measurable business asset. By enforcing local data validation through an MCP framework, it guarantees:

- 100% Structural Safety Alignment: Bids match certified internal engineering capacities perfectly every single time, removing the risk of dangerous technical compliance failures.

- Drastic Administrative Cost Reductions: Compiling initial complex engineering proposals drops from a multi-day human review loop down to seconds, dramatically accelerating corporate agility.

- Defensive IP Isolation: High-value technical documentation and intellectual property remain protected within the secure perimeter of the firm, fully satisfying data governance mandates across enterprise engineering landscapes.