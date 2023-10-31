import argparse
from typing import Optional, Type
from scapy.sendrecv import AsyncSniffer

#if you run "cicflowmeter" cmd
from .flow_session import generate_session_class


#if you run "main.py" cmd
#from flow_session import generate_session_class


def create_sniffer(input_file: Optional[str], input_interface: Optional[str], output_mode: Optional[str],
                   output_file: str, url_model: Optional[str] = None) -> AsyncSniffer:
    assert (input_file is None) ^ (input_interface is None), "Either input_file or input_interface should be provided."

    NewFlowSession = generate_session_class(output_mode, output_file, url_model)

    common_args = {
        'filter': "ip and (tcp or udp)",
        'prn': None,
        'session': NewFlowSession,
        'store': False,
    }

    if input_file is not None:
        return AsyncSniffer(offline=input_file, **common_args)
    else:
        return AsyncSniffer(iface=input_interface, **common_args)


def main() -> None:
    parser = argparse.ArgumentParser()

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-i", "--interface", action="store", dest="input_interface",
                            help="capture online data from INPUT_INTERFACE")

    input_group.add_argument("-f", "--file", action="store", dest="input_file",
                            help="capture offline data from INPUT_FILE")

    output_group = parser.add_mutually_exclusive_group(required=False)
    output_group.add_argument("-c", "--csv", "--flow", action="store_const", const="flow", dest="output_mode",
                            help="output flows as csv")

    url_model = parser.add_mutually_exclusive_group(required=False)
    url_model.add_argument("-u", "--url", action="store", dest="url_model",
                          help="URL endpoint for sending to Machine Learning Model, e.g., http://0.0.0.0:80/prediction")

    parser.add_argument("output", help="output file name (in flow mode) or directory (in sequence mode)")

    args = parser.parse_args()

    sniffer = create_sniffer(args.input_file, args.input_interface, args.output_mode, args.output, args.url_model)
    sniffer.start()

    try:
        sniffer.join()
    except KeyboardInterrupt:
        sniffer.stop()
    finally:
        sniffer.join()


if __name__ == "__main__":
    main()
