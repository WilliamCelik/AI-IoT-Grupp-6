'''

import streamlit as st
import boto3
import uuid

# AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"  # eller "en_US"
AWS_REGION = "eu-central-1"

# Session ID per användare
session_id = str(uuid.uuid4())

# Initiera Lex-client
lex_client = boto3.client('lexv2-runtime', region_name=AWS_REGION)

st.title("💬 Väderassistent Annika")

user_input = st.text_input("Ställ en väderfråga:")

if user_input:
    try:
        response = lex_client.recognize_text(
            botId=LEX_BOT_ID,
            botAliasId=LEX_BOT_ALIAS_ID,
            localeId=LEX_LOCALE_ID,
            sessionId=session_id,
            text=user_input
        )

        # Hämta svar från Lex
        lex_message = response['messages'][0]['content'] if 'messages' in response else "Inget svar från Lex 🤖"
        st.markdown(f"**Svar:** {lex_message}")

    except Exception as e:
        st.error(f"Något gick fel: {e}")

import streamlit as st
import boto3
import uuid

# AWS-konfiguration
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"

# Starta session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initiera Lex
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# Streamlit UI
st.title("💬 Väderassistent Annika")

st.markdown("Skriv din fråga nedan:")

# Visa tidigare meddelanden
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**Du:** {msg}")
    else:
        st.markdown(f"**Annika:** {msg}")

# Ny fråga
user_input = st.text_input("Skriv här...", key="user_input")

if st.button("Skicka") and user_input:
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = lex_client.recognize_text(
            botId=LEX_BOT_ID,
            botAliasId=LEX_BOT_ALIAS_ID,
            localeId=LEX_LOCALE_ID,
            sessionId=st.session_state.session_id,
            text=user_input
        )

        lex_response = response['messages'][0]['content'] if 'messages' in response else "🤖 Inget svar från Lex."
        st.session_state.chat_history.append(("bot", lex_response))
        st.rerun()

    except Exception as e:
        st.error(f"❌ Något gick fel: {e}")



import streamlit as st
import boto3
import uuid

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"

# Initiera session och meddelandelista
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Initiera Lex-client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI
st.title("💬 Väderassistent Annika")
st.subheader("Skriv din fråga nedan:")

# 🖼️ Visa hela konversationen
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(f"**Du:** {message}")
    else:
        st.markdown(f"**Annika:** {message}")

# 🧾 Inputfält med formulär (Enter = submit)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", key="user_input")
    submitted = st.form_submit_button("Skicka")

    if submitted and user_input:
        try:
            # ➡️ Lägg till ditt meddelande
            st.session_state.messages.append(("Du", user_input))

            # ➡️ Skicka till Lex
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            # 🧠 Hämta Lex-svar
            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Lex 🤖"
            )
            st.session_state.messages.append(("Annika", lex_message))
            st.rerun()

        except Exception as e:
            st.error(f"Något gick fel: {e}")


import streamlit as st
import boto3
import uuid

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️")

# 🧹 Rensa konversation
if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="T.ex. Hur blir vädret i Umeå imorgon?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )
            st.session_state.messages.append(("Väderannika", lex_message))
            st.rerun()

        except Exception as e:
            st.error(f"Något gick fel: {e}")

# Uppdaterad version med feta rubriker mm.

import streamlit as st 
import boto3
import uuid
import re

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️ som också kan allt ogräs")

# 🧹 Rensa konversation
if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        # 🔍 Leta efter eventuell bildlänk
        image_url = None
        image_match = re.search(r"(https?://[^\s]+\.jpg)", message)
        if image_match:
            image_url = image_match.group(1)
            message = message.replace(image_url, "")  # Ta bort länken från texten

        # 💬 Visa meddelandet med formatering
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

        # 🔗 Visa klickbar länk separat
        if image_url:
            st.markdown(f"[📷 Klicka här för bild]({image_url})", unsafe_allow_html=True)

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            # 🧹 Formatera svaret
            formatted_message = lex_message

            # Fetmarkera rubriker som slutar med kolon
            formatted_message = re.sub(r'(?m)^([^:\n]+?):', r'**\1:**', formatted_message)

            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()



# Uppdaterad version för bildhantering

import streamlit as st 
import boto3
import uuid
import re

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️ som också kan allt ogräs")

# 🧹 Rensa konversation
if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        # 🔍 Leta efter eventuell bildlänk
        image_url = None
        image_match = re.search(r"(https?://[^\s]+\.jpg)", message)
        if image_match:
            image_url = image_match.group(1)
            message = message.replace(image_url, "")  # Ta bort länken från texten

        # 💬 Visa meddelandet med formatering
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

        # 🔗 Visa klickbar länk separat
        if image_url:
            st.markdown(f"[📷 Klicka här för bild]({image_url})", unsafe_allow_html=True)


# 📸 Bildigenkänning
st.subheader("🔍 Identifiera ogräs från bild")

uploaded_file = st.file_uploader("Ladda upp en bild på ogräs (JPG-format)", type=["jpg", "jpeg"])

if uploaded_file:
    if st.button("🔎 Identifiera ogräset"):
        with st.spinner("🔍 Analyserar bilden..."):
            import base64
            import requests

            # Konvertera till base64-sträng
            img_bytes = uploaded_file.read()
            img_b64 = base64.b64encode(img_bytes).decode("utf-8")

            # 🛰️ Skicka till din API Gateway
            response = requests.post(
                "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify",
                data=img_b64,
                headers={"Content-Type": "application/octet-stream"},
            )

            if response.status_code == 200:
                result = response.json().get("result", "Inget resultat mottaget.")
                st.session_state.messages.append(("Väderannika", result))
            else:
                st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))

        st.rerun()


# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            # 🧹 Formatera svaret
            formatted_message = lex_message

            # Fetmarkera rubriker som slutar med kolon
            formatted_message = re.sub(r'(?m)^([^:\n]+?):', r'**\1:**', formatted_message)

            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()


# Ändrat så att regex hanterar specifikt ordet Bedömning eftersom rubriken blev med **
# samt också hanterar att rensa sessionen i AWS när man trycker rensa konversation.

import streamlit as st 
import boto3
import uuid
import re
import base64
import requests

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"
IDENTIFY_API_URL = "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️ som också kan allt ogräs")

# 🧹 Rensa konversation
if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []

    #  Rensa även AWS Lex-sessionen om den inte redan blivit inaktiv
    try:
        lex_client.delete_session(
        botId=LEX_BOT_ID,
        botAliasId=LEX_BOT_ALIAS_ID,
        localeId=LEX_LOCALE_ID,
        sessionId=st.session_state.session_id
    )
    except lex_client.exceptions.ResourceNotFoundException:
        pass  # Sessionen är redan borta, allt är lugnt


# 📸 Alltid synlig: Ladda upp bild för identifiering
st.subheader("📷 Ladda upp en bild på ogräs")
uploaded_file = st.file_uploader("Välj en bild (JPG/JPEG)", type=["jpg", "jpeg"])
if uploaded_file and st.button("🔎 Identifiera ogräset"):
    with st.spinner("🔍 Analyserar bilden..."):
        img_bytes = uploaded_file.read()
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")

        response = requests.post(
            IDENTIFY_API_URL,
            data=img_b64,
            headers={"Content-Type": "application/octet-stream"},
        )

        if response.status_code == 200:
            result = response.json().get("result", "Inget resultat mottaget.")
            st.session_state.messages.append(("Väderannika", result))
        else:
            st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))

    st.rerun()

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            formatted_message = lex_message
            #formatted_message = re.sub(r'(?m)^([^:\n]+?):', r'**\1:**', lex_message)
            #formatted_message = re.sub(r'(?m)^(?!.*\*\*)([^:\n]+?):', r'**\1:**', lex_message)
            #formatted_message = re.sub(r'(?m)^[^\S\r\n]*[^\*\n]*?([^:\n]+?):', r'**\1:**', lex_message)
            #formatted_message = re.sub(r'(?m)^(?!\s*\*\*)([^:\n]+?):', r'**\1:**', lex_message)
            #formatted_message = re.sub(r'(?m)^(?!.*Bedömning)([^:\n]+?):', r'**\1:**', lex_message)
            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()

# Tagit bort regex helt samt annan layout för bildhantering

import streamlit as st 
import boto3
import uuid
import re
import base64
import requests

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"
IDENTIFY_API_URL = "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️ som också kan allt om ogräs och ogräsbekämpning")

# 🧹 Rensa konversation
if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []

    #  Rensa även AWS Lex-sessionen om den inte redan blivit inaktiv
    try:
        lex_client.delete_session(
        botId=LEX_BOT_ID,
        botAliasId=LEX_BOT_ALIAS_ID,
        localeId=LEX_LOCALE_ID,
        sessionId=st.session_state.session_id
    )
    except lex_client.exceptions.ResourceNotFoundException:
        pass  # Sessionen är redan borta, allt är lugnt


# 📸 Interaktiv: Ladda upp en bild på ogräs
with st.expander("📷 Klicka här för att identifiera ogräs från bild"):
    uploaded_file = st.file_uploader("Välj en bild (JPG/JPEG)", type=["jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="⬆️ Din uppladdade bild", use_container_width=True)

        if st.button("🔎 Identifiera ogräset"):
            with st.spinner("🔍 Analyserar bilden..."):
                img_bytes = uploaded_file.read()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")

                response = requests.post(
                    IDENTIFY_API_URL,
                    data=img_b64,
                    headers={"Content-Type": "application/octet-stream"},
                )

                if response.status_code == 200:
                    result = response.json().get("result", "Inget resultat mottaget.")
                    st.session_state.messages.append(("Väderannika", result))
                else:
                    st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))

            st.rerun()

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            formatted_message = lex_message
        
            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()



# Även bilden försvinner när man trycker rensa konversation. Tillägg för det finns i rensa
# konversation samt själva bilduppläggningen samt separat block för att rensa Lex sessionen.

import streamlit as st 
import boto3
import uuid
import re
import base64
import requests

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"
IDENTIFY_API_URL = "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify"

# 🧠 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🤖 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 Titel och instruktion
st.title("💬 Väderannika")
st.subheader("Din personliga väderassistent ☁️ som också kan allt om ogräs och ogräsbekämpning")

if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []
    st.session_state.uploaded_file = None
    st.session_state.reset_uploader = True  # 🔁 Tvingar ny key för file_uploader
    st.rerun()  # ⬅️ Detta gör att filuppladdaren nollställs "på riktigt"

    # 🧼 Rensa även AWS Lex-sessionen
    try:
        lex_client.delete_session(
            botId=LEX_BOT_ID,
            botAliasId=LEX_BOT_ALIAS_ID,
            localeId=LEX_LOCALE_ID,
            sessionId=st.session_state.session_id
        )
    except lex_client.exceptions.ResourceNotFoundException:
        pass

import uuid  # Se till att detta finns överst i scriptet

# 📸 Interaktiv: Ladda upp en bild på ogräs
# 🟡 Dynamisk key hanterar "reset" av file_uploader
dynamic_key = "file_upload" if not st.session_state.get("reset_uploader") else str(uuid.uuid4())

with st.expander("📷 Klicka här för att identifiera ogräs från bild"):
    uploaded_file = st.file_uploader("Välj en bild (JPG/JPEG)", type=["jpg", "jpeg"], key=dynamic_key)

    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file

    if st.session_state.get("uploaded_file"):
        st.image(st.session_state.uploaded_file, caption="⬆️ Din uppladdade bild", use_container_width=True)

        if st.button("🔎 Identifiera ogräset"):
            with st.spinner("🔍 Analyserar bilden..."):
                img_bytes = st.session_state.uploaded_file.read()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")

                response = requests.post(
                    IDENTIFY_API_URL,
                    data=img_b64,
                    headers={"Content-Type": "application/octet-stream"},
                )

                if response.status_code == 200:
                    result = response.json().get("result", "Inget resultat mottaget.")
                    st.session_state.messages.append(("Väderannika", result))
                else:
                    st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))

            st.rerun()

# 🧼 Rensa "reset"-flaggan efter användning
if st.session_state.get("reset_uploader"):
    st.session_state.reset_uploader = False

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🙋‍♂️ <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            formatted_message = lex_message
        
            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()


#Ytterligare justering för att kunna hämta en bild på första försöket i en ny konversation (efter rensnin)

import streamlit as st  
import boto3
import uuid
import re
import base64
import requests

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"
IDENTIFY_API_URL = "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify"

# 🧐 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = str(uuid.uuid4())

# 🧠 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🗒 Titel och instruktion
st.title("💬 Väderannika🌞")
st.subheader("Din personliga väderassistent som också kan allt om ogräs och ogräsbekämpning")

if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []
    st.session_state.uploaded_file = None
    st.session_state.uploader_key = str(uuid.uuid4())  # 🔁 Tvinga ny file_uploader-key
    
    # 🎧 Rensa även AWS Lex-sessionen
    try:
        lex_client.delete_session(
            botId=LEX_BOT_ID,
            botAliasId=LEX_BOT_ALIAS_ID,
            localeId=LEX_LOCALE_ID,
            sessionId=st.session_state.session_id
        )
    except lex_client.exceptions.ResourceNotFoundException:
        pass

    st.rerun()

# 📸 Interaktiv: Ladda upp en bild på ogräs
with st.expander("📷 Klicka här för att identifiera ogräs från bild"):
    uploaded_file = st.file_uploader("Välj en bild (JPG/JPEG)", type=["jpg", "jpeg"], key=st.session_state.uploader_key)

    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file

    if st.session_state.get("uploaded_file"):
        st.image(st.session_state.uploaded_file, caption="⬆️ Din uppladdade bild", use_container_width=True)

        if st.button("🔎 Identifiera ogräset"):
            with st.spinner("🔍 Analyserar bilden..."):
                img_bytes = st.session_state.uploaded_file.read()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")

                response = requests.post(
                    IDENTIFY_API_URL,
                    data=img_b64,
                    headers={"Content-Type": "application/octet-stream"},
                )

                if response.status_code == 200:
                    result = response.json().get("result", "Inget resultat mottaget.")
                    st.session_state.messages.append(("Väderannika", result))
                else:
                    st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))

            st.rerun()

# 💬 Visa chatt
for sender, message in st.session_state.messages:
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🤛 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )

# ✍️ Input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )

            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🤖"
            )

            formatted_message = lex_message
            st.session_state.messages.append(("Väderannika", formatted_message))

        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))

    st.rerun()

'''
import streamlit as st  
import boto3
import uuid
import re
import base64
import requests

# 🔧 AWS Lex config
LEX_BOT_ID = "9GZWYDPS5T"
LEX_BOT_ALIAS_ID = "TSTALIASID"
LEX_LOCALE_ID = "sv_SE"
AWS_REGION = "eu-central-1"
IDENTIFY_API_URL = "https://hqgt82fq98.execute-api.eu-central-1.amazonaws.com/prod/identify"

# 🧐 Session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = str(uuid.uuid4())

# 🧠 Lex client
lex_client = boto3.client("lexv2-runtime", region_name=AWS_REGION)

# 🎨 UI-style
st.markdown("""
    <style>
        .chat-bubble {
            padding: 1rem;
            border-radius: 1rem;
            margin: 0.5rem 0;
            max-width: 85%;
        }
        .user-bubble {
            background-color: #2c2f33;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #40444b;
            color: white;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
        }
        a {
            color: #1f77b4;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# 🗒 Titel och instruktion
st.title("💬 Väderannika🌞")
st.subheader("Din personliga väderassistent som också kan allt om ogräs och ogräsbekämpning")

if st.button("🗑️ Rensa konversation"):
    st.session_state.messages = []
    st.session_state.uploaded_file = None
    st.session_state.uploader_key = str(uuid.uuid4())
    try:
        lex_client.delete_session(
            botId=LEX_BOT_ID,
            botAliasId=LEX_BOT_ALIAS_ID,
            localeId=LEX_LOCALE_ID,
            sessionId=st.session_state.session_id
        )
    except lex_client.exceptions.ResourceNotFoundException:
        pass
    st.rerun()

# 📸 Interaktiv: Ladda upp en bild på ogräs
with st.expander("📷 Klicka här för att identifiera ogräs från bild"):
    uploaded_file = st.file_uploader("Välj en bild (JPG/JPEG)", type=["jpg", "jpeg"], key=st.session_state.uploader_key)
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file

    if st.session_state.get("uploaded_file"):
        st.image(st.session_state.uploaded_file, caption="⬆️ Din uppladdade bild", use_container_width=True)
        if st.button("🔎 Identifiera ogräset"):
            with st.spinner("🔍 Analyserar bilden..."):
                img_bytes = st.session_state.uploaded_file.read()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")
                response = requests.post(
                    IDENTIFY_API_URL,
                    data=img_b64,
                    headers={"Content-Type": "application/octet-stream"},
                )
                if response.status_code == 200:
                    result = response.json().get("result", "Inget resultat mottaget.")
                    st.session_state.messages.append(("Väderannika", result))
                else:
                    st.session_state.messages.append(("Väderannika", f"Något gick fel vid bildanalysen: {response.text}"))
            st.rerun()

# ✍️ Input (nu överst)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Skriv här...", placeholder="Vad vill du veta om väder och ogrässituationen?")
    submitted = st.form_submit_button("Skicka")

# 📨 Skicka till Lex
if submitted and user_input:
    st.session_state.messages.append(("Du", user_input))
    with st.spinner("⏳ Väderannika tänker..."):
        try:
            response = lex_client.recognize_text(
                botId=LEX_BOT_ID,
                botAliasId=LEX_BOT_ALIAS_ID,
                localeId=LEX_LOCALE_ID,
                sessionId=st.session_state.session_id,
                text=user_input,
            )
            lex_message = (
                response["messages"][0]["content"]
                if "messages" in response and response["messages"]
                else "Inget svar från Väderannika 🧠"
            )
            st.session_state.messages.append(("Väderannika", lex_message))
        except Exception as e:
            st.session_state.messages.append(("Väderannika", f"Något gick fel: {e}"))
    st.rerun()

# 📌 Visa chatt (senaste meddelanden först)
for sender, message in reversed(st.session_state.messages):
    if sender == "Du":
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble user-bubble">🫋 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div class="chat-container"><div class="chat-bubble bot-bubble">🤖 <strong>{sender}:</strong><br>{message}</div></div>""",
            unsafe_allow_html=True
        )
