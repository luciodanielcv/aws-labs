cat << EOF >> /home/ldcv/Projects/terraform/.ssh/config
Host ${hostname}
  HostName ${hostname}
  User ${user}
  IdentityFile ${identityfile}
EOF
