## Visual Studio IDE
Since mid of 2025:
* all developments for **Typee** are done using the Microsoft&trade; Visual Studio&trade; IDE.
* **c++23** is the programming language and its related standard used for all code development.
* Unitary tests are implemented with Google Tests.

A global VS-2022 solution is provided here. It embeds and synchronizes all the VS c++ projects associated with **Typee-language** and **Typee-environment** implementations.


### Visual Studio&trade; 2022 Community - free version
The curious or interested reader will take benefit of the installation of Visual Studio&trade; 2022 Community (free version of the IDE for individual developers as well as for organizations under some restrictions - e.g. for learning environment, academic research, or contribution to open source projects - see [https://visualstudio.microsoft.com](https://visualstudio.microsoft.com) for complete information).


### Platforms and Configurations
All VS projects are configured for 32-bits and 64-bits platforms and for Debug and Release configurations. By mid-2025, they are set to use the c++ compiler in its latest version, i.e. with flags `/std` set to `/std:latest` and `/std:clatest`, automatically overriding the option `/std:c++23preview`.


### Startup Project
Solution `vs-2022` is preconfigured to run the currently selected project in the list of projects.

So, just click on the project you want to run before asking for a run (Ctrl + F5) or before starting a debug session on it (F5).