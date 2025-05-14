1.	`pulumi up`
    - Provisions or updates cloud resources based on your code.
    - Use --yes to skip confirmation.
2.	`pulumi preview`
    - Shows what changes would be made without applying them.
3.	`pulumi destroy`
    - Tears down all resources in the current stack.
4.	`pulumi stack`
    - Displays current stack name, configuration, and resources.
5.	`pulumi config`
    - Manage stack configuration values.
    - E.g., pulumi config set aws:region us-west-2.
6.	`pulumi logs`
    - Streams or retrieves logs from the resources in your stack.
7.	`pulumi new`
    - Creates a new Pulumi project from a template.
8.	`pulumi refresh`
    - Syncs the stack’s state with the actual deployed resources.
9.	`pulumi import`
    - Imports an existing cloud resource into Pulumi state.
10.	`pulumi state`