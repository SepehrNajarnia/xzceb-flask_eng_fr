import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('wH2aZD6esw3N6f7RkTuHNhCDoq_reXkeQIvwCXifFh8i')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/575985a6-4deb-47fa-9047-f96b3c3f3da7'
    )

def english_to_french(english_text):
    #Translate from English to French
    frenchtranslation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(french_text):
    #Translate from French to English
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
