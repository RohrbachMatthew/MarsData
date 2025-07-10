#  Mars Weather Data Ingestion

This Python script fetches weather data from NASA's InSight Mars mission and stores it in a local MySQL database. It loops through multiple sols (Martian days) and inserts new data only if it hasn't already been recorded.

---

##  Features

- Fetches data from NASA’s InSight API
- Parses multiple sols (not just the latest)
- Avoids duplicate entries by checking dates
- Prints logs for inserted and skipped records
- Ready for extension into visualizations or dashboards

---

## Notes
- Radiation data may be NULL if missing in the feed.
- You can modify the script to include sol numbers in your table for deeper tracking.
- This script is built for automation — feel free to integrate it into cron jobs or pipelines.
