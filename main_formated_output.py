#main

def is_float(s):
    # Define valid characters for a floating-point number
    valid_chars = set("0123456789.-")
    
    # Remove non-valid characters from the string
    cleaned_string = ''.join(char for char in s if char in valid_chars)
    
    # Attempt to convert the cleaned string to a float
    try:
        float(cleaned_string)
        return True
    except ValueError:
        return False


def clean_float_string(s):
    # Define valid characters for a floating-point number
    valid_chars = set("0123456789.-")
    
    # Iterate through each character in the string until a non-valid character or a second decimal point is encountered
    cleaned_chars = []
    decimal_point_seen = False
    for char in s:
        if char in valid_chars:
            if char == '.':
                if decimal_point_seen:
                    break  # Stop iteration if a second decimal point is encountered
                decimal_point_seen = True
            cleaned_chars.append(char)
        else:
            break  # Stop iteration if a non-valid character is encountered
    
    # Return the cleaned string
    return ''.join(cleaned_chars)


strg = [
    "USOIL sell now @ 80.82\n\ntp @ 77.50\ntp2 @ 73.25\n\nSL @ 82.60",
    "EURCHF buy now @ 0.9616\ntp @ 0.9670\ntp2 @ 0.9760\n\nSL @ 0.9585(31 pips)",
    "EURCAD POSSIBLE SELL\n\nSELL IT @ 1.47718\n\nStop loss @ 1.47834\n\nTake profit @ 1.46571",
    "🟢Sell Aud-Usd now at .6526\nStop loss .6535\ntarget .6476\nTrade Based On M15 Ex-POI \nAfter Mitigation We Have a SCOB also",
    "Buy Gold session Trade now 2125.34\nstop loss 2123.50\ntarget 2128",
    "GBPUSD POSSIBLE BUY SETUP\n\nBUY IT @ 1.26874\n\nStop loss @ 1.26708\n\nTake profit @ 1.27723\n\nTargeting Previous weeks high",
    "Use proper risk management\nNZDCHF SELL @ 0.5435\n\nTP: 0.5415 (scalper) \nTP: 0.5385 (intraday) \nTP: 0.5335 (swing)\nSL: 0.5500\n\n▪️Use money management 2-3%",
    "NZDUSD - BUY 0.6110\n\nTP 0.6130\nTP 0.6160\nTP 0.6210\nSL 0.6020",
    "AUDJPY - SELL 97.37\n\nTP 97.17\nTP 96.87\nTP 96.37\nSL 98.00",
    "GBPUSD Sell now 1.26630\nTP 1.26330\nTP 1.26055 (close 50% profits, SL to BE)\nTP 1.25480\nSL 1.27020\n\nUse Proper Risk Management\nlongterm trade",
    "gold buy limit @ 2024\n\ntp @ 2044\nsl @ 2013",
    "GBPUSD BUY @ 1.2620 / 1.2625\n\nTP: 1.2640 (scalper) \nTP: 1.2670 (intraday) \nTP: 1.2720 (swing)\nSL: 1.2550\n\n▪️Use money management 2-3%"
]


