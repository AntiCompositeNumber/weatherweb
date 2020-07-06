# weatherweb

## Structure
- Temperature sensor daemon
  - Writes to rrd
- Web frontend
  - Reads from rrd
  - Calls AC controller
- HomeKit bridge
  - Reads from rrd
  - Calls AC controller
