# LLM Agent Security - Research Log

## Standing Instructions
- Continuously collect recent papers related to LLM agents with a focus on security.
- Provide Jiayi with a digest every 2-3 days summarizing noteworthy findings, trends, and actionable takeaways.

## Tracking
- **Last digest sent:** 2026-02-17
- **Next digest due:** 2026-02-19 (target)

## Candidate Sources
- arXiv (cs.CR, cs.AI, stat.ML)
- Major lab/security blogs (e.g., OpenAI, DeepMind, Anthropic, Meta FAIR, MSR, Google, Mandiant, Trail of Bits)

_Future expansion (on hold until requested): alignment newsletters, community forums, broader conference monitoring._

## Notes
- Use this file to log collected papers, key points, and pending follow-ups.

### 2026-02-14 Sweep
1. **MalTool: Malicious Tool Attacks on LLM Agents** (arXiv:2602.12194, 2026-02-12)
   - *Why it matters*: First systematic taxonomy + generation pipeline for embedding malicious behaviors inside tools that LLM agents call. Demonstrates existing detectors fail on tool-level payloads. Action item: evaluate current tool vetting vs their threat model.
2. **DeepSight: An All-in-One LM Safety Toolkit** (arXiv:2602.12092, 2026-02-12)
   - *Why it matters*: Integrated eval/diagnosis stack for LM safety, including frontier-risk scenarios. Could be adapted for agent red-teaming pipelines.
3. **Agentic AI for Cybersecurity: A Meta-Cognitive Architecture for Governable Autonomy** (arXiv:2602.11897, 2026-02-12)
   - *Why it matters*: Proposes governance layer (meta-cognitive judge) for multi-agent security operations. Relevant for aligning autonomous SOC-style LLM agents with policy constraints.
- Lower priority: CVE text simplification (less agent-specific), LoRA malware Det (edge security, not agent), unless needed for broader context.

### 2026-02-17 Digest Prep
- Compiled digest covering MalTool, DeepSight, and Agentic AI meta-cognitive architecture (see `research/digests/2026-02-17.md`).
- Blocker: Brave Search API key missing in this environment; new sweeps limited to manually curated sources until configured.

### 2026-02-19 Sweep
1. **Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections** (arXiv:2602.15654, 2026-02-17)
   - *Why it matters:* Shows how long-term memory writes in self-evolving agents can be hijacked via indirect prompt injection, yielding persistent “zombie” behavior across sessions.
   - *Takeaways/Actions:* Need memory sanitation + provenance on writes; simulate infection/trigger phases inside our agent sandboxes.
2. **Overthinking Loops in Agents: A Structural Risk via MCP Tools** (arXiv:2602.14798, 2026-02-16)
   - *Why it matters:* Malicious MCP tool servers can induce cyclic tool-call trajectories that waste resources and derail tasks without obvious per-step anomalies.
   - *Takeaways/Actions:* Add structural loop detection in orchestrators; enforce allowlists + behavioral rate limits for newly registered tools.
3. **NEST: Nascent Encoded Steganographic Thoughts** (arXiv:2602.14095, 2026-02-15)
   - *Why it matters:* Demonstrates that advanced models can hide covert chain-of-thought instructions inside innocent-looking text, undermining CoT oversight mechanisms.
   - *Takeaways/Actions:* Incorporate steganography detectors into log review; require dual-channel reasoning (public vs. private) for sensitive agents.
4. **OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage** (arXiv:2602.13477, 2026-02-13)
   - *Why it matters:* Red-teams an orchestrator-style multi-agent system and leaks sensitive data via single indirect prompt injection even with access controls.
   - *Takeaways/Actions:* Review our orchestrator policies—need defense-in-depth across delegation, plus agent-to-agent data minimization + tamper-evident logs.
5. **In-Context Autonomous Network Incident Response: An End-to-End LLM Agent Approach** (arXiv:2602.13156, 2026-02-13)
   - *Why it matters:* Proposes a fully agentic SOC workflow (perception→action in one 14B model) that adapts via in-context loops, raising stakes for guarding autonomous remediation tooling.
   - *Takeaways/Actions:* Benchmark their “hypothesize–simulate–act” loop vs. our incident response automations; evaluate guardrails before adopting similar pipelines.
