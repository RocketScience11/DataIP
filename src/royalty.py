import os
from web3 import Web3
from . import start_client

story_client = start_client()

def collect_royalty(parent_ip_id, child_ip_id):
    response = story_client.Royalty.collectRoyaltyTokens(
        parent_ip_id=parent_ip_id,
        #"0xA34611b0E11Bba2b11c69864f7D36aC83D862A9c",
        child_ip_id=child_ip_id
        #"0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7"
    )
    print(f"Collected royalty token {response['royaltyTokensCollected']} at transaction hash {response['txHash']}")
    return response

def snaspshot(child_ip_id):
    response = story_client.Royalty.snapshot(
        child_ip_id=child_ip_id
        #"0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7"
        )
    print(f"Took a snapshot with id {response['snapshotId']} at transaction hash {response['txHash']}")
    return response

def claim_revenue(snapshotIds, child_ip_id, token):
    response = story_client.Royalty.claimRevenue(
        snapshotIds=snapshotIds,
        #[1, 2],
        child_ip_id=child_ip_id,
        #"0x9C098DF37b2324aaC8792dDc7BcEF7Bb0057A9C7",
        token=token
        #"0xB132A6B7AE652c974EE1557A3521D53d18F6739f"
        )
    print(f"Claimed revenue token {response['claimableToken']} at transaction hash {response['txHash']}")
    return response

