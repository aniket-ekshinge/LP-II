import streamlit as st
from typing import List

knowledge_base = {
    "cold": {
        "symptoms": ["headache", "runny nose", "sneezing", "sore throat"],
        "actions": ["Take rest", "Stay hydrated", "Take over-the-counter cold medicines"],
    },
    "typhoid": {
        "symptoms": ["headache", "abdominal pain", "poor appetite", "fever"],
        "actions": ["Consult a doctor", "Take prescribed antibiotics", "Stay hydrated"],
    },
    "measles": {
        "symptoms": ["fever", "runny nose", "rash", "conjunctivitis"],
        "actions": ["Isolate the patient to prevent spreading the disease", "Administer measles vaccine if not already vaccinated", "Provide supportive care for fever and discomfort"],
    },
    "influenza": {
        "symptoms": ["sore throat", "fever", "headache", "chills", "body ache"],
        "actions": ["Rest in bed", "Stay hydrated", "Take over-the-counter flu medications", "Consult a doctor if symptoms worsen"],
    },
    "malaria": {
        "symptoms": ["fever", "sweating", "headache", "nausea", "vomiting", "diarrhea"],
        "actions": ["Seek medical attention immediately", "Take prescribed antimalarial medications", "Prevent mosquito bites by using bed nets and insect repellents"],
    },
    "diabetes": {
        "symptoms": ["excessive thirst", "frequent urination", "fatigue", "blurry vision", "slow healing of wounds"],
        "actions": ["Monitor blood sugar levels regularly", "Follow a healthy diet and exercise regimen", "Take prescribed medications as directed by a healthcare provider"],
    },
    "asthma": {
        "symptoms": ["shortness of breath", "wheezing", "coughing", "chest tightness"],
        "actions": ["Use inhalers or nebulizers as prescribed", "Avoid triggers such as smoke and allergens", "Develop an asthma action plan with a healthcare provider"],
    },
    # Add more issues, symptoms, and actions as needed
}


st.header("Information Management Expert System")


def respond(selected_symptoms: List[str]):
    matching_issues = []
    for issue, data in knowledge_base.items():
        if all(symptom in data["symptoms"] for symptom in selected_symptoms):
            matching_issues.append(issue)

    if matching_issues:
        for issue in matching_issues:
            st.write(f"You may have {issue}. Here are some recommended actions:")
            for action in knowledge_base[issue]["actions"]:
                st.write(action)
    else:
        st.write("No matching issue found. Please consult a professional for assistance.")


if __name__ == "__main__":
    all_symptoms = set()
    for issue in knowledge_base.values():
        all_symptoms.update(issue["symptoms"])

    options = st.multiselect(
        'What symptoms are you experiencing?',
        list(all_symptoms),
        [])

    col1, col2 = st.columns([1, 0.1])
    with col1:
        ask_button = st.button("Ask")
    with col2:
        quit_button = st.button("Quit")

    if ask_button:
        respond(options)
    if quit_button:
        st.write("Thank you for using the Expert system!")

