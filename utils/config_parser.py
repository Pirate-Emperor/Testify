import json


class ConfigParser:
    """A class to parse and manage config/config.json file."""

    def __init__(self, config_file='config/config.json'):
        """
        Initializes the ConfigParser with the specified configuration file.

        Args:
            config_file (str): Path to the JSON configuration file.

        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
        """
        try:
            with open(config_file) as file:
                self.config = json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

    def get_web_urls(self):
        """Retrieve URLs from the WEB section.

        Returns:
            dict: A dictionary containing URLs for the web application.

        Raises:
            KeyError: If the WEB section or URLs are missing in the config.
        """
        try:
            return self.config['WEB']['urls']
        except KeyError as e:
            raise KeyError(f"Missing urls key in configuration: {e}")

    def get_web_browser(self):
        """Retrieve the specified browser from the WEB section.

        Returns:
            str: A browser specified in the WEB section.

        Raises:
            KeyError: If the WEB section or browser are missing in the config.
        """
        try:
            return self.config['WEB']['browser'].lower()
        except KeyError as e:
            raise KeyError(f"Missing browser key in configuration: {e}")

    def get_mobile_appium_server(self):
        """Retrieve the address of Appium server from the MOBILE section.

        Returns:
            str: the address of Appium server in the MOBILE section.

        Raises:
            KeyError: If the MOBILE section or appium_server are missing in the config.
        """
        try:
            return self.config['MOBILE']['appium_server']
        except KeyError as e:
            raise KeyError(f"Missing appium_server key in configuration: {e}")

    def get_mobile_desired_capabilities(self):
        """Retrieve the desired_capabilities from the MOBILE section.

        Returns:
            dict: desired_capabilities in the MOBILE section.

        Raises:
            KeyError: If the MOBILE section or desired_capabilities are missing in the config.
        """
        try:
            return self.config['MOBILE']['desired_capabilities']
        except KeyError as e:
            raise KeyError(f"Missing desired_capabilities key in configuration: {e}")
