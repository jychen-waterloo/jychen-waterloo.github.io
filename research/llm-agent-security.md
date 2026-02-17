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
