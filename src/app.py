import json
import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from web3 import Web3
from story_protocol_python_sdk import StoryClient

app = Flask(__name__)
app.debug = True

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

def start_client():
    private_key = os.getenv('WALLET_PRIVATE_KEY')
    rpc_url = os.getenv('RPC_PROVIDER_URL')
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    account = web3.eth.account.from_key(private_key)
    story_client = StoryClient(web3, account, 11155111)
    return story_client

def query(api_url):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Ensure we raise an error for bad status codes
    return response.json()

@app.route("/ipRegister", methods=["GET", "POST"])
def ip_register():
    ip_info = None
    error = None
    json_content = None
    api_data = None

    if request.method == "POST":
        nft_address = request.form.get('content1')
        token_id = request.form.get('content2')
        api_url = request.form.get('api_url')
        story_client = start_client()

        if not nft_address or not token_id:
            error = "Missing nft_address or token_id"
        else:
            try:
                # Ensure the types match the expected function signature
                token_id_int = int(token_id)  # Assuming token_id should be an integer
                nft_address_str = str(nft_address)  # Assuming nft_address should be a string

                asset_register = ip.register_asset(story_client, nft_address_str, token_id_int)
                ip_info = {
                    "nft_address": nft_address,
                    "token_id": token_id,
                    "ip_id": asset_register['ipId'],
                }

                with open('ip_json.json', 'w') as ip_json:
                    json.dump(ip_info, ip_json, indent=7)

                with open('ip_json.json', 'r') as ip_json:
                    json_content = json.load(ip_json)

                # Query the external API if the API URL is provided
                if api_url:
                    api_data = query(api_url)

            except Exception as e:
                error = str(e)

    return render_template("ip_register.html", ip_info=ip_info, error=error, json_content=json_content, api_data=api_data)

if __name__ == "__main__":
    app.run()
