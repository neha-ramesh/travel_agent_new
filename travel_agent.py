from dotenv import load_dotenv
import streamlit as st
from datetime import date
from PIL import Image
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure Streamlit App
st.set_page_config(page_title="Travel Agent App", layout="wide")

# Navbar
st.sidebar.title("Travel Agent Portal")
option = st.sidebar.radio(
    "Explore Options:",
    ["Home", "Plan Your Trip", "Accommodation", "Travel", "Food & Cuisine", "Attractions"]
)

# Home Page
if option == "Home":
    st.title("Welcome to the Travel Agent Portal!")
    st.image("D:\College\AI\Project\download.jpeg", caption="Discover Your Next Adventure!", use_column_width=True)
    st.write("""
        Explore amazing destinations, plan your itinerary, and make memories to last a lifetime. 
        Use the sidebar to navigate through our services.
    """)

# Plan Your Trip
elif option == "Plan Your Trip":
    st.title("Plan Your Dream Vacation")

    # Select a major city
    cities = ["Paris", "New York", "Tokyo", "London", "Dubai", "Sydney"]
    city = st.selectbox("Choose your destination city:", cities)

    # Date range
    st.write("Select your travel dates:")
    start_date = st.date_input("From", date.today())
    end_date = st.date_input("To", date.today())

    # Number of people
    people = st.slider("Number of people:", 1, 10, 1)

    # Search Bar
    search = st.text_input("Search for activities or specific locations:")

    # Submit Button
    if st.button("Get Recommendations"):
        # Call Gemini API for trip recommendations
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Plan a trip to {city} from {start_date} to {end_date} for {people} people. Highlight major attractions, accommodations, travel tips, and activities. Search context: {search}"
        response = model.generate_content(prompt)
        st.subheader("Trip Recommendations:")
        st.write(response.text)

# Accommodation
elif option == "Accommodation":
    st.title("Find the Perfect Stay")
    city = st.text_input("Enter the city:")
    check_in = st.date_input("Check-in Date", date.today())
    check_out = st.date_input("Check-out Date", date.today())
    if st.button("Search Accommodations"):
        # Call Gemini API for accommodation suggestions
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Find top accommodations in {city} from {check_in} to {check_out} with great reviews and budget options."
        response = model.generate_content(prompt)
        st.subheader("Recommended Accommodations:")
        st.write(response.text)

# Travel
elif option == "Travel":
    st.title("Plan Your Travel")
    start_location = st.text_input("Starting Location:")
    destination = st.text_input("Destination:")
    travel_date = st.date_input("Travel Date", date.today())
    if st.button("Find Travel Options"):
        # Call Gemini API for travel suggestions
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Suggest travel options from {start_location} to {destination} on {travel_date}."
        response = model.generate_content(prompt)
        st.subheader("Travel Options:")
        st.write(response.text)

# Food & Cuisine
elif option == "Food & Cuisine":
    st.title("Explore Local Delicacies")
    city = st.text_input("Enter the city to explore:")
    if st.button("Find Food Options"):
        # Call Gemini API for food recommendations
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Recommend must-try food and cuisine in {city}, including popular restaurants."
        response = model.generate_content(prompt)
        st.subheader("Food Recommendations:")
        st.write(response.text)

# Attractions
elif option == "Attractions":
    st.title("Top Attractions")
    city = st.text_input("Enter the city to explore:")
    if st.button("Discover Attractions"):
        # Call Gemini API for attraction suggestions
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"List the top attractions in {city}, including historical, cultural, and modern sites."
        response = model.generate_content(prompt)
        st.subheader("Top Attractions:")
        st.write(response.text)
