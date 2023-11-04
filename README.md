

docker build -t dash-plotly:v1 . 

docker run -p 8091:8090 dash-plotly:v1

docker rmi dash-plotly:v1 -f

