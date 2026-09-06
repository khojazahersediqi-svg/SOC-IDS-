import json

TACTICS = [
    {"id": "TA0043", "name": "Reconnaissance"},
    {"id": "TA0042", "name": "Resource Development"},
    {"id": "TA0001", "name": "Initial Access"},
    {"id": "TA0002", "name": "Execution"},
    {"id": "TA0003", "name": "Persistence"},
    {"id": "TA0004", "name": "Privilege Escalation"},
    {"id": "TA0005", "name": "Defense Evasion"},
    {"id": "TA0006", "name": "Credential Access"},
    {"id": "TA0007", "name": "Discovery"},
    {"id": "TA0008", "name": "Lateral Movement"},
    {"id": "TA0009", "name": "Collection"},
    {"id": "TA0011", "name": "Command and Control"},
    {"id": "TA0010", "name": "Exfiltration"},
    {"id": "TA0040", "name": "Impact"},
]

TECHNIQUES = [
    # Reconnaissance
    ("T1595", "Active Scanning", "TA0043", "Network, Host"),
    ("T1592", "Gather Victim Host Information", "TA0043", "Network"),
    ("T1589", "Gather Victim Identity Information", "TA0043", "Network"),
    ("T1590", "Gather Victim Network Information", "TA0043", "Network"),
    ("T1598", "Phishing for Information", "TA0043", "Email, Network"),
    ("T1597", "Search Closed Sources", "TA0043", "Network"),
    ("T1596", "Search Open Technical Databases", "TA0043", "Network"),
    ("T1593", "Search Open Websites/Domains", "TA0043", "Network"),

    # Resource Development
    ("T1583", "Acquire Infrastructure", "TA0042", "Network"),
    ("T1586", "Compromise Accounts", "TA0042", "Network"),
    ("T1584", "Compromise Infrastructure", "TA0042", "Network"),
    ("T1587", "Develop Capabilities", "TA0042", "Network"),
    ("T1585", "Establish Accounts", "TA0042", "Network"),
    ("T1588", "Obtain Capabilities", "TA0042", "Network"),
    ("T1608", "Stage Capabilities", "TA0042", "Network"),

    # Initial Access
    ("T1189", "Drive-by Compromise", "TA0001", "Host, Network"),
    ("T1190", "Exploit Public-Facing Application", "TA0001", "Network, Host"),
    ("T1133", "External Remote Services", "TA0001", "Network"),
    ("T1200", "Hardware Additions", "TA0001", "Host"),
    ("T1566", "Phishing", "TA0001", "Email"),
    ("T1091", "Replication Through Removable Media", "TA0001", "Host"),
    ("T1195", "Supply Chain Compromise", "TA0001", "Host, Network"),
    ("T1199", "Trusted Relationship", "TA0001", "Network"),
    ("T1078", "Valid Accounts", "TA0001", "Identity, Network"),

    # Execution
    ("T1059", "Command and Scripting Interpreter", "TA0002", "Host"),
    ("T1609", "Container Administration Command", "TA0002", "Container"),
    ("T1203", "Exploitation for Client Execution", "TA0002", "Host"),
    ("T1559", "Inter-Process Communication", "TA0002", "Host"),
    ("T1106", "Native API", "TA0002", "Host"),
    ("T1053", "Scheduled Task/Job", "TA0002", "Host"),
    ("T1129", "Shared Modules", "TA0002", "Host"),
    ("T1204", "User Execution", "TA0002", "Host, Email"),
    ("T1047", "Windows Management Instrumentation", "TA0002", "Host"),

    # Persistence
    ("T1098", "Account Manipulation", "TA0003", "Identity"),
    ("T1547", "Boot or Logon Autostart Execution", "TA0003", "Host"),
    ("T1037", "Boot or Logon Initialization Scripts", "TA0003", "Host"),
    ("T1176", "Browser Extensions", "TA0003", "Host"),
    ("T1554", "Compromise Client Software Binary", "TA0003", "Host"),
    ("T1136", "Create Account", "TA0003", "Identity, Host"),
    ("T1543", "Create or Modify System Process", "TA0003", "Host"),
    ("T1546", "Event Triggered Execution", "TA0003", "Host"),
    ("T1574", "Hijack Execution Flow", "TA0003", "Host"),

    # Privilege Escalation
    ("T1548", "Abuse Elevation Control Mechanism", "TA0004", "Host"),
    ("T1134", "Access Token Manipulation", "TA0004", "Host"),
    ("T1611", "Escape to Host", "TA0004", "Container"),
    ("T1068", "Exploitation for Privilege Escalation", "TA0004", "Host"),
    ("T1055", "Process Injection", "TA0004", "Host"),
    ("T1053", "Scheduled Task/Job", "TA0004", "Host"),
    ("T1078", "Valid Accounts", "TA0004", "Identity"),

    # Defense Evasion
    ("T1548", "Abuse Elevation Control Mechanism", "TA0005", "Host"),
    ("T1140", "Deobfuscate/Decode Files or Information", "TA0005", "Host"),
    ("T1006", "Direct Volume Access", "TA0005", "Host"),
    ("T1484", "Domain Policy Modification", "TA0005", "Identity"),
    ("T1211", "Exploitation for Defense Evasion", "TA0005", "Host"),
    ("T1222", "File and Directory Permissions Modification", "TA0005", "Host"),
    ("T1562", "Impair Defenses", "TA0005", "Host"),
    ("T1070", "Indicator Removal", "TA0005", "Host"),
    ("T1036", "Masquerading", "TA0005", "Host"),
    ("T1027", "Obfuscated Files or Information", "TA0005", "Host"),
    ("T1620", "Reflective Code Loading", "TA0005", "Host"),

    # Credential Access
    ("T1110", "Brute Force", "TA0006", "Identity, Network"),
    ("T1555", "Credentials from Password Stores", "TA0006", "Host"),
    ("T1212", "Exploitation for Credential Access", "TA0006", "Host"),
    ("T1187", "Forced Authentication", "TA0006", "Network"),
    ("T1606", "Forge Web Credentials", "TA0006", "Identity"),
    ("T1056", "Input Capture", "TA0006", "Host"),
    ("T1557", "Adversary-in-the-Middle", "TA0006", "Network"),
    ("T1003", "OS Credential Dumping", "TA0006", "Host"),
    ("T1558", "Steal or Forge Kerberos Tickets", "TA0006", "Identity"),

    # Discovery
    ("T1087", "Account Discovery", "TA0007", "Identity, Host"),
    ("T1010", "Application Window Discovery", "TA0007", "Host"),
    ("T1217", "Browser Information Discovery", "TA0007", "Host"),
    ("T1482", "Domain Trust Discovery", "TA0007", "Identity"),
    ("T1083", "File and Directory Discovery", "TA0007", "Host"),
    ("T1046", "Network Service Discovery", "TA0007", "Network"),
    ("T1057", "Process Discovery", "TA0007", "Host"),
    ("T1012", "Query Registry", "TA0007", "Host"),
    ("T1518", "Software Discovery", "TA0007", "Host"),
    ("T1082", "System Information Discovery", "TA0007", "Host"),

    # Lateral Movement
    ("T1210", "Exploitation of Remote Services", "TA0008", "Network"),
    ("T1570", "Lateral Tool Transfer", "TA0008", "Network, Host"),
    ("T1534", "Internal Spearphishing", "TA0008", "Email"),
    ("T1021", "Remote Services", "TA0008", "Network"),
    ("T1091", "Replication Through Removable Media", "TA0008", "Host"),
    ("T1080", "Taint Shared Content", "TA0008", "Host"),
    ("T1550", "Use Alternate Authentication Material", "TA0008", "Identity"),

    # Collection
    ("T1560", "Archive Collected Data", "TA0009", "Host"),
    ("T1123", "Audio Capture", "TA0009", "Host"),
    ("T1119", "Automated Collection", "TA0009", "Host"),
    ("T1115", "Clipboard Data", "TA0009", "Host"),
    ("T1213", "Data from Information Repositories", "TA0009", "Network"),
    ("T1005", "Data from Local System", "TA0009", "Host"),
    ("T1114", "Email Collection", "TA0009", "Email"),
    ("T1056", "Input Capture", "TA0009", "Host"),
    ("T1113", "Screen Capture", "TA0009", "Host"),

    # Command and Control
    ("T1071", "Application Layer Protocol", "TA0011", "Network"),
    ("T1092", "Communication Through Removable Media", "TA0011", "Host"),
    ("T1132", "Data Encoding", "TA0011", "Network"),
    ("T1001", "Data Obfuscation", "TA0011", "Network"),
    ("T1568", "Dynamic Resolution", "TA0011", "Network"),
    ("T1573", "Encrypted Channel", "TA0011", "Network"),
    ("T1008", "Fallback Channels", "TA0011", "Network"),
    ("T1105", "Ingress Tool Transfer", "TA0011", "Network, Host"),
    ("T1095", "Non-Application Layer Protocol", "TA0011", "Network"),
    ("T1090", "Proxy", "TA0011", "Network"),

    # Exfiltration
    ("T1020", "Automated Exfiltration", "TA0010", "Network"),
    ("T1030", "Data Transfer Size Limits", "TA0010", "Network"),
    ("T1048", "Exfiltration Over Alternative Protocol", "TA0010", "Network"),
    ("T1041", "Exfiltration Over C2 Channel", "TA0010", "Network"),
    ("T1011", "Exfiltration Over Other Network Medium", "TA0010", "Network"),
    ("T1052", "Exfiltration Over Physical Medium", "TA0010", "Host"),
    ("T1567", "Exfiltration Over Web Service", "TA0010", "Network"),

    # Impact
    ("T1531", "Account Access Removal", "TA0040", "Identity"),
    ("T1485", "Data Destruction", "TA0040", "Host"),
    ("T1486", "Data Encrypted for Impact", "TA0040", "Host"),
    ("T1565", "Data Manipulation", "TA0040", "Host"),
    ("T1491", "Defacement", "TA0040", "Host, Network"),
    ("T1499", "Endpoint Denial of Service", "TA0040", "Network, Host"),
    ("T1495", "Firmware Corruption", "TA0040", "Host"),
    ("T1490", "Inhibit System Recovery", "TA0040", "Host"),
    ("T1498", "Network Denial of Service", "TA0040", "Network"),
    ("T1489", "Service Stop", "TA0040", "Host"),
]

techniques_out = []
for tid, name, tactic_id, data_sources in TECHNIQUES:
    techniques_out.append({
        "technique_id": tid,
        "name": name,
        "tactic_id": tactic_id,
        "data_sources": data_sources,
        "description": f"{name} — see attack.mitre.org/techniques/{tid.replace('.', '/')}/ for full MITRE documentation.",
    })

output = {"tactics": TACTICS, "techniques": techniques_out}

with open("data/attack_data.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Wrote {len(TACTICS)} tactics and {len(techniques_out)} technique entries to data/attack_data.json")


# ================================================================================
# FILE: data/generate_detections.py
# ================================================================================

"""
generate_detections.py

Simulates a SOC's existing detection rule inventory (the kind of list you'd
export from Sentinel/Splunk/QRadar correlation rules) mapped to ATT&CK
technique IDs. This is what the coverage engine uses to compute which
techniques are detected, partially detected, or completely uncovered --
mirroring the real analyst workflow of mapping detections to ATT&CK to
find blind spots (the same idea behind tools like DeTT&CT).

Coverage levels are deliberately uneven and incomplete -- a real
environment never has 100% coverage, and the gaps are the interesting
part of this tool.
"""

import json
import random

random.seed(7)

with open("data/attack_data.json") as f:
    attack_data = json.load(f)

technique_ids = [t["technique_id"] for t in attack_data["techniques"]]
unique_ids = sorted(set(technique_ids))

DETECTION_SOURCES = ["Sentinel Analytics Rule", "Splunk Correlation Search",
                     "QRadar Building Block", "Endpoint EDR Alert", "Custom Sigma Rule"]

detections = []
rule_counter = 1000

# ~55% of unique techniques get at least one detection rule (realistic gap profile)
covered_ids = random.sample(unique_ids, k=int(len(unique_ids) * 0.55))

for tid in covered_ids:
    n_rules = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
    for _ in range(n_rules):
        confidence = random.choice(["High", "Medium", "Low"])
        detections.append({
            "rule_id": f"DR-{rule_counter}",
            "rule_name": f"Detection for {tid}",
            "technique_id": tid,
            "source": random.choice(DETECTION_SOURCES),
            "confidence": confidence,
        })
        rule_counter += 1

with open("data/detections.csv", "w") as f:
    f.write("rule_id,rule_name,technique_id,source,confidence\n")
    for d in detections:
        f.write(f'{d["rule_id"]},"{d["rule_name"]}",{d["technique_id"]},{d["source"]},{d["confidence"]}\n')

print(f"Generated {len(detections)} detection rules covering {len(covered_ids)}/{len(unique_ids)} unique techniques")


# ================================================================================
# FILE: coverage_engine.py
# ================================================================================

"""
coverage_engine.py

Core logic: loads the ATT&CK dataset + detection rule inventory, and
computes coverage status for every technique.

Coverage levels:
  "none"     - no detection rules map to this technique
  "partial"  - 1 rule, or rules with only Low/Medium confidence
  "full"     - 2+ rules with at least one High confidence rule

This mirrors how a real detection-engineering team would triage gaps:
a single low-confidence rule is a start, not full coverage.
"""

import json
import csv
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_attack_data():
    with open(os.path.join(BASE_DIR, "data", "attack_data.json")) as f:
        return json.load(f)


def load_detections():
    path = os.path.join(BASE_DIR, "data", "detections.csv")
    detections = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            detections.append(row)
    return detections


def load_manual_layer():
    """User-added manual annotations (In Progress / Planned / Not Applicable)."""
    path = os.path.join(BASE_DIR, "data", "manual_layer.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_manual_layer(layer):
    path = os.path.join(BASE_DIR, "data", "manual_layer.json")
    with open(path, "w") as f:
        json.dump(layer, f, indent=2)


def _score_technique(rules_for_technique):
    if not rules_for_technique:
        return "none"
    has_high = any(r["confidence"] == "High" for r in rules_for_technique)
    if len(rules_for_technique) >= 2 and has_high:
        return "full"
    return "partial"


def compute_coverage():
    """
    Returns:
      techniques: list of technique dicts, each enriched with
                  coverage, rule_count, rules (list), manual_status
      tactic_summary: dict of tactic_id -> {full, partial, none, total, pct_covered}
      overall_summary: dict with total counts + overall pct
    """
    attack_data = load_attack_data()
    detections = load_detections()
    manual_layer = load_manual_layer()

    rules_by_technique = defaultdict(list)
    for d in detections:
        rules_by_technique[d["technique_id"]].append(d)

    tactic_lookup = {t["id"]: t["name"] for t in attack_data["tactics"]}

    techniques = []
    for t in attack_data["techniques"]:
        tid = t["technique_id"]
        rules = rules_by_technique.get(tid, [])
        coverage = _score_technique(rules)
        techniques.append({
            **t,
            "tactic_name": tactic_lookup.get(t["tactic_id"], "Unknown"),
            "coverage": coverage,
            "rule_count": len(rules),
            "rules": rules,
            "manual_status": manual_layer.get(tid, ""),
        })

    tactic_summary = defaultdict(lambda: {"full": 0, "partial": 0, "none": 0, "total": 0})
    for t in techniques:
        s = tactic_summary[t["tactic_id"]]
        s[t["coverage"]] += 1
        s["total"] += 1

    for tactic_id, s in tactic_summary.items():
        covered = s["full"] + s["partial"]
        s["pct_covered"] = round((covered / s["total"]) * 100, 1) if s["total"] else 0

    total = len(techniques)
    full = sum(1 for t in techniques if t["coverage"] == "full")
    partial = sum(1 for t in techniques if t["coverage"] == "partial")
    none = sum(1 for t in techniques if t["coverage"] == "none")

    overall_summary = {
        "total": total,
        "full": full,
        "partial": partial,
        "none": none,
        "pct_full": round((full / total) * 100, 1) if total else 0,
        "pct_any_coverage": round(((full + partial) / total) * 100, 1) if total else 0,
    }

    return techniques, dict(tactic_summary), overall_summary, tactic_lookup


def get_gap_report():
    """Techniques with no detection coverage, sorted by tactic."""
    techniques, _, _, _ = compute_coverage()
    gaps = [t for t in techniques if t["coverage"] == "none"]
    gaps.sort(key=lambda t: (t["tactic_id"], t["technique_id"]))
    return gaps


# ================================================================================
# FILE: app.py
# ================================================================================

"""
app.py

Flask app for the ATT&CK Detection Coverage Navigator.

Routes:
  /                        matrix view - all tactics/techniques color-coded by coverage
  /technique/<id>          technique detail: rules mapped, description, manual status
  /gap-report              sortable list of uncovered techniques
  /gap-report/export       downloads gap report as CSV
  /api/coverage            JSON summary (overall + per-tactic)
  /api/layer/annotate      POST: set a manual status (In Progress/Planned/Not Applicable) on a technique
"""

import os
import csv
import io
from flask import Flask, render_template, jsonify, request, send_file, abort

from coverage_engine import (
    compute_coverage, get_gap_report, load_manual_layer, save_manual_layer, load_attack_data
)

app = Flask(__name__)

MANUAL_STATUSES = ["", "In Progress", "Planned", "Not Applicable"]


@app.route("/")
def matrix_view():
    techniques, tactic_summary, overall, tactic_lookup = compute_coverage()
    attack_data = load_attack_data()

    # group techniques by tactic, in the canonical tactic order
    by_tactic = {t["id"]: [] for t in attack_data["tactics"]}
    for t in techniques:
        by_tactic.setdefault(t["tactic_id"], []).append(t)
    for tid in by_tactic:
        by_tactic[tid].sort(key=lambda x: x["technique_id"])

    return render_template(
        "matrix.html",
        tactics=attack_data["tactics"],
        by_tactic=by_tactic,
        tactic_summary=tactic_summary,
        overall=overall,
    )


@app.route("/technique/<technique_id>")
def technique_detail(technique_id):
    techniques, _, _, _ = compute_coverage()
    matches = [t for t in techniques if t["technique_id"] == technique_id]
    if not matches:
        abort(404)
    # a technique_id can map to multiple tactics (e.g. T1078 appears in several) -
    # show all tactic contexts for it
    return render_template(
        "technique_detail.html",
        technique_id=technique_id,
        entries=matches,
        manual_statuses=MANUAL_STATUSES,
    )


@app.route("/gap-report")
def gap_report():
    gaps = get_gap_report()
    # group by tactic for readability
    by_tactic = {}
    for g in gaps:
        by_tactic.setdefault(g["tactic_name"], []).append(g)
    return render_template("gap_report.html", by_tactic=by_tactic, total_gaps=len(gaps))


@app.route("/gap-report/export")
def gap_report_export():
    gaps = get_gap_report()
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["technique_id", "name", "tactic", "data_sources", "manual_status"])
    for g in gaps:
        writer.writerow([g["technique_id"], g["name"], g["tactic_name"],
                          g["data_sources"], g["manual_status"]])
    mem = io.BytesIO(buf.getvalue().encode("utf-8"))
    return send_file(mem, mimetype="text/csv", as_attachment=True,
                      download_name="attack_coverage_gap_report.csv")


@app.route("/api/coverage")
def api_coverage():
    _, tactic_summary, overall, tactic_lookup = compute_coverage()
    return jsonify({
        "overall": overall,
        "by_tactic": [
            {"tactic_id": tid, "tactic_name": tactic_lookup[tid], **stats}
            for tid, stats in tactic_summary.items()
        ],
    })


@app.route("/api/layer/annotate", methods=["POST"])
def annotate_technique():
    payload = request.get_json(force=True)
    technique_id = payload.get("technique_id")
    status = payload.get("status", "")

    if status not in MANUAL_STATUSES:
        return jsonify({"error": "invalid status"}), 400

    layer = load_manual_layer()
    if status == "":
        layer.pop(technique_id, None)
    else:
        layer[technique_id] = status
    save_manual_layer(layer)

    return jsonify({"status": "ok", "technique_id": technique_id, "manual_status": status})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060, debug=True)