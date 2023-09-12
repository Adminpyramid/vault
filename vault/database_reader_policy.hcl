# database-reader-policy.hcl

path "database/creds/readonly" {
  capabilities = ["read"]
}
