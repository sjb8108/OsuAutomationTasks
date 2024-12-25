from osu import Client

client_id = 29661
client_secret = "CwzqipNRs7axuZ0C43PwEFzpe4BD3g5tyyiVqlTA"
redirect_url = "http://127.0.0.1:8080"
client = Client.from_credentials(client_id, client_secret, redirect_url)
