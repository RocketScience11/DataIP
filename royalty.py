from story_protocol_python_sdk import StoryClient
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
private_key = os.getenv('WALLET_PRIVATE_KEY')
rpc_url = os.getenv('RPC_PROVIDER_URL')

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Set up the account with the private key
account = web3.eth.account.from_key(private_key)

story_client = StoryClient(web3, account, 11155111)


response = story_client.Royalty.collectRoyaltyTokens(
    parent_ip_id="0xA34611b0E11Bba2b11c69864f7D36aC83D862A9c",
    child_ip_id="0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7"
)

print(f"Collected royalty token {response['royaltyTokensCollected']} at transaction hash {response['txHash']}")

response = story_client.Royalty.snapshot(
    child_ip_id="0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7"
)

print(f"Took a snapshot with id {response['snapshotId']} at transaction hash {response['txHash']}")

response = story_client.Royalty.claimRevenue(
    snapshotIds=[1, 2],
    child_ip_id="0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7",
    token="0xB132A6B7AE652c974EE1557A3521D53d18F6739f"
)

print(f"Claimed revenue token {response['claimableToken']} at transaction hash {response['txHash']}")

