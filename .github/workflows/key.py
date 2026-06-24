"""
Token generation script for PCDC document registration API.
Generates an access token using API key and key ID.
"""

import os
import sys
import requests


def main():
    """Generate authentication token and set it as GITHUB_ENV variable."""
    
    # Get environment variables
    fence_client_id = os.environ.get("FENCE_CLIENT_ID")
    fence_client_secret = os.environ.get("FENCE_CLIENT_SECRET")
    url = os.environ.get("PORTAL_API_URL")

    # Validate required environment variables
    if not url:
        error_msg = "REQUESTURL environment variable is not set. Please check GitHub secrets."
        print(f"ERROR: {error_msg}", file=sys.stderr)
        raise RuntimeError(error_msg)
    url = url + "/user/oauth2/token?grant_type=client_credentials&scope=openid"

    if not fence_client_secret:
        error_msg = "FENCE_CLIENT_SECRET environment variable is not set. Please check GitHub secrets."
        print(f"ERROR: {error_msg}", file=sys.stderr)
        raise RuntimeError(error_msg)

    if not fence_client_id:
        error_msg = "FENCE_CLIENT_ID environment variable is not set. Please check GitHub secrets."
        print(f"ERROR: {error_msg}", file=sys.stderr)
        raise RuntimeError(error_msg)

    print(f"Requesting token from: {url}", file=sys.stderr)

    try:
        response = requests.post(
            url,
            auth=(
                fence_client_id,
                fence_client_secret,
            ),
            timeout=30  
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Failed to obtain access token using OIDC client credentials - {response.status_code}:\n{response.text}"
            )

        # Parse response
        token_data = response.json()
        token = token_data.get("access_token") #["access_token"]

        if not token:
            error_msg = "No access_token found in API response"
            print(f"ERROR: {error_msg}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
            raise RuntimeError(error_msg)

        # Write token to GITHUB_ENV for use in subsequent steps
        github_env = os.environ.get("GITHUB_ENV")
        if not github_env:
            error_msg = "GITHUB_ENV environment variable not set"
            print(f"ERROR: {error_msg}", file=sys.stderr)
            raise RuntimeError(error_msg)

        with open(github_env, "a") as f:
            f.write(f"TOKEN={token}\n")

        print(f"Token generated successfully!", file=sys.stderr)
        print(f"Token length: {len(token)} characters", file=sys.stderr)

    except requests.exceptions.Timeout:
        error_msg = "Request to token service timed out after 30 seconds"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        sys.exit(1)
        
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection error while accessing token service: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        sys.exit(1)
        
    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP error from token service: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        if hasattr(e, 'response') and e.response:
            print(f"Response status: {e.response.status_code}", file=sys.stderr)
            print(f"Response body: {e.response.text}", file=sys.stderr)
        sys.exit(1)
        
    except ValueError as e:
        error_msg = f"Invalid JSON response from token service: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        print(f"Response text: {response.text if 'response' in locals() else 'No response'}", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        error_msg = f"Unexpected error generating token: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()