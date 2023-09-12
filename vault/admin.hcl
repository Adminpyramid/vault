# System Administrator Policy

# Manage authentication methods
path "auth/*" {
  capabilities = ["read", "create", "update", "delete", "list"]
}

# Manage policies
path "sys/policies/acl/*" {
  capabilities = ["read", "create", "update", "delete", "list"]
}

# Manage tokens and token roles
path "auth/token/*" {
  capabilities = ["read", "create", "update", "delete", "list"]
}

# Manage identity entities and groups
path "identity/*" {
  capabilities = ["read", "create", "update", "delete", "list"]
}

# Manage Vault's configuration
path "sys/config/*" {
  capabilities = ["read", "update"]
}

# Perform database management (adjust paths based on your database)
path "database/*" {
  capabilities = ["read", "create", "update", "delete", "list"]
}
