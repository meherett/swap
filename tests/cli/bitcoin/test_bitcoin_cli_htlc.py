#!/usr/bin/env python3

from shuttle.providers.bitcoin.wallet import Wallet
from shuttle.cli.__main__ import main as cli_main
from shuttle.utils import sha256


network = "testnet"
sender_wallet = Wallet(network=network).from_passphrase("meheret tesfaye batu bayou")
recipient_wallet = Wallet(network=network).from_passphrase("meheret")
secret_hash = sha256("Hello Meheret!")
sequence = 1000


def test_bitcoin_cli_htlc(cli_tester):

    htlc = cli_tester.invoke(
        cli_main, [
            "bitcoin",
            "htlc",
            "--secret-hash", secret_hash,
            "--recipient-address", recipient_wallet.address(),
            "--sender-address", sender_wallet.address(),
            "--sequence", sequence,
            "--network", network
        ]
    )
    assert htlc.exit_code == 0
    assert htlc.output == "63aa204683a21fd5ce2425adc90a3674b6d8d3d418935540fc3a71c6ec3cb249925dd388" \
                          "76a91498f879fb7f8b4951dee9bc8a0327b792fbe332b888ac6702e803b27576a91464a8" \
                          "390b0b1685fcbf2d4b457118dc8da92d553488ac68" + "\n"

    htlc = cli_tester.invoke(
        cli_main, [
            "bitcoin",
            "htlc",
            "--secret-hash", secret_hash,
            "--recipient-address", "L5tUq6mCbE84XobZ1mphBPZf15cRFcvg7Q",
            "--sender-address", sender_wallet.address(),
            "--sequence", sequence,
            "--network", network
        ]
    )
    assert htlc.exit_code == 0
    assert htlc.output == "Error: invalid testnet recipient L5tUq6mCbE84XobZ1mphBPZf15cRFcvg7Q address" + "\n"
