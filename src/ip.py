import os
from web3 import Web3

def register_asset(story_client, nft_address, token_id):
  response = story_client.IPAsset.register(
    token_contract=nft_address,
    #"0x0230926BEF507d2E94ad9b3aA753f88271489C3B", # your NFT contract address
    token_id=token_id # your NFT token ID
    )
  print(f"Root IPA created at transaction hash {response['txHash']}")
  print(f"IPA ID: {response['ipId']}")
  return response

def register_commecial_use_pil(story_client, minting_fee, currency, royalty_policy):
  response = story_client.License.registerCommercialUsePIL(
    minting_fee=minting_fee,
    #1,
    currency=currency,
    #"0xB132A6B7AE652c974EE1557A3521D53d18F6739f",
    royalty_policy=royalty_policy
    #"0xAAbaf349C7a2A84564F9CC4Ac130B3f19A718E86"
    )
  print(f"PIL Terms registered at transaction hash {response['txHash']} License Terms ID: {response['licenseTermsId']}")
  return response

def register_remix_pil(story_client, minting_fee, currency, rev_share, royalty_policy):
  response = story_client.License.registerCommercialRemixPIL(
    minting_fee=minting_fee,
    #1,
    currency=currency,
    #"0xB132A6B7AE652c974EE1557A3521D53d18F6739f",
    commercial_rev_share=rev_share,
    #10,
    royalty_policy=royalty_policy
    #"0xAAbaf349C7a2A84564F9CC4Ac130B3f19A718E86"
    )
  print(f"PIL Terms registered at transaction hash {response['txHash']} License Terms ID: {response['licenseTermsId']}")
  return response

def attach_license_terms(story_client, ip_id, license_template, terms_id):
  try:
    response = story_client.License.attachLicenseTerms(
      ip_id=ip_id,
      #"0x431A7Cc86381F9bA437b575D3F9E931652fFbbdd", 
      license_template=license_template,
      #"0x260B6CB6284c89dbE660c0004233f7bB99B5edE7", 
      license_terms_id=terms_id)
    print(f"Attached License Terms to IPA at transaction hash {response['txHash']}.") 
  except Exception as e:
    print("License Terms already attached to this IPA")
  return response

def mint_ip(ip_id, license_template, terms_id, amount, receiver_address):
  response = story_client.License.mintLicenseTokens(
    licensor_ip_id=ip_id,
    #"0x431A7Cc86381F9bA437b575D3F9E931652fFbbdd",  # Licensor IP ID
    license_template=license_template,
    #"0x260B6CB6284c89dbE660c0004233f7bB99B5edE7",  # License Template address
    license_terms_id=terms_id,
    #2,  # License Terms ID
    amount=amount,
    #1,  # Amount of license tokens to mint
    receiver=receiver_address
    #"0xA0BED684b1eF839A93d565EeB2B736C9ADE50f2e"  # Address of the receiver
    )
  print(f"License Token minted at transaction hash {response['txHash']} License ID: {response['licenseTokenIds']}")
  return response