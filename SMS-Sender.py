from twilio.rest import Client
from dotenv import load_dotenv
import os
import schedule
import time
from datetime import datetime

load_dotenv()
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH"]
client = Client(account_sid, auth_token)


def send():
    with open("Groceries.txt", "r") as f:
        groceries = f.read()

    try:
        message = client.messages.create(
            from_="+your twilio number",
            body=f'{datetime.now()}: {groceries}',
            to="+your phone number",
        )

        print(f"SID:{message.sid} \nStatus:{message.status}")
    except:
        print('error sending SMS')





# Schedule the task to run after 6 days
schedule.every(6).days.do(send)


def main():
    done = False
    # Keep the script running to execute the scheduled task
    while not done:
        # Get the next scheduled event
        next_run = schedule.next_run()

        # Calculate the time remaining
        time_remaining = next_run - datetime.now()

        # Display the time remaining
        print(f"Time remaining until next task execution: {time_remaining}")

        # Check for pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)
        # Check if the task has finished
        if time_remaining.total_seconds() <= 0:
            done = True


if __name__ == '__main__':
    main()
