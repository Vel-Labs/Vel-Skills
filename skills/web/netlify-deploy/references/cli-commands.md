<!-- Vel-Skills uses local CLI tools and lockfile-based setup. -->
# Netlify CLI Commands Reference

Quick reference for common Netlify CLI commands used in deployments.

## Authentication

```bash
# Login via browser OAuth
netlify login

# Check authentication status and site link
netlify status

# Logout
netlify logout
```

## Site Management

```bash
# Link current directory to existing site
netlify link

# Link by Git remote URL
netlify link --git-remote-url <url>

# Create and link new site
netlify init

# Unlink from current site
netlify unlink

# Open site in Netlify dashboard
netlify open

# Open site admin panel
netlify open:admin

# Open site in browser
netlify open:site
```

## Deployment

```bash
# Deploy preview/draft (safe for testing)
netlify deploy

# Deploy to production
netlify deploy --prod

# Deploy with specific directory
netlify deploy --dir=dist

# Deploy with message
netlify deploy --message="Deploy message"

# List all deploys
netlify deploy:list
```

## Development

```bash
# Run local dev server with Netlify features
netlify dev

# Run local dev server on specific port
netlify dev --port 3000
```

## Site Information

```bash
# Get site info
netlify sites:list

# Get current site info
netlify api getSite --data '{"site_id": "YOUR_SITE_ID"}'
```

## Environment Variables

```bash
# List environment variables
netlify env:list

# Set environment variable
netlify env:set KEY value

# Get environment variable value
netlify env:get KEY

# Import env vars from file
netlify env:import .env
```

## Build

```bash
# Show build settings
netlify build --dry

# Run build locally
netlify build
```

## Functions (Serverless)

```bash
# List functions
netlify functions:list

# Invoke function locally
netlify functions:invoke FUNCTION_NAME

# Create new function
netlify functions:create FUNCTION_NAME
```

## Logs

```bash
# Stream function logs
netlify logs

# View logs for specific function
netlify logs:function FUNCTION_NAME
```

## Troubleshooting Commands

```bash
# Check CLI version
netlify --version

# Get help for any command
netlify help [command]

# Check status with verbose output
netlify status --verbose
```

## Exit Codes

- `0` - Success
- `1` - General error
- `2` - Authentication error
- `3` - Site not found
- `4` - Build failed

## Common Flags

- `--json` - Output as JSON
- `--silent` - Suppress output
- `--debug` - Show debug information
- `--force` - Skip confirmation prompts

## Resources

- Full CLI documentation: https://docs.netlify.com/cli/get-started/
- CLI GitHub repository: https://github.com/netlify/cli
