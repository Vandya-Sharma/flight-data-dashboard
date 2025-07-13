# Flight Data Analytics Dashboard
- This is a beginner-friendly flight data analytics project using real-time data from the Aviationstack API. The project involves API-based data extraction, JSON normalization, data cleaning, interactive filtering, visualizations, and dashboard deployment using Streamlit.

## Dataset
- Real-time flight data accessed and extracted via the Aviationstack API.
- Preprocessed data stored as cleaned_flight_data.csv.

## Dashboard
- This project includes a Streamlit-based interactive dashboard that allows users to analyze and filter flight data dynamically.

[View Interactive Dashboard](https://vandya-sharma.github.io/sales-data-analysis/)

## Technologies Used

- Python

- Pandas

- Matplotlib & Seaborn

- Streamlit

- REST API (Aviationstack)

## Key Features

- Real-time flight data ingestion using API

- Cleaned and transformed nested JSON into structured tabular format using Pandas

- Filters for Flight Number, Airline, Airport, Status, and Date Range

- Key Metrics: Total Flights, Unique Airlines, Departure & Arrival Airports

- Visualizations:

Line Chart: Flights by Departure Hour

Bar Chart: Departures by Airport

Pie Chart: Flight Status Distribution

Horizontal Bar: Top 10 Departure Airports

- Data Table with search and export to CSV

- Optional: Raw dataset view toggle

## Limitations

- Real‑time scope: The Aviationstack free tier only provides current flight data—no historical or scheduled future flights.

- Limited date variety: Flight records often share the same departure date due to real-time API constraints.

- API quota constraints: The free tier imposes monthly API call limits, impacting data volume.

- Incomplete fields: Some records lack flight numbers or airline names; these were filtered or handled during cleaning.

- Geolocation constraints: Mapping features were omitted due to missing or incomplete latitude/longitude data.

- Time zone normalization: All times are treated as UTC since the API doesn’t adjust for airport-specific time zones.

- Static snapshot: Data is fetched in a single batch; live updates only occur when the dashboard is re-run.

## Output

- Cleaned and filtered CSV file download

- Streamlit dashboard with real-time data interaction

- Visual insights into flight patterns and status trends

## Objective
- To demonstrate hands-on experience in using public APIs, performing real-time data analysis, and building interactive dashboards with Streamlit for business and operational insights.
