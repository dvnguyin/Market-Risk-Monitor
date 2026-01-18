CREATE OR REPLACE VIEW v_market_risk_metrics AS
SELECT
    date,
    AVG(CASE WHEN series = 'CPI' THEN value END) AS cpi,
    AVG(CASE WHEN series = 'UNRATE' THEN value END) AS unemployment,
    AVG(CASE WHEN series = 'FEDFUNDS' THEN value END) AS fed_funds,
    AVG(CASE WHEN series = 'DGS10' THEN value END) AS treasury_10y,
    AVG(CASE WHEN series = 'SP500' THEN value END) AS sp500
FROM fred_observations
GROUP BY date
ORDER BY date;

