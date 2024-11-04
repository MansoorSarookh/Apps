# Import necessary libraries
import os
import streamlit as st
from groq import Groq

# Set up the Groq API Key
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit app title and description
st.title("Personalized Study Assistant Chatbot by Mansoor Sarookh")
st.write("I’m here to help you organize your study plan with tailored resources and tips. Let's get started!")

# User input for study details
study_topic = st.text_input("What is your study topic or exam?")
prep_days = st.number_input("How many days do you have to prepare?", min_value=1, step=1)
hours_per_day = st.number_input("How many hours can you dedicate per day?", min_value=1, step=1)

# Display loading message while waiting for response
if st.button("Generate Study Plan"):
    if study_topic and prep_days and hours_per_day:
        with st.spinner("Generating your study plan... Please wait."):
            try:
                # Function to generate chatbot response based on user input
                def generate_study_plan(topic, days, hours):
                    prompt = (
                        f"I am a study assistant chatbot helping a user prepare for {topic} over {days} days "
                        f"with {hours} hours per day. Please provide a personalized study plan, tips for effective "
                        "study habits, and suggest specific resources for each session."
                    )

                    # Generate response using Groq API
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama3-8b-8192",
                    )
                    
                    response = chat_completion.choices[0].message.content
                    return response

                # Get and display the generated study plan
                study_plan = generate_study_plan(study_topic, prep_days, hours_per_day)
                st.success("Your Study Plan:")
                st.write(study_plan)

            except Exception as e:
                st.error("There was an error generating the study plan. Please try again later.")
                st.write(f"Error details: {e}")
    else:
        st.warning("Please enter all required fields (study topic, preparation days, and available hours) to receive a study plan.")
