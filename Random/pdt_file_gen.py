import pandas as pd
import datetime as dt
import pytz


# Read the CSV file
def update_event_date(csv_file, output_file):
    # Load the CSV without a header
    df = pd.read_csv(csv_file, header=None)

    # Rename columns for easier handling
    df.columns = ["record_id", "merchant", "country", "amount", "event_date"]

    # Define the target date and timezone
    target_date = dt.date(2024, 11, 03)  # 10 Mar 2024
    pst = pytz.timezone("utc")

    # Create 24-hour timestamps for the target date
    start_datetime = dt.datetime.combine(target_date, dt.time.min, tzinfo=pst)
    hourly_datetimes = [start_datetime + dt.timedelta(hours=i) for i in range(24)]

    # Generate 170 timestamps evenly distributed across the 24 hours
    timestamps = []
    for hour in hourly_datetimes:
        for minute in range(0, 60, int(60 / (170 // 24))):
            timestamps.append(hour + dt.timedelta(minutes=minute))

    # Limit timestamps to 170 entries
    timestamps = timestamps[:170]

    # Truncate the dataframe to match the new timestamps
    df = df.head(len(timestamps))

    # Replace the event_date column with the new timestamps
    df["event_date"] = [ts.isoformat() for ts in timestamps]

    # Save the updated DataFrame to the output CSV
    df.to_csv(output_file, index=False, header=False)
    print(f"Updated file saved to {output_file}")


# Example usage
update_event_date("adt_check_daylight_source.csv", "adt_check_daylight_source_output_utc.csv")
