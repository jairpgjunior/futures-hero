live_trade      = True    # False to see the output & verify your API key is working
troubleshooting = False   # Troubleshooting mode for @zyairelai

# ====================================================
#                  User Settings
# ====================================================
coin     = ["BTC", "ETH"]
quantity = [0.001, 0.01]
leverage, pair = [], []

# ====================================================
#        !! DO NOT CHANGE THESE SETTINGS !!
# ====================================================
pair = []
for i in range(len(coin)):
    pair.append(coin[i] + "USDT")
    if   coin[i] == "BTC": leverage.append(50)
    elif coin[i] == "ETH": leverage.append(40)
    else: leverage.append(30)
    print("Pair Name        :   " + pair[i])
    print("Trade Quantity   :   " + str(quantity[i]) + " " + coin[i])
    print("Leverage         :   " + str(leverage[i]))
    print()
