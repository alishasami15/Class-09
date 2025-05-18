import streamlit as st
from deep_translator import GoogleTranslator
from payment import generate_payment_link, process_payment

st.set_page_config(page_title="LingoBridge", layout="centered")


# HEADER
st.markdown("""
     <h1 style='text-align:center; color:#4B8BBE;'>🌐 LingoBridge</h1>
     <p style='text-align:center; font-size:18px;'>Your Ultimate Language, Grammar, and Sentence Structure Guide</p>
     <hr>      
  """, unsafe_allow_html=True)


page = st.sidebar.radio("Go to", [
    "🌍 Language Translator",
    "⏳ English Tenses",
    "📘 Grammar Terms",
    "🧠 Sentence Structures",
    "💳 Premium Access "
])

# Language Translator
if page == "🌍 Language Translator":
    st.subheader( "Translate Between Language")

    direction = st.selectbox("🌐 Choose Translation Direction", [
        "English ➜ Urdu",
        "Urdu ➜ English",
        "English ➜ Arabic",
        "English ➜ Pashto",
        "English ➜ Sindhi"

    ])

    input_text = st.text_input("✍️ Type your text here:")

    lang_map = {
        "English ➜ Urdu": ('en' , 'ur'),
        "Urdu ➜ English": ('ur' , 'en'),
        "English ➜ Arabic": ('en' , 'ar'),
        "English ➜ Pashto": ('en' , 'ps'),
        "English ➜ Sindhi": ('en' , 'sd'),
    }

    if input_text:
        src, tgt = lang_map[direction]
        try:
            translated = GoogleTranslator(source=src, target=tgt).translate(input_text)
            st.success(f"Translated Text:\n\n**{translated}**")
        except Exception as e:
            st.error(f"Translation failed: {e}")


# English Tenses
elif page == "⏳ English Tenses":
    st.subheader("⏰ Master Tenses")

    tenses = {
        "present Simple":{
            "structure": "Subject + base verb",
            "example":"I eat an apple",
            "use": "Used for habits, routines, or general truths."
        },
           "Present Continuous": {
            "structure": "Subject + is/am/are + verb-ing",
            "example": "I am eating an apple.",
            "use": "Used for actions happening right now."
        },
        "Present Perfect": {
            "structure": "Subject + have/has + past participle",
            "example": "I have eaten an apple.",
            "use": "Used for actions completed in the recent past."
        },
        "Present Perfect Continuous": {
        "structure": "Subject + has/have been + verb-ing",
        "example": "I have been eating an apple.",
        "use": "Used for actions that started in the past and are still continuing or just stopped."
       },
        "Past Simple": {
            "structure": "Subject + past verb",
            "example": "I ate an apple.",
            "use": "Used for actions that happened in the past."
        },
        "Past Continuous": {
            "structure": "Subject + was/were + verb-ing",
            "example": "I was eating an apple.",
            "use": "Used for actions that were in progress in the past."
        },
        "Past Perfect": {
            "structure": "Subject + had + past participle",
            "example": "I had eaten an apple.",
            "use": "Used for actions completed before another past action."
        },
        "Past Perfect Continuous": {
        "structure": "Subject + had been + verb-ing",
        "example": "I had been eating an apple.",
        "use": "Used for actions that were ongoing in the past before another past action."
        },
        "Future Simple": {
            "structure": "Subject + will + base verb",
            "example": "I will eat an apple.",
            "use": "Used for actions that will happen."
        },
        "Future Continuous": {
            "structure": "Subject + will be + verb-ing",
            "example": "I will be eating an apple.",
            "use": "Used for future actions in progress."
        },
        "Future Perfect": {
            "structure": "Subject + will have + past participle",
            "example": "I will have eaten an apple.",
            "use": "Used for actions completed before a certain future time."
        },
        "Future Perfect Continuous": {
        "structure": "Subject + will have been + verb-ing",
        "example": "I will have been eating an apple.",
        "use": "Used for actions that will be ongoing up to a specific point in the future."
        }
    }

    selected_tense = st.selectbox ("Select a Tense", list(tenses.keys()))
    data = tenses[selected_tense]

    st.markdown(f"""
         <div style="background-color:#eef6ff; padding:15px; border-radius:10px;">
                <h4 style="color:#1f77b4;">🔹{selected_tense}</h4>
                <p><strong>  Structure:</strong> {data["structure"]}</p>
                <p><strong>  Usage:</strong> {data["use"]}</p>
                <p><strong>  Example:</strong> {data["example"]}</p>
         </div> 
    """, unsafe_allow_html=True)


# Grammar Terms

elif page == "📘 Grammar Terms":
    st.subheader(" 📚 English Grammar Terms Explained")

    grammar = {
        "Noun": "A noun names a person, place, thing, or idea. _Example: Ali, city, book._",
        "Pronoun": "A word that replaces a noun. _Example: he, she, it._",
        "Verb": "Describes an action or state. _Example: run, eat, is._",
        "Adjective": "Describes a noun. _Example: red, tall, beautiful._",
        "Adverb": "Modifies a verb, adjective, or another adverb. _Example: quickly, very, silently._",
        "Preposition": "Shows relationships between nouns. _Example: in, on, under._",
        "Conjunction": "Connects words or phrases. _Example: and, but, or._",
        "Interjection": "Expresses sudden emotion. _Example: Wow! Oh no! Yay!_"
    }

    selected_term = st.selectbox("Select a Grammar Term", list(grammar.keys()))
    if selected_term:
       st.markdown(f"""
          <div style="background-color:#fdf6e3; padding:15px; border-radius:10px;">
                <h4 style="color:#228B22;">📌 {selected_term}</h4>
                <p>{grammar[selected_term]}</p>
        </div>        
                
     """,unsafe_allow_html=True)
    
# Sentence Structure
elif page == "🧠 Sentence Structures":
    st.subheader("🧱 Basic English Sentence Structures")

    structures = {
        "Simple Sentence":{
            "structure":"Subject + Verb",
            "example": "She sings."
        },
        "Compound Sentence": {
            "structure": "Independent clause + Conjunction + Independent clause",
            "example": "She sings and he plays the piano."
        },
        "Complex Sentence":{
            "structure": "Independent clause + Subordinate clause",
            "example": "She sings because she is happy."   
        },
        "Compound-Complex Sentence":{
            "structure": "At least two independent clauses + one dependent clause",
            "example": "She sings and he plays, although they are tired."
        }
    } 

    selected_structure = st.selectbox("Select a Sentence Structure", list(structures.keys()))
    structure = structures[selected_structure]

    st.markdown(f"""
        <div style="background-color:#e8f5e9; padding:15px; border-radius:10px;">
            <h4 style="color:#2E7D32;"> {selected_structure}</h4>
            <p><strong>🧱 Structure:</strong> {structure["structure"]}</p>
            <p> <strong>✍️ Example:</strong> {structure["example"]}</p>
        </div>       
                
    """,unsafe_allow_html=True)

elif page == "💳 Premium Access ":
    st.subheader("LingoBridge Premium")

    st.markdown("""
    Unlock premium features like:
    AI-powered Translation
    offline Grammar Downloads
    Ad-free Experience
    Extra Language (Arabic, Pashto, Sindhi,Urdu, English)

    **One-time Payment:Rs.500**
    """)  

    email = st.text_input ("Enter your email to continue:")  
    if st.button("Pay Now"):
        if email:
            result = process_payment(email, 500)
            st.success(f"Payment successful!\n\n**Translation ID:** `{result['transaction_id']}`")
        else:
            st.error("Please enter your email first.")    