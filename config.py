live_trade = True

coin     = ["BTC", "ETH" "SOL", "GRT", "KSM", "BNB", "AAVE", "HNT", "ADA", "DOT"]
quantity = [0.002, 0.03, 1, 50, 0.2, 0.12, 0.2, 3, 40, 2]


# profit_margin * leverage = Actual Profit Percentage.
profit_margin = 2

# ====================================================
#        !! DO NOT CHANGE THE LEVERAGE !!
# ====================================================
leverage, pair = [], []
for i in range(len(coin)):
    pair.append(coin[i] + "USDT")
    if   coin[i] == "BTC": leverage.append(50)
    elif coin[i] == "ETH": leverage.append(40)
    else: leverage.append(25)

    print("Pair Name        :   " + pair[i])
    print("Trade Quantity   :   " + str(quantity[i]) + " " + coin[i])
    print("Leverage         :   " + str(leverage[i]))
    print()
