# Test Cases – Cybersecurity Asset Inventory System

| TC ID | Test Case | Input / Action | Expected Result |
|---|---|---|---|
| TC01 | Add valid asset | Enter all required fields with valid values | Asset is added and saved |
| TC02 | Duplicate Asset ID | Add an existing Asset ID | System rejects duplicate ID |
| TC03 | Invalid IP | Enter `999.999.1.1` | System asks for a valid IP |
| TC04 | Display assets | Select Display Assets | All stored assets are shown |
| TC05 | Search existing asset | Search `A102` | A102 details are displayed |
| TC06 | Search by name | Search `Web-Server` | Matching asset is displayed |
| TC07 | Search missing asset | Search `A999` | No matching asset message |
| TC08 | Update asset | Update A102 details | Asset is updated and saved |
| TC09 | Update missing asset | Update A999 | Asset not found message |
| TC10 | Delete asset | Delete A103 | A103 is removed |
| TC11 | Delete missing asset | Delete A999 | Asset not found message |
| TC12 | Risk summary | Select Security Summary | Low/Medium/High/Critical counts are displayed |
| TC13 | Status summary | Select Security Summary | Secure/Warning/Vulnerable counts are displayed |
| TC14 | Invalid menu option | Enter `9` | Invalid menu choice message |
| TC15 | Sample data | Select Load Sample Data on empty database | Three assignment sample assets are loaded |
