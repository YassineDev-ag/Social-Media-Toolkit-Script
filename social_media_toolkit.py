# social_media_toolkit.py

# Import necessary libraries
import instaloader
import pyautogui
import base64
from time import sleep 

# Infinite loop to keep the script running
while True:
    # Display menu options to the user
    num = input("""
                1 > Download image profile Instagram
                2 > Send message social media 
                3 > encoder base64
                4 > information  Instagram account
                >> : """)

    # Option 1: Download Instagram profile picture
    if num == "1":
        ig = instaloader.Instaloader()  # Create an instance of Instaloader
        dp = input("Enter Instagram username : ")  # Get username from user
        ig.download_profile(dp, profile_pic_only=True)  # Download profile picture
        
    # Option 2: Send messages on social media
    elif num == "2": 
        msg = input("Enter Your Msg  :")  # Get message from user
        num_msg = int(input("Chose Your Numbr of Msg  :"))  # Get number of messages to send
        time_msg = float(input("Chose Your Time Of Msg  :"))  # Get time interval between messages
        for num in range(num_msg + 1):  # Loop to send messages
            pyautogui.typewrite(msg)  # Type the message
            sleep(time_msg)  # Wait for the specified time
            pyautogui.press('enter')  # Press enter to send the message
            sleep(time_msg)  # Wait again before sending the next message
             
    # Option 3: Encode and decode text using base64
    elif num == "3":
        def encode_text(text):
            encoded_text = base64.b64encode(text.encode('UTF-8')).decode('ascii')  # Encode text
            return encoded_text
        
        def decode_text(Decode):
            decoded_ha = base64.b64decode(Decode)  # Decode base64 text
            decoded_text = decoded_ha.decode('UTF-8')  # Convert bytes to string
            return decoded_text
        
        encoder = input("Enter your text for encoding: ")  # Get text to encode
        encoded_text = encode_text(encoder)  # Encode the text
        print("Encoded: " + encoded_text)  # Print encoded text

        decoder = input("Enter your text for decoding: ")  # Get text to decode
        decoded_code = decode_text(decoder)  # Decode the text
        print("Decoded: " + decoded_code)  # Print decoded text
        
    # Option 4: Get information about an Instagram account
    elif num == "4":
        L = instaloader.Instaloader()  # Create an instance of Instaloader
        TARGET = 'name account '  # Specify the target account name

        profile = instaloader.Profile.from_username(L.context, TARGET)  # Get profile information
        # Print profile details
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Biography: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Number of Posts: {profile.mediacount}")
        print(f"External URL: {profile.external_url}")
        print(f"Is Private: {'Yes' if profile.is_private else 'No'}")
        print(f"Is Verified: {'Yes' if profile.is_verified else 'No'}")

        # Check if the account is private
        if profile.is_private:
            print("\nThis is a private account. You need to be following this account to see its posts.")
        else:
            print("\nLast 5 Posts:")  # Display last 5 posts
            for post in profile.get_posts():
                if profile.mediacount - profile.get_posts().count <= 5:
                    print(f"\nPost ID: {post.mediaid}")
                    print(f"Post Date: {post.date}")
                    print(f"Likes: {post.likes}")
                    print(f"Comments: {post.comments}")
                    print(f"Caption: {post.caption}")
                    print(f"URL: https://www.instagram.com/p/{post.shortcode}/")

        print("\nScript completed.")  # Indicate that the script has finished