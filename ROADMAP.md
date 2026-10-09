# 90-Day Cybersecurity Portfolio Roadmap

**Goal:** five documented, reproducible security labs on GitHub, and job-ready for SOC Analyst L1 and junior security roles in the UAE within 12 weeks.

**Time budget:** about 10–12 hours a week alongside a full-time job: two weekday evenings (2 hours each) plus one weekend day (6–8 hours).

**Lab machine:** Windows 11 laptop, 16 GB RAM, VirtualBox. Plan the VMs so no more than about 12 GB of guest RAM runs at once:

| VM | RAM | Used in |
|----|-----|---------|
| Ubuntu Server 24.04 (`lab-ubuntu`) | 2 GB | Weeks 1–5, 8–11 |
| Wazuh server (all-in-one) | 6–8 GB | Weeks 3–5 (shut down during the Windows weeks) |
| Windows Server 2022 Evaluation (domain controller) | 4 GB | Weeks 6–7 |
| Windows 10/11 Enterprise Evaluation (client) | 4 GB | Weeks 6–7 |
| Kali Linux | 2–4 GB | Weeks 8–11 |
| Vulnerable target (Metasploitable 2 or DVWA) | 1 GB | Weeks 10–11, host-only network **only** |

**Rule for every week:** a week is complete only when its "Done when" items are true **and** pushed to GitHub with real evidence. Planned work is never described as finished.

---

## Month 1 — Linux foundations and security monitoring

### Week 1 · Lab build, users and permissions
- **Tasks:** build the VirtualBox host-only network and the `lab-ubuntu` VM ([lab-setup.md](https://github.com/sins05/linux-security-hardening-lab/blob/main/docs/lab-setup.md)); run the baseline audit; Exercises 0–2 (users, groups, setgid, SUID hunt). Publish the `linux-security-hardening-lab` repo.
- **Done when:** `reports/before.txt` saved locally; screenshots 00–03 captured; `tests/run-tests.sh` passes on your VM; repo public with status "in progress".

### Week 2 · SSH, firewall and log analysis → Project 1 complete
- **Tasks:** Exercises 3–6 (key-only SSH, UFW, auth-log analysis, updates); write `reports/hardening-report.md`.
- **Done when:** every SSH refusal test, both port tests and the rate-limit test are captured; after-audit shows no unexplained WARN; README "Lab VM results" filled from your own run; profile README marks Project 1 **Completed**.

### Week 3 · Wazuh SIEM installed
- **Tasks:** create `soc-home-lab` repo; install the Wazuh all-in-one server (official OVA or install script); enroll `lab-ubuntu` as an agent; draw the lab architecture diagram.
- **Done when:** the agent shows **Active** in the dashboard; Linux auth events visible; install steps documented so someone else could repeat them.

### Week 4 · Detections and first investigation
- **Tasks:** reproduce SSH brute force against `lab-ubuntu` and find it in Wazuh; enable File Integrity Monitoring on `/etc`; trigger a FIM alert by editing a test file; write **Incident Report #1 (SSH brute force)**.
- **Done when:** report includes timeline, rule IDs, evidence screenshots, severity reasoning and remediation; any custom rule is in the repo and tested.

---

## Month 2 — Windows security and network monitoring

### Week 5 · SOC lab complete → Project 2 complete
- **Tasks:** second scenario (new local user created + added to `sudo`) → **Incident Report #2**; document detection gaps and false positives; finish the README.
- **Done when:** two incident reports, detection rules, limitations section; profile marks Project 2 **Completed**. **Start applying for jobs this week**, 5–10 applications per week from here on.

### Week 6 · Windows Server and Active Directory
- **Tasks:** create `windows-security-lab`; install Windows Server 2022 Evaluation, promote to domain controller (`lab.local`); join a Windows client; create OUs, users and security groups with PowerShell.
- **Done when:** client joined to the domain; `Get-ADUser` / `Get-ADGroupMember` output saved; lab design and isolation explained in the README.

### Week 7 · Group Policy, Event Viewer, failed logons → Project 3 complete
- **Tasks:** GPO for password and account-lockout policy and advanced audit policy; trigger failed logons and a lockout; investigate Event IDs **4625, 4740, 4624, 4720, 4732** in Event Viewer and with `Get-WinEvent`; basic audit (stale accounts, privileged group members).
- **Done when:** lockout investigation report with event evidence; PowerShell audit script tested; profile marks Project 3 **Completed**.

### Week 8 · Packet analysis fundamentals
- **Tasks:** create `network-security-monitoring-lab`; network diagram; capture your own lab traffic in Wireshark: TCP handshake, DNS query/response, HTTP to a local test web server; practise display filters.
- **Done when:** three annotated captures (self-generated, no personal traffic) with filters used and what each shows.

---

## Month 3 — Vulnerability assessment and job readiness

### Week 9 · Suspicious traffic → Project 4 complete
- **Tasks:** from Kali, run an `nmap` scan against `lab-ubuntu` on the host-only network; identify it in Wireshark (SYN pattern, ports); analyse one public training PCAP, chosen from a reputable source and analysed only in Wireshark (never extract or run files from it); write findings, false-positive notes and defensive recommendations.
- **Done when:** 2 investigations written up with PCAP filters and evidence; profile marks Project 4 **Completed**.

### Week 10 · Vulnerability scanning
- **Tasks:** create `vulnerability-assessment-lab`; write **scope and rules of engagement** (target IP, host-only only, dates); deploy Metasploitable 2 or DVWA; scan with Nmap and Greenbone/OpenVAS (or Nessus Essentials); manually verify the top findings.
- **Done when:** raw scan exported; at least 5 findings verified with evidence and a CVSS score each; false positives identified.

### Week 11 · Remediate, retest, report → Project 5 complete
- **Tasks:** fix or mitigate the verified findings; rescan; write the professional vulnerability assessment report (executive summary, findings, risk, remediation, retest results).
- **Done when:** before/after scan comparison; report in `reports/`; profile marks Project 5 **Completed**.

### Week 12 · Portfolio review and interview preparation
- **Tasks:** consistency pass across all five READMEs; pin the five projects; update the CV and LinkedIn using only completed work; build an interview question bank (about 40 questions: networking, Linux, Windows events, SIEM, incident response); rehearse a 3-minute walkthrough of each project; set up an application tracker.
- **Done when:** every README's first screen explains the project to a recruiter; each walkthrough rehearsed aloud; tracker shows applications sent since Week 5 and follow-ups due.

---

## Parallel habits (every week)

- **30 minutes a day** of guided practice, for example TryHackMe's SOC Level 1 path or Blue Team Labs Online free challenges. Note what you learn in the relevant lab repo, not as separate filler repos.
- **One commit per work session**, with clear messages. Steady, honest history is better than a burst before applying.
- **Certification:** keep CCNA study going if it fits. A beginner security certification such as CompTIA Security+ or ISC2 CC can follow once the labs are done. Don't let exam prep crowd out the labs.

## Progress tracker

| Week | Milestone | Status |
|------|-----------|--------|
| 1 | Lab VM + Exercises 0–2 | Not started |
| 2 | Project 1 complete | Not started |
| 3 | Wazuh running, agent active | Not started |
| 4 | Incident Report #1 | Not started |
| 5 | Project 2 complete · applications start | Not started |
| 6 | AD domain built | Not started |
| 7 | Project 3 complete | Not started |
| 8 | Packet analysis captures | Not started |
| 9 | Project 4 complete | Not started |
| 10 | Scans verified | Not started |
| 11 | Project 5 complete | Not started |
| 12 | Portfolio review + interview prep | Not started |
