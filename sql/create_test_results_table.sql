CREATE TABLE IF NOT EXISTS test_results (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id VARCHAR(50) NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    status VARCHAR(10) NOT NULL,
    duration_seconds NUMERIC(10,3) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

GRANT INSERT, SELECT, UPDATE, DELETE ON test_results TO lab_user;
GRANT USAGE, SELECT ON SEQUENCE test_results_id_seq TO lab_user;
