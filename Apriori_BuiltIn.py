import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

def select_amazon():
    print("The store you selected is Amazon")
    file_name = "amazon_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    dataset = [transaction.split(', ') for transaction in transaction_list]
    return dataset

def select_bestbuy():
    print("The store you selected is Best Buy")
    file_name = "bestbuy_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    dataset = [transaction.split(', ') for transaction in transaction_list]
    return dataset

def select_nike():
    print("The store you selected is Nike")
    file_name = "nike_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    dataset = [transaction.split(', ') for transaction in transaction_list]
    return dataset

def select_kmart():
    print("The store you selected is KMart")
    file_name = "kmart_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    dataset = [transaction.split(', ') for transaction in transaction_list]
    return dataset

def select_homedepot():
    print("The store you selected is Home Depot")
    file_name = "homedepot_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    dataset = [transaction.split(', ') for transaction in transaction_list]
    return dataset

def main():
    while True:
        print("Please select the store")
        print("1. Amazon")
        print("2. Best Buy")
        print("3. Nike")
        print("4. KMart")
        print("5. Home Depot")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dataset = select_amazon()
            break 
        elif choice == '2':
            dataset = select_bestbuy()
            break 
        elif choice == '3':
            dataset = select_nike()
            break
        elif choice == '4':
            dataset = select_kmart()
            break
        elif choice == '5':
            dataset = select_homedepot()
            break
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid Choice. Please try again.")

    if choice in ['1', '2', '3', '4', '5']:
        min_support = float(input("Enter minimum support (0-1):"))
        min_confidence = float(input("Enter minimum confidence (0-1):"))
        if min_support > 1:
            min_support = 1
        elif min_support <= 0:
            min_support = 0.1
        elif min_confidence > 1:
            min_confidence = 1
        elif min_confidence <= 0:
            min_confidence = 0.1
         
    return dataset, min_support, min_confidence

dataset, min_support, min_confidence = main()

dataset

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)

df = pd.DataFrame(te_ary, columns = te.columns_)
pd.set_option('display.max_colwidth', None)
df

min_support, min_confidence

freq_itemsets = apriori(df, min_support, use_colnames=True)
freq_itemsets

res = association_rules(freq_itemsets, metric = "confidence", min_threshold = min_confidence)
res

res1 = res[['antecedents', 'consequents', 'support', 'confidence']]
res1 

if not res1.empty:
    for index, row in res1.iterrows():
        print(f"Rule: {row['antecedents']} -> {row['consequents']}, \nSupport: {row['support']}, \nConfidence: {row['confidence']}\n")
else:
    print("NO ASSOCIATION RULES FOUND")

fpgrowth(df, min_support)

frequent_itemsets = fpgrowth(df, min_support, use_colnames=True)
frequent_itemsets

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold = min_confidence)
rules

if not rules.empty:
    for index, row in res1.iterrows():
        print(f"Rule: {row['antecedents']} -> {row['consequents']}, \nSupport: {row['support']}, \nConfidence: {row['confidence']}\n")
else:
    print("NO ASSOCIATION RULES FOUND")

%timeit apriori(df, min_support)

%timeit fpgrowth(df, min_support)



