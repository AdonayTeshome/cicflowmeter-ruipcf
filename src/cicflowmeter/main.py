
from src.cicflowmeter.sniffer import create_sniffer

def run():
    args = {"input_file": None,
            "input_interface": "TP-Link Wireless MU-MIMO USB Adapter",
            "output_mode": "flow",
            "output_file": "flow.csv"}


    sniffer = create_sniffer(**args)

    sniffer.start()
    try:
        sniffer.join()
    except KeyboardInterrupt:
        sniffer.stop()
    finally:
        sniffer.join()

if __name__ == "__main__":
    run()