import click
from two1.commands.config import pass_config
from two1.lib.server import rest_client
from two1.commands.config import TWO1_HOST
from two1.lib.util.uxstring import UxString


@click.command()
@pass_config
def flush(config):
    """Sends all earned bitcoins to your wallet"""

    client = rest_client.TwentyOneRestClient(TWO1_HOST)

    flush_earnings(config, client)

    config.log("")


def flush_earnings(config, client):
    response = client.flush_earnings(config.username)
    if response.ok:
        config.log(UxString.flush_success)
    else:
        config.log(UxString.Error.server_err)