import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("AI Powered Travel Planner 📍🗺️")

Route = st.text_input("Enter From(Departure) and To(Arrival) Places (e.g., Mumbai to Delhi):")

if st.button("Generate Travel Choices"):
    if Route:
        try:
            parts = Route.split(" to ")
            if len(parts) != 2:
                st.error("Please enter the input in the format 'Source to Destination'.")
                st.stop()
            source, destination = parts[0].strip(), parts[1].strip()

            prompt_template = ChatPromptTemplate.from_messages(
                [
                    "system",
                    "You are a helpful AI Powered Travel planning agent designed to assist users in finding optimal travel options between a given source and destination. Process user inputs and generate various travel choices such as cab, train, bus, and flights, along with their estimated costs.",
                    "human",
                    "Help me in finding the optimal travel options from {source} to {destination}",
                ]
            )

            chat_model = GoogleGenerativeAI(
                model="models/gemini-2.0-pro-exp", api_key="Enter Your API Key Here"
            )

            output_parser = StrOutputParser()

            chain = prompt_template | chat_model | output_parser

            raw_input = {"source": source, "destination": destination}

            with st.spinner("Generating Optimal way of travel.... ✈︎ "):
                result = chain.invoke(raw_input)

            st.write("## Optimal Route map:")
            st.write(result)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter the correct source and destination or check if the source and destination are not same if they are same kindly change one.")
