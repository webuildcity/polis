#!/bin/bash

mkdir -p ~/hamburg

rm -f ~/hamburg/imverfahren.json
ogr2ogr -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON ~/hamburg/imverfahren.json WFS:"http://geodienste-hamburg.de/HH_WFS_Bebauungsplaene" app:imverfahren

rm -f ~/hamburg/festgestellt.json
ogr2ogr -s_srs EPSG:25832 -t_srs WGS84 -f geoJSON ~/hamburg/festgestellt.json WFS:"http://geodienste-hamburg.de/HH_WFS_Bebauungsplaene" app:hh_hh_planung_festgestellt
