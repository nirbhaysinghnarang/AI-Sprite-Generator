from driver import img_create
import streamlit as st
import json
import os



st.title("SpriteAI ")
desc = st.text_input("Enter a description here")
st.caption("Enter a physical description of a person, be as descriptive as possible!")
submit = st.button("Submit🚀")
if submit:
    st.header("Result 👉🏻")
    st.image(img_create(description=desc))   
st.link_button("Built by Nirbhay S.", "https://www.nirbhaysinghnarang.com")

st.caption("""
Sprites by: Johannes Sjölund (wulax),
Michael Whitlock (bigbeargames),
Matthew Krohn (makrohn), Nila122, 
David Conway Jr. (JaidynReiman),
Carlo Enrico Victoria (Nemisys), 
Thane Brimhall (pennomi), bluecarrot16, 
Luke Mehl, Benjamin K. Smith (BenCreating),
ElizaWy, MuffinElZangano, Durrani, kheftel, Stephen Challener 
(Redshrike), TheraHedwig, Evert, Pierre Vigier (pvigier), Eliza Wyatt (ElizaWy),
Johannes Sj?lund (wulax), Sander Frenken (castelonia), dalonedrau, Lanea Zimmerman (Sharm),
laetissima, kirts, Mark Weyer, Joe White, Mandi Paugh, William.Thompsonj, Manuel Riecke (MrBeast), 
Barbara Riviera, thecilekli, Yamilian, Fabzy, Skorpio, Radomir Dopieralski, Emilio J. Sanchez-Sierra,
kcilds/Rocetti/Eredah, Cobra Hubbard (BlueVortexGames), DCSS authors, Marcel van de Steeg (MadMarcel), 
DarkwallLKE, Charles Sanchez (CharlesGabriel), Shaun Williams, Tuomo Untinen (reemax), Stafford McIntyre, 
PlatForge project, Tracy, Daniel Eddeland (daneeklu), William.Thomsponj, Joshua Taylor, Zi Ye, AntumDeluge,
drjamgo@hotmail.com, Lori Angela Nagel (jastiv), gr3yh47, pswerlang, XOR, tskaufma, Inboxninja, Dr. Jamgo, 
LordNeo 
Sprites contributed as part of the Liberated Pixel Cup project from OpenGameArt.org: 
http://opengameart.org/content/lpc-collection License: Creative Commons Attribution-ShareAlike 3.0 (CC-BY-SA 3.0) http://creativecommons.org/licenses/by-sa/3.0/            
""")