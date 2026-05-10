
import os
import pandas as pd

def preprocess_data():
    """
    This function preprocesses the raw sensor data for each participant.
    It loads the EEG, EYE, GSR, and TIVA data, handles missing values,
    merges the data into a single DataFrame, and saves it as a CSV file.
    """
    base_dir = os.getcwd()
    for i in range(1, 39):
        participant_folder = os.path.join(base_dir, str(i))
        if os.path.isdir(participant_folder):
            print(f"Processing data for participant {i}...")

            # File paths
            eeg_file = os.path.join(participant_folder, f"{i}_EEG.csv")
            eye_file = os.path.join(participant_folder, f"{i}_EYE.csv")
            gsr_file = os.path.join(participant_folder, f"{i}_GSR.csv")
            tiva_file = os.path.join(participant_folder, f"{i}_TIVA.csv")

            # Load data
            try:
                eeg_df = pd.read_csv(eeg_file)
                eye_df = pd.read_csv(eye_file)
                gsr_df = pd.read_csv(gsr_file)
                tiva_df = pd.read_csv(tiva_file)
            except FileNotFoundError as e:
                print(f"  Error loading data for participant {i}: {e}")
                continue

            # Handle missing values (forward fill)
            eeg_df.fillna(method='ffill', inplace=True)
            eye_df.fillna(method='ffill', inplace=True)
            gsr_df.fillna(method='ffill', inplace=True)
            tiva_df.fillna(method='ffill', inplace=True)

            # Merge dataframes
            merged_df = pd.concat([eeg_df, eye_df, gsr_df, tiva_df], axis=1)

            # Save preprocessed data
            output_file = os.path.join(participant_folder, "preprocessed_data.csv")
            merged_df.to_csv(output_file, index=False)
            print(f"  Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data()
