#!/usr/bin/env python3
"""
Cybersecurity Asset Inventory System
Weekly Mini Project - 01

A CLI-based CRUD application for managing IT asset security information.
"""

import json
import ipaddress
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "assets.json"

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


def load_assets():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_assets(assets):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4)


def valid_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def prompt_choice(label, choices):
    while True:
        print(f"\n{label}")
        for i, item in enumerate(choices, 1):
            print(f"{i}. {item}")
        choice = input("Enter choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(choices):
            return choices[int(choice) - 1]
        print("Invalid choice. Please select a valid option.")


def prompt_ip():
    while True:
        value = input("IP Address: ").strip()
        if valid_ip(value):
            return value
        print("Invalid IP address. Please try again.")


def prompt_required(label, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        value = input(f"{label}{suffix}: ").strip()
        if not value and default is not None:
            return default
        if value:
            return value
        print(f"{label} cannot be empty.")


def display_asset(asset):
    print("-----------------------------------------")
    print(f"Asset ID : {asset['asset_id']}")
    print(f"Asset Name : {asset['asset_name']}")
    print(f"Asset Type : {asset['asset_type']}")
    print(f"IP Address : {asset['ip_address']}")
    print(f"OS : {asset['operating_system']}")
    print(f"Department : {asset['department']}")
    print(f"Risk Level : {asset['risk_level']}")
    print(f"Status : {asset['security_status']}")


def add_asset(assets):
    print("\n=== ADD ASSET ===")
    asset_id = prompt_required("Asset ID")
    if any(a["asset_id"].lower() == asset_id.lower() for a in assets):
        print("Error: Asset ID already exists.")
        return

    asset = {
        "asset_id": asset_id,
        "asset_name": prompt_required("Asset Name"),
        "asset_type": prompt_choice("Asset Type", ASSET_TYPES),
        "ip_address": prompt_ip(),
        "operating_system": prompt_required("Operating System"),
        "department": prompt_required("Owner/Department"),
        "risk_level": prompt_choice("Risk Level", RISK_LEVELS),
        "security_status": prompt_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print("Asset added successfully.")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets found.")
        print("=========================================")
        return
    for asset in assets:
        display_asset(asset)
    print("=========================================")
    print(f"Total Assets : {len(assets)}")
    print(f"Critical Assets : {sum(a['risk_level'] == 'Critical' for a in assets)}")
    print(f"High Risk Assets : {sum(a['risk_level'] == 'High' for a in assets)}")
    print(f"Medium Risk Assets : {sum(a['risk_level'] == 'Medium' for a in assets)}")
    print(f"Vulnerable Assets : {sum(a['security_status'] == 'Vulnerable' for a in assets)}")
    print("=========================================")


def search_asset(assets):
    print("\n=== SEARCH ASSET ===")
    query = input("Enter Asset ID or Asset Name: ").strip().lower()
    matches = [
        a for a in assets
        if query in a["asset_id"].lower() or query in a["asset_name"].lower()
    ]
    if not matches:
        print("No matching asset found.")
        return
    for asset in matches:
        display_asset(asset)


def update_asset(assets):
    print("\n=== UPDATE ASSET ===")
    asset_id = input("Enter Asset ID to update: ").strip()
    asset = next((a for a in assets if a["asset_id"].lower() == asset_id.lower()), None)
    if not asset:
        print("Asset not found.")
        return

    print("Press Enter to keep the current value.")
    asset["asset_name"] = prompt_required("Asset Name", asset["asset_name"])
    asset["asset_type"] = prompt_choice("Asset Type", ASSET_TYPES)
    asset["ip_address"] = prompt_ip()
    asset["operating_system"] = prompt_required("Operating System", asset["operating_system"])
    asset["department"] = prompt_required("Owner/Department", asset["department"])
    asset["risk_level"] = prompt_choice("Risk Level", RISK_LEVELS)
    asset["security_status"] = prompt_choice("Security Status", SECURITY_STATUSES)
    save_assets(assets)
    print("Asset updated successfully.")


def delete_asset(assets):
    print("\n=== DELETE ASSET ===")
    asset_id = input("Enter Asset ID to delete: ").strip()
    index = next((i for i, a in enumerate(assets)
                  if a["asset_id"].lower() == asset_id.lower()), None)
    if index is None:
        print("Asset not found.")
        return
    removed = assets.pop(index)
    save_assets(assets)
    print(f"Asset {removed['asset_id']} deleted successfully.")


def show_security_summary(assets):
    print("\n=== SECURITY SUMMARY ===")
    if not assets:
        print("No assets available.")
        return
    for level in RISK_LEVELS:
        print(f"{level}: {sum(a['risk_level'] == level for a in assets)}")
    print("\nSecurity Status:")
    for status in SECURITY_STATUSES:
        print(f"{status}: {sum(a['security_status'] == status for a in assets)}")


def seed_sample_data(assets):
    """Load the three assets described in the assignment sample."""
    sample = [
        {
            "asset_id": "A101",
            "asset_name": "HR-PC-01",
            "asset_type": "Workstation",
            "ip_address": "192.168.1.10",
            "operating_system": "Windows 11",
            "department": "HR",
            "risk_level": "Medium",
            "security_status": "Secure",
        },
        {
            "asset_id": "A102",
            "asset_name": "Web-Server",
            "asset_type": "Server",
            "ip_address": "192.168.1.20",
            "operating_system": "Ubuntu",
            "department": "IT",
            "risk_level": "Critical",
            "security_status": "Vulnerable",
        },
        {
            "asset_id": "A103",
            "asset_name": "Core-Router",
            "asset_type": "Router",
            "ip_address": "192.168.1.1",
            "operating_system": "Cisco IOS",
            "department": "Network",
            "risk_level": "High",
            "security_status": "Warning",
        },
    ]
    if not assets:
        assets.extend(sample)
        save_assets(assets)
        print("Sample assets loaded successfully.")
    else:
        print("Data file already contains assets; sample data was not added.")


def menu():
    assets = load_assets()
    while True:
        print("\n=========================================")
        print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("=========================================")
        print("1. Add Asset")
        print("2. Display Assets")
        print("3. Search Asset")
        print("4. Update Asset")
        print("5. Delete Asset")
        print("6. Security Summary")
        print("7. Load Sample Data")
        print("8. Exit")
        print("=========================================")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            show_security_summary(assets)
        elif choice == "7":
            seed_sample_data(assets)
        elif choice == "8":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please enter 1-8.")


if __name__ == "__main__":
    menu()
