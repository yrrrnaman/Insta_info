# IGRecon - Instagram Reconnaissance Tool
## What This Tool Does
IGRecon is an **authorized penetration testing tool** designed for cybersecurity professionals to gather publicly available information from Instagram accounts as part of legitimate security assessments.
### Key Functions:

1. **Account Verification**
   - Checks if an Instagram account exists
   - Determines if the account is active

2. **Public Profile Information Gathering**
   - Retrieves basic profile details (when public)
   - Identifies if account is private or public
   - Detects if account is verified
   - Extracts biography information
   - Finds associated website links

3. **Statistics Collection**
   - Counts number of posts
   - Gets follower count
   - Gets following count

4. **Data Export**
   - Saves all findings in structured JSON format
   - Creates timestamped reports for documentation

### Technical Approach:
- Uses standard HTTP requests to access publicly available Instagram web pages
- Parses embedded JSON data from profile pages
- Implements respectful delays between requests
- Works entirely through Instagram's public web interface

### Important Limitations:
- **Only accesses PUBLIC information** - Cannot bypass Instagram's privacy settings
- **No authentication required** - Works without logging into Instagram
- **Passive reconnaissance** - Doesn't interact with the account or other users


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




- **Rate limited** - Built-in delays prevent aggressive scanning

