# database-dynamic-creds-policy.hcl

# Generate dynamic database credentials
path "database/creds/staff" {
  capabilities = ["read"]
}

# Revoke dynamic database credentials (optional)
path "sys/leases/revoke" {
  capabilities = ["create"]
}
