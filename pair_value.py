#currency pair value
from main_formated_output import *



def pair_func():
    pair = ''

    keyword = [
        "AUDCAD", "AUDCHF", "AUDCNH", "AUDCZK", "AUDDKK", "AUDHKD", "AUDHUF", "AUDJPY", "AUDMXN", "AUDNOK",
        "AUDNZD", "AUDPLN", "AUDSEK", "AUDSGD", "AUDUSD", "AUDZAR", "CADCHF", "CADCNH", "CADCZK", "CADDKK",
        "CADHKD", "CADHUF", "CADJPY", "CADMXN", "CADNOK", "CADPLN", "CADSEK", "CADSGD", "CADZAR", "CHFCNH",
        "CHFCZK", "CHFDKK", "CHFHKD", "CHFHUF", "CHFJPY", "CHFMXN", "CHFNOK", "CHFPLN", "CHFSEK", "CHFSGD",
        "CHFTRY", "CHFZAR", "DKKCZK", "DKKHKD", "DKKHUF", "DKKMXN", "DKKNOK", "DKKPLN", "DKKSEK", "DKKSGD",
        "DKKZAR", "EURAUD", "EURCAD", "EURCHF", "EURCNH", "EURCZK", "EURDKK", "EURGBP", "EURHKD", "EURHUF",
        "EURILS", "EURJPY", "EURMXN", "EURNOK", "EURNZD", "EURPLN", "EURSEK", "EURSGD", "EURTRY", "EURUSD",
        "EURZAR", "GBPAUD", "GBPCAD", "GBPCHF", "GBPCNH", "GBPCZK", "GBPDKK", "GBPHKD", "GBPHUF", "GBPJPY",
        "GBPMXN", "GBPNOK", "GBPNZD", "GBPPLN", "GBPSEK", "GBPSGD", "GBPUSD", "GBPZAR", "JPYCZK", "JPYDKK",
        "JPYHKD", "JPYHUF", "JPYMXN", "JPYNOK", "JPYPLN", "JPYSEK", "JPYSGD", "JPYZAR", "NOKCZK", "NOKHKD",
        "NOKHUF", "NOKMXN", "NOKPLN", "NOKSEK", "NOKSGD", "NOKZAR", "NZDCAD", "NZDCHF", "NZDCZK", "NZDDKK",
        "NZDHKD", "NZDHUF", "NZDJPY", "NZDMXN", "NZDNOK", "NZDPLN", "NZDSEK", "NZDSGD", "NZDUSD", "NZDZAR",
        "USDCAD", "USDCHF", "USDCNH", "USDCZK", "USDDKK", "USDHKD", "USDHUF", "USDILS", "USDJPY", "USDMXN",
        "USDNOK", "USDPLN", "USDSEK", "USDSGD", "USDTRY", "USDZAR",

        "AUD/CAD", "AUD/CHF", "AUD/CNH", "AUD/CZK", "AUD/DKK", "AUD/HKD", "AUD/HUF", "AUD/JPY", "AUD/MXN", "AUD/NOK",
        "AUD/NZD", "AUD/PLN", "AUD/SEK", "AUD/SGD", "AUD/USD", "AUD/ZAR", "CAD/CHF", "CAD/CNH", "CAD/CZK", "CAD/DKK",
        "CAD/HKD", "CAD/HUF", "CAD/JPY", "CAD/MXN", "CAD/NOK", "CAD/PLN", "CAD/SEK", "CAD/SGD", "CAD/ZAR", "CHF/CNH",
        "CHF/CZK", "CHF/DKK", "CHF/HKD", "CHF/HUF", "CHF/JPY", "CHF/MXN", "CHF/NOK", "CHF/PLN", "CHF/SEK", "CHF/SGD",
        "CHF/TRY", "CHF/ZAR", "DKK/CZK", "DKK/HKD", "DKK/HUF", "DKK/MXN", "DKK/NOK", "DKK/PLN", "DKK/SEK", "DKK/SGD",
        "DKK/ZAR", "EUR/AUD", "EUR/CAD", "EUR/CHF", "EUR/CNH", "EUR/CZK", "EUR/DKK", "EUR/GBP", "EUR/HKD", "EUR/HUF",
        "EUR/ILS", "EUR/JPY", "EUR/MXN", "EUR/NOK", "EUR/NZD", "EUR/PLN", "EUR/SEK", "EUR/SGD", "EUR/TRY", "EUR/USD",
        "EUR/ZAR", "GBP/AUD", "GBP/CAD", "GBP/CHF", "GBP/CNH", "GBP/CZK", "GBP/DKK", "GBP/HKD", "GBP/HUF", "GBP/JPY",
        "GBP/MXN", "GBP/NOK", "GBP/NZD", "GBP/PLN", "GBP/SEK", "GBP/SGD", "GBP/USD", "GBP/ZAR", "JPY/CZK", "JPY/DKK",
        "JPY/HKD", "JPY/HUF", "JPY/MXN", "JPY/NOK", "JPY/PLN", "JPY/SEK", "JPY/SGD", "JPY/ZAR", "NOK/CZK", "NOK/HKD",
        "NOK/HUF", "NOK/MXN", "NOK/PLN", "NOK/SEK", "NOK/SGD", "NOK/ZAR", "NZD/CAD", "NZD/CHF", "NZD/CZK", "NZD/DKK",
        "NZD/HKD", "NZD/HUF", "NZD/JPY", "NZD/MXN", "NZD/NOK", "NZD/PLN", "NZD/SEK", "NZD/SGD", "NZD/USD", "NZD/ZAR",
        "USD/CAD", "USD/CHF", "USD/CNH", "USD/CZK", "USD/DKK", "USD/HKD", "USD/HUF", "USD/ILS", "USD/JPY", "USD/MXN",
        "USD/NOK", "USD/PLN", "USD/SEK", "USD/SGD", "USD/TRY", "USD/ZAR",

        "Aud-Cad", "Aud-Chf", "Aud-Cnh", "Aud-Czk", "Aud-Dkk", "Aud-Hkd", "Aud-Huf", "Aud-Jpy", "Aud-Mxn", "Aud-Nok",
        "Aud-Nzd", "Aud-Pln", "Aud-Sek", "Aud-Sgd", "Aud-Usd", "Aud-Zar", "Cad-Chf", "Cad-Cnh", "Cad-Czk", "Cad-Dkk",
        "Cad-Hkd", "Cad-Huf", "Cad-Jpy", "Cad-Mxn", "Cad-Nok", "Cad-Pln", "Cad-Sek", "Cad-Sgd", "Cad-Zar", "Chf-Cnh",
        "Chf-Czk", "Chf-Dkk", "Chf-Hkd", "Chf-Huf", "Chf-Jpy", "Chf-Mxn", "Chf-Nok", "Chf-Pln", "Chf-Sek", "Chf-Sgd",
        "Chf-Try", "Chf-Zar", "Dkk-Czk", "Dkk-Hkd", "Dkk-Huf", "Dkk-Mxn", "Dkk-Nok", "Dkk-Pln", "Dkk-Sek", "Dkk-Sgd",
        "Dkk-Zar", "Eur-Aud", "Eur-Cad", "Eur-Chf", "Eur-Cnh", "Eur-Czk", "Eur-Dkk", "Eur-Gbp", "Eur-Hkd", "Eur-Huf",
        "Eur-Ils", "Eur-Jpy", "Eur-Mxn", "Eur-Nok", "Eur-Nzd", "Eur-Pln", "Eur-Sek", "Eur-Sgd", "Eur-Try", "Eur-Usd",
        "Eur-Zar", "Gbp-Aud", "Gbp-Cad", "Gbp-Chf", "Gbp-Cnh", "Gbp-Czk", "Gbp-Dkk", "Gbp-Hkd", "Gbp-Huf", "Gbp-Jpy",
        "Gbp-Mxn", "Gbp-Nok", "Gbp-Nzd", "Gbp-Pln", "Gbp-Sek", "Gbp-Sgd", "Gbp-Usd", "Gbp-Zar", "Jpy-Czk", "Jpy-Dkk",
        "Jpy-Hkd", "Jpy-Huf", "Jpy-Mxn", "Jpy-Nok", "Jpy-Pln", "Jpy-Sek", "Jpy-Sgd", "Jpy-Zar", "Nok-Czk", "Nok-Hkd",
        "Nok-Huf", "Nok-Mxn", "Nok-Pln", "Nok-Sek", "Nok-Sgd", "Nok-Zar", "Nzd-Cad", "Nzd-Chf", "Nzd-Czk", "Nzd-Dkk",
        "Nzd-Hkd", "Nzd-Huf", "Nzd-Jpy", "Nzd-Mxn", "Nzd-Nok", "Nzd-Pln", "Nzd-Sek", "Nzd-Sgd", "Nzd-Usd", "Nzd-Zar",
        "Usd-Cad", "Usd-Chf", "Usd-Cnh", "Usd-Czk", "Usd-Dkk", "Usd-Hkd", "Usd-Huf", "Usd-Ils", "Usd-Jpy", "Usd-Mxn",
        "Usd-Nok", "Usd-Pln", "Usd-Sek", "Usd-Sgd", "Usd-Try", "Usd-Zar",

        'USOIL', 'NAS100', 'US30', 'XAUUSD', 'Gold', 'gold', 'GOLD'
        ]

    cnt = 0

    for str in strg:
        cnt += 1
        print(cnt)
        for keywrd in keyword:
            if str.find(keywrd) == -1:
                continue
            else:
                pair = keywrd
                return(pair)


