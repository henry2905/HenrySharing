import json
import requests
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import sqlite3


st.set_page_config(page_title="Henry's webpage", page_icon=":hot_face:", layout=("wide"))

posts = []

with open("posts.txt", "r") as f:
    posts = [line.strip() for line in f.readlines()]

# Define function to display posts
def display_posts():
    if not posts:
        st.write("No posts yet.")
    else:
        for post in posts:
            st.write(post)

# Define function to add new post
def add_post():
    new_post = st.text_input("Write your post here:")
    if new_post:
        posts.append(new_post)
        with open("posts.txt", "a") as f:
            f.write(new_post + "\n")
        st.success("Post added!")

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Posts", "Account", "Contact", "Introduction"],
        icons=["body-text", "person-circle", "envelope-at", "book"],
        default_index=0
    )

if selected == "Posts":
    st.header("Posts")
    add_post()  # Add new post
    display_posts()
if selected == "Account":
    st.title(f"You have selected {selected}")
    username = "Henry Nguyen"
    avatar = "https://scontent.fsgn8-2.fna.fbcdn.net/v/t39.30808-6/353397553_1413312982845366_7631198211481807075_n.jpg?_nc_cat=111&cb=99be929b-3346023f&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=_sRB31e9qHgAX8zPCDe&_nc_ht=scontent.fsgn8-2.fna&oh=00_AfCWSQoK4xc2P_jD-NrGDb_6_q-6X-7Ml_zf7Iq7YxRLJA&oe=64CCB29D"

    # Display user profile
    st.image(avatar, width=100)
    st.write(f"Username: {username}")
    st.write(f"Number of posts: {len(posts)}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
    st.subheader("Here are my list of contacts:")
    st.write("[Facebook >](https://www.facebook.com/profile.php?id=100025000342932)")
    st.write("Phone number: 096337795*")
    st.write("Email: tienhung2905@gmail.com")
if selected == "Introduction":
    st.title(f"You have selected {selected}")
    st.subheader("Wassup nerds, Henry is here! ")
    st.title("An outstanding individual from Vietnam")
    st.write("I have a Silver medal in the City's Olympic Competition, Third place in the City's Gifted Students Competition. Not good enough? I am currently studying at Le Hong Phong High school for the Gifted!")
    st.write("[Learn more >](https://www.facebook.com/profile.php?id=100025000342932)")
    st.write("---"),
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Welcome to my webpage!")
        st.write("##")
        st.write(
            """
        This is the webpage that I created in order for you to share your stories, opinions, experiences anonymously with others. 
        
        
        Please be respectful and enjoy yourself here.
        
        
        I am open to any suggestion/feedback. If you want to contact me, you can find it in the 'Contact' section.
        
        """
        )
    with right_column:
        st.write("""
        Terms and conditions:
        
        
        -Respect Henry
        """)








