# Step 1: Import necessary modules
import os
import json
from openai import OpenAI
from data import training_data, validation_data

# AI-GEN START - cursor
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
# AI-GEN END


# Step 2: Initialize the OpenAI client with the API key from environment variables
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

# Step 3: Define the names of the training and validation data files
training_file_name = "training_data.jsonl"
validation_file_name = "validation_data.jsonl"

training_file="file-j6VyeNbItlF7Q6LHNqEUSkEz"
validation_file="file-FkXdQLATD41Yh3LYEVcZUTUo"

if not training_file or not validation_file:
  # Step 4: Function to prepare data and write it to a JSONL file

  # AI-GEN START - cursor
  def prepare_data(data, file_name):
      """
      Prepares data and writes it to a JSONL file.

      Args:
          data (list): A list of dictionaries containing the data.
          file_name (str): The name of the file to write the data to.
      """
      with open(file_name, 'w') as f:
          f.write('\n'.join(json.dumps(entry) for entry in data) + '\n')

  # AI-GEN END


  # Step 5: Call the prepare_data function for both training and validation data
  prepare_data(training_data, training_file_name)
  prepare_data(validation_data, validation_file_name)

  # Step 6: Upload the training data file to OpenAI and get the file ID


  training_file = client.files.create(
      file=open(training_file_name, 'rb'),
      purpose='fine-tune'
  ).id

  # Step 7: Upload the validation data file to OpenAI and get the file ID
  validation_file = client.files.create(
      file=open(validation_file_name, 'rb'),
      purpose='fine-tune'
  ).id
  # Step 8: Print the file IDs for reference

  print(f"Training file ID: {training_file}")
  print(f"Validation file ID: {validation_file}")
  import pdb; pdb.set_trace()

# Step 9: Create a fine-tuning job with the uploaded files and specific hyperparameters

# AI-GEN START - cursor
job = client.fine_tuning.jobs.create(
    training_file=training_file,
    validation_file=validation_file,
    model="davinci-002",
    hyperparameters={
#        "batch_size": 3,
 #       "learning_rate_multiplier": 0.3,
  #      "n_epochs": 15
    }
)
# AI-GEN END


# Step 10: Retrieve the job ID and status from the response
status = client.fine_tuning.jobs.retrieve(job.id).status


# Step 11: Print the job ID and initial status
print(f"Job ID: {job.id}")
print(f"Initial status: {status}")

# Step 12: Import signal and datetime modules for handling interruptions and timestamps
import signal
import datetime

# Step 13: Define a signal handler to manage interruptions

# AI-GEN START - cursor
def signal_handler(signum, frame):
    status = client.fine_tuning.jobs.retrieve(job.id).status
    print(f"Process interrupted, job status: {status}")    
# AI-GEN END

# Step 14: Print the start of event streaming
# AI-GEN START - cursor
print("Starting event streaming...")
# AI-GEN END

# Step 15: Set up the signal handler for keyboard interruptions
# AI-GEN START - cursor
signal.signal(signal.SIGINT, signal_handler)
# AI-GEN END


# Step 16: List events for the fine-tuning job and print them with timestamps
events = client.fine_tuning.jobs.list_events(job.id)
try:
    for event in events:
        print(f"{datetime.datetime.fromtimestamp(event.created_at).strftime('%Y-%m-%d %H:%M:%S')} - {event.message}")
except Exception as e:
    print(f"Error listing events: {e}")
# Step 17: Import time module for sleep function
import time

# Step 18: Check the status of the fine-tuning job and wait if it is not in a terminal state
# AI-GEN START - cursor
terminal_states = ["succeeded", "failed"]

while status not in terminal_states:
    print(f"Current status: {status}. Waiting for job to complete...")
    time.sleep(60)  # Wait for 60 seconds before checking the status again
    status = client.fine_tuning.jobs.retrieve(job.id).status

print(f"Final status: {status}")
# AI-GEN END


# Step 19: Print the status of other fine-tuning jobs in the subscription
# AI-GEN START - cursor
other_jobs = client.fine_tuning.jobs.list()

print("Status of other fine-tuning jobs in the subscription:")
for other_job in other_jobs:
    if other_job.id != job.id:
        print(f"Job ID: {other_job.id}, Status: {other_job.status}")
# AI-GEN END


# Step 20: Retrieve and print the ID of the fine-tuned model
# AI-GEN START - cursor
fine_tuned_model_id = client.fine_tuning.jobs.retrieve(job.id).fine_tuned_model
print(f"Fine-tuned model ID: {fine_tuned_model_id}")
# AI-GEN END

