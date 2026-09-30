# Week-01-Cybersecurity-Asset-Inventory

## Weekly Mini Project – 01
**Title:** Cybersecurity Asset Inventory System

This project implements a command-line Cybersecurity Asset Inventory System for managing IT assets.

## Features
- Add asset
- Display all assets
- Search by Asset ID or Asset Name
- Update asset
- Delete asset
- Security summary
- JSON-based persistent storage
- Input validation for required fields and IP addresses
- Controlled values for Asset Type, Risk Level and Security Status

## Assignment Fields
Each asset stores:
- Asset ID
- Asset Name
- Asset Type
- IP Address
- Operating System
- Owner/Department
- Risk Level
- Security Status

### Allowed Asset Types
Workstation, Server, Router, Switch, Application

### Allowed Risk Levels
Low, Medium, High, Critical

### Allowed Security Status
Secure, Warning, Vulnerable

## Project Structure

```text
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## Requirements
- Python 3.9 or newer
- No external Python packages are required.

## How to Run

From the repository root:

```bash
python src/asset_inventory.py
```

Then choose an option from the menu.

### Quick demo
1. Run the program.
2. Select `7` to load the assignment sample data.
3. Select `2` to display all assets.
4. Select `3` to search for `A102`.
5. Select `6` to view the security summary.

## Data Storage
Asset records are stored in `data/assets.json`, so data remains available after the program is closed.

## Validation
- Asset ID must be unique.
- Required text fields cannot be empty.
- IP address must be valid IPv4/IPv6.
- Asset Type, Risk Level and Security Status use predefined choices.

## Screenshots
The `screenshots/` folder contains evidence for add, display, search, update, delete, security summary and input validation.

## Assignment Alignment
The implementation follows the fields, classifications, sample records, expected summary counts, and repository structure specified in the Week 1 task document.
