# AI-IoT Grupp 6 – Växtvärk AB 🌱🤖

Detta är ett AI- och IoT-projekt skapat av Grupp 6, där vi utvecklat ett system som hjälper lantbrukare att identifiera ogräs, få väderinformation och rekommendationer kring sprutförhållanden.

Projektet består av:
- En **frontend-applikation i Streamlit** för interaktion
- En **backend i AWS Lambda** som hanterar Lex, Rekognition och API-anrop
- Användning av tjänster som **Amazon Lex, Rekognition, S3, SMHI API** och OpenCage Geocoding

---

## 📁 Projektstruktur

```
.
├── streamlit_app/
│   └── app.py               # Streamlit-baserat gränssnitt
│
├── lambda/
│   └── lambda_function.py   # AWS Lambda-kod (kommer senare)
│
├── .env.example             # Exempelfil för miljövariabler
├── requirements.txt         # Paket som krävs för att köra appen lokalt
└── README.md                # Denna fil
```

---

## 🛠 Installation (lokalt)

1. **Klona repot:**
   ```bash
   git clone https://github.com/WilliamCelik/AI-IoT-Grupp-6.git
   cd AI-IoT-Grupp-6
   ```

2. **Skapa en `.env`-fil** baserat på `.env.example` och fyll i:
   ```
   LEX_BOT_ID=din-bot-id
   LEX_BOT_ALIAS_ID=din-alias-id
   LEX_LOCALE_ID=sv_SE
   AWS_REGION=eu-central-1
   ```

3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Kör appen:**
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## 🧪 Funktioner

- 💬 Ställ frågor till väderassistenten via Amazon Lex
- 🌦 Hämta väderdata via SMHI
- 🧠 Identifiera ogräs med bilduppladdning (Rekognition)
- 🧴 Få råd om sprutförhållanden
- 🧾 Få information om ogräs och herbicider

---

## 🔐 Säkerhet

Känsliga nycklar och ARN:er ska **inte** läggas in i denna publika repo. All autentisering sker via miljövariabler.

---

## 📄 Dokument

Se mappen för teknisk dokumentation:
- `Växtvärk AB.docx`
- `Technical Draft Växtvärk AB.docx`
- `Final Group Project - AI-IOT.docx`
