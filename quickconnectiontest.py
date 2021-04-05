# Import the client
from td.client import TDClient

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id='WUZ0GLJOO30L1ZFPJPO2GF1S0L708ASW',
    redirect_uri='http://localhost',
    credentials_path='./creds.txt'
)

# Login to the session
TDSession.login()

# Grab real-time quotes for 'MSFT' (Microsoft)
msft_quotes = TDSession.get_quotes(instruments=['MSFT'])
print(msft_quotes)

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
multiple_quotes = TDSession.get_quotes(instruments=['AMZN','SQ'])
print(multiple_quotes)