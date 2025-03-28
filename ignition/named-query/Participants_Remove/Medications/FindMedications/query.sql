SELECT TOP 200
	Name
FROM
	humans.Medications
WHERE
	(:filter <> '' AND :filter <> '%' AND :filter <> '%%')
		AND
	Name LIKE :filter