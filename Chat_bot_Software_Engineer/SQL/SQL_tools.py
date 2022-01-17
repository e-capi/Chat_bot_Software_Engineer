import sqlite3

#GET sale_if from merchant_id

def get_sale_id_SQL(merchant_id):

    #/!\ SQL Hardcoded Implement Cloud SQL on GCP
    conn = sqlite3.connect('/home/ecapi/code/e-capi/Chat_bot_Software_Engineer/Chat_bot_Software_Engineer/data/simulation-db')
    c = conn.cursor()
    query = """
        SELECT id_sale
        FROM sales
        WHERE sales.merchant_id = ?
    """
    c.execute(query, (merchant_id,))
    sale_id = c.fetchone()
    return {"id_sale": str(sale_id[0])} #gives a tupple, with a second null arg

#GET receipt info from merchant_id

def get_receipt_info_SQL(merchant_id):

    #/!\ SQL Hardcoded Implement Cloud SQL on GCP
    conn = sqlite3.connect('/home/ecapi/code/e-capi/Chat_bot_Software_Engineer/Chat_bot_Software_Engineer/data/simulation-db')
    c = conn.cursor()
    query = """
        SELECT status, description, value
        FROM receipt
        WHERE receipt.merchant_id = ?
    """
    c.execute(query, (merchant_id,))
    receipt_info = c.fetchone()

    #variables
    status = receipt_info[0]
    description = receipt_info[1]
    value = receipt_info[2]

    answ_dict = {'status':status, 'description': description, 'value': value }
    return answ_dict

#GET chip status from merchant_id
def get_chip_id_SQL(merchant_id):

    #/!\ SQL Hardcoded Implement Cloud SQL on GCP
    conn = sqlite3.connect('/home/ecapi/code/e-capi/Chat_bot_Software_Engineer/Chat_bot_Software_Engineer/data/simulation-db')
    c = conn.cursor()
    query = """
        SELECT chip_id
        FROM sales
        WHERE sales.merchant_id = ?
    """
    c.execute(query, (merchant_id,))
    chip_id = c.fetchone()
    return {"chip_id": str(chip_id[0])} #gives a tupple, with a second null arg

#GET transactions from merchant_id

def get_transactions_info_SQL(merchant_id):

    #/!\ SQL Hardcoded Implement Cloud SQL on GCP
    conn = sqlite3.connect('/home/ecapi/code/e-capi/Chat_bot_Software_Engineer/Chat_bot_Software_Engineer/data/simulation-db')
    c = conn.cursor()
    query = """
        SELECT transaction_id, created_at, value
        FROM transactions
        WHERE transactions.merchant_id = ?
    """
    c.execute(query, (merchant_id,))
    transactions_info = c.fetchall()

    return transactions_info #returns a list of transaction_id, created_at, value

#GET aggregated transactions from merchant_id

def get_transactions_aggregate_SQL(merchant_id): #for now initialize to first act conv

    #/!\ SQL Hardcoded Implement Cloud SQL on GCP
    conn = sqlite3.connect('/home/ecapi/code/e-capi/Chat_bot_Software_Engineer/Chat_bot_Software_Engineer/data/simulation-db')
    c = conn.cursor()
    query = """
        SELECT COUNT(transaction_id) as total_transactions, SUM(value) as total_value
        FROM transactions
        WHERE transactions.merchant_id = ?
    """
    c.execute(query, (merchant_id,))
    transactions_aggregation = c.fetchone()

    #variables
    transactions_amount = transactions_aggregation[0]
    transactions_value = transactions_aggregation[1]


    answ_dict = {'transactions_amount':transactions_amount, 'transactions_value': transactions_value }
    return answ_dict
