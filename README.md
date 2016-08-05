# ftrack-from-source
A learning tool for running ftrack from the source.

# Usage:
1. Clone the project
  - Download the API package and place it in the pythonpath folder:
  - Go to yourstudioname.ftrackapp.com site.
  - Click on your account icon in the upper right> "System Settings"
  - Download the API package
  - Extract the contents of the python-api.tar into this folder [root_dir]/modules/ftrack/pythonpath/ftrack_api
  - It should look like this:
    - +[root_dir]
      - +modules
        - +ftrack
          - +pythonpath
            - +frack_api
              - +clique
              - +requests 
              - ftrack.py
              - FTrackCore.egg
              - pyparsing.py
              - six.py
              - websocket.py
2. Manually install the virtual env packages into this dir: [root_dir]/venv/ftrack-api-env 
  - (Important because the "site-packages" folder is being added in an env var)
  - In VS you can do this by utilizing the "requirements.txt" file.
    - In Visual Studio, right click on Python Environment
    - "Add Virtual Env" 
    - Create it in the proper dir: [root_dir]/venv/ftrack-api-env
    - Right click the new ftrack-api-env 
    - "Install from requirements.txt"
  - Just a note-- I tried installing from requirements.txt at home on my laptop and I got an error around the installation of connect which was related to cmake.  I ended up having to install the PySide package first and then manually installing the ftrack-connect package through a cmd prompt.
3. Go to [root_dir]/bin/launcher.py> right click and set it as your Startup File.
4. To launch from VS, hit the Start button.


# Launching from outside of VS:

- Once you have the venv setup, just go into the bin folder and run the launch_ftrack_connect.bat file.
- A log directory ([root_dir]\logs) prints out all of the env vars during Ftrack launch so you can see what is being set.
