CREATE TABLE IF NOT EXISTS fred_observations (
    series_id TEXT,
    series TEXT,
    date DATE,
    value NUMERIC
);

CREATE INDEX IF NOT EXISTS idx_fred_series_date
ON fred_observations (series_id, date);
