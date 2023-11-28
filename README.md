#Real Time Flood Monitoring System

A flood monitoring web application built on the plotly-dash analytics framework. It leverages data from multiple sources to provide a hyperlocal narrative at the river basin level on the climate situation in India, with the current focus being on the southern region, particularly the western ghats.

The data for the same are being collected from both governmental sources and our own burgeoning community data network.

### As of now, climatewatch consists of 3 modules:
+ ### Rainwatch
  Consists of precipitation data from multiple sources
  a. Indian Meteorological Department (IMD) - Precipitation
  b. Community Data Gatherer Network - Precipitation
  The data is being measured from 0830 hours to 0830 hours the next day.
+ ### Floodwatch
  a. Kerala State Electricity Board, Kerala (KSEB) - Reservoir Level & Storage
  b. Irrigation Design and Research Board, Kerala (IDRB) - Reservoir Level & Storage
  c. Irrigation Management System, Tamil Nadu (IMS) - Reservoir Level & Storage
  e. Central Water Commission (CWC) - River Level
  d. Community Data Gatherer Network - Ground Water / Well Water Level
+ ### Tidalwatch
  a. Autonomous Tidal Gauge Station, Kumbalangi, Kerala - Tidal Level, Ambient & Water Temperature, pH, Salinity Data
  b. Community Data Gatherer Network - Tidal Level

