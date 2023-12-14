# Test Kodi Plugin for Managing Addon State

Welcome to the repository for a simple test Kodi plugin. This plugin is designed to explore different methods of managing addon state while performing various actions such as searching within Kodi.

## Repository Structure

In the future, this repository will contain multiple branches, each representing explorations and approaches to managing application state. You will be able to explore these branches to understand the different strategies and their implementations.

## Getting Started

Follow these steps to get the addon up and running:

1. Run `build.py` in the root directory of the project. This will create a zip file named `plugin.video.addonstatetest.zip` in the `dist` directory.
2. Copy the generated zip file to a location accessible by your Kodi installation.
3. In Kodi, go to Settings, then Addons. Choose "Install from zip file" and navigate to the location of the copied zip file.

### Using the Deploy Script
The deploy.py script is a tool for Windows developers to streamline the testing process. It copies the necessary files from your project to the Kodi addons directory (%AppData%\Kodi\addons\plugin.video.addonstatetest).

Please ensure that the addon has been installed at least once using the build script before using the deploy script. This script is intended for development and testing, not for distributing the plugin to end users.

## Purpose of This Repository
The main purpose of this repository is to standardize the approach to managing state in Kodi plugins. Kodi plugins have unique requirements due to the nature of their lifecycle and the way they handle user interactions.

### Unique Requirements of Kodi Plugins
Kodi plugins are ephemeral in nature. The lifetime of the application only exists for a short time to generate a list of directories. Each time a link is clicked, everything in the application is re-instantiated. This presents a unique challenge in managing the state of the application.

### Managing State in Kodi Plugins
All parameters for the program must be encoded into a URL and parsed as the program recursively calls itself. We are essentially clicking a series of links like ‘plugin://plugin.video.addon/?param1=value1&param2=value2’. The program should be designed to handle going backwards through these states as well as recursively deeper.

This repository aims to explore and standardize the best practices for managing such state transitions in Kodi plugins. By doing so, it will provide a solid foundation for building robust and reliable Kodi plugins.

## Contributing

Contributions to this project are always welcome. If you have a new approach to managing application state or an improvement to an existing method, feel free to create a new branch and submit a pull request.

## Contact

If you have any questions or run into any issues, please open an issue in this repository. I appreciate your feedback and am always looking to improve.

Thank you for visiting this repository!