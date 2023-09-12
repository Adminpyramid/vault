# Database Manager Policy

path "database/data/*" {
  capabilities = ["read", "create", "update"]
}
