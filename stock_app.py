#imports
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

#App Title
st.markdown(f'<h1 style="color:#DAA520;font-size:35px;">{"Stock Prices for Top Tech Companies "}</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.subheader('Filter Data')
start_date = st.sidebar.date_input("Start Date", datetime.date(2017, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2022, 7, 7))

#Ticker Data
ticker_list = ['AAPL','ZG','IBM','NFLX','CSCO','CRM','MSFT','GOOGL','TSLA','AMZN', 'META', 'NVDA', 'BABA', 'PYPL', 'YELP']
tickerBox = st.sidebar.selectbox('Stock Ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerBox) # Get ticker data
tickerDf = tickerData.history(period='1mo', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
ticker_name = tickerData.info['longName']
st.header('**%s**' % ticker_name)


market_cap = tickerData.info["marketCap"]
website = tickerData.info["website"]
st.write('Follow link to learn more  ' + str(website))
original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Market Cap:</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.info(market_cap)

#st.write(tickerData.info)

# Ticker data
st.markdown(f'<h1 style="color:#062a78;font-size:24px;">{"Ticker data(first 10 rows)"}</h1>', unsafe_allow_html=True)
st.write('The Dataset has: ' + str(tickerDf.shape[0]) + ' rows and ' + str(tickerDf.shape[1]) + ' columns.')
st.write(tickerDf.head(10))
st.markdown(f'<h1 style="color:#062a78;font-size:24px;">{"Closing Price by Month"}</h1>', unsafe_allow_html=True)
st.line_chart(tickerDf.Close)
st.markdown(f'<h1 style="color:#062a78;font-size:24px;">{"Volume by Month"}</h1>', unsafe_allow_html=True)
st.line_chart(tickerDf.Volume)

#Adding Back-ground
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://c.neh.tw/thumb/f/720/comvecteezy570746.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
