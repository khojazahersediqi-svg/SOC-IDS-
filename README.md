BlueTeam Attack Map

A Defensive Attack Visualization, Detection Mapping, and SOC Investigation Framework

Project Overview

BlueTeam Attack Map is a defensive security project designed to visualize attack behaviors, map them to the MITRE ATT&CK framework, identify relevant data sources, and connect security events to detection and investigation workflows.

The project focuses on the Blue Team perspective:

Attack Behavior → ATT&CK Technique → Data Source → Detection → Alert → Investigation → Response → Mitigation

The goal is to demonstrate how security analysts can use attack intelligence, log data, detection logic, and security controls to understand and investigate suspicious activity.

⸻

Project Objectives

This project aims to:

* Visualize common attack behaviors.
* Map adversary behaviors to MITRE ATT&CK.
* Identify useful security data sources.
* Develop defensive detection logic.
* Demonstrate SIEM-style event correlation.
* Support SOC investigation workflows.
* Identify security control and visibility gaps.
* Connect detection opportunities with mitigation strategies.
* Provide a practical Blue Team learning environment.

⸻

Key Features

Attack Visualization

Visualize an attack across multiple stages and understand how individual behaviors connect together.

MITRE ATT&CK Mapping

Map observed behaviors to relevant:

* Tactics
* Techniques
* Sub-techniques
* Data Sources
* Detection Opportunities
* Mitigations

MITRE ATT&CK provides a common framework for describing adversary behavior and can help defenders connect available data sources with detection opportunities.

Detection Mapping

For each technique, identify:

* What behavior may be observed.
* Which logs can provide evidence.
* What indicators may be suspicious.
* Which detection opportunities are available.
* How a SOC analyst can investigate the activity.

Event Correlation

Connect multiple events to identify patterns that may not be obvious from a single log.

Threat Investigation

Provide a structured investigation workflow for suspicious activity.

Defensive Controls

Document security controls that can reduce risk or improve visibility.

⸻

System Architecture

                    ┌─────────────────────┐
                    │   Attack Scenario   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ MITRE ATT&CK Mapping│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Data Sources     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Detection Logic     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Alert Generation  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SOC Investigation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Response & Mitigation│
                    └─────────────────────┘

⸻

Attack Lifecycle

The project represents attack behavior through a defensive lifecycle:

Reconnaissance
      ↓
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Defense Evasion
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command & Control
      ↓
Exfiltration
      ↓
Impact

The project does not focus only on the attack itself. Each stage is connected to possible visibility, detection, investigation, and mitigation opportunities.

⸻

MITRE ATT&CK Mapping

Each attack behavior can be represented using a structured record:

Technique
├── Technique ID
├── Technique Name
├── Tactic
├── Description
├── Data Sources
├── Detection Opportunities
├── Investigation Steps
└── Mitigations

MITRE ATT&CK can be used to translate observed behaviors into tactics, techniques, and sub-techniques and to connect those behaviors with defensive data and detection opportunities.

⸻

Security Data Sources

The project considers multiple sources of security telemetry:

* Windows Event Logs
* Authentication Logs
* DNS Logs
* Firewall Logs
* Network Traffic
* Endpoint Telemetry
* VPN Logs
* Cloud Logs
* Identity Logs
* Application Logs

The purpose is to demonstrate that effective detection depends on both visibility and context.

⸻

Detection Methodology

The detection process follows:

Collect
   ↓
Normalize
   ↓
Baseline
   ↓
Detect
   ↓
Correlate
   ↓
Investigate
   ↓
Respond
   ↓
Improve

For each detection, the project considers:

* Normal behavior
* Suspicious behavior
* Indicators
* Data sources
* Detection logic
* Correlated events
* Investigation questions
* Response actions
* Mitigation opportunities

⸻

Event Correlation

A single event may not provide enough context.

Example:

Multiple Failed Logins
        +
Successful Login
        +
Unusual Source IP
        +
Unusual Login Time
        +
Sensitive Resource Access
        ↓
   Correlation
        ↓
 Suspicious Activity
        ↓
 SOC Investigation

The project demonstrates how multiple low-confidence events can provide stronger context when analyzed together.

⸻

SOC Investigation Workflow

When an alert is generated, the analyst follows a structured process:

1. Alert Validation

Determine whether the alert represents expected or suspicious activity.

2. Context Gathering

Collect:

* User
* Host
* IP address
* Timestamp
* Authentication activity
* Related processes
* Network activity
* Accessed resources

3. Event Correlation

Search for related events across available data sources.

4. Timeline Analysis

Build a timeline of relevant activity.

5. Scope Assessment

Determine which systems, accounts, and resources may be involved.

6. Response Decision

Determine whether containment or escalation is required.

7. Documentation

Record findings, evidence, actions, and lessons learned.

⸻

Defensive Controls

The project documents defensive controls such as:

* Multi-Factor Authentication
* Least Privilege
* Identity and Access Management
* Network Segmentation
* Endpoint Monitoring
* Security Monitoring
* Data Loss Prevention
* Firewall Controls
* Access Reviews
* Security Awareness
* Backup and Recovery
* Incident Response

⸻

Attack Scenarios

The project uses controlled and synthetic scenarios for educational purposes.

Scenario 01 — Suspicious Authentication

Failed Authentication
        ↓
Successful Authentication
        ↓
Unusual Location
        ↓
Abnormal Behavior
        ↓
Detection
        ↓
Investigation

Scenario 02 — Phishing-Related Activity

Suspicious Message
        ↓
User Interaction
        ↓
Account Activity
        ↓
Authentication Anomaly
        ↓
Detection
        ↓
Investigation

Scenario 03 — Lateral Movement

Compromised Endpoint
        ↓
Internal Discovery
        ↓
Unexpected Authentication
        ↓
Remote Access Activity
        ↓
Detection
        ↓
Investigation

Scenario 04 — Unusual Data Transfer

Sensitive Data Access
        ↓
Large Data Transfer
        ↓
Unusual Destination
        ↓
Monitoring Alert
        ↓
Investigation

⸻

Detection Coverage

The project can track defensive coverage using a simple matrix:

Technique	Data Source	Detection	Investigation	Mitigation	Coverage
Technique A	Authentication	✅	✅	✅	High
Technique B	Endpoint	✅	✅	⚠️	Medium
Technique C	Network	⚠️	✅	✅	Partial

The purpose is not to claim complete ATT&CK coverage, but to identify useful defensive visibility and detection gaps.

⸻

Technology Stack

The project is designed around:

* Python
* JSON
* Git & GitHub
* MITRE ATT&CK
* Log Analysis
* SIEM Concepts
* Network Security
* Security Monitoring
* Threat Detection

Optional visualization components may include:

* Streamlit
* NetworkX
* Plotly
* Pandas

⸻

Project Structure

BlueTeam-Attack-Map/
│
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
│
├── docs/
│   ├── 01-project-overview.md
│   ├── 02-architecture.md
│   ├── 03-attack-lifecycle.md
│   ├── 04-mitre-attack-mapping.md
│   ├── 05-detection-methodology.md
│   ├── 06-log-sources.md
│   ├── 07-investigation-workflow.md
│   ├── 08-mitigation-strategy.md
│   └── 09-future-improvements.md
│
├── data/
│   ├── attack-techniques.json
│   ├── attack-tactics.json
│   ├── detection-rules.json
│   ├── log-sources.json
│   └── mitigations.json
│
├── src/
│   ├── main.py
│   ├── attack_map.py
│   ├── detector.py
│   ├── correlator.py
│   └── utils.py
│
├── detections/
│   ├── authentication/
│   ├── endpoint/
│   ├── network/
│   ├── dns/
│   └── cloud/
│
├── scenarios/
│   ├── phishing.md
│   ├── credential-compromise.md
│   ├── lateral-movement.md
│   └── data-exfiltration.md
│
├── reports/
│   ├── sample-incident-report.md
│   └── detection-coverage.md
│
├── screenshots/
│   ├── attack-map.png
│   ├── dashboard.png
│   ├── detection-alert.png
│   └── investigation.png
│
└── tests/
    ├── test_detector.py
    └── test_correlator.py

⸻

Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/BlueTeam-Attack-Map.git
cd BlueTeam-Attack-Map

Create a virtual environment:

python -m venv .venv

Activate it:

Windows

.venv\Scripts\activate

Linux/macOS

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

⸻

Usage

Run the project:

python src/main.py

If the project includes a Streamlit interface:

streamlit run src/main.py

⸻

Project Screenshots

Attack Map

Detection Dashboard

Detection Alert

Investigation Workflow

⸻

Future Improvements

Planned improvements include:

* Interactive attack-map visualization.
* Additional ATT&CK technique mappings.
* More synthetic security logs.
* Advanced event correlation.
* SIEM integration.
* Automated detection testing.
* Detection coverage scoring.
* Threat-hunting workflows.
* Cloud security telemetry.
* Endpoint telemetry analysis.
* Automated reporting.
* API-based ATT&CK data synchronization.

⸻

Ethical & Security Disclaimer

This project is intended for educational and defensive security purposes.

All attack scenarios should use:

* Synthetic data
* Authorized environments
* Isolated laboratories
* Controlled simulations

Do not use the project to access, test, or compromise systems without explicit authorization.

⸻

References

* MITRE ATT&CK
* MITRE ATT&CK Data Sources
* GitHub Documentation
* Security Monitoring and Detection Engineering References

⸻

Author

Khwaja Zaher 
cybersecurity Expert| IT | Networking | Security Operations

Interested in:

* IT Operations
* Networking
* Security Monitoring
* SOC Operations
* Threat Detection
* Incident Response
* Python
* SIEM
* Blue Team Security

⸻

Project Purpose

This project is part of my practical learning journey in defensive security.

The main goal is to move beyond theory and understand how attack behaviors can be translated into:

Visibility → Detection → Investigation → Response → Improvement

If you find the project useful, consider giving it a ⭐ on GitHub.