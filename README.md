# pressure_log

Javascript amCharts are used to present the logged data. amcharts folder needs to be copied to this folder.
Data is logged by running a cronjob (every hour) script that writes the files in the log folder. The crontab line is:
```sh
0 * * * * /home/pi/source/pressure_log/log_pressure.py
```
These logs need to be merged in a single CSV file that will be read by amCharts. This is done using make_csv.py.
A python HTTP server has to started to show the html page. This is done with start_httpd.py.
