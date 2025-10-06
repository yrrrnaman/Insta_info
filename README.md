# Insta_info
I'll create a Linux-based Instagram information gathering tool for your authorized penetration test. This type of reconnaissance is commonly used in OSINT (Open Source Intelligence) gathering during legitimate security assessments.

Legal Notice
This tool is for authorized penetration testing only. Ensure you have explicit written permission before testing any Instagram account. Unauthorized use may violate Instagram's Terms of Service and applicable laws. EOF

echo "[+] Setup complete!" echo "[] Tool installed in ~/pentest_tools/ig_recon/" echo "[] Run with: cd ~/pentest_tools/ig_recon && python3 ig_recon.py -u USERNAME"


## How to Use the Tool

1. **Setup**:
   ```bash
   chmod +x ig_recon_setup.sh
   ./ig_recon_setup.sh

2. Run Basic Reconnaissance:
3. ```bash
   cd ~/pentest_tools/ig_recon
   python3 ig_recon.py -u target_username

4. Save Results to File:
5. ```bash
   python3 ig_recon.py -u target_username -o target_recon.json


Checks if Instagram account exists
Gathers public profile information
Retrieves follower/following counts
Collects post statistics
Saves results in structured JSON format
Implements rate limiting controls
Important Legal Notice
⚠️ AUTHORIZED PENETRATION TESTING ONLY

This tool is strictly for authorized security testing of Instagram accounts. Before using this tool:

Ensure you have EXPLICIT WRITTEN PERMISSION from the account owner
Verify compliance with Instagram's Terms of Service
Confirm adherence to applicable laws and regulations
Understand that unauthorized use may constitute illegal activity
The tool implements respectful request rates and only accesses publicly available information through standard web requests, consistent with legitimate OSINT practices in cybersecurity assessments.

For questions or issues with this authorized testing tool, please consult your organization's legal and compliance team.
[instagram @yrrr_naman
](https://www.instagram.com/yrrr_naman/)
