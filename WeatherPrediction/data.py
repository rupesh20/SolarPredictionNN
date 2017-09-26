import numpy as np
import pandas as pd 
import sys,os
import requests


apiKey='giBQpljM4m7S2OmafxWaUoZUv3K0l95NaZReZUqA'
lat,lon,year = 25.5633, 84.8698, 2015

attr = 'ghi,dhi,dni,wind_speed_10m_nwpsurface_air_temperature_nwp,solar_zenith_angle'
leap_year = 'false'

interval = '30'

utc= 'false'

your_name = 'Rupesh+patil'
reason_for_use = 'beta+testing'
your_affiliation = 'IET+institution'
your_email = 'rupesh.patil741@gmail.com'
mailing_list = 'true'

url = 'http://developer.nrel.gov/api/solar/suny_india_download?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, 
	utc=utc, name=your_name, email=your_email,
	mailing_list=mailing_list, 
	affiliation=your_affiliation,
	reason=reason_for_use, api=apiKey)

r=requests.get(url)
print(r.json)
