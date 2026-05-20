import os

sas_folder = 'samples'

for file in os.listdir(sas_folder):
    if file.endswith('.sas'):
        print(f"Migrating: {file}")

print("Migration completed")
