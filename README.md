# Data Stack

Taking recent experiments and applying to data stack.

Main goal is to have a full data lakehouse stack that runs from GitOps. Hoping to learn more about GitOps to start migrating my homelab setup that direction (did some early experiments and got close). Maybe convert to Kubernetes later.


## TODO:

- [ ] Integrate with Flux CD
- [ ] Create Ansible playbooks
- [x] Set up RustFS for S3 buckets
- [ ] Tika for PDF parsing
- [x] Pangolin blueprints for reverse proxy labeling
- [ ] Switch to Airflow from Kestra for this stack
- [ ] Prepare custom Playwright/Python containers and push to ghcr.io
- [ ] Hoppscotch for API testing
- [ ] SQL users and tables in Docker init script
- [ ] Add WikiJS or OpenMetadata for documentation
- [ ] Add to monitoring stack via Alloy
- [ ] Health checks for containers
- [x] Subdomain for stack
- [ ] Great Expectations
- [ ] Migrate stack to Kubernetes