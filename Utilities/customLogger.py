
import logging

# Remove all handlers associated with the root logger object.
"code recupéré sur stack over flow, suite à un conflit de sauvegarde du doc.log"
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
