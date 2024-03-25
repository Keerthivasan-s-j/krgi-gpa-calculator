import streamlit as st

# Define social media links and corresponding logos
social_media_links = {
    "Twitter": "https://twitter.com/",
    "Facebook": "https://www.facebook.com/",
    "Instagram": "https://www.instagram.com/"
}

social_media_logos = {
    "Twitter": "https://upload.wikimedia.org/wikipedia/en/6/60/Twitter_Logo_as_of_2021.svg",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
    "Instagram": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
}

# Function to display social media links with logos
def display_social_media_links(links, logos):
    for platform, link in links.items():
        st.write(f"### Follow us on {platform}")
        st.markdown(f"<a href='{link}' target='_blank'><img src='{logos[platform]}' width='50'></a>", unsafe_allow_html=True)
        st.markdown(f"[{platform}]({link})")

# Display social media links
st.title("Welcome to Our Page!")
display_social_media_links(social_media_links, social_media_logos)
