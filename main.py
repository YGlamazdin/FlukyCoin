import argparse
from node.node_manager import NodeManager
from tools.config_loader import ConfigLoader
from tools.logger import Log

import sys
sys.path.append('/home/rdpuser/FlukyCoin/crypto')


def parse_arguments():
    parser = argparse.ArgumentParser(description='FluckyCoin node')
    parser.add_argument('--config', '-c', type=str, required=False,
                        default='node_config.yaml', help="Node host")
                        # default='node_config3.yaml', help="Node host")
                        # default='node_config_off.yaml', help="Node host")

    # parser.add_argument('--mining_thread_count', '-m', dest='mining_thread_count', type=int, required=False,
    #                     default=None, help="Number of threads for mining")
    # parser.add_argument('--quiet', '-q', dest='quiet', action='store_true', required=False, default=False,
    #                     help="Avoid writing data to the console")
    parser.add_argument("-l", "--loglevel", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level")

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_arguments()

    config_loader = ConfigLoader('config/', args.config)
    config = config_loader.load_config()

    # run_node(port, known_peers)
    log = Log(config["address_reward"])
    node = NodeManager(config, log = log)

    try:
        node.run_node()
    except KeyboardInterrupt:
        pass

