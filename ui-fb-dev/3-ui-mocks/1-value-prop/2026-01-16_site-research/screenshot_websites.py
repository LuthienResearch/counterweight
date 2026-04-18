#!/usr/bin/env python3
"""
Screenshot automation script for capturing website screenshots.
Takes screenshots of websites from the Excel file and saves them to inspire_v1 directory.
"""

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
import logging

def setup_driver():
    """Set up Chrome WebDriver with appropriate options for screenshots."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.set_page_load_timeout(30)
    return driver

def clean_filename(url):
    """Convert URL to a clean filename for the screenshot."""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    return domain.replace('.', '_')

def take_screenshot(driver, url, output_dir):
    """Take a screenshot of the given URL and save it to output_dir."""
    try:
        print(f"Taking screenshot of: {url}")
        driver.get(url)
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Additional wait for dynamic content
        time.sleep(3)
        
        # Set window size for consistent screenshots
        driver.set_window_size(1920, 1080)
        
        # Take screenshot
        filename = clean_filename(url) + ".png"
        filepath = os.path.join(output_dir, filename)
        
        success = driver.save_screenshot(filepath)
        if success:
            print(f"✓ Screenshot saved: {filename}")
            return True
        else:
            print(f"✗ Failed to save screenshot for {url}")
            return False
            
    except Exception as e:
        print(f"✗ Error taking screenshot of {url}: {str(e)}")
        return False

def main():
    """Main function to process all URLs and take screenshots."""
    # Paths
    excel_file = "landing_pages_developer_infra_with_taglines.xlsx"
    output_dir = "inspire_v1"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read URLs from Excel file
    print("Reading URLs from Excel file...")
    df = pd.read_excel(excel_file)
    urls = df['URL'].dropna().tolist()
    
    print(f"Found {len(urls)} URLs to process")
    
    # Set up WebDriver
    print("Setting up Chrome WebDriver...")
    driver = setup_driver()
    
    # Process each URL
    successful = 0
    failed = 0
    
    try:
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}]", end=" ")
            if take_screenshot(driver, url, output_dir):
                successful += 1
            else:
                failed += 1
            
            # Small delay between requests to be respectful
            time.sleep(2)
            
    finally:
        driver.quit()
        print(f"\n\nScreenshot process completed!")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Screenshots saved to: {output_dir}/")

if __name__ == "__main__":
    main()