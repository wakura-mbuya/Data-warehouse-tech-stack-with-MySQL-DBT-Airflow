-- create traffic_flow table
CREATE TABLE IF NOT EXISTS traffic_flow (
    id SERIAL PRIMARY KEY, 
    track_id int,
    vehicle_type VARCHAR NOT NULL,
    travelled_distance float NOT NULL,
    avg_speed float NOT NULL,
    lat float, 
    lon float,
    speed float,
    long_acc float,
    lat_acc float
);