#!/usr/bin/env python3
"""
Instagram Reconnaissance Tool (IGRecon)
For authorized penetration testing only

This tool performs passive reconnaissance on Instagram accounts
to gather publicly available information as part of an authorized
penetration test or security assessment.
"""

import requests
import json
import argparse
import sys
import time
from datetime import datetime
import os

class IGRecon:
    def __init__(self, username, output_file=None):
        self.username = username
        self.output_file = output_file
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
    def check_account_exists(self):
        """Check if Instagram account exists"""
        try:
            url = f"https://www.instagram.com/{self.username}/"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 404:
                return False
            elif "Login • Instagram" in response.text:
                return False
            elif response.status_code == 200:
                return True
            else:
                return None
                
        except Exception as e:
            print(f"[!] Error checking account: {e}")
            return None
    
    def get_profile_info(self):
        """Extract profile information from Instagram page"""
        try:
            url = f"https://www.instagram.com/{self.username}/"
            response = self.session.get(url, timeout=10)
            
            if response.status_code != 200:
                return None
            
            # Extract JSON data from page
            start_text = "window._sharedData = "
            end_text = ";</script>"
            
            start_index = response.text.find(start_text)
            if start_index == -1:
                return None
                
            start_index += len(start_text)
            end_index = response.text.find(end_text, start_index)
            
            if end_index == -1:
                return None
                
            json_str = response.text[start_index:end_index]
            
            try:
                data = json.loads(json_str)
                user_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
                return user_data
            except (KeyError, json.JSONDecodeError):
                # Try alternative method
                return self.extract_basic_info(response.text)
                
        except Exception as e:
            print(f"[!] Error fetching profile info: {e}")
            return None
    
    def extract_basic_info(self, html_content):
        """Extract basic information from HTML when JSON parsing fails"""
        user_data = {}
        
        # Basic extraction attempts
        try:
            # Look for meta tags and other indicators
            if '"is_private":true' in html_content:
                user_data['is_private'] = True
            elif '"is_private":false' in html_content:
                user_data['is_private'] = False
                
            if '"followed_by"' in html_content:
                user_data['is_verified'] = '"is_verified":true' in html_content
                
            # Extract profile picture URL
            pic_start = html_content.find('"profile_pic_url_hd":"')
            if pic_start != -1:
                pic_start += len('"profile_pic_url_hd":"')
                pic_end = html_content.find('"', pic_start)
                if pic_end != -1:
                    user_data['profile_pic_url_hd'] = html_content[pic_start:pic_end].replace('\\u0026', '&')
                    
        except Exception:
            pass
            
        return user_data if user_data else None
    
    def get_user_stories(self):
        """Check for public stories (limited due to authentication)"""
        # Note: Full story access requires authentication
        # This is a placeholder for demonstration
        return {"stories_available": "Requires authentication for private accounts"}
    
    def get_posts_info(self):
        """Get basic post information"""
        try:
            url = f"https://www.instagram.com/{self.username}/"
            response = self.session.get(url, timeout=10)
            
            # Simple regex-based extraction for demonstration
            import re
            
            # Extract post count
            post_match = re.search(r'"edge_owner_to_timeline_media":{"count":(\d+)', response.text)
            posts_count = int(post_match.group(1)) if post_match else "Unknown"
            
            # Extract follower count
            follower_match = re.search(r'"edge_followed_by":{"count":(\d+)', response.text)
            followers_count = int(follower_match.group(1)) if follower_match else "Unknown"
            
            # Extract following count
            following_match = re.search(r'"edge_follow":{"count":(\d+)', response.text)
            following_count = int(following_match.group(1)) if following_match else "Unknown"
            
            return {
                "posts_count": posts_count,
                "followers_count": followers_count,
                "following_count": following_count
            }
            
        except Exception as e:
            print(f"[!] Error getting posts info: {e}")
            return None
    
    def search_for_mentions(self):
        """Search for mentions of the user (basic implementation)"""
        # This would require a more sophisticated approach in a real tool
        return {"mentions_search": "Basic tool - requires advanced implementation"}
    
    def run_recon(self):
        """Execute the reconnaissance process"""
        print(f"[*] Starting Instagram reconnaissance for @{self.username}")
        print(f"[*] Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
        
        # Check if account exists
        print("[*] Checking if account exists...")
        account_status = self.check_account_exists()
        
        if account_status is False:
            result = {
                "username": self.username,
                "account_exists": False,
                "timestamp": datetime.now().isoformat()
            }
            print("[-] Account does not exist or is unavailable")
            self.save_results(result)
            return result
        elif account_status is None:
            print("[!] Unable to determine account status")
            return None
            
        print("[+] Account exists")
        
        # Get profile information
        print("[*] Gathering profile information...")
        profile_info = self.get_profile_info()
        
        # Get basic stats
        print("[*] Gathering statistics...")
        stats_info = self.get_posts_info()
        
        # Compile results
        result = {
            "username": self.username,
            "account_exists": True,
            "profile_info": profile_info,
            "statistics": stats_info,
            "timestamp": datetime.now().isoformat(),
            "tool": "IGRecon v1.0 - Authorized Pentest Tool"
        }
        
        # Display results
        self.display_results(result)
        
        # Save results
        self.save_results(result)
        
        return result
    
    def display_results(self, result):
        """Display gathered information"""
        print("\n" + "="*60)
        print("INSTAGRAM RECONNAISSANCE RESULTS")
        print("="*60)
        print(f"Username: @{result['username']}")
        print(f"Scan Time: {result['timestamp']}")
        print("-"*60)
        
        if result['statistics']:
            stats = result['statistics']
            print(f"Posts: {stats.get('posts_count', 'N/A')}")
            print(f"Followers: {stats.get('followers_count', 'N/A')}")
            print(f"Following: {stats.get('following_count', 'N/A')}")
        
        if result['profile_info']:
            profile = result['profile_info']
            print(f"\nProfile Status:")
            print(f"  Private: {'Yes' if profile.get('is_private') else 'No'}")
            print(f"  Verified: {'Yes' if profile.get('is_verified') else 'No'}")
            print(f"  Business Account: {'Yes' if profile.get('is_business_account') else 'No'}")
            
            if profile.get('full_name'):
                print(f"Full Name: {profile['full_name']}")
                
            if profile.get('biography'):
                print(f"Bio: {profile['biography'][:100]}{'...' if len(profile['biography']) > 100 else ''}")
                
            if profile.get('external_url'):
                print(f"Website: {profile['external_url']}")
        
        print("-"*60)
    
    def save_results(self, result):
        """Save results to file"""
        if self.output_file:
            try:
                with open(self.output_file, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"[+] Results saved to {self.output_file}")
            except Exception as e:
                print(f"[!] Error saving results: {e}")
        else:
            # Default filename
            default_file = f"ig_recon_{self.username}_{int(time.time())}.json"
            try:
                with open(default_file, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"[+] Results saved to {default_file}")
            except Exception as e:
                print(f"[!] Error saving results: {e}")

def main():
    parser = argparse.ArgumentParser(description="Instagram Reconnaissance Tool for Authorized Pentesting")
    parser.add_argument("-u", "--username", required=True, help="Instagram username to investigate")
    parser.add_argument("-o", "--output", help="Output file for results (JSON format)")
    parser.add_argument("--delay", type=int, default=1, help="Delay between requests in seconds (default: 1)")
    
    args = parser.parse_args()
    
    # Authorization reminder
    print("!"*60)
    print("INSTAGRAM RECONNAISSANCE TOOL")
    print("!"*60)
    print("AUTHORIZED PENETRATION TESTING ONLY")
    print("Ensure you have explicit permission to test this account")
    print("!"*60)
    
    # Confirm authorization
    confirm = input("\nDo you have written authorization to test this account? (yes/no): ")
    if confirm.lower() not in ['yes', 'y']:
        print("[-] Authorization required. Exiting.")
        sys.exit(1)
    
    # Initialize and run recon
    recon_tool = IGRecon(args.username, args.output)
    results = recon_tool.run_recon()
    
    if results:
        print(f"\n[*] Scan completed successfully")
    else:
        print(f"\n[!] Scan encountered errors")

if __name__ == "__main__":
    main()
