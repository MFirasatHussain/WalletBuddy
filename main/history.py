from main import helper
import logging

group_expenses_file = "group_expenses.json"


def run(message, bot):
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_data = helper.getUserData(chat_id)

        if user_data is None:
            raise Exception("Sorry! No spending records found!")

        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_data) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_data["data"]:
                spend_total_str += str(rec) + "\n"

            transactions_list = helper.read_json(group_expenses_file)
            for transaction_id in user_data["transactions"]:
                if transaction_id not in transactions_list:
                    raise Exception("An unknown transaction was found in your records, please try again later.")
                txn = transactions_list[transaction_id]
                rec = txn["created_at"] + "," + txn["category"] + "," + str(txn["members"][str(chat_id)])
                spend_total_str += str(rec) + "\n"

        bot.send_message(chat_id, spend_total_str)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))
