import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def app():

    # Define and connect a new Web3 provider
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

################################################################################
# Load_Contract Function
################################################################################


    @st.cache(allow_output_mutation=True)
    def load_contract():

        # Load the contract ABI
        with open(Path(".//contracts//compiled//jointbankaccount_abi.json")) as f:
            contract_abi = json.load(f)

        # Set the contract address (this is the address of the deployed contract)
        contract_address = "0xDe97D4962CDB27819Ca2D7A088b5f297b9841ba9"

        # Get the contract
        contract = w3.eth.contract(
            address=contract_address,
            abi=contract_abi
    )

        return contract


    # Load the contract
    contract = load_contract()

################################################################################
# Streamlit Integration #
################################################################################

    st.write("Choose an account to get started")
    accounts = w3.eth.accounts
    address = st.selectbox("Select Account", options=accounts)
    # Request input in Ether # The amount is actually in wei initially
    wei_amount = st.number_input("Amount to send in Wei", min_value=0, max_value=1000000000)
    # Convert to Ether
    #eth_amount = w3.fromWei(wei_amount,'ether')

    st.markdown("---")

    if st.button("Donate to The Relevant Element"):
        st.write("Donating to The Relevant Element")


        tx_hash = contract.functions.deposit(
        ).transact({'from': address, 'value' : wei_amount, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Transaction receipt mined:")
        st.write(dict(receipt))
        # if st.download_button("Download Transaction Receipt", receipt):
        #     st.write(dict(receipt))
        #     st.write("Transaction receipt downloaded")
    st.markdown("---")



