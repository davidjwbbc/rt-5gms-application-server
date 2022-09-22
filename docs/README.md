5G-MAG Reference Tools: 5GMS Application Server - Development
=============================================================

In this directory you will find files to assist with development and testing of
the 5G-MAG Reference Tools 5GMS Application Server (AS).

Files in this repository:
- README.md      - Project README file.
- LICENSE        - The software license for this project.
- pyproject.toml - The Python project description for building and installing the application.
- docs/          - Development documentation and examples.
  - README.md - This document.
  - chc.json - An example ContentHostingConfiguration JSON file which provisions a pull-ingest AS for "Big Buck Bunny".
- src/           - The application source modules.
  - rt_5gms_as - The main Python module for this application
    - app.py - Application entry point.
    - openapi_5g - Python bindings generated by openapi-generator for 5G APIs.
    - proxy_factory.py - Factory module to pick a suitable web server/proxy.
    - proxies/ - Contains the web server/proxy detection and configuration classes and any data files they need.
    - utils.py - Common utility functions for the web server/proxy classes.
- tests/         - Regression and build acceptance tests.

Running the example without building
------------------------------------
Make sure that nginx is installed on the local system and is found on the
current command path (`$PATH`).

Then:
```
cd rt-5gms-application-server/src
python3 -m rt_5gms_as.app ../docs/chc.json
```

This will start nginx with a configuration which will provide a reverse proxy to the Big Buck Bunny DASH media at <http://localhost:8080/m4d/provisioning-session-1234abcd/BigBuckBunny_4s_onDemand_2014_05_09.mpd>.

Regenerating the 5G API bindings
--------------------------------
Download the openapi-generator, e.g.
```
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.0.1/openapi-generator-cli-6.0.1.jar -O openapi-generator-cli.jar
```

Get a copy of the 5G APIs:
```
git clone -b REL-17 https://forge.3gpp.org/rep/all/5G_APIs.git
```

Generate the bindings:
```
mkdir 5g-api-python
java -jar openapi-generator-cli.jar generate -i 5G_APIs/TS26512_M1_ContentHostingProvisioning.yaml -g python --additional-properties packageName=rt_5gms_as.openapi_5g,projectName=openapi-5g -o 5g-api-python
rm -rf rt-5gms-application-server/src/rt_5gms_as/openapi_5g
mv 5g-api-python/rt_5gms_as/openapi_5g rt-5gms-application-server/src/rt_5gms_as/
```
