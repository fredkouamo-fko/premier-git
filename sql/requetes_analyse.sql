-- Requetes d'analyse du projet ventes 2024
SELECT region, SUM(montant) AS ca_region
FROM ventes
GROUP BY region
ORDER BY ca_region DESC;
