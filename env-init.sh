#!/bin/bash
output=$(az group create --location $ARM_TEST_LOCATION --name capdeploy$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1) --tags openqa_created_by openqa_ttl=18000)
RESOURCE_GROUP_NAME=$(echo "$output" | jq .name | tr -d '"')
CLUSTER_FQDN=http://$RESOURCE_GROUP_NAME.openqa.com
#az ad sp create-for-rbac --name $CLUSTER_FQDN --role contributor --scopes /subscriptions/$ARM_SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP_NAME
az role assignment create --role "DNS Zone Contributor" --assignee-object-id $SERVICE_PRINCIPAL_OBJECT_ID --assignee-principal-type ServicePrincipal --resource-group $RESOURCE_GROUP_NAME
