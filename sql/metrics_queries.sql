-- Metrics queries for semiconductor test results

-- Total number of test records
SELECT COUNT(*) AS total_records
FROM test_results;

-- Count results by PASS/FAIL status
SELECT status, COUNT(*) AS total
FROM test_results
GROUP BY status
ORDER BY status;

-- Average test duration
SELECT ROUND(AVG(duration_seconds), 3) AS average_duration_seconds
FROM test_results;

-- Slowest test execution
SELECT device_id, test_name, status, duration_seconds
FROM test_results
ORDER BY duration_seconds DESC
LIMIT 1;

-- Failed test details
SELECT timestamp, device_id, test_name, duration_seconds
FROM test_results
WHERE status = 'FAIL'
ORDER BY timestamp;
