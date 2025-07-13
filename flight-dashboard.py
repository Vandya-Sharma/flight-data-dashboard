import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_flight_data.csv")
df = df[df['Flight Number'].notna()]
df['Departure Time'] = pd.to_datetime(df['Departure Time'])

# Title and Intro
st.title("✈️ Flight Data Dashboard")
st.markdown("""
This dashboard shows live flight information using the **Aviationstack API**.  
You can explore **flight statuses**, **departure and arrival details**, and **filter based on flight parameters**.
""")

# Sidebar - Search and Filters
st.sidebar.header("🔎 Search & Filters")

# Flight number search
search = st.sidebar.text_input("Search by Flight Number (IATA):")

# Airline filter
airlines = df['Airline'].dropna().unique().tolist()
selected_airline = st.sidebar.selectbox("Filter by Airline", ["All"] + sorted(airlines))
if selected_airline != "All":
    df = df[df['Airline'] == selected_airline]


# Filter by Departure Airport
airports = df['Departure Airport'].dropna().unique()
selected_airports = st.sidebar.multiselect("Filter by Departure Airport(s):", sorted(airports))

# Filter by Flight Status
statuses = df['Status'].dropna().unique()
selected_status = st.sidebar.multiselect("Filter by Flight Status(es):", sorted(statuses))

# Filter by Date Range
min_date = df['Departure Time'].min().date()
max_date = df['Departure Time'].max().date()
date_range = st.sidebar.date_input("Filter by Departure Date:", [min_date, max_date])

# Apply all filters
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[filtered_df['Flight Number'].str.contains(search, case=False, na=False)]
    if filtered_df.empty:
        st.warning(f"No flights found matching '{search}'")


if selected_airports:
    filtered_df = filtered_df[filtered_df['Departure Airport'].isin(selected_airports)]

if selected_status:
    filtered_df = filtered_df[filtered_df['Status'].isin(selected_status)]

if len(date_range) == 2:
    start_date, end_date = date_range
    mask = (filtered_df['Departure Time'].dt.date >= start_date) & (filtered_df['Departure Time'].dt.date <= end_date)
    filtered_df = filtered_df[mask]

# ✅ Summary Metrics
st.subheader("📊 Flight Summary Statistics")

total_flights = len(filtered_df)
unique_airlines = filtered_df['Airline'].nunique()
departure_airports = filtered_df['Departure Airport'].nunique()
arrival_airports = filtered_df['Arrival Airport'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("✈️ Total Flights", total_flights)
col2.metric("🛫 Departure Airports", departure_airports)
col3.metric("🛬 Arrival Airports", arrival_airports)
col4.metric("🏢 Airlines", unique_airlines)

# ✅ Visualizations Section
st.markdown("---")
st.subheader("📈 Visualizations")

# Flights by Departure Hour (Line Chart)
st.markdown("**🕓 Flights by Departure Hour**")
filtered_df['Departure Hour'] = filtered_df['Departure Time'].dt.hour
hourly_counts = filtered_df['Departure Hour'].value_counts().sort_index()

fig, ax = plt.subplots()

# Plot the line
ax.plot(hourly_counts.index, hourly_counts.values, color='lightcoral', marker='o')

# Set background color to black
fig.patch.set_facecolor('black')       # background around the plot
ax.set_facecolor('black')              # background inside the plot area

# Set axis labels and title with white color
ax.set_xlabel("Departure Hour", color='white')
ax.set_ylabel("Number of Flights", color='white')
ax.set_title("Flights by Hour of Departure", color='white')

# Set ticks color to white
ax.tick_params(colors='white')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.3)

# Adjust spines (border lines)
for spine in ax.spines.values():
    spine.set_color('white')

# Display the plot in Streamlit
st.pyplot(fig)


# Departure Airport Bar Chart
st.markdown("**📍 Departures by Airport**")
departure_counts = filtered_df['Departure Airport'].value_counts().reset_index()
departure_counts.columns = ['Airport', 'Departures']
st.bar_chart(departure_counts.set_index('Airport'))

# Pie Chart for Status
st.markdown("**🛬 Flight Status Distribution**")
status_counts = filtered_df['Status'].value_counts().reset_index()
status_counts.columns = ['Flight Status', 'Count']
fig1, ax1 = plt.subplots()
ax1.pie(status_counts['Count'], labels=status_counts['Flight Status'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
ax1.axis('equal')
st.pyplot(fig1)

# Top Departure Airports (Horizontal Bar)
st.markdown("**🏙️ Top 10 Departure Airports**")
top_departures = filtered_df['Departure Airport'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_departures.values, y=top_departures.index, palette='crest', ax=ax2)
ax2.set_xlabel("Number of Departures")
ax2.set_ylabel("Airport")
st.pyplot(fig2)

# ✅ Filtered Data Table
st.markdown("---")
st.subheader("✈️ Filtered Flight Data")
st.dataframe(filtered_df)

# ✅ Download Button
st.subheader("📥 Download Filtered Data")
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv.encode('utf-8'),
    file_name="filtered_flight_data.csv",
    mime="text/csv"
)

# ✅ Optional: Show Raw Data
with st.expander("📄 Show Raw Data"):
    st.write(df)

# Footer
st.markdown("---")

