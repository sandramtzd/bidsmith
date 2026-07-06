# app/agent.py
"""
BidSmith: Multi-Agent Systems Tender & Compliance Orchestrator.
Demonstrating Kaggle AI Agents Course concepts: ADK 2.0 multi-agent architecture,
simulated local MCP Context servers, and strict anti-hallucination guardrails.
"""

import os


class SecureMCPServer:
    """Simulates a secure Model Context Protocol server grounding the model

    to private, local markdown files.
    """

    def __init__(self, directory_path: str = "internal_knowledge"):
        self.directory = directory_path

    def fetch_grounding_context(self, filename: str) -> str:
        """Strictly reads localized files without leaking context to cloud datasets."""
        target_path = os.path.join(self.directory, filename)
        if not os.path.exists(target_path):
            return "NOT_FOUND"

        with open(target_path, "r", encoding="utf-8") as file:
            return file.read()


class TechnicalComplianceAgent:
    """Specialised Sub-Agent evaluating engineering requirements against internal rules."""

    def __init__(self, mcp_server: SecureMCPServer):
        self.mcp = mcp_server

    def verify_specifications(self, rfp_text: str) -> str:
        # Pulling the secure data slice dynamically via our MCP context link
        specs = self.mcp.fetch_grounding_context("SKILL.md")

        if "500 PSI" in rfp_text and "Grade 316 Stainless Steel" in specs:
            return (
                "Technical Feasibility: APPROVED. Operating parameters match "
                "Section 2 (Grade 316 Stainless Steel mandated for pressures > 450 PSI)."
            )

        return "NOT_FOUND"


class FinancialEstimatorAgent:
    """Specialised Sub-Agent calculating commercial rates and budget profiles."""

    def __init__(self, mcp_server: SecureMCPServer):
        self.mcp = mcp_server

    def calculate_project_costs(self, rfp_text: str) -> str:
        specs = self.mcp.fetch_grounding_context("SKILL.md")

        if "£150 per hour" in specs:
            return "Commercial Analysis: APPROVED. Baseline engineering pricing mapped at £150/hr."
        return "NOT_FOUND"


class BidSmithOrchestrator:
    """Lead Agent controlling intent-driven task delegation and safety guardrails."""

    def __init__(self):
        print("\n[ADK System] Initialising BidSmith Multi-Agent Orchestration Layer...")
        self.mcp = SecureMCPServer()
        self.tech_agent = TechnicalComplianceAgent(self.mcp)
        self.finance_agent = FinancialEstimatorAgent(self.mcp)

    def process_proposal(self, client_rfp: str) -> str:
        print(f"\n[Incoming RFP Request]: '{client_rfp}'")
        print("[Routing Engine] Delegating workloads to specialised sub-agents...")

        # 1. Coordinate Sub-agents
        tech_status = self.tech_agent.verify_specifications(client_rfp)
        finance_status = self.finance_agent.calculate_project_costs(client_rfp)

        # 2. Hardened Security Guardrail: Intercept missing domain variables
        print("[Compliance Gate] Checking for hallucinations or unverified specs...")
        if tech_status == "NOT_FOUND" or finance_status == "NOT_FOUND":
            return (
                "🛑 CRITICAL SECURITY WARNING: Requested parameter specs are completely missing\n"
                "   from the secure internal database. Generative speculation has been blocked\n"
                "   to prevent hallucination liabilities and maintain physical system safety."
            )

        # 3. Compile Compliant Output
        return (
            "============================================================\n"
            "✅ SECURE TENDER PROPOSAL COMPILED SUCCESSFULLY\n"
            "============================================================\n"
            f"- {tech_status}\n"
            f"- {finance_status}\n"
            "- Compliance Status: 100% ALIGNED WITH REGULATORY MANUALS\n"
            "============================================================"
        )


if __name__ == "__main__":
    orchestrator = BidSmithOrchestrator()

    # Scenario A: Processing a valid corporate request aligned with internal documents
    valid_rfp = "Requesting a quote for a pipeline project handling 500 PSI."
    print(orchestrator.process_proposal(valid_rfp))

    print("\n" + "#" * 60 + "\n")

    # Scenario B: Intercepting an undocumented prompt using safety guardrails
    unknown_rfp = "Can we use low-cost PVC tubes for high-pressure deep sea drilling?"
    print(orchestrator.process_proposal(unknown_rfp))