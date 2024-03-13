# Develop Locally and Deploy with Github Actions

The code in this repository demonstrates how to deploy updates to the main branch of your project to Streamlit in Snowflake using GitHub Actions. This means you can:
* Develop your app locally
* Push your changes to GitHub
* See your latest app code automatically redeployed to Snowflake

This CI/CD setup is useful for several reasons. Firstly, it allows you to use your favorite editor for development, providing a familiar and efficient coding experience. Additionally, you can work with as many files as you need, enabling you to organize your codebase in a way that makes sense for your project. Lastly, you can create multiple pages in your app, providing a seamless and interactive user experience.

To see the automatic deployment, check out the [Actions Page](/actions)

To see how the deployment works, check out [.github/workflows/deploy.yml](/blob/main/.github/workflows/deploy.yml)

# Prerequisites

## GitHub Secrets

In GitHub, go to
- Settings, then
-  Secrets and Variables, then
- Actions

Then add the following as secrets

* `SNOWFLAKE_ACCOUNT`
* `SNOWFLAKE_USER`
* `SNOWFLAKE_PASSWORD`

## secrets.toml (for local development)

Create a file called .streamlit/secrets.toml that looks something like

```toml
[connections.snowflake]
account = "<ACCOUNT>"
user = "<USER>"
authenticator = "externalbrowser"
```

or

```toml
[connections.snowflake]
account = "<ACCOUNT>"
user = "<USER>"
password = "<PASSWORD>"
```

## Sample Data (if using this exact app code)

For this example to work, upload [event_data.csv](/blob/main/event_data.csv) to a table, and change
`TABLE_NAME` in `common/get_data.py` to be the full path of the uploaded data.