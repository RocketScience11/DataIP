import os
from dotenv import load_dotenv
from web3 import Web3

from story_protocol_python_sdk import StoryClient

load_dotenv()
private_key = os.getenv('WALLET_PRIVATE_KEY')
rpc_url = os.getenv('RPC_PROVIDER_URL')

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Set up the account with the private key
account = web3.eth.account.from_key(private_key)

# Create StoryClient instance
story_client = StoryClient(web3, account, 11155111)

response = story_client.IPAsset.register(
    token_contract="0x0230926BEF507d2E94ad9b3aA753f88271489C3B", # your NFT contract address
    token_id=0 # your NFT token ID
)

print(f"Root IPA created at transaction hash {response['txHash']}")
print(f"IPA ID: {response['ipId']}")

response = story_client.License.registerCommercialRemixPIL(
    minting_fee=1,
    currency="0xB132A6B7AE652c974EE1557A3521D53d18F6739f",
    commercial_rev_share=10,
    royalty_policy="0xAAbaf349C7a2A84564F9CC4Ac130B3f19A718E86"
)

print(f"PIL Terms registered at transaction hash {response['txHash']} License Terms ID: {response['licenseTermsId']}")

try:
  response = story_client.License.attachLicenseTerms(
    ip_id="0x431A7Cc86381F9bA437b575D3F9E931652fFbbdd", 
    license_template="0x260B6CB6284c89dbE660c0004233f7bB99B5edE7", 
    license_terms_id=3)
  print(f"Attached License Terms to IPA at transaction hash {response['txHash']}.")
  
except Exception as e:
  print("License Terms already attached to this IPA")

response = story_client.License.mintLicenseTokens(
    licensor_ip_id="0x431A7Cc86381F9bA437b575D3F9E931652fFbbdd",  # Licensor IP ID
    license_template="0x260B6CB6284c89dbE660c0004233f7bB99B5edE7",  # License Template address
    license_terms_id=2,  # License Terms ID
    amount=1,  # Amount of license tokens to mint
    receiver="0xA0BED684b1eF839A93d565EeB2B736C9ADE50f2e"  # Address of the receiver
)

print(f"License Token minted at transaction hash {response['txHash']} License ID: {response['licenseTokenIds']}")