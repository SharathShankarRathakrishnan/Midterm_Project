from itertools import combinations
import csv
import pandas as pd
import time

def countof_itemsets(split_transaction_list):
    total_transactions = len(split_transaction_list)
    counts = dict()
    
    for tritem in split_transaction_list:
        for item in tritem:
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] += 1
    
    return counts, total_transactions

def check_support(counts, total_transactions, min_support, frequent_items):
    support = dict()
    freq_list = list()
    
    for item, count in counts.items():
        support[item] = count / total_transactions

    for item, sup in support.items():
        if sup >= min_support:
            frequent_items.update({item : sup})
            freq_list.append(item)

    return frequent_items, freq_list

def get_combinations(freq_list, frequent_items, split_transaction_list, total_transactions, min_support, length):
    combi_counts = dict()  

    if freq_list:
        combi = list(combinations(freq_list, length))  
        
        for tritem in split_transaction_list:
            for comb in combi:
                if set(comb).issubset(tritem):
                    if comb not in combi_counts:
                        combi_counts[comb] = 1
                    else:
                        combi_counts[comb] += 1
    
    next_frequent_items = frequent_items
    next_freq_list = list()
    if combi_counts:                   
        next_frequent_items, next_freq_list = check_support(combi_counts, total_transactions, min_support, frequent_items)

    if next_freq_list:
        get_combinations(freq_list, frequent_items, split_transaction_list, total_transactions, min_support, length+1)

    return next_frequent_items, next_freq_list

def generate_association_rules(next_frequent_items, min_confidence):
    rules = []
    
    for itemset in next_frequent_items:
        if isinstance(itemset, tuple) and len(itemset) > 1:
            for i in range(1, len(itemset)):
                subsets = list(combinations(itemset, i))
                for subset in subsets:
                    antecedent = subset
                    consequent = tuple(set(itemset) - set(subset))
                    if len(consequent) > 0:
                        if len(antecedent) == 1:
                            antecedent_support = next_frequent_items[antecedent[0]]
                        else:
                            antecedent_support = next_frequent_items[antecedent]
                        itemset_support = next_frequent_items[itemset]
                        confidence = itemset_support / antecedent_support
                        if confidence >= min_confidence:
                            rules.append((antecedent, consequent, itemset_support, confidence))
    
    return rules

def select_amazon():
    print("The store you selected is Amazon")
    file_name = "amazon_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Item Name"])
    item_list = df["Item Name"].tolist()
    cleaned_item_list = [item for item in item_list if pd.notna(item)]

    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    split_transaction_list = [transaction.split(', ') for transaction in transaction_list]

    return cleaned_item_list, split_transaction_list

def select_bestbuy():
    print("The store you selected is Best Buy")
    file_name = "bestbuy_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Item Name"])
    item_list = df["Item Name"].tolist()
    cleaned_item_list = [item for item in item_list if pd.notna(item)]

    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    split_transaction_list = [transaction.split(', ') for transaction in transaction_list]

    return cleaned_item_list, split_transaction_list

def select_nike():
    print("The store you selected is Nike")
    file_name = "nike_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Item Name"])
    item_list = df["Item Name"].tolist()
    cleaned_item_list = [item for item in item_list if pd.notna(item)]

    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    split_transaction_list = [transaction.split(', ') for transaction in transaction_list]

    return cleaned_item_list, split_transaction_list

def select_kmart():
    print("The store you selected is KMart")
    file_name = "kmart_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Item Name"])
    item_list = df["Item Name"].tolist()
    cleaned_item_list = [item for item in item_list if pd.notna(item)]

    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    split_transaction_list = [transaction.split(', ') for transaction in transaction_list]

    return cleaned_item_list, split_transaction_list

def select_homedepot():
    print("The store you selected is Home Depot")
    file_name = "homedepot_transactions.csv"
    df = pd.read_csv(file_name, usecols=["Item Name"])
    item_list = df["Item Name"].tolist()
    cleaned_item_list = [item for item in item_list if pd.notna(item)]

    df = pd.read_csv(file_name, usecols=["Transaction"])
    transaction_list = df["Transaction"].tolist()
    split_transaction_list = [transaction.split(', ') for transaction in transaction_list]

    return cleaned_item_list, split_transaction_list

start_time = time.perf_counter()
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
            cleaned_item_list, split_transaction_list = select_amazon()
            break 
        elif choice == '2':
            cleaned_item_list, split_transaction_list = select_bestbuy()
            break
        elif choice == '3':
            cleaned_item_list, split_transaction_list = select_nike()
            break
        elif choice == '4':
            cleaned_item_list, split_transaction_list = select_kmart()
            break
        elif choice == '5':
            cleaned_item_list, split_transaction_list = select_homedepot()
            break
        elif choice == '6':
            print("Exiting the program.")
            return
        else:
            print("Invalid Choice. Please try again.")

    if choice in ['1', '2', '3', '4', '5']:
        min_support = float(input("Enter minimum support in the range 0 to 1:"))
        min_confidence = float(input("Enter minimum confidence in the range 0 to 1:"))
        if min_support > 1 and min_confidence > 1:
            min_support = min_confidence = 1
        elif min_support <= 0 and min_confidence <= 0:
            min_support = min_confidence = 0.1

    frequent_items = dict()
    
    counts, total_transactions = countof_itemsets(split_transaction_list)
    frequent_items, freq_list = check_support(counts, total_transactions, min_support, frequent_items)
    next_frequent_items, next_freq_list = get_combinations(freq_list, frequent_items, split_transaction_list, total_transactions, min_support, length=2)

    print("\nFREQUENT ITEMSETS:\n")
    for itemset, support in next_frequent_items.items():
        print(f"{itemset}: {support}\n")

    rules = generate_association_rules(next_frequent_items, min_confidence)
    
    print("\nASSOCIATION RULES:")
    for antecedent, consequent, support, confidence in rules:
        print(f"\n{antecedent} => {consequent} (support: {support:.2f})(confidence: {confidence:.2f})")

main()

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\nTotal execution time: {elapsed_time:.4f} seconds")



