import streamlit as st
import json
from dotenv import load_dotenv
load_dotenv()
import os

# Define the filename for the JSON file
json_file = "blog_urls.json"

def download_json_file():
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open("downloaded.json", 'w') as f:
        json.dump(data, f)
    st.sidebar.success(f"{json_file} downloaded successfully as a JSON file!")

# Load the blog URLs from the JSON file
try:
    with open(json_file, "r") as f:
        blog_dict = json.load(f)
except FileNotFoundError:
    blog_dict = {}

# Define the password

password = os.environ.get('PASSWORD')

# Define a function to check the user's password
def user_auth():
    """Authenticates user.

    Returns:
        bool: True if password matches. Else False.
    """
    user_password = st.sidebar.text_input("Enter the password to add or delete blog URLs", type="password")
    if user_password == password:
        return True
    elif user_password != "":
        st.sidebar.warning("Incorrect password")
    return False

# Define a function to save the blog URLs to the JSON file
def save_to_json():
    """Saves content to json file
    """
    with open(json_file, "w") as f:
        json.dump(blog_dict, f)

def add_blog():
    """Saves the user input of title,url, and section to json file.
    """
    st.sidebar.header("Add a Blog URL")
    blog_title= st.sidebar.text_input("Input Blog Title")
    blog_url= st.sidebar.text_input("Input Blog URL")
    blog_section = st.sidebar.selectbox("Select a section",list(blog_dict.keys()))

    if st.sidebar.button("Save"):
        blog_dict.setdefault(blog_section, {})[blog_title] = blog_url
        st.sidebar.success("Saved")
        save_to_json()

def delete_blog():
    """Deletes blog url from json file.
    """
    st.sidebar.header("Delete Blog")
    blog_section = st.sidebar.selectbox("Select a section for the blog URL to delete", list(blog_dict.keys()))
    blog_title = st.sidebar.selectbox("Select the blog URL to delete", list(blog_dict[blog_section].keys()))
    if st.sidebar.button("Delete"):
        del blog_dict[blog_section][blog_title]
        st.sidebar.success(f"Deleted")
        save_to_json()
def add_section():
    """Creates New section.
    """
    st.sidebar.header("Create a New Section")
    new_section = st.sidebar.text_input("Enter a name for the new section")
    if st.sidebar.button("Create"):
        if new_section in blog_dict.keys():
            st.sidebar.warning(f"The '{new_section}' section already exists")
        else:
            blog_dict[new_section] = {}
            st.sidebar.success(f"Created '{new_section}' section")
            save_to_json()
def remove_section():
    """Deletes section from json.
    """
    st.sidebar.header("Delete Section")
    blog_section=st.sidebar.selectbox("select section",list(blog_dict.keys()))
    if st.sidebar.button("Delete Section"):
        del blog_dict[blog_section]
        st.sidebar.success(f"Deleted")
        save_to_json()

def search():
    """Searches for content on json file.

    Returns:
        List: Matched content dict item.
    """
    search_term = st.text_input("Search")
    results = []
    for section, urls in blog_dict.items():
        if search_term.lower() in section.lower():
            results.append(f"## {section}")
            for url_name, url_link in urls.items():
                results.append(f"- [{url_name}]({url_link})")
        else:
            for url_name, url_link in urls.items():
                if search_term.lower() in url_name.lower() or search_term.lower() in url_link.lower():
                    results.append(f"- {section}: [{url_name}]({url_link})")
    return results

def main():
    st.title("# Saved Blog Manager")

    if user_auth():
        add_blog()
        add_section()
        delete_blog()
        remove_section()
    else:
        st.header("## Authenticate to add urls")
    if st.sidebar.button('Download JSON file'):
        
        download_json_file()
    #view section
    results = search()
    if results:
        for result in results:
            st.write(result)
    else:
        for section, urls in blog_dict.items():
            st.write(f"## {section}")
            for url_name, url_link in urls.items():
                st.write(f"- [{url_name}]({url_link})")

if __name__=="__main__":
    main()