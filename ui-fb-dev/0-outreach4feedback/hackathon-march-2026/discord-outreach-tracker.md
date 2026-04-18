# Hackathon Discord Outreach Tracker

_Apart Research AI Control Hackathon, March 20-22, 2026_
_Goal: Get hackathon participants to build on Luthien as infrastructure_

---

## How to use this doc

1. Work top-down by rank
2. For each target: open the full Discord thread, screenshot it, share with Claude
3. Claude drafts a message based on full context
4. Scott reviews, edits, sends
5. Update status after sending

---

## Outreach targets

| Rank | Person | Thread | Posted | Why they fit | Full context? | Status | Draft angle |
|------|--------|--------|--------|-------------|--------------|--------|-------------|
| 1 | **Preeti** | [Multi-Agent Governance at the Tool Call Boundary](https://discord.com/channels/1029547539424366632/1483901610277998692) | Mar 18 | Her research question is Luthien's thesis: "can we demonstrate that output-level governance misses action-level failures?" Has existing infra (BGT pipeline, 52 experiments), extending to tool call boundary interception. | Yes | **Sent** | See draft below |
| 2 | **Rono (Ranbir)** | [AI Control Hackathon \| Seeking collaborators, ControlScope](https://discord.com/channels/1029547539424366632/1482402091551953077) | Mar 14 | MLE/Tech Lead at eBay building white-box monitoring for ControlArena. His white-box probes + Luthien's black-box interception are complementary. Faiaz already flagged scope as a risk; Luthien handles transcript monitoring + staged response so Rono can focus on the novel activation probe. | Yes | **Sent; replied positively** | "Thanks a ton!" Added multi-step attack + memory/decay control design. |
| 3 | **Archana** | [Novel Control Protocols](https://discord.com/channels/1029547539424366632/1354810697531265137) | Mar 2025 (active: replies Mar 10, 17, 19) | Connected to Tyler from Redwood. 5 specific protocols that each map to Luthien policy patterns. People actively using this thread to find teams for the current hackathon. Engaging here also reaches Igor, Jay, Universa8075. | Yes | **Sent; posted follow-up clarification** | Jay referenced this thread; clarified how protocols map to Luthien policies. |
| 4a | **Jay** | [Replicating the existing control protocols in Linux Arena](https://discord.com/channels/1029547539424366632/1484655714323660954) | Mar 20 | New to AI Control, wants to implement Trusted editing, Trusted feedback, Resampling. keivn c replied wanting to team up. Luthien's policy architecture fits these protocols directly. | Yes | **Active DM convo** | Jay DMed asking about Luthien as live monitor in LinuxArena. Scott replied honestly: haven't used LinuxArena, Luthien is complementary (API-layer real-time vs post-hoc container state). Flagged to Jai for technical backup. |

---

## Draft message: Preeti (#1)

> Hey Preeti, this resonates. We've been working on a related problem at Luthien: an open-source proxy that sits between AI agents and the LLM API, intercepting requests/responses and running them through configurable control policies (monitor, modify, block) with conversation logging.
>
> It might be useful as a starting point for the tool call boundary interception piece, or at least save some plumbing. Feel free to fork it, build on top of it, or just tell us what's missing or broken.
>
> Repo: https://github.com/LuthienResearch/luthien-proxy

---

## Draft message: Rono (#2)

> Hey Ranbir, cool project. Faiaz's point about timeline is real; the full pipeline is a lot for a weekend. We've been building an open-source proxy (Luthien) that handles the transcript/action monitoring and staged policy response pieces. Might let you focus your hackathon time on the activation probe, which is the novel part.
>
> If it's useful: https://github.com/LuthienResearch/luthien-proxy. Happy to answer questions or hear what's missing.

---

## Draft message: Archana (#3)

> Hey Archana, several of these protocols (especially "U picks from T outputs" and "Untrusted plan, trusted implementation") map pretty directly to policy patterns in Luthien, an open-source proxy we've been building. It intercepts agent API calls and runs them through configurable policies before execution.
>
> If anyone working on this for the current hackathon wants to skip the interception plumbing and jump straight to protocol logic, the repo might be a useful starting point: https://github.com/LuthienResearch/luthien-proxy
>
> Happy to help if anything's unclear or broken.

---

## Draft message: Jay - LinuxArena (#4a)

> Hey Jay, Luthien might save you some setup time here. It's an open-source proxy that intercepts agent API calls and runs them through configurable policies. Trusted editing and trusted feedback are close to what the existing policy patterns already do, so you could focus on the protocol logic rather than building the interception layer from scratch.
>
> Repo: https://github.com/LuthienResearch/luthien-proxy. Happy to help if you hit any rough edges.

---

## Deprioritized (don't engage unless time permits)

| Person | Thread | Why deprioritized |
|--------|--------|-------------------|
| SOUHARDA MANDAL | ConstitutionGuard | "Don't steal my idea" tag + "I am also new to this"; likely feels threatened by existing solutions |
| Revathi Prasad | Red Team + Blue Team Collab | Relevant but less specific than top 5 |
| Alfred | Multi-Agent Deliberation Collusion | Interesting but indirect fit |
| Igor Pereverzev | Looking for a team | Strong builder but already replied in Archana's thread; reaching him there |
| Zuzana | Flight recorder / tamper-proof audit | Very aligned but thread is >30d old, likely cold |
| Nico Hill | Steganography detection | Relevant but niche |
| Jay | Prompt injection for better red-teaming | Already messaged Jay in LinuxArena thread; two messages to same person is too much |
| bgsbgsbgs | Consistency-Based Interrogation Protocol | 4 messages in one session is enough; more looks like carpet-bombing |

---

_Last updated: 2026-03-20_
