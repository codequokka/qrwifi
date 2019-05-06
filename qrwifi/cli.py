import click

from .functions import wifi_qr


@click.group()
def main():
    pass


@main.command()
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
def terminal(ssid, security, password):
    qr = wifi_qr(ssid=ssid, security=security, password=password)
    print(qr.terminal())


@main.command()
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
@click.option("--filename", help="full path to the png file", required=True)
def png(ssid, security, password, filename, scale=10):
    qr = wifi_qr(ssid=ssid, security=security, password=password)
    qr.png(filename, scale)


def start():
    main()


if __name__ == "__main__":
    start()
