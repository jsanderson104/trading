import sys,os

# Defaults
AccountBalance = 35000;
SL = .25;
TP = SL * 2;


def clear_terminal():
    """
    Clears the terminal screen based on the operating system.
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (Unix-like systems)
    else:
        _ = os.system('clear')

# Call the function to clear the terminal
clear_terminal()

print(" POSITION SIZE CALCULATOR ");

print("Account Balanace: ",end=" ");
AccountBalance = input();
AccountBalance = float(AccountBalance);

print('Risk Tolerance %: ',end=" ");
RiskTolerance = input(); RiskTolerance = float(RiskTolerance); RiskTolerance = RiskTolerance/100;


print('Option Price:' , end=" ");
OptionPrice = input(); OptionPrice = float(OptionPrice); OptionPrice = OptionPrice/100;

# How much of my account to use for collateral. This is not the STOPLOSS
CollateralNeeded = AccountBalance * RiskTolerance;

# STOP-LOSS CALCS
print('Stop-Loss % of Position (def: 25%) :',end=" ");
StopLossPercent = input();
StopLossPercent = int(StopLossPercent);
SL = float(StopLossPercent/100);

# Take-PROFIT CALCS
print('Take-Profit % of Position (def: 50%) :',end=" ");
TakeProfitPercent = input();
TakeProfitPercent = int(TakeProfitPercent);
TP = float(TakeProfitPercent/100);

# Calculate prices of the option that I want to EXIT position with.
StopOutPrice = OptionPrice - (OptionPrice * SL) ;
TakeProfitPrice = OptionPrice + (OptionPrice * TP) ;

# How much am I risking per option?
CapitalRiskPerOption = (OptionPrice*100) * SL;
CapitalGainPerOption = (OptionPrice*100) * TP;

# Position Size
SizeOfOrder = CollateralNeeded / CapitalRiskPerOption;
SizeOfOrder = int(SizeOfOrder);

StopOutCapitalLoss = SizeOfOrder * CapitalRiskPerOption;
TakeProfitCapitalGain = SizeOfOrder * (CapitalGainPerOption);


print("");
print("========== POSITION DETAILS ========");
print("Potential Loss: " + str(StopOutCapitalLoss) );
print("Potential Gain: " + str(TakeProfitCapitalGain) );
print("Capital Risk Tolerance: " + str(CollateralNeeded));
print("Stop-Out Price: " + str(round(StopOutPrice,2)));
print("Take-Profit Price: " + str(round(TakeProfitPrice,2)));
print("How many to purchase: " + str(SizeOfOrder));
print("");
