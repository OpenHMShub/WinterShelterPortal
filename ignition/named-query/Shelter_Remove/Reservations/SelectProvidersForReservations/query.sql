SELECT id as 'value' , providerName as 'label'
FROM organization.provider
WHERE providerTypeId = :typeId and timeRetired is null
order by providerName