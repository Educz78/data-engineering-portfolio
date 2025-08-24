-- Consulta 1: Top 10 horários mais quentes
SELECT data_hora, temperatura_celsius
FROM `graceful-tenure-469816-p4` 
ORDER BY temperatura_celsius DESC
LIMIT 10;

-- Consulta 2: Temperatura média por dia
SELECT DATE(data_hora) AS dia, ROUND(AVG(temperatura_celsius), 2) AS temperatura_media_celsius
FROM `graceful-tenure-469816-p4` 
GROUP BY dia
ORDER BY dia;