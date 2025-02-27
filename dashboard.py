
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset
@st.cache_data
def load_data():
    day_df = pd.read_csv("content/day.csv")
    hour_df = pd.read_csv("content/hour.csv")
    return day_df, hour_df


day_df, hour_df = load_data()

# Data Processing
day_df["season"].replace((1, 2, 3, 4), ('Spring', 'Summer', 'Fall', 'Winter'), inplace=True)
day_df["yr"].replace((0, 1), (2011, 2012), inplace=True)
day_df["mnth"].replace(range(1, 13),
                       ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                       inplace=True)
day_df["weekday"].replace((0, 1, 2, 3, 4, 5, 6),
                          ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'), inplace=True)

# Title
st.title("📊 Bike Rental Data Analysis")

# Sidebar
st.sidebar.header("Bike Navigation")
menu = st.sidebar.radio("Go to", ["Overview", "Analysis 1: Workday vs Holiday", "Analysis 2: Registered Users"])

# Show dataset
if menu == "Overview":
    # st.title("🚲 Bike Sharing Dataset Overview")

    st.markdown("""
        ## 📌 Dataset Information
        **Bike sharing systems** are the new generation of traditional bike rentals where the whole process, from membership, rental, and return, has become automatic. Users can easily rent a bike from one location and return it at another. 

        Currently, there are over **500 bike-sharing programs worldwide**, comprising over **500,000 bicycles**. These systems play an essential role in traffic management, environmental sustainability, and public health.

        **Why is this data useful?**  
        Unlike buses or subways, bike-sharing systems record **travel duration, departure, and arrival locations** explicitly. This transforms the system into a **virtual sensor network** that can help **monitor city mobility**. As a result, this data can be used to analyze trends, predict demand, and even detect significant events in a city.

        ---

        ## 🔢 Attribute Information
        The dataset consists of **two files: `day.csv` and `hour.csv`**. Both files share the same attributes, except that `hr` (hour) is **not available** in `day.csv`.

        | Feature | Description |
        |---------|------------|
        | **instant** | Record index |
        | **dteday** | Date |
        | **season** | Season (1: Spring, 2: Summer, 3: Fall, 4: Winter) |
        | **yr** | Year (0: 2011, 1: 2012) |
        | **mnth** | Month (1 to 12) |
        | **hr** | Hour (0 to 23) *(Only in hour.csv)* |
        | **holiday** | Whether the day is a holiday (1: Yes, 0: No) |
        | **weekday** | Day of the week (0: Sunday → 6: Saturday) |
        | **workingday** | Whether the day is a working day (1: Yes, 0: No) |
        | **weathersit** | Weather condition (1: Clear, 2: Mist, 3: Light Snow/Rain, 4: Heavy Rain/Snow) |
        | **temp** | Normalized temperature (-8°C to +39°C) |
        | **atemp** | Normalized 'feels like' temperature (-16°C to +50°C) |
        | **hum** | Normalized humidity (max: 100) |
        | **windspeed** | Normalized wind speed (max: 67) |
        | **casual** | Count of casual users |
        | **registered** | Count of registered users |
        | **cnt** | Total number of rental bikes (casual + registered) |

        🔗 **Source:** [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)
        """)

    st.header("Dataset Preview")
    st.write("### 📅 Day Data")
    st.dataframe(day_df.head())
    st.write("### ⏳ Hourly Data")
    st.dataframe(hour_df.head())

elif menu == "Analysis 1: Workday vs Holiday":
    st.header("🚲 Rental Pattern: Workday vs Holiday")

    holiday_vs_workingday = day_df.groupby("workingday")["cnt"].mean()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(["Workday", "Holiday"], holiday_vs_workingday.values, color=['#E17055', '#2980B9'])

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 100, round(yval, 2), ha='center', va='bottom')

    ax.set_xlabel("Type of Day")
    ax.set_ylabel("Avg Rentals")
    ax.set_title("Bike Rentals: Workday vs Holiday")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

    st.markdown(f"""
        ## 📊 Analisis Penyewaan Sepeda
        Berdasarkan data, rata-rata jumlah penyewaan sepeda per hari adalah:
        - **🏢 Hari Kerja (Weekdays):** {round(holiday_vs_workingday[1], 2)}
        - **🌅 Akhir Pekan (Weekend):** {round(holiday_vs_workingday[0], 2)}

        **🔍 Faktor yang Mempengaruhi Perbedaan Penyewaan:**
        - **Waktu Luang:** Pada akhir pekan, orang memiliki lebih banyak waktu luang untuk beraktivitas di luar ruangan, termasuk bersepeda.
        - **Kegiatan Rekreasi:** Akhir pekan sering kali diisi dengan kegiatan rekreasi bersama keluarga atau teman, dan bersepeda bisa menjadi salah satu pilihan aktivitas yang menyenangkan.
        - **Tujuan Penggunaan:** Pada hari kerja, penyewaan sepeda mungkin lebih didominasi oleh tujuan transportasi, seperti pergi ke tempat kerja atau sekolah. Sedangkan pada akhir pekan, tujuan penggunaan sepeda lebih bervariasi, seperti untuk olahraga atau sekadar bersantai.
        """)

elif menu == "Analysis 2: Registered Users":
    st.header("👥 Registered Users Per Hour")

    registered_hourly = hour_df.groupby("hr")['registered'].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=registered_hourly.values, x=registered_hourly.index, ax=ax)
    ax.set_title("Total Registered Rentals Per Hour")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Total Registered Rentals")

    st.pyplot(fig)

    st.markdown("""
       ## 🔍 Analisis
       Berdasarkan data, rata-rata waktu jam pengguna baru yang mendaftar untuk peminjaman sepeda dapat dilihat dari jumlah penyewaan per jam.

       **Jam dengan Penyewaan Terbanyak Berdasarkan Data:**
       - 🏆 **Jam 17** memiliki jumlah penyewaan terdaftar tertinggi (**282.640**).
       - 🥈 **Jam 18** memiliki jumlah penyewaan terdaftar kedua tertinggi (**265.276**).
       - 🥉 **Jam 8** memiliki jumlah penyewaan terdaftar ketiga tertinggi (**245.240**).

       **Pola Penyewaan:**
       - Penyewaan terdaftar cenderung tinggi pada jam-jam sibuk, seperti **jam pulang kerja (17:00 - 18:00)**.
       - Jam **16:00 dan 19:00** mungkin menunjukkan fleksibilitas jam kerja atau kegiatan tambahan / lembur di luar jam kerja reguler.
       - Jam **7:00 - 8:00** menunjukkan lonjakan seiring dengan jam berangkat kerja atau sekolah.

       **📌 Manfaat Data Ini:**
       - Memahami kapan permintaan penyewaan sepeda paling tinggi untuk pengelolaan **inventaris dan operasional**.
       - Menentukan waktu yang tepat untuk melakukan **promosi atau penawaran khusus**.
       """)

